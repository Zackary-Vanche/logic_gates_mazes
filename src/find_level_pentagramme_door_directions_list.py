from tqdm import tqdm
from itertools import product

import levels as lvls 

all_l = list(product([0, 1], repeat=10))

with open('levels/pentagramme_door_directions_list.txt', 'w') as f:
    for l in tqdm(all_l):
        maze = lvls.level_pentagramme.aux(l)
        solutions_that_work, nb_iterations, nb_operations = maze.find_all_solutions()
        if len(solutions_that_work) == 1:
            f.write(''.join([str(i) for i in l])+'\n')
            # print(solutions_that_work)