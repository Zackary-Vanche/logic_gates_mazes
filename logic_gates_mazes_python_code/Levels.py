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
# from levels.level_4_queens import level_4_queens
# from levels.level_absolute import level_absolute # (tree)
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
# from levels.level_exact_cover import level_exact_cover
from levels.level_fluid import level_fluid
from levels.level_fractal import level_fractal
from levels.level_graph import level_graph # -> from levels.level_eulerian import level_eulerian
# from levels.level_hamiltonian import level_hamiltonian
from levels.level_hello_world import level_hello_world
# from levels.level_hitting_set import level_hitting_set
# from levels.level_ILP import level_ILP
from levels.level_independent_set import level_independent_set
from levels.level_infinity import level_infinity
# from levels.level_kakuro import level_kakuro
from levels.level_knapsack import level_knapsack
from levels.level_linear import level_linear
# from levels.level_longest_path import level_longest_path
from levels.level_loop import level_loop
from levels.level_manhattan_distance import level_manhattan_distance
from levels.level_matrix import level_matrix
from levels.level_naturals import level_naturals
from levels.level_odd import level_odd
# from levels.from levels.level_or import level_or
from levels.level_parallel import level_parallel
from levels.level_partition import level_partition
from levels.level_point_of_no_return import level_point_of_no_return
from levels.level_recurrence import level_recurrence
from levels.level_river import level_river
# from levels.level_set_cover import level_set_cover
# from levels.level_shortest_path import level_shortest_path
from levels.level_sinusoidal import level_sinusoidal # -> from levels.level_wave import level_wave
# from levels.level_sinusoidal import level_sinusoidal
from levels.level_square import level_square
# from levels.level_sudoku import level_sudoku
from levels.level_temple import level_temple
from levels.level_tesseract import level_tesseract
from levels.level_tetrahedron import level_tetrahedron
# from levels.level_travelling_salesman import level_travelling_salesman
from levels.level_tree import level_tree
from levels.level_xor import level_xor

# from levels.level_icone import level_icone
# from levels.level_random import level_random

class Levels: 
    
    levels_functions_list = [
                             # level_icone,
                             level_hello_world,
                             level_linear,
                             level_loop,
                             level_backward,
                             level_bis_repetita,
                             level_binary,
                             level_crossroad,
                             level_square,
                             level_fluid,
                             level_independent_set,
                             level_odd,
                             level_dominating_set,
                             level_chessboard,
                             level_point_of_no_return,
                             level_4_colors_theorem,
                             level_alice_and_bob,
                             level_recurrence,
                             level_partition,
                             level_infinity,
                             level_parallel,
                             level_matrix,
                             level_tetrahedron,
                             level_knapsack,
                             level_bipartite,
                             level_alien,
                             level_tesseract,
                             level_tree,
                             level_river,
                             level_crystal,
                             level_cartesian,
                             level_fractal,
                             level_xor,
                             level_graph,
                             level_dead_ends,
                             level_electricity,
                             level_sinusoidal,
                             level_manhattan_distance,
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
                # txt += str(level.simplify_solution()) + '\n\n'
        else:
            calculations_times = []
            for k in range(Levels.number_of_levels):
                # level = Levels.levels_functions_list[k]()
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
                    # txt += str(level.simplify_solution(sol)) + '\n'
                if verbose >= 1:
                    print(t3 - t2, 's')
                    calculations_times.append(t3 - t2)
                txt += '\n'
        with open('solutions/solutions.txt', 'w') as f:
            f.write(txt)
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times
    
if __name__ == "__main__":
    
    Levels.save_solutions_txt(do_it_fast=True)
    
    # DO NOT REMOVE THIS CODE
    # with open('Temp_help_menus.txt', 'w') as f:
    #     for level_function in Levels.levels_functions_list: #sorted(Levels.levels_functions_list, key = lambda level_function : level_function().name):
    #         level = level_function()
    #         f.write('help_menus_list["')
    #         f.write(level.name)
    #         f.write('"] = """')
    #         f.write(level.help_txt[0])
    #         f.write('"""\n\n')

    level = level_naturals

    solutions = level().find_all_solutions(verbose=3,
                                           stop_at_first_solution=False)
        
    print(solutions[-1])