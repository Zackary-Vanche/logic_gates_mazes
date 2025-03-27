import levels as lvls
from itertools import product

all_l = list(product([0, 1], repeat=4))

for l in all_l:
    solutions_that_work, nb_iterations, nb_operations = lvls.level_exclusive.aux(l).find_all_solutions()
    if len(solutions_that_work) == 1:
        print(l)