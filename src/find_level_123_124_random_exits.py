from levels.level_123_124 import aux
import itertools

ll = itertools.permutations([0, 1, 2, 3])

for l in ll:
    solutions_that_work, nb_iterations, nb_operations = aux(l).find_all_solutions()
    if len(solutions_that_work) != 0:
        print(l)