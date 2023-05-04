from time import time, sleep
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from inspect import signature

from levels.level_3sat import level_3sat
from levels.level_4_colors_theorem import level_4_colors_theorem
from levels.level_the_4_queens import level_the_4_queens
from levels.level_the_4th_dimension import level_the_4th_dimension
from levels.level_alice_and_bob import level_alice_and_bob
from levels.level_backward import level_backward
from levels.level_baguenaudier import level_baguenaudier
from levels.level_betweenness import level_betweenness
from levels.level_binary import level_binary
from levels.level_bipartite import level_bipartite
from levels.level_bis_repetita import level_bis_repetita
from levels.level_cartesian import level_cartesian
from levels.level_chessboard import level_chessboard
from levels.level_code import level_code
from levels.level_combinatorics import level_combinatorics
from levels.level_compact import level_compact
from levels.level_congruence import level_congruence
from levels.level_crossroad import level_crossroad
from levels.level_crystal import level_crystal
from levels.level_cube import level_cube
from levels.level_dead_ends import level_dead_ends
# from levels.level_desert_crossing import level_desert_crossing
from levels.level_diagonal import level_diagonal
from levels.level_dichotomy import level_dichotomy
from levels.level_dominating_set import level_dominating_set
from levels.level_doppelganger import level_doppelganger
from levels.level_egyptian_fractions import level_egyptian_fractions
from levels.level_electricity import level_electricity
from levels.level_elementary import level_elementary
from levels.level_eulerian import level_eulerian
from levels.level_exact_cover import level_exact_cover
from levels.level_five import level_five
from levels.level_flash_back import level_flash_back
from levels.level_fluid import level_fluid
from levels.level_fractal import level_fractal
from levels.level_grid import level_grid
from levels.level_hamiltonian import level_hamiltonian
from levels.level_hello_world import level_hello_world
from levels.level_hitting_set import level_hitting_set
from levels.level_hungarian_rings import level_hungarian_rings
from levels.level_independent_set import level_independent_set
from levels.level_infinity import level_infinity
from levels.level_initiation import level_initiation
from levels.level_inversions import level_inversions
from levels.level_k import level_k
from levels.level_knapsack import level_knapsack
from levels.level_knight import level_knight
from levels.level_lights_out import level_lights_out
from levels.level_linear import level_linear
from levels.level_longest_path import level_longest_path
from levels.level_loop import level_loop
from levels.level_manhattan_distance import level_manhattan_distance
from levels.level_matrix import level_matrix
from levels.level_magic_square import level_magic_square  # kakuro
from levels.level_mastermind import level_mastermind
from levels.level_mols import level_mols
from levels.level_naturals import level_naturals
from levels.level_nonogram import level_nonogram
from levels.level_no_three_in_line import level_no_three_in_line
from levels.level_numeration import level_numeration
from levels.level_odd import level_odd
from levels.level_or import level_or
from levels.level_oval_track_puzzle import level_oval_track_puzzle
from levels.level_pancake_sorting import level_pancake_sorting
from levels.level_panex import level_panex
from levels.level_parallel import level_parallel
from levels.level_parking import level_parking
from levels.level_partition import level_partition
from levels.level_permutations import level_permutations
from levels.level_point_of_no_return import level_point_of_no_return
from levels.level_pong import level_pong
from levels.level_product import level_product
from levels.level_puzzle import level_puzzle
from levels.level_pythagorean import level_pythagorean
from levels.level_random_binary_tree import level_random_binary_tree
from levels.level_random_boustrophedon import level_random_boustrophedon
from levels.level_random_bull import level_random_bull
from levels.level_random_butterfly import level_random_butterfly
from levels.level_random_come_back import level_random_come_back
from levels.level_random_cuboctahedron import level_random_cuboctahedron
from levels.level_random_gemini import level_random_gemini
from levels.level_random_K2 import level_random_K2
from levels.level_random_K5 import level_random_K5
from levels.level_random_K33 import level_random_K33
from levels.level_random_loop import level_random_loop
from levels.level_random_ladder import level_random_ladder
from levels.level_random_line import level_random_line
from levels.level_random_petersen import level_random_petersen
# from levels.level_random_tetractys import level_random_tetractys
from levels.level_random_simple import level_random_simple
from levels.level_random_star import level_random_star
from levels.level_sign import level_sign
from levels.level_random_starting_point import level_random_starting_point
from levels.level_sum import level_sum
from levels.level_random_wheel import level_random_wheel
from levels.level_rotation import level_rotation
from levels.level_rotation_bis import level_rotation_bis
from levels.level_recurrence import level_recurrence
from levels.level_river import level_river
from levels.level_second import level_second
from levels.level_shuffled import level_shuffled
from levels.level_small import level_small
from levels.level_small_panex import level_small_panex
from levels.level_square import level_square
from levels.level_solitaire import level_solitaire
from levels.level_spare import level_spare
from levels.level_spaceship import level_spaceship
from levels.level_strange import level_strange
from levels.level_sudoku import level_sudoku
from levels.level_sujiko import level_sujiko
from levels.level_superflip import level_superflip
from levels.level_superpermutation import level_superpermutation
from levels.level_syracuse import level_syracuse
from levels.level_takuzu import level_takuzu
from levels.level_taxicab_number import level_taxicab_number
from levels.level_temple import level_temple
from levels.level_tesseract import level_tesseract
from levels.level_tetrahedron import level_tetrahedron
from levels.level_tetris import level_tetris
from levels.level_travelling_salesman import level_travelling_salesman
from levels.level_tree import level_tree
from levels.level_triangulate import level_triangulate
from levels.level_vortex import level_vortex
from levels.level_wasted import level_wasted
from levels.level_water_pouring import level_water_pouring
from levels.level_wave import level_wave
from levels.level_weights import level_weights
from levels.level_xor import level_xor
from levels.level_zebra import level_zebra

