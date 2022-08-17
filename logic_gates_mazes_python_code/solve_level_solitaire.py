# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:33:47 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from levels.level_solitaire import level_solitaire
from time import time

possibles_moves = [
                   '''D0 S0 S1 S2 D2 D4 D6 D8 D10''',
                   '''D0 S1 S2 S3 D2 D4 D6 D8 D10''',
                   '''D0 S2 S3 S4 D2 D4 D6 D8 D10''',
                   '''D0 D2 S6 S7 S8 D4 D6 D8 D10''',
                   '''D0 D2 S7 S8 S9 D4 D6 D8 D10''',
                   '''D0 D2 D4 S12 S13 S14 D6 D8 D10''',
                   
                   '''D0 S0 D2 S6 D4 S12 D6 D8 D10''',
                   '''D0 D2 S6 D4 S12 D6 S18 D8 D10''',
                   '''D0 D2 D4 S12 D6 S18 D8 S24 D10''',
                   '''D0 S1 D2 S7 D4 S13 D6 D8 D10''',
                   '''D0 D2 S7 D4 S13 D6 S19 D8 D10''',
                   '''D0 S2 D2 S8 D4 S14 D6 D8 D10''',
                   
                   '''D0 S4 D2 S9 D4 S14 D6 D8 D10''',
                   '''D0 D2 S9 D4 S14 D6 S19 D8 D10''',
                   '''D0 D2 D4 S14 D6 S19 D8 S24 D10''',
                   '''D0 S3 D2 S8 D4 S13 D6 D8 D10''',
                   '''D0 D2 S8 D4 S13 D6 S18 D8 D10''',
                   '''D0 S2 D2 S7 D4 S12 D6 D8 D10''',

                   '''D1 D3 D5 S15 S16 S17 D7 D9 D11''',
                   '''D1 D3 D5 D7 S20 S21 S22 D9 D11''',
                   '''D1 D3 D5 D7 S21 S22 S23 D9 D11''',
                   '''D1 D3 D5 D7 D9 S25 S26 S27 D11''',
                   '''D1 D3 D5 D7 D9 S26 S27 S28 D11''',
                   '''D1 D3 D5 D7 D9 S27 S28 S29 D11''',
                   
                   '''D1 S5 D3 S11 D5 S17 D7 D9 D11''',
                   '''D1 D3 S11 D5 S17 D7 S23 D9 D11''',
                   '''D1 D3 D5 S17 D7 S23 D9 S29 D11''',
                   '''D1 D3 S10 D5 S16 D7 S22 D9 D11''',
                   '''D1 D3 D5 S16 D7 S22 D9 S28 D11''',
                   '''D1 D3 D5 S15 D7 S21 D9 S27 D11''',
                   
                   '''D1 S5 D3 S10 D5 S15 D7 D9 D11''',
                   '''D1 D3 S10 D5 S15 D7 S20 D9 D11''',
                   '''D1 D3 D5 S15 D7 S20 D9 S25 D11''',
                   '''D1 D3 S11 D5 S16 D7 S21 D9 D11''',
                   '''D1 D3 D5 S16 D7 S21 D9 S26 D11''',
                   '''D1 D3 D5 S17 D7 S22 D9 S27 D11''',
                   ]

return_doors = ['D12', 'D13', 'D14', 'D15']

def solve_level_solitaire(verbose=0,
                          nb_iterations_print=10**3,
                          stop_at_first_solution=False):
    level = level_solitaire()
    t0 = time()
    visited_situations = set()
    solutions_to_visit = ['']
    solutions_that_work = []
    nb_iterations = 0
    while solutions_to_visit != []:
        # print(visited_situations)
        nb_iterations += 1
        if nb_iterations % nb_iterations_print == 0 and verbose >= 1:
            print('nb_iterations : {}'.format(nb_iterations))
            print('solutions_to_visit[-1] : {}'.format(solutions_to_visit[-1]))
            print('len(solutions_to_visit) : {}'.format(len(solutions_to_visit)))
            print("solutions_to_visit[-1].count('D') : {}".format(' '.join(solutions_to_visit[-1]).count('D')))
            print('len(solutions_to_visit)/nb_iterations : {}'.format(len(solutions_to_visit)/nb_iterations))
            print('len(solutions_that_work) : {}'.format(len(solutions_that_work)))
            print('')
        solution = solutions_to_visit.pop(0)
        result_solution = level.try_solution(solution)
        current_situation_vector = level.current_situation_to_vector()
        # print('solution tried', solution, result_solution)
        if result_solution == 1:
            current_room_name = level.current_room_name()
            # print(current_room_name)
            if current_situation_vector not in visited_situations:
                if current_room_name == 'R11':
                    for pm in possibles_moves:
                        new_sol = ' '.join([solution, pm])
                        solutions_to_visit.append(new_sol)
                        # print(new_sol)
                elif current_room_name == 'R10':
                    for rd in return_doors:
                        new_sol = ' '.join([solution, rd])
                        solutions_to_visit.append(new_sol)
                        # print(new_sol)
            # else:
            #     print('already visited', current_situation_vector, visited_situations)
            visited_situations.add(current_situation_vector)
        elif result_solution == 2:
            solutions_that_work.append(solution)
            print(solution)
        level.reboot_solution()
    else:
        solutions_that_work = level.all_solutions
    print("solutions found")
    print(solutions_that_work)
    print("solution in memory")
    print(str(level.fastest_solution))
    print('')
    level.all_solutions = solutions_that_work
    if verbose >= 1:
        t1 = time()
        print(t1 - t0, 's')
    return solutions_that_work

if __name__ == '__main__':
    
    l = ''''D0 S0 S1 S2 S3 S4 D2 S6 S7 S8 S9 D4 S12 S13 S14 D6 S18 S19 D8 S24 D10
D1 S5 D3 S10 S11 D5 S15 S16 S17 D7 S20 S21 S22 S23 D9 S25 S26 S27 S28 S29 D11'''
    for pm in possibles_moves:
        pm = pm.split(' ')
        li = []
        for a in pm:
            assert a in l, a
            li.append(l.index(a))
        assert sorted(li) == li, pm
    
    solutions = solve_level_solitaire(verbose=1, nb_iterations_print=10**4)



































