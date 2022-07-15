# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:12:20 2022

@author: utilisateur
"""

from time import time
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir

# from levels.level_3d_matching import level_3d_matching
# from levels.level_3sat import level_3sat
from levels.level_4_colors_theorem import level_4_colors_theorem
from levels.level_the_4_queens import level_the_4_queens
#from levels.level_absolute import level_absolute
from levels.level_alice_and_bob import level_alice_and_bob
from levels.level_alien import level_alien
from levels.level_backward import level_backward
from levels.level_binary import level_binary
from levels.level_bipartite import level_bipartite
from levels.level_bis_repetita import level_bis_repetita
from levels.level_cartesian import level_cartesian
from levels.level_chessboard import level_chessboard
from levels.level_crossroad import level_crossroad
from levels.level_crystal import level_crystal
from levels.level_dead_ends import level_dead_ends
from levels.level_dominating_set import level_dominating_set
from levels.level_electricity import level_electricity
from levels.level_eulerian import level_eulerian
from levels.level_exact_cover import level_exact_cover
from levels.level_fluid import level_fluid
from levels.level_fractal import level_fractal 
# from levels.level_hamiltonian import level_hamiltonian
from levels.level_hello_world import level_hello_world
from levels.level_hitting_set import level_hitting_set
# from levels.level_ILP import level_ILP
from levels.level_independent_set import level_independent_set
from levels.level_infinity import level_infinity
from levels.level_knapsack import level_knapsack
from levels.level_knight import level_knight
from levels.level_linear import level_linear
# from levels.level_longest_path import level_longest_path
from levels.level_loop import level_loop
from levels.level_manhattan_distance import level_manhattan_distance
from levels.level_matrix import level_matrix
from levels.level_magic_square import level_magic_square # kakuro
from levels.level_naturals import level_naturals
from levels.level_odd import level_odd
from levels.level_or import level_or
from levels.level_parallel import level_parallel
from levels.level_partition import level_partition
from levels.level_point_of_no_return import level_point_of_no_return
from levels.level_pythagorean import level_pythagorean
from levels.level_pong import level_pong
from levels.level_recurrence import level_recurrence
from levels.level_river import level_river
# from levels.level_set_cover import level_set_cover
# from levels.level_shortest_path import level_shortest_path
# from levels.level_sinusoidal import level_sinusoidal
from levels.level_square import level_square
# from levels.level_sudoku import level_sudoku
from levels.level_temple import level_temple
from levels.level_tesseract import level_tesseract
from levels.level_tetrahedron import level_tetrahedron
# from levels.level_travelling_salesman import level_travelling_salesman
from levels.level_tree import level_tree
from levels.level_wave import level_wave
from levels.level_xor import level_xor

# from levels.level_icone import level_icone
# from levels.level_random import level_random

class Levels: 
    
    levels_functions_list = [
                             # level_icone,
                             level_magic_square,
                             level_hello_world,
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
                             level_bipartite,
                             level_alien,
                             level_pong,
                             level_hitting_set,
                             level_independent_set,
                             level_dominating_set,
                             level_exact_cover,
                             level_odd,
                             level_recurrence,
                             level_naturals,
                             level_parallel,
                             level_pythagorean,
                             level_tetrahedron,
                             level_point_of_no_return,
                             level_chessboard,
                             level_the_4_queens,
                             level_alice_and_bob,
                             level_crystal,
                             level_4_colors_theorem,
                             level_partition,
                             level_knapsack,
                             level_xor,
                             level_matrix,
                             level_river,
                             level_tree,
                             level_fractal,
                             level_tesseract,
                             level_cartesian,
                             level_eulerian,
                             level_electricity,
                             level_wave,
                             level_dead_ends,
                             level_manhattan_distance,
                             level_knight,
                             level_temple,
                             #level_random,
                             ]

    number_of_levels = len(levels_functions_list)
    
    levels_list = [None for k in range(number_of_levels)]
    
    def get_level(level_number):
        if Levels.levels_list[level_number] == None:
            Levels.levels_list[level_number] = Levels.levels_functions_list[level_number]()
        else:
            Levels.levels_list[level_number].reboot_solution()
        return Levels.levels_list[level_number]
    
    def save_solutions_txt(verbose=0, do_it_fast=False):
        t0 = time()
        txt = ''
        if not os_path_exists('solutions'):
            os_mkdir('solutions')
        if do_it_fast:
            for k in range(Levels.number_of_levels):
                level = Levels.get_level(k)
                name = level.name
                if verbose > 0:
                    print('\nLevel', k, ':', name)
                txt += 'Level ' + str(k) + ' : ' + name + '\n'
                txt += str(level.fastest_solution) + '\n\n'
        else:
            calculations_times = []
            for k in range(Levels.number_of_levels):
                level = Levels.get_level(k)
                print('')
                name = level.name
                print('Level', k, ':', name)
                txt += 'Level ' + str(k) + ' : ' + name + '\n'
                t2 = time()
                solutions = level.find_all_solutions(stop_at_first_solution=False,
                                                     verbose=0)
                t3 = time()
                for sol in solutions:
                    print(sol)
                    txt += sol + '\n'
                if verbose >= 1:
                    print(t3 - t2, 's')
                    calculations_times.append(t3 - t2)
                txt += '\n' + level_dominating_set
        with open('solutions/solutions.txt', 'w') as f:
            f.write(txt)
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times
    
if __name__ == "__main__":
    
    Levels.save_solutions_txt(do_it_fast=True, verbose=0)
    
    # DO NOT REMOVE THIS CODE
    # with open('Temp_help_menus.txt', 'w') as f:
    #     for level_function in Levels.levels_functions_list: #sorted(Levels.levels_functions_list, key = lambda level_function : level_function().name):
    #         level = level_function()
    #         f.write('help_menus_list["')
    #         f.write(level.name)
    #         f.write('"] = """')
    #         f.write(level.help_txt[0])
    #         f.write('"""\n\n')