from levels.level_random_K2 import aux_level_random_K2
from levels.level_random_K5 import aux_level_random_K5
from levels.level_random_K33 import aux_level_random_K33
from levels.level_random_star import aux_level_random_star
from levels.level_random_starting_point import aux_level_random_starting_point
from levels.level_random_loop import aux_level_random_loop
from levels.level_random_line import aux_level_random_line
from levels.level_random_binary_tree import aux_level_random_binary_tree
from levels.level_random_wheel import aux_level_random_wheel
from levels.level_random_bull import aux_level_random_bull
from levels.level_random_butterfly import aux_level_random_butterfly
from levels.level_random_come_back import aux_level_random_come_back
from levels.level_random_gemini import aux_level_random_gemini
from levels.level_random_ladder import aux_level_random_ladder
from levels.level_random_boustrophedon import aux_level_random_boustrophedon
from levels.level_random_simple import aux_level_random_simple
from levels.level_random_petersen import aux_level_random_petersen
from levels.level_random_cuboctahedron import aux_level_random_cuboctahedron

# Hungarian Rings

class Levels:
    levels_functions_list = [#level_the_4th_dimension,
        level_hello_world,
        level_initiation,
        level_linear,
        level_loop,
        level_backward,
        level_bis_repetita,
        level_binary,
        level_or,
        level_crossroad,
        level_square,
        level_infinity,
        level_fluid,
        level_numeration,
        level_sum,
        level_product,
        level_congruence,
        level_3sat,
        level_point_of_no_return,
        level_bipartite,
        level_hamiltonian,
        level_pong,
        level_longest_path,
        level_hitting_set,
        level_independent_set,
        level_dominating_set,
        level_exact_cover,
        level_odd,
        level_triangulate,
        level_recurrence,
        level_naturals,
        level_wasted,
        level_doppelganger,
        level_compact,
        level_random_simple,
        level_random_boustrophedon,
        level_parallel,
        level_random_bull,
        level_pythagorean,
        level_random_butterfly,
        level_elementary,
        level_rotation,
        level_superpermutation,
        level_chessboard,
        level_dichotomy,
        level_random_star,
        level_partition,
        level_second,
        level_knapsack,
        level_random_K2,
        level_egyptian_fractions,
        level_code,
        level_random_binary_tree,
        level_taxicab_number,
        level_tetrahedron,
        level_small,
        level_strange,
        level_the_4_queens,
        level_k,
        level_alice_and_bob,
        level_rotation_bis,
        level_nonogram,
        level_crystal,
        level_mastermind,
        level_tetris,
        level_xor,
        level_lights_out,
        level_weights,
        level_baguenaudier,
        level_spare,
        level_4_colors_theorem,
        level_grid,
        level_flash_back,
        level_spaceship,
        level_magic_square,
        level_matrix,
        level_river,
        level_vortex,
        level_tree,
        level_dead_ends,
        level_betweenness,
        level_fractal,
        level_tesseract,
        level_random_loop,
        level_oval_track_puzzle,
        level_cartesian,
        level_random_line,
        level_eulerian,
        level_random_starting_point,
        level_sujiko,
        level_electricity,
        level_random_wheel,
        level_pancake_sorting,
        level_random_ladder,
        level_wave,
        level_cube,
        level_random_come_back,
        level_inversions,
        level_permutations,
        level_random_K5,
        level_takuzu,
        level_random_K33,
        level_travelling_salesman,
        level_random_petersen,
        level_no_three_in_line,
        level_manhattan_distance,
        level_random_gemini,
        level_random_cuboctahedron,
        level_diagonal,
        level_sudoku,
        level_knight,
        level_temple,
        level_syracuse,
        level_five,
        level_shuffled,
        level_sign,
        level_combinatorics,
        level_hungarian_rings,
        level_water_pouring,
        level_puzzle,
        level_solitaire,
        level_mols,
        level_small_panex,
        level_zebra,
        level_parking,
        level_panex,
        level_superflip,
    ]

    aux_level_function_list = [
        aux_level_random_simple,
        aux_level_random_bull,
        aux_level_random_butterfly,
        aux_level_random_star,
        aux_level_random_K2,
        aux_level_random_binary_tree,
        aux_level_random_line,
        aux_level_random_loop,
        aux_level_random_wheel,
        aux_level_random_boustrophedon,
        aux_level_random_come_back,
        aux_level_random_starting_point,
        aux_level_random_ladder,
        aux_level_random_K5,
        aux_level_random_K33,
        aux_level_random_petersen,
        aux_level_random_cuboctahedron,
        aux_level_random_gemini,
        # aux_level_random_tetractys
    ]

    number_of_levels = len(levels_functions_list)

    levels_list = [None for k in range(number_of_levels)]

    def get_level(level_number, fast_solution_finding=False, get_new_level=False):
        if get_new_level:
            Levels.levels_list[level_number] = Levels.levels_functions_list[level_number]()
        else:
            if Levels.levels_list[level_number] is None:
                if fast_solution_finding and len(signature(Levels.levels_functions_list[level_number]).parameters) > 0:
                    Levels.levels_list[level_number] = Levels.levels_functions_list[level_number](True)
                else:
                    Levels.levels_list[level_number] = Levels.levels_functions_list[level_number]()
            else:
                Levels.levels_list[level_number].reboot_solution()
        return Levels.levels_list[level_number]

    def save_solutions_txt(verbose=0,
                           do_it_fast=False,
                           multithreads=False,
                           fast_solution_finding=True,
                           max_calculation_time=float('inf'),
                           save_as_txt=True,
                           only_if_known_solution=False,
                           only_if_not_yet_calculated=False):
        t0 = time()
        txt = ''
        nb_iterations_list = []
        nb_operations_list = []
        for folder in ['solutions', 'solutions/levels', 'solutions/levels/random']:
            if not os_path_exists(folder):
                os_mkdir(folder)
        if not do_it_fast:
            calculations_times = [None for i in range(Levels.number_of_levels)]

            def find_solution(k):
                global n_level_sol_found
                level = Levels.get_level(k, fast_solution_finding)
                if verbose == 1 and multithreads:
                    print(f'\nLevel {k} : {level.name}')
                if level.name in ['Dichotomy', 'Mastermind', 'Zebra', 'Panex', 'Superflip']:
                    return
                if only_if_known_solution and level.fastest_solution is None:
                    return
                if verbose == 1 and multithreads:
                    txt = ' '.join(['Level', str(k), ':', level.name, '\n'])
                t2 = time()
                solutions, nb_iterations, nb_operations = level.find_all_solutions(stop_at_first_solution=False,
                                                                                   verbose=verbose * (not multithreads),
                                                                                   max_calculation_time=max_calculation_time,
                                                                                   level_number=k,
                                                                                   save_solutions_txt=True,
                                                                                   only_if_not_yet_calculated=only_if_not_yet_calculated)
                t3 = time()
                nb_iterations_list.append(nb_iterations)
                nb_operations_list.append(nb_operations)
                if verbose == 1 and multithreads:
                    for sol in solutions:
                        txt = txt + ' '.join(sol) + '\n'
                    if verbose >= 1:
                        txt = txt + str(t3 - t2) + 's'
                    txt = '\n' + txt + '\n'
                    if verbose > 0:
                        print(txt)
                calculations_times[k] = t3 - t2

            if multithreads:
                import threading
                l_threads = []
                for k in range(Levels.number_of_levels):  # creating the threads
                    thread = threading.Thread(target=find_solution, args=(k,))
                    l_threads.append(thread)
                n_threads = len(l_threads)
                print(f'number of threads : {n_threads}\n\n')
                for thread in l_threads:  # starting all the threads
                    thread.start()
                for thread in l_threads:  # waiting for all threads to end
                    thread.join()
            else:
                for k in range(Levels.number_of_levels):
                    find_solution(k)
                    sleep(1e-5)
        txt = ''
        for k in range(Levels.number_of_levels):
            level = Levels.get_level(k, fast_solution_finding)
            name = level.name
            try:
                txt += ''.join(('Level ', str(k), ' : ', name, '\n'))
                txt += str(level.fastest_solution) + '\n\n'
            except:
                print(txt, ('Level ', str(k), ' : ', name, '\n'))
                raise
        if save_as_txt:
            with open('solutions/solutions.txt', 'w') as f:  # solutions/ directory is ignored when pushed on github
                f.write(txt)
        if verbose == 1 and multithreads:
            t1 = time()
            if verbose >= 1:
                print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times, nb_iterations_list, nb_operations_list
        else:
            a = [1 for i in range(Levels.number_of_levels)]
            return a, a, a


