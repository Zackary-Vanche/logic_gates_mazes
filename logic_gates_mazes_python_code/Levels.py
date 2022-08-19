# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:12:20 2022

@author: utilisateur
"""

from time import time
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from inspect import signature

from levels.level_3sat import level_3sat
from levels.level_4_colors_theorem import level_4_colors_theorem
from levels.level_the_4_queens import level_the_4_queens
from levels.level_alice_and_bob import level_alice_and_bob
from levels.level_backward import level_backward
from levels.level_betweenness import level_betweenness
from levels.level_binary import level_binary
from levels.level_bipartite import level_bipartite
from levels.level_bis_repetita import level_bis_repetita
from levels.level_cartesian import level_cartesian
from levels.level_chessboard import level_chessboard
from levels.level_congruence import level_congruence
from levels.level_crossroad import level_crossroad
from levels.level_crystal import level_crystal
from levels.level_dead_ends import level_dead_ends
from levels.level_dominating_set import level_dominating_set
from levels.level_electricity import level_electricity
from levels.level_eulerian import level_eulerian
from levels.level_exact_cover import level_exact_cover
from levels.level_fluid import level_fluid
from levels.level_fractal import level_fractal
from levels.level_hamiltonian import level_hamiltonian
from levels.level_hello_world import level_hello_world
from levels.level_hitting_set import level_hitting_set
from levels.level_independent_set import level_independent_set
from levels.level_infinity import level_infinity
from levels.level_knapsack import level_knapsack
from levels.level_knight import level_knight
from levels.level_linear import level_linear
from levels.level_longest_path import level_longest_path
from levels.level_loop import level_loop
from levels.level_manhattan_distance import level_manhattan_distance
from levels.level_matrix import level_matrix
from levels.level_magic_square import level_magic_square  # kakuro
from levels.level_naturals import level_naturals
from levels.level_nonogram import level_nonogram
from levels.level_no_three_in_line import level_no_three_in_line
from levels.level_odd import level_odd
from levels.level_or import level_or
from levels.level_pancake_sorting import level_pancake_sorting
from levels.level_parallel import level_parallel
from levels.level_partition import level_partition
from levels.level_permutation import level_permutation
from levels.level_point_of_no_return import level_point_of_no_return
from levels.level_puzzle import level_puzzle
from levels.level_pythagorean import level_pythagorean
from levels.level_pong import level_pong
from levels.level_recurrence import level_recurrence
from levels.level_river import level_river
from levels.level_square import level_square
from levels.level_solitaire import level_solitaire
from levels.level_sudoku import level_sudoku
from levels.level_sujiko import level_sujiko
from levels.level_syracuse import level_syracuse
from levels.level_temple import level_temple
from levels.level_taxicab_number import level_taxicab_number
from levels.level_tesseract import level_tesseract
from levels.level_tetrahedron import level_tetrahedron
from levels.level_tetris import level_tetris
from levels.level_travelling_salesman import level_travelling_salesman
from levels.level_tree import level_tree
from levels.level_water_pouring import level_water_pouring
from levels.level_wave import level_wave
from levels.level_xor import level_xor


class Levels:

    levels_functions_list = [level_hello_world,
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
                             level_recurrence,
                             level_naturals,
                             level_parallel,
                             level_pythagorean,
                             level_chessboard,
                             level_partition,
                             level_knapsack,
                             level_permutation,
                             level_betweenness,
                             level_taxicab_number,
                             level_tetrahedron,
                             level_the_4_queens,
                             level_alice_and_bob,
                             level_nonogram,
                             level_crystal,
                             level_tetris,
                             level_xor,
                             level_4_colors_theorem,
                             level_magic_square,
                             level_matrix,
                             level_river,
                             level_tree,
                             level_dead_ends,
                             level_fractal,
                             level_tesseract,
                             level_cartesian,
                             level_eulerian,
                             level_sujiko,
                             level_electricity,
                             level_pancake_sorting,
                             level_wave,
                             level_travelling_salesman,
                             level_no_three_in_line,
                             level_manhattan_distance,
                             level_sudoku,
                             level_knight,
                             level_temple,
                             level_syracuse,
                             level_water_pouring,
                             level_puzzle,
                             level_solitaire,
                             ]

    number_of_levels = len(levels_functions_list)

    levels_list = [None for k in range(number_of_levels)]

    def get_level(level_number, fast_solution_finding=False):
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
                           max_calculation_time=float('inf')):
        t0 = time()
        txt = ''
        if not os_path_exists('solutions'):
            os_mkdir('solutions')
        if not do_it_fast:
            calculations_times = [None for i in range(Levels.number_of_levels)]

            def find_solution(k):
                level = Levels.get_level(k, fast_solution_finding)
                txt = '\n'
                name = level.name
                txt = txt + ' '.join(['Level', str(k), ':', name, '\n'])
                t2 = time()
                solutions = level.find_all_solutions(stop_at_first_solution=False,
                                                     verbose=0,
                                                     max_calculation_time=max_calculation_time)
                t3 = time()
                for sol in solutions:
                    txt = txt + ' '.join(sol) + '\n'
                if verbose >= 1:
                    txt = txt + str(t3 - t2) + 's'
                    calculations_times[k] = t3 - t2
                print(txt)
            if multithreads:
                import threading
                l_threads = []
                for k in range(Levels.number_of_levels):  # creating the threads
                    thread = threading.Thread(target=find_solution, args=(k,))
                    l_threads.append(thread)
                for thread in l_threads:  # starting all the threads
                    thread.start()
                for thread in l_threads:  # waiting for all threads to end
                    thread.join()
            else:
                for k in range(Levels.number_of_levels):
                    find_solution(k)
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
        with open('solutions/solutions.txt', 'w') as f:
            f.write(txt)
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    print('\nTrying all solutions')

    for level_function in Levels.levels_functions_list:
        level = level_function()
        if level.fastest_solution is not None:
            r = level.try_solution(level.fastest_solution)
            if r != 2:
                print(level.name, 'wrong solution')

    print('\nSaving solutions')

    Levels.save_solutions_txt(do_it_fast=True, verbose=1)

    print('\nCalculating solutions lenghts')

    solutions_lenghts = []
    for level_function in Levels.levels_functions_list:
        level = level_function()
        if level.fastest_solution is not None:
            solutions_lenghts.append(len(level.fastest_solution.split(' ')))
    plt.figure(figsize=(15, 5))
    x_list = [i for i in range(len(solutions_lenghts))]
    plt.plot(x_list,
             solutions_lenghts, lw=0.3, color='k')
    plt.scatter(x_list,
                solutions_lenghts, lw=0.1, color='r')
    plt.show()

    print('')

    # import cProfile
    # cProfile.run('solutions = level_manhattan_distance().find_all_solutions(verbose=1, stop_at_first_solution=False, nb_iterations_print=10**3)')

    # solutions = level_solitaire(True).find_all_solutions(verbose=1, stop_at_first_solution=False, nb_iterations_print=10**3)