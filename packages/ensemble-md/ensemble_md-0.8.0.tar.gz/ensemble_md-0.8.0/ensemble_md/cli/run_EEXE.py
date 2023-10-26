####################################################################
#                                                                  #
#    ensemble_md,                                                  #
#    a python package for running GROMACS simulation ensembles     #
#                                                                  #
#    Written by Wei-Tse Hsu <wehs7661@colorado.edu>                #
#    Copyright (c) 2022 University of Colorado Boulder             #
#                                                                  #
####################################################################
import os
import sys
import time
import copy
import shutil
import traceback
import argparse
import numpy as np
from mpi4py import MPI
from datetime import datetime

from ensemble_md.utils import utils
from ensemble_md.ensemble_EXE import EnsembleEXE


def initialize(args):
    parser = argparse.ArgumentParser(
        description='This code runs an ensemble of expanded ensemble given necessary inputs.')
    parser.add_argument('-y',
                        '--yaml',
                        type=str,
                        default='params.yaml',
                        help='The input YAML file that contains EEXE parameters. (Default: params.yaml)')
    parser.add_argument('-c',
                        '--ckpt',
                        type=str,
                        default='rep_trajs.npy',
                        help='The NPY file containing the replica-space trajectories. This file is a \
                            necessary checkpoint file for extending the simulaiton. (Default: rep_trajs.npy)')
    parser.add_argument('-g',
                        '--g_vecs',
                        type=str,
                        default='g_vecs.npy',
                        help='The NPY file containing the timeseries of the whole-range alchemical weights. \
                            This file is a necessary input if ones wants to update the file when extending \
                            the simulation. (Default: g_vecs.npy)')
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default='run_EEXE_log.txt',
                        help='The output file for logging how replicas interact with each other. \
                            (Default: run_EEXE_log.txt)')
    parser.add_argument('-m',
                        '--maxwarn',
                        type=int,
                        default=0,
                        help='The maximum number of warnings in parameter specification to be ignored.')
    args_parse = parser.parse_args(args)

    return args_parse