def test_levels(test_random_levels=False):
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 15})

    print('\nTrying all solutions')
    for level_function in Levels.levels_functions_list:
        level = level_function()
        if level.fastest_solution is not None:
            r = level.try_solution(level.fastest_solution)
            if r != 2:
                print(level.name, 'wrong solution')

    print('\nSaving solutions')
    Levels.save_solutions_txt(do_it_fast=True, verbose=0)

    print('\nCalculating solutions lenghts')
    solutions_lenghts = []
    for level_function in Levels.levels_functions_list:
        level = level_function()
        if level.fastest_solution is not None:
            solutions_lenghts.append(len(level.fastest_solution.split(' ')))
    plt.figure(figsize=(15, 5))
    x_list = [i for i in range(len(solutions_lenghts))]
    plt.plot(x_list, solutions_lenghts, lw=0.3, color='k')
    plt.scatter(x_list, solutions_lenghts, lw=0.1, color='r')
    plt.xlabel('Level number')
    plt.ylabel('Number of actions in the solution')
    plt.close()

    if test_random_levels:
        print('Testing random levels')
        from numpy import array, median
        for aux_level in Levels.aux_level_function_list:
            print(aux_level().name)
            solution_length, number_of_solutions = calculates_random_level_solution_length(aux_level)
            if solution_length == []:
                print('*')
                continue
            print('len', len(solution_length))
            print('solutions length')
            print('min', min(solution_length))
            print('avg', sum(solution_length) / len(solution_length))
            print('med', median(array(solution_length)))
            print('max', max(solution_length))
            print('number of solutions')
            print('min', min(number_of_solutions))
            print('avg', sum(number_of_solutions) / len(number_of_solutions))
            print('med', median(array(number_of_solutions)))
            print('max', max(number_of_solutions))
            bins_list = [i for i in range(max(solution_length) + 1)]
            plt.figure(figsize=(30, 5))
            plt.hist(solution_length, bins=bins_list)
            plt.xticks(bins_list)
            plt.show()
            print('')


def calculates_random_level_solution_length(aux_level_function):
    from os import listdir as os_listdir
    from os.path import exists as os_path_exists
    from Maze import Maze
    folder = f'levels/{aux_level_function().name}'
    solution_length = []
    number_of_solutions = []
    if os_path_exists(folder):
        for file_name in os_listdir(folder):
            level = Maze.get_random_level_from_file(aux_level_function, file_name)
            solutions = level.find_all_solutions(verbose=0, stop_at_first_solution=False)[0]
            try:
                solution_length.append(len(solutions[0]))
                number_of_solutions.append(len(solutions))
            except IndexError:
                level.find_all_solutions(verbose=1, stop_at_first_solution=False, nb_iterations_print=1)
                print(file_name)
                raise
    return solution_length, number_of_solutions


if __name__ == "__main__":
    pass

    import os
    # import collections
    # import numpy as np

    if os.path.exists('temp.txt'):
        os.remove('temp.txt')

    test_levels()
    
    solutions = level_the_4th_dimension().find_all_solutions(verbose=2, nb_iterations_print=10**4, stop_at_first_solution=False)

    # import cProfile
    # cProfile.run('''Levels.save_solutions_txt(verbose=1, multithreads=False, max_calculation_time=float('inf'), save_as_txt=False)''', sort=1)