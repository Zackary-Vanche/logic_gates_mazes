# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:12:20 2022

@author: utilisateur
"""

from time import time
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir

class Levels: 
    
    from level_alice_and_bob import level_alice_and_bob
    from level_alien import level_alien
    from level_backward import level_backward
    from level_binary import level_binary
    from level_bipartite import level_bipartite
    from level_bis_repetita import level_bis_repetita
    from level_cartesian import level_cartesian
    from level_chessboard import level_chessboard
    from level_crossroad import level_crossroad
    from level_crystal import level_crystal
    from level_dead_ends import level_dead_ends
    from level_electricity import level_electricity
    from level_fluid import level_fluid
    from level_fractal import level_fractal
    from level_graph import level_graph
    from level_hello_world import level_hello_world
    from level_infinity import level_infinity
    from level_icone import level_icone
    from level_linear import level_linear
    from level_loop import level_loop
    from level_manhattan_distance import level_manhattan_distance
    from level_odd import level_odd
    from level_parallel import level_parallel
    from level_point_of_no_return import level_point_of_no_return
    from level_recurrence import level_recurrence
    from level_river import level_river
    from level_sinusoidal import level_sinusoidal
    from level_square import level_square
    from level_temple import level_temple
    from level_tree import level_tree
    from level_tesseract import level_tesseract
    from level_tetrahedron import level_tetrahedron
    from level_xor import level_xor
        
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
                             level_odd,
                             level_chessboard,
                             level_point_of_no_return,
                             level_alice_and_bob,
                             level_recurrence,
                             level_parallel,
                             level_infinity,
                             level_tetrahedron,
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
                             level_temple
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
        if not os_path_exists('mazes'):
            os_mkdir('mazes')
        if do_it_fast:
            for k in range(Levels.number_of_levels):
                level = Levels.get_level(k)
                print('')
                name = level.name
                print('Level', k, ':', name)
                txt += name + '\n'
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
                txt += name + '\n'
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
        with open('mazes/solutions.txt', 'w') as f:
            f.write(txt)
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times
    
if __name__ == "__main__":
    
    for level_function in Levels.levels_functions_list:
        level = level_function()
    