def main():
    t1 = time.time()
    args = initialize(sys.argv[1:])
    sys.stdout = utils.Logger(logfile=args.output)
    sys.stderr = utils.Logger(logfile=args.output)

    # Step 1: Set up MPI rank and instantiate EnsembleEXE to set up EEXE parameters
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # Note that this is a GLOBAL variable

    if rank == 0:
        print(f'Current time: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        print(f'Command line: {" ".join(sys.argv)}\n')

    EEXE = EnsembleEXE(args.yaml)

    if rank == 0:
        # Print out simulation parameters
        EEXE.print_params()

        # Print out warnings and fail if needed
        for i in EEXE.warnings:
            print(f'\n{i}\n')

        if len(EEXE.warnings) > args.maxwarn:
            print(f"The execution failed due to warning(s) about parameter spcificaiton. Check the warnings, or consider setting maxwarn in the input YAML file if you find them harmless.")  # noqa: E501, F541
            comm.Abort(101)

    # Step 2: If there is no checkpoint file found/provided, perform the 1st iteration (index 0)
    if os.path.isfile(args.ckpt) is False:
        start_idx = 1

        # 2-1. Set up input files for all simulations
        if rank == 0:
            for i in range(EEXE.n_sim):
                os.mkdir(f'sim_{i}')
                os.mkdir(f'sim_{i}/iteration_0')
                MDP = EEXE.initialize_MDP(i)
                MDP.write(f"sim_{i}/iteration_0/expanded.mdp", skipempty=True)

        # 2-2. Run the first ensemble of simulations
        EEXE.run_EEXE(0)

    else:
        if rank == 0:
            # If there is a checkpoint file, we see the execution as an extension of an EEXE simulation
            ckpt_data = np.load(args.ckpt)
            start_idx = len(ckpt_data[0])  # The length should be the same for the same axis
            print(f'\nGetting prepared to extend the EEXE simulation from iteration {start_idx} ...')

            if start_idx == EEXE.n_iter:
                print('Extension aborted: The expected number of iterations have been completed!')
                MPI.COMM_WORLD.Abort(1)
            else:
                print('Deleting data generated after the checkpoint ...')
                for i in range(EEXE.n_sim):
                    n_finished = len(next(os.walk(f'sim_{i}'))[1])  # number of finished iterations
                    for j in range(start_idx, n_finished):
                        print(f'  Deleting the folder sim_{i}/iteration_{j}')
                        shutil.rmtree(f'sim_{i}/iteration_{j}')

            # Read g_vecs.npy and rep_trajs.npy so that new data can be appended, if any.
            # Note that these two arrays are created in rank 0 and should always be operated in rank 0,
            # or broadcasting is required.
            EEXE.rep_trajs = [list(i) for i in ckpt_data]
            if os.path.isfile(args.g_vecs) is True:
                EEXE.g_vecs = [list(i) for i in np.load(args.g_vecs)]
        else:
            start_idx = None

        start_idx = comm.bcast(start_idx, root=0)  # so that all the ranks are aware of start_idx

    # 2-3. Get the reference distance for the distance restraint specified in the pull code, if any.
    EEXE.get_ref_dist()

    for i in range(start_idx, EEXE.n_iter):
        # For a large code block like below executed on rank 0, we try to catch any exception and abort the simulation.
        # So if there is bug, the execution will be terminated and no computation time will be wasted.
        try:
            if rank == 0:
                # Step 3: Swap the coordinates
                # 3-1. For all the replica simulations,
                #   (1) Find the last sampled state and the corresponding lambda values from the DHDL files.
                #   (2) Find the final Wang-Landau incrementors and weights from the LOG files.
                dhdl_files = [f'sim_{j}/iteration_{i - 1}/dhdl.xvg' for j in range(EEXE.n_sim)]
                log_files = [f'sim_{j}/iteration_{i - 1}/md.log' for j in range(EEXE.n_sim)]
                states_ = EEXE.extract_final_dhdl_info(dhdl_files)
                wl_delta, weights_, counts_ = EEXE.extract_final_log_info(log_files)
                print()

                # 3-2. Identify swappable pairs, propose swap(s), calculate P_acc, and accept/reject swap(s)
                # Note after `get_swapping_pattern`, `states_` and `weights_` won't be necessarily
                # since they are updated by `get_swapping_pattern`. (Even if the function does not explicitly
                # returns `states_` and `weights_`, `states_` and `weights_` can still be different after
                # the use of the function.) Therefore, here we create copies for `states_` and `weights_`
                # before the use of `get_swapping_pattern`, so we can use them in `weight_correction`,
                # `combine_weights` and `update_MDP`.
                states = copy.deepcopy(states_)
                weights = copy.deepcopy(weights_)
                counts = copy.deepcopy(counts_)
                swap_pattern, swap_list = EEXE.get_swapping_pattern(dhdl_files, states_, weights_)  # swap_list will only be used for modify_coords  # noqa: E501

                # 3-3. Perform weight correction/weight combination
                if wl_delta != [None for i in range(EEXE.n_sim)]:  # weight-updating
                    print(f'\nCurrent Wang-Landau incrementors: {wl_delta}\n')

                # (1) First we prepare the weights to be combined.
                # Note that although averaged weights are sometimes used for weight correction/weight combination,
                # the final weights are always used for calculating the acceptance ratio.
                if EEXE.N_cutoff != -1 or EEXE.w_combine is not None:
                    # Only when weight correction/weight combination is needed.
                    weights_avg, weights_err = EEXE.get_averaged_weights(log_files)
                    weights_input = EEXE.prepare_weights(weights_avg, weights)  # weights_input is for weight combination  # noqa: E501

                # (2) Now we perform weight correction/weight combination.
                # The product of this step should always be named as "weights" to be used in update_MDP
                if EEXE.N_cutoff != -1 and EEXE.w_combine is not None:
                    # perform both
                    if weights_input is None:
                        # Then only weight correction will be performed
                        print('Note: Weight combination is deactivated because the weights are too noisy.')
                        weights = EEXE.weight_correction(weights, counts)
                        _ = EEXE.combine_weights(counts_, weights, print_values=False)[1]  # just to print the combiend weights  # noqa: E501
                    else:
                        weights_preprocessed = EEXE.weight_correction(weights_input, counts)
                        if EEXE.verbose is True:
                            print('Performing weight combination ...')
                        else:
                            print('Performing weight combination ...', end='')
                        counts, weights, g_vec = EEXE.combine_weights(counts_, weights_preprocessed)  # inverse-variance weighting seems worse  # noqa: E501
                        EEXE.g_vecs.append(g_vec)
                elif EEXE.N_cutoff == -1 and EEXE.w_combine is not None:
                    # only perform weight combination
                    print('Note: No weight correction will be performed.')
                    if weights_input is None:
                        print('Note: Weight combination is deactivated because the weights are too noisy.')
                        _ = EEXE.combine_weights(counts_, weights, print_values=False)[1]  # just to print the combined weights  # noqa: E501
                    else:
                        if EEXE.verbose is True:
                            print('Performing weight combination ...')
                        else:
                            print('Performing weight combination ...', end='')
                        counts, weights, g_vec = EEXE.combine_weights(counts_, weights_input)  # inverse-variance weighting seems worse  # noqa: E501
                        EEXE.g_vecs.append(g_vec)
                elif EEXE.N_cutoff != -1 and EEXE.w_combine is None:
                    # only perform weight correction
                    print('Note: No weight combination will be performed.')
                    weights = EEXE.histogram_correction(weights_input, counts)
                    _ = EEXE.combine_weights(counts_, weights, print_values=False)[1]  # just to print the combined weights  # noqa: E501
                else:
                    print('Note: No weight correction will be performed.')
                    print('Note: No weight combination will be performed.')
                    _ = EEXE.combine_weights(counts_, weights, print_values=False)[1]  # just to print the combiend weights  # noqa: E501

                # 3-5. Modify the MDP files and swap out the GRO files (if needed)
                # Here we keep the lambda range set in mdp the same across different iterations in the same folder but swap out the gro file  # noqa: E501
                # Note we use states (copy of states_) instead of states_ in update_MDP.
                for j in list(range(EEXE.n_sim)):
                    os.mkdir(f'sim_{j}/iteration_{i}')
                    MDP = EEXE.update_MDP(f"sim_{j}/iteration_{i - 1}/expanded.mdp", j, i, states, wl_delta, weights, counts)   # modify with a new template  # noqa: E501
                    MDP.write(f"sim_{j}/iteration_{i}/expanded.mdp", skipempty=True)
                    # In run_EEXE(i, swap_pattern), where the tpr files will be generated, we use the top file at the
                    # level of the simulation (the file that will be shared by all simulations). For the gro file, we
                    # pass swap_pattern to the function to figure it out internally.
            else:
                swap_pattern, swap_list = None, None

        except Exception:
            print('\n--------------------------------------------------------------------------\n')
            print(f'An error occurred on rank 0:\n{traceback.format_exc()}')
            MPI.COMM_WORLD.Abort(1)

        if -1 not in EEXE.equil and 0 not in EEXE.equil:
            # This is the case where the weights are equilibrated in a weight-updating simulation.
            # As a remidner, EEXE.equil should be a list of 0 after extract_final_log_info in a
            # fixed-weight simulation, and a list of -1 for a weight-updating simulation with unequilibrated weights.
            print('\nSimulation terminated: The weights have been equilibrated for all replicas.')  # this will only be printed in rank 0  # noqa: E501

            # Note that EEXE.equil is avaiable for all ranks but only updated in rank 0. So the if condition here
            # can only be satisfied in rank 0. We broadcast exit_loop to all ranks so that all ranks can exit the
            # simulation at the same time, if the weights get equilibrated.
            exit_loop = True
            comm.bcast(exit_loop, root=0)
            break
        else:
            # Receive exit_loop from rank 0. If exit_loop is True, all ranks will exit the simulation.
            exit_loop = comm.bcast(False, root=0)
            if exit_loop:
                break

        # Step 4: Perform another iteration
        # 4-1. Modify the coordinates of the output gro files if needed.
        swap_pattern = comm.bcast(swap_pattern, root=0)
        swap_list = comm.bcast(swap_list, root=0)

        if len(swap_list) == 0:
            pass
        else:
            if EEXE.modify_coords_fn is not None:
                try:
                    if rank == 0:
                        for j in range(len(swap_list)):
                            print('\nModifying the coordinates of the following output GRO files ...')
                            # gro_1 and gro_2 are the simlation outputs (that we want to back up) and the inputs to modify_coords  # noqa: E501
                            gro_1 = f'sim_{swap_list[j][0]}/iteration_{i-1}/confout.gro'
                            gro_2 = f'sim_{swap_list[j][1]}/iteration_{i-1}/confout.gro'
                            print(f'  - {gro_1}\n  - {gro_2}')

                            # Now we rename gro_1 and gro_2 to back them up
                            gro_1_backup = gro_1.split('.gro')[0] + '_backup.gro'
                            gro_2_backup = gro_2.split('.gro')[0] + '_backup.gro'
                            os.rename(gro_1, gro_1_backup)
                            os.rename(gro_2, gro_2_backup)

                            # Here we input gro_1_backup and gro_2_backup and modify_coords_fn will save the modified gro files as gro_1 and gro_2  # noqa: E501
                            EEXE.modify_coords_fn(gro_1_backup, gro_2_backup)  # the order should not matter
                except Exception:
                    print('\n--------------------------------------------------------------------------\n')
                    print(f'\nAn error occurred on rank 0:\n{traceback.format_exc()}')
                    MPI.COMM_WORLD.Abort(1)

        # 4-2. Run another ensemble of simulations
        EEXE.run_EEXE(i, swap_pattern)

        # 4-3. Save data
        if rank == 0:
            if (i + 1) % EEXE.n_ckpt == 0:
                if len(EEXE.g_vecs) != 0:
                    # Save g_vec as a function of time if weight combination was used.
                    np.save('g_vecs.npy', EEXE.g_vecs)

                print('\n----- Saving .npy files to checkpoint the simulation ---')
                np.save('rep_trajs.npy', EEXE.rep_trajs)

    # Save the npy files at the end of the simulation anyway.
    if rank == 0:
        if len(EEXE.g_vecs) != 0:  # The length will be 0 only if there is no weight combination.
            np.save('g_vecs.npy', EEXE.g_vecs)
        np.save('rep_trajs.npy', EEXE.rep_trajs)

    # Step 5: Write a summary for the simulation ensemble
    if rank == 0:
        print('\nSummary of the simulation ensemble')
        print('==================================')
        print('Simulation status:')
        for i in range(EEXE.n_sim):
            if EEXE.fixed_weights is True:
                print(f'- Rep {i}: The weights were fixed throughout the simulation.')
            elif EEXE.equil[i] == -1:
                print(f'  - Rep {i}: The weights have not been equilibrated.')
            else:
                idx = int(np.floor(EEXE.equil[i] / (EEXE.dt * EEXE.nst_sim)))
                if EEXE.equil[i] > 1000:
                    units = 'ns'
                    EEXE.equil[i] /= 1000
                else:
                    units = 'ps'
                print(f'  - Rep {i}: The weights have been equilibrated at {EEXE.equil[i]:.2f} {units} (iteration {idx}).')  # noqa: E501

        print(f'\n{EEXE.n_empty_swappable} out of {EEXE.n_iter}, or {EEXE.n_empty_swappable / EEXE.n_iter * 100:.1f}% iterations had an empty list of swappable pairs.')  # noqa: E501
        if EEXE.n_swap_attempts != 0:
            print(f'{EEXE.n_rejected} out of {EEXE.n_swap_attempts}, or {EEXE.n_rejected / EEXE.n_swap_attempts * 100:.1f}% of attempted exchanges were rejected.')  # noqa: E501

        print(f'\nTime elapsed: {utils.format_time(time.time() - t1)}')

    MPI.Finalize()