#    import cProfile
#    level = level_bipartite()
#    cProfile.run("solutions = level.find_all_solutions(verbose=3, stop_at_first_solution=False)")     
    
#    for level_function in [
#                             level_hello_world,
#                             level_linear,
#                             level_loop,
#                             level_backward,
#                             level_bis_repetita,
#                           ]:
#        level = level_function()
#        print(level.name)
#        solutions = level.find_all_solutions(verbose=3, stop_at_first_solution=False, nb_iterations_print=10**3)
#        print(solutions)
#    print('')
    
    
#    l = [('S0', 'S3', 'D0', 'D1', 'S9', 'S10', 'D2', 'S15', 'D3', 'S16', 'D4', 'S21', 'S23', 'D5', 'S24', 'S25', 'D6', 'S28', 'S30', 'D7', 'S32', 'S33', 'S35', 'D8', 'S37', 'D9', 'S42', 'D10', 'D11'), ('S0', 'S3', 'D0', 'D1', 'S9', 'S10', 'D2', 'S15', 'D3', 'S16', 'D4', 'S21', 'S23', 'D5', 'S26', 'D6', 'S29', 'D7', 'S32', 'S33', 'S35', 'D8', 'S36', 'S38', 'D9', 'S40', 'S41', 'D10', 'D11'), ('S1', 'S2', 'D0', 'D1', 'S8', 'S11', 'D2', 'S12', 'S13', 'S14', 'D3', 'S16', 'D4', 'S21', 'S23', 'D5', 'S24', 'S25', 'D6', 'S28', 'S30', 'D7', 'S32', 'S33', 'S35', 'D8', 'S37', 'D9', 'S42', 'D10', 'D11'), ('S1', 'S2', 'D0', 'D1', 'S8', 'S11', 'D2', 'S12', 'S13', 'S14', 'D3', 'S16', 'D4', 'S21', 'S23', 'D5', 'S26', 'D6', 'S29', 'D7', 'S32', 'S33', 'S35', 'D8', 'S36', 'S38', 'D9', 'S40', 'S41', 'D10', 'D11'), ('S1', 'S2', 'D0', 'S7', 'D1', 'S8', 'D2', 'S12', 'S13', 'S14', 'D3', 'S16', 'S19', 'D4', 'S21', 'D5', 'S24', 'S25', 'S27', 'D6', 'S28', 'S30', 'D7', 'S32', 'S33', 'D8', 'S37', 'S39', 'D9', 'S42', 'D10', 'D11'), ('S1', 'S2', 'D0', 'S7', 'D1', 'S8', 'D2', 'S12', 'S13', 'S14', 'D3', 'S16', 'S19', 'D4', 'S21', 'D5', 'S26', 'D6', 'S29', 'S31', 'D7', 'S32', 'S33', 'D8', 'S36', 'S38', 'D9', 'S40', 'S41', 'S43', 'D10', 'D11')]
#    
#    l = ['S0 S3 D0 D1 S9 S10 D2 S15 D3 S16 D4 S21 S23 D5 S24 S25 D6 S28 S30 D7 S32 S33 S35 D8 S37 D9 S42 D10 D11',
#     'S0 S3 D0 D1 S9 S10 D2 S15 D3 S16 D4 S21 S23 D5 S26 D6 S29 D7 S32 S33 S35 D8 S36 S38 D9 S40 S41 D10 D11',
#     'S1 S2 D0 D1 S8 S11 D2 S12 S13 S14 D3 S16 D4 S21 S23 D5 S24 S25 D6 S28 S30 D7 S32 S33 S35 D8 S37 D9 S42 D10 D11',
#     'S1 S2 D0 D1 S8 S11 D2 S12 S13 S14 D3 S16 D4 S21 S23 D5 S26 D6 S29 D7 S32 S33 S35 D8 S36 S38 D9 S40 S41 D10 D11',
#     'S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S24 S25 S27 D6 S28 S30 D7 S32 S33 D8 S37 S39 D9 S42 D10 D11',
#     'S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S26 D6 S29 S31 D7 S32 S33 D8 S36 S38 D9 S40 S41 S43 D10 D11']
    
    
    
