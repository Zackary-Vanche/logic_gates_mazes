from tqdm import tqdm
from itertools import product

import levels as lvls 

all_l = list(product([0, 1], repeat=10))

with open('levels/k5_eulerian_circuit_door_directions_list.txt', 'w') as f:
    for l in tqdm(all_l):
        maze = lvls.level_k5_eulerian_circuit.aux(l)
        solutions_that_work, nb_iterations, nb_operations = maze.find_all_solutions()
        if len(solutions_that_work) > 0:
            f.write(''.join([str(i) for i in l])+'\n')