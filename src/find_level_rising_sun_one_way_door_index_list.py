from tqdm import tqdm
from itertools import combinations

l_combi = list(combinations([i for i in range(12)], 6))

# l_not = [[0, 1],
#          [3, 9],
#          [6, 10],
#          [0, 2, 3, 4, 5],
#          [1, 2, 6, 7, 8],
#          [4, 7, 9, 11],
#          [5, 8, 10, 11]
#          ]

# l_all = []

# for combi in l_combi:
#     allowed = True
#     for l in l_not:
#         if all([i in combi for i in l]):
#             allowed = False
#             break
#     if allowed:
#         l_all.append(combi)
        
filename = 'levels/rising_sun_one_way_door_index_list.txt'
        
import levels as lvls

l_all = []
for one_way_door_index in tqdm(l_combi):
    maze = lvls.level_rising_sun.aux(one_way_door_index)
    initial_try = tuple([f"S{i}" for i in range(12) if not i in one_way_door_index])
    solutions = maze.find_all_solutions(initial_try=initial_try, stop_at_first_solution=True)[0]
    if len(solutions) != 0:
        l_all.append(one_way_door_index)
    