#    l = ['S0 S3 D0 D1 S9 S10 D2 S15 D3 S16 D4 S21 S23 D5 S24 S25 D6 S28 S30 D7 S32 S33 S35 D8 S37 D9 D10 D11',
#     'S0 S3 D0 D1 S9 S10 D2 S15 D3 S16 D4 S21 S23 D5 S26 D6 S29 D7 S32 S33 S35 D8 S36 S38 D9 S40 S41 D10 D11',
#     'S1 S2 D0 D1 S8 S11 D2 S12 S13 S14 D3 S16 D4 S21 S23 D5 S24 S25 D6 S28 S30 D7 S32 S33 S35 D8 S37 D9 D10 D11',
#     'S1 S2 D0 D1 S8 S11 D2 S12 S13 S14 D3 S16 D4 S21 S23 D5 S26 D6 S29 D7 S32 S33 S35 D8 S36 S38 D9 D10 D11',
#     'S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S24 S25 S27 D6 S28 S30 D7 S32 S33 D8 S37 S39 D9 D10 D11',
#     'S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S26 D6 S29 S31 D7 S32 S33 D8 S36 S38 D9 D10 D11']
#    level = level_knight()
#    for sol in l:
#        print(sol)
#        print(level.try_solution(sol, verbose=0))
#    level_knight().try_solution('S1 S2 D0 S7 D1 S8 D2 S12 S13 S14 D3 S16 S19 D4 S21 D5 S26 D6 S29 S31 D7 S32 S33 D8 S36 S38 D9 D10 D11', verbose=2)
##    
    
    
#    l = ['S0 S3 S6 S11 S12 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S3 S4 S8 S11 S12 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S3 S4 S9 S10 S12 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S0 S2 S3 S6 S10 S11 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S0 S3 S6 S11 S12 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S0 S3 S7 S11 S12 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S2 S3 S4 S8 S10 S11 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S3 S4 S8 S11 S12 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S3 S4 S9 S10 S12 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S0 S2 S3 S6 S7 S10 S11 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S0 S2 S3 S6 S10 S11 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S2 S3 S4 S8 S10 S11 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S3 S4 S7 S8 S11 S12 S13 S14 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19',
#     'S2 S3 S4 S6 S7 S8 S10 S11 S13 S15 D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18 D19'] 
##    S2 S3 S4 S6 S7 S8 S10 S11 S13 S15
#    level = level_4_colors_theorem()
#    for sol in l:
#        print('nS', sol.count("S"))
#        print(sol.split(' D0')[0])
#        print(level.try_solution(sol, verbose=0))
    
    level_magic_square().find_all_solutions(verbose=3, stop_at_first_solution=False, nb_iterations_print=10**4)
    
    
