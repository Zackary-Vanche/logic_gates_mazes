from Maze import Maze
from Levels import Levels
import os
from levels.level_cube import level_cube
from levels.level_oval_track_puzzle import level_oval_track_puzzle

def create_random_levels(a, b):
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=a+b, i0=a)

if __name__ == '__main__':
    for aux_level in Levels.aux_level_function_list:
        print(aux_level().name)
        Maze.save_random_door_trees_list(aux_level, n_files=128, i0=0)
        
    for level in [level_cube(),
                  level_oval_track_puzzle(),]:
        exits_txt = f'levels/{level.name}_random_exits.txt'
        if not os.path.exists(exits_txt):
            solutions = level.find_all_solutions(stop_at_first_solution=False, verbose=0, nb_iterations_print=10**4)
            with open(exits_txt, 'w') as fw:
                for sol in solutions[0]:
                    level.try_solution(sol)
                    fw.write(f"{''.join([str(S.value) for S in level.switches_list])}\n")