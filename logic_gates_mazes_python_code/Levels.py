# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:12:20 2022

@author: utilisateur
"""

class Levels: 
    
    from level_backward import level_backward
    from level_binary import level_binary
    from level_cartesian import level_cartesian
    from level_crossroad import level_crossroad
    from level_crystal import level_crystal
    from level_dead_ends import level_dead_ends
    from level_electricity import level_electricity
    from level_fluid import level_fluid
    from level_graph import level_graph
    from level_hello_world import level_hello_world
    from level_infinity import level_infinity
    from level_icone import level_icone
    from level_linear import level_linear
    from level_loop import level_loop
    from level_odd import level_odd
    from level_parallel import level_parallel
    from level_point_of_no_return import level_point_of_no_return
    from level_recurrence import level_recurrence
    from level_sinusoidal import level_sinusoidal
    from level_square import level_square
    from level_tetrahedron import level_tetrahedron
    from level_xor import level_xor
        
    levels_functions_list = [#level_icone,
                             # level_sinusoidal,
                             level_hello_world,        # GREY
                             level_linear,             # BRIGHT GREEN
                             level_loop,               # RED
                             level_backward,           # BROWN
                             level_binary,             # BRIGHT BLUE AND GREY
                             level_crossroad,          # YELLOW
                             level_square,             # BLACK AND RED
                             level_fluid,              # GREEN_BLUE
                             level_odd,                # PURPLE
                             level_point_of_no_return, # BLUE
                             level_recurrence,         # BLACK AND WHITE
                             level_parallel,           # PINK
                             level_infinity,           # YELLOW AND BLACK
                             level_crystal,            # SALMON AND BRIGHT_GREY
                             level_tetrahedron,        # PURPLE_BLUE
                             level_cartesian,          # GREEN AND GREY
                             level_xor,                # RED AND ORANGE
                             level_graph,              # BLACK AND BLUE
                             level_dead_ends,          # DARK GREEN
                             level_electricity,        # YELLOW AND SILVER
                             level_sinusoidal          # BEIGE
                             ] 

    number_of_levels = len(levels_functions_list)
    
    levels_list = [None for k in range(number_of_levels)]
    
    def get_level(level_number):
        if Levels.levels_list[level_number] == None:
            Levels.levels_list[level_number] = Levels.levels_functions_list[level_number]()
        else:
            Levels.levels_list[level_number].reboot_solution()
        return Levels.levels_list[level_number]
    
if __name__ == "__main__":
    
    for level_function in Levels.levels_functions_list:
        level = level_function()
    