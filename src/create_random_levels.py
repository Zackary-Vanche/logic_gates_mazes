from Maze import Maze
from Levels import Levels
import os
# from levels.level_the_4th_dimension import level_the_4th_dimension
from levels.level_cube import level_cube
from levels.level_error import level_error
from levels.level_grid import level_grid
from levels.level_oval_track_puzzle import level_oval_track_puzzle
from levels.level_rotation import level_rotation
from levels.level_rotation_bis import level_rotation_bis
from levels.level_wasted import level_wasted

def create_random_levels(a, b):
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=a+b, i0=a)

if __name__ == '__main__':
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=128, i0=0)
        
    for level in [#level_the_4th_dimension(),
                  level_cube(),
                  level_error(),
                  level_grid(),
                  level_oval_track_puzzle(),
                  level_rotation(),
                  level_rotation_bis(),
                  level_wasted()]:
        exits_txt = f'levels/{level.name}_random_exits.txt'
        if not os.path.exists(exits_txt):
            solutions = level.find_all_solutions(stop_at_first_solution=False, verbose=2, nb_iterations_print=10**4)
            with open(exits_txt, 'w') as fw:
                for sol in solutions[0]:
                    level.try_solution(sol)
                    fw.write(f"{''.join([str(S.value) for S in level.switches_list])}\n")