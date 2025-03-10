import itertools
from tqdm import tqdm

import levels as lvls

lst = list(itertools.product([0, 1], repeat=14))

exit_lst = []

for l in tqdm(lst):
    if sum(l)%2 == 1:
        continue
    maze = lvls.level_necklace_splitting.aux(l)
    solutions_that_work, nb_iterations, nb_operations = maze.find_all_solutions(stop_at_first_solution=True, DFS=True)
    if len(solutions_that_work) != 0:
        exit_lst.append(l)
        
with open("levels/necklace_splitting_random_list.txt", 'w') as fw:
    for l in exit_lst:
        l = [str(x) for x in l]
        fw.write(''.join(l)+'\n')