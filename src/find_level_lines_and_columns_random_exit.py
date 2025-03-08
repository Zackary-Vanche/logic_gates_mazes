import levels as lvls

maze = lvls.level_line_and_columns.f()
solutions_that_work, nb_iterations, nb_operations = maze.find_all_solutions()
sol_list = [' '.join(sol) for sol in solutions_that_work]

with open('levels/Line_and_columns_random_exits.txt', 'w') as fw:
    for sol in sol_list:
        maze.try_solution(sol)
        for S in maze.switches_list[1:]:
            if S.value:
                fw.write('T')
            else:
                fw.write('F')
        fw.write('\n')