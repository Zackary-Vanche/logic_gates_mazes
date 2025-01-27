from time import time, sleep
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from inspect import signature

import levels as lvls

from tree_geometry import make_chain as mkc

def flatten(liste):
    flat = []
    for l in liste:
        if isinstance(l, list):
            flat.extend(flatten(l))
        else:
            flat.append(l)
    return flat

class Levels:
    
    lt = mkc(lvls.level_trivial,
             lvls.level_choice,
             lvls.level_hello_world,
             lvls.level_playground,
             lvls.level_cardinal_directions,
             [lvls.level_initiation,
                [lvls.level_linear,
                 mkc(lvls.level_order,
                     lvls.level_blind_alleys,
                     lvls.level_dead_ends,),
                 mkc(lvls.level_orchard,
                     lvls.level_forest,
                     lvls.level_jungle,
                     lvls.level_rainforest,),
                 [lvls.level_loop,
                  mkc(lvls.level_yoyo,
                      lvls.level_power_down,),
                 mkc(lvls.level_crossroad,
                     lvls.level_backward,
                     lvls.level_square,
                     lvls.level_binary,
                     lvls.level_bis_repetita,
                     lvls.level_recurrence,
                     lvls.level_bipartite,
                     lvls.level_fluid,
                     lvls.level_parallel,
                     lvls.level_odd,
                     lvls.level_compact,
                     lvls.level_infinity,
                     lvls.level_crystal,
                     lvls.level_platonic,
                     lvls.level_small,
                     lvls.level_cartesian,
                     lvls.level_fractal,)],
                 [lvls.level_expand_and_simplify,
                  mkc(lvls.level_eliminate,
                      [lvls.level_3sat,
                      mkc(lvls.level_boustrophedon,
                          lvls.level_point_of_no_return,
                          lvls.level_stairs,
                          lvls.level_conjunctive_normal_form),
                      mkc(lvls.level_relay,
                          lvls.level_circuit,
                          lvls.level_network,
                          lvls.level_pyramid,
                          lvls.level_sheffer_stroke,
                          lvls.level_peirce_s_arrow,),]),
                  mkc(lvls.level_variable,
                     [lvls.level_boolean,
                      [lvls.level_alternation,
                        mkc(lvls.level_hut,
                            lvls.level_village,
                            lvls.level_palace,
                            lvls.level_mansion,
                            lvls.level_town,),
                       [lvls.level_numeration,
                        mkc(lvls.level_random_simple,
                         lvls.level_random_bull,
                         lvls.level_random_butterfly,
                         lvls.level_random_K2,
                         lvls.level_random_w6,
                         lvls.level_random_binary_tree,
                         lvls.level_random_star,
                         lvls.level_random_K5,
                         lvls.level_random_K33,
                         lvls.level_random_turning,
                         lvls.level_random_petersen,
                         lvls.level_random_line,
                         lvls.level_random_starting_point,
                         lvls.level_random_up_and_down,
                         lvls.level_random_come_back,
                         lvls.level_random_gemini,
                         lvls.level_random_cuboctahedron,),
                        [lvls.level_move,
                           mkc(lvls.level_tetrahedron,
                               lvls.level_octahedron,
                               lvls.level_cube,
                            mkc(lvls.level_meanders,
                                [lvls.level_wind_compass,
                                mkc(lvls.level_silex,
                                    lvls.level_spider,
                                    lvls.level_house,
                                    lvls.level_draw,),
                                mkc(lvls.level_desire_path,
                                    lvls.level_connect_the_dots,),
                                mkc(lvls.level_hamiltonian,
                                    lvls.level_eulerian,),
                                mkc(lvls.level_random_travelling_salesman,
                                    lvls.level_random_bottleneck_travelling_salesman,
                                    lvls.level_travelling_salesman),
                                mkc(lvls.level_longest_path,
                                    lvls.level_shortest_path,),]),
                            [lvls.level_shortcut,
                             mkc(lvls.level_walk,
                                 lvls.level_trail,
                                 lvls.level_path,
                                 mkc(lvls.level_love,
                                     [lvls.level_podium,
                                     mkc(lvls.level_singletons,
                                         lvls.level_intersection,
                                         lvls.level_traversal),
                                     mkc(lvls.level_roadblock,
                                         lvls.level_passage,
                                         lvls.level_impasse,
                                         lvls.level_route,)
                                     ]),
                                 mkc(lvls.level_water_lily,
                                     [lvls.level_wind_flower,
                                      mkc(lvls.level_journey,
                                          lvls.level_expedition,
                                          lvls.level_voyage,),
                                      mkc(lvls.level_harmony,
                                          lvls.level_worms,
                                          lvls.level_wander,
                                          lvls.level_sneckdown,
                                          lvls.level_central_symmetry,
                                          lvls.level_separation,)]),
                                 ),
                                 mkc(lvls.level_manhattan_distance,
                                     lvls.level_electricity,
                                     lvls.level_wave,),
                             ],
                            mkc(lvls.level_chessboard,
                                lvls.level_tour,
                                lvls.level_knight,),
                            [lvls.level_pong,
                            mkc(lvls.level_naturals,
                                lvls.level_doppelganger,
                                [lvls.level_flash_back,
                                 mkc(lvls.level_entropy,
                                     lvls.level_tree,
                                     lvls.level_tree_diameter,
                                     lvls.level_tesseract,
                                     lvls.level_bridges,
                                     lvls.level_chinese_postman_problem,),
                                 mkc(lvls.level_code,
                                     lvls.level_syracuse,)
                                 ],
                                ),   
                            [lvls.level_walls,
                            mkc(lvls.level_jail,
                                lvls.level_prison),
                            mkc(lvls.level_rampart,
                                lvls.level_fortification,)],],
                                ),
                           mkc(lvls.level_bonsai,
                               mkc(lvls.level_poppy,
                                   lvls.level_peony,
                                   lvls.level_geranium,
                                   lvls.level_petunia,
                                   lvls.level_iris,
                                   lvls.level_magnolia,
                                   lvls.level_orchid,
                                   [lvls.level_tulip,
                                    mkc(lvls.level_roses_are_red,
                                        lvls.level_edelweiss,
                                        lvls.level_violets_are_blue,),
                                    mkc(lvls.level_linear_arboricity,
                                        lvls.level_arboricity,
                                        lvls.level_forest_partition,),
                                    mkc(lvls.level_weights,
                                        lvls.level_sign,)]),
                               mkc(lvls.level_sunflower,
                                  lvls.level_minimum_spanning_tree,
                                  lvls.level_tetractys,
                                  lvls.level_honeycomb,),
                               mkc(lvls.level_willow,
                                   lvls.level_beech,
                                   lvls.level_birch,
                                   lvls.level_elm,
                                   lvls.level_maple,
                                   [lvls.level_pine,
                                    mkc(lvls.level_palm_tree,
                                        lvls.level_baobab,
                                        lvls.level_cedar,
                                        lvls.level_oak),
                                    mkc(lvls.level_bamboos,
                                        lvls.level_gingko_biloba,
                                        lvls.level_cypress),
                                    lvls.level_fir,]),
                               ),    
                           mkc(lvls.level_domination_number,
                               [lvls.level_chromatic,
                                lvls.level_chromagraph,
                                mkc(lvls.level_wheel,
                                    lvls.level_rainbow,
                                    lvls.level_coloring,),
                                mkc(lvls.level_leaves,
                                    lvls.level_branches,
                                    lvls.level_tree_skin,
                                    lvls.level_tree_bark,),
                                mkc(lvls.level_torus_maximum_matching,
                                    lvls.level_tetrahedron_maximum_matching,
                                    lvls.level_octahedron_maximum_matching,
                                    lvls.level_cube_maximum_matching,
                                    lvls.level_toroid_maximum_matching,
                                    lvls.level_moser_graph_maximum_matching,
                                    lvls.level_herringbone,
                                    lvls.level_perfect_matching,
                                    lvls.level_3_dimensional_matching,),
                                mkc(lvls.level_tetrahedron_edges_coloring,
                                    lvls.level_cube_edges_coloring,
                                    lvls.level_octahedron_edges_coloring,
                                    lvls.level_k5_edges_coloring,
                                    lvls.level_k6_edges_coloring,
                                    lvls.level_petersen_graph_edges_coloring),
                                lvls.level_articulation_point,
                                ],
                                mkc(lvls.level_spy,
                                    lvls.level_secret,
                                    lvls.level_dominating_set,
                                    lvls.level_hitting_set,
                                    lvls.level_independent_set,
                                    lvls.level_exact_cover,
                                    lvls.level_domatic_number,),
                               [lvls.level_shared,
                                mkc(lvls.level_cubic,
                                    lvls.level_molecule,
                                    lvls.level_zero_3_vertex_clique,
                                    lvls.level_points,
                                    lvls.level_dots,
                                    lvls.level_von_neumann_neighborhood,
                                    lvls.level_moore_neighborhood,
                                    lvls.level_4_colors_theorem,),
                                mkc(lvls.level_no_three_in_line,
                                    lvls.level_k,
                                    lvls.level_the_4_queens,
                                    lvls.level_the_8_queens,),
                                mkc(lvls.level_min_cut,
                                    lvls.level_max_flow,
                                    lvls.level_graph_realization_problem,)],
                               mkc(lvls.level_butterfly_graph,
                                   lvls.level_sierpinski,
                                   lvls.level_the_fourth_triangle,
                                   lvls.level_hexagon,
                                   lvls.level_octahedral_graph,
                                   lvls.level_hexagonal_bipyramid,
                                   lvls.level_triangles,),
                               [lvls.level_graceful_baby_path,
                                mkc(lvls.level_graceful_triangle,
                                    lvls.level_graceful_square,
                                    lvls.level_graceful_tetrahedron),
                                mkc(lvls.level_graceful_star,
                                    lvls.level_graceful_path,
                                    lvls.level_graceful_baby_caterpillar,
                                    lvls.level_graceful_firecracker,
                                    [lvls.level_graceful_caterpillar,
                                     lvls.level_graceful_random_tree,
                                     mkc(lvls.level_graceful_lobster,
                                         lvls.level_graceful_large_caterpillar,)]),
                                [lvls.level_harmonious_cycle,
                                 lvls.level_edge_graceful_tetrahedron,
                                 mkc(lvls.level_harmonious_caterpillar,
                                     lvls.level_harmonious_bull,
                                     lvls.level_harmonious_house,
                                     lvls.level_harmonious_star)],],),
                           ],
                      mkc(lvls.level_inside_out,
                          [lvls.level_sorted,
                           [lvls.level_bubble_sort,
                            mkc(lvls.level_odd_even_sort,
                                lvls.level_cocktail_sort,),
                            mkc(lvls.level_pigeonhole_sort,
                                lvls.level_insertion_sort,
                                lvls.level_selection_sort,
                                lvls.level_gnome_sort,
                                lvls.level_cycle_sort,
                                lvls.level_merge_sort,
                                lvls.level_quick_sort,
                                lvls.level_heapsort,
                                 lvls.level_pancake_sorting,)],
                          mkc(lvls.level_invert,
                              [lvls.level_permutate,
                               lvls.level_superpermutation,
                               mkc(lvls.level_3_cycle,
                                   lvls.level_elementary,
                                   lvls.level_permutations,
                                   lvls.level_inversions,
                                   lvls.level_spare,
                                   [lvls.level_vortex,
                                    mkc(lvls.level_first_guarini_s_problem,
                                        lvls.level_second_guarini_s_problem,),
                                    mkc(lvls.level_oval_track_puzzle,
                                        [lvls.level_puzzle,
                                         mkc(lvls.level_grid,
                                             lvls.level_line_and_columns,),
                                         mkc(lvls.level_panex,
                                             lvls.level_hungarian_rings,
                                             [lvls.level_cellular_automaton,
                                              lvls.level_spaceship,
                                              lvls.level_mountains,
                                              mkc(lvls.level_organize,
                                                  lvls.level_parking,)])]),
                                    mkc(lvls.level_box,
                                        lvls.level_error,),]),
                               mkc(lvls.level_temple,
                                   lvls.level_classified,
                                   lvls.level_baguenaudier,
                                   lvls.level_towers,
                                   lvls.level_solitaire,
                                   lvls.level_water_pouring,),
                               mkc(lvls.level_necklace,
                                   lvls.level_necklaces_enumeration),
                               ],),
                          mkc(lvls.level_alice_and_bob,
                              lvls.level_river,
                              lvls.level_cattle,
                              lvls.level_herd,),
                          lvls.level_lights_out,
                          mkc(lvls.level_wasted,
                             lvls.level_rotation,
                             lvls.level_rotation_bis,
                             lvls.level_the_4th_dimension,),
                          ]),
                       [lvls.level_sum,
                       [lvls.level_product,
                        [lvls.level_arithmetic,
                          mkc(lvls.level_one_third,
                              lvls.level_quaternary_cryptarithmetic,
                              lvls.level_two_plus_two_equals_four,
                              lvls.level_send_more_money),
                          mkc(lvls.level_fibonacci_sequence,
                              lvls.level_factorial,
                              lvls.level_prime_number,
                              lvls.level_eratosthenes,
                              lvls.level_euclidean_algorithm,),
                           mkc(lvls.level_iterations,
                               lvls.level_equation,
                               lvls.level_pythagorean,
                               lvls.level_triangulate,
                               lvls.level_congruence,
                               lvls.level_second,
                               lvls.level_the_answer,
                               lvls.level_coincidence,
                               lvls.level_printer_error,
                               lvls.level_random_matrix_inversion,
                               lvls.level_egyptian_fractions,
                               lvls.level_strange,
                               lvls.level_taxicab_number,
                               lvls.level_matrix,),
                           mkc(lvls.level_partition,
                               lvls.level_knapsack,
                               lvls.level_young_tableaux,
                               lvls.level_ferrers_diagram,
                               lvls.level_integer_partition,
                               lvls.level_integer_factorization,),
                           mkc(lvls.level_bloodline,
                               lvls.level_takuzu,
                               lvls.level_sujiko,
                               lvls.level_magic_circles,
                               lvls.level_magic_square,
                               lvls.level_melencolia_1,
                               lvls.level_diagonal,
                               lvls.level_sudoku,
                               lvls.level_mols,
                               lvls.level_combinatorics,
                               lvls.level_zebra,
                               lvls.level_five,
                               lvls.level_shuffled,)
                          ],
                        mkc(lvls.level_water_tower,
                            lvls.level_betweenness,
                            lvls.level_nonogram,
                            lvls.level_tetris,),
                        mkc(lvls.level_guess,
                            lvls.level_dichotomy,
                            lvls.level_mastermind,),
                        ],
    ]                     
    ]
    ]
    ]
    )
    ]
    ]
    ]
    )
    
    level_tree = lt
    
    aux_level_function_list = [
        lvls.level_random_simple.aux,
        lvls.level_random_bull.aux,
        lvls.level_random_butterfly.aux,
        lvls.level_random_star.aux,
        lvls.level_random_K2.aux,
        lvls.level_random_binary_tree.aux,
        lvls.level_random_line.aux,
        lvls.level_random_turning.aux,
        lvls.level_random_w6.aux,
        lvls.level_random_come_back.aux,
        lvls.level_random_starting_point.aux,
        lvls.level_random_up_and_down.aux,
        lvls.level_random_K5.aux,
        lvls.level_random_K33.aux,
        lvls.level_random_petersen.aux,
        lvls.level_random_cuboctahedron.aux,
        lvls.level_random_gemini.aux,
    ]
    
    levels_modules_list = flatten(level_tree)

    number_of_levels = len(levels_modules_list)

    levels_list = [None for k in range(number_of_levels)]

    def get_level(level_number, fast_solution_finding=False, get_new_level=False):
        if get_new_level:
            Levels.levels_list[level_number] = Levels.levels_modules_list[level_number](
            )
        else:
            try:
                level_number = level_number % Levels.number_of_levels
                if Levels.levels_list[level_number] is None:
                    if fast_solution_finding and len(signature(Levels.levels_modules_list[level_number].f).parameters) > 0:
                        Levels.levels_list[level_number] = Levels.levels_modules_list[level_number].f(True)
                    else:
                        Levels.levels_list[level_number] = Levels.levels_modules_list[level_number].f()
                else:
                    Levels.levels_list[level_number].reboot_solution()
            except IndexError:
                print(level_number)
                raise
        return Levels.levels_list[level_number]

    def save_solutions_txt(verbose=0,
                           do_it_fast=False,
                           multithreads=False,
                           fast_solution_finding=True,
                           max_calculation_time=float('inf'),
                           save_as_txt=True,
                           only_if_known_solution=False,
                           only_if_not_yet_calculated=False):
        t0 = time()
        txt = ''
        nb_iterations_list = []
        nb_operations_list = []
        for folder in ['solutions', 'solutions/levels', 'solutions/levels/random']:
            if not os_path_exists(folder):
                os_mkdir(folder)
        if not do_it_fast:
            calculations_times = [None for i in range(Levels.number_of_levels)]

            def find_solution(k):
                global n_level_sol_found
                level = Levels.get_level(k, fast_solution_finding)
                if verbose == 1 and multithreads:
                    print(f'\nLevel {k} : {level.name}')
                if level.name in ['Dichotomy',
                                  'Mastermind',
                                  'Harmony',
                                  'Honeycomb',
                                  'SEND + MORE = MONEY',
                                  'Zebra',
                                  'Separation',
                                  'Minimum spanning tree',
                                  'Panex',
                                  'Superflip']:
                    return
                if only_if_known_solution and level.fastest_solution is None:
                    return
                if verbose == 1 and multithreads:
                    txt = ' '.join(['Level', str(k), ':', level.name, '\n'])
                t2 = time()
                solutions, nb_iterations, nb_operations = level.find_all_solutions(stop_at_first_solution=False,
                                                                                   verbose=verbose * (not multithreads),
                                                                                   max_calculation_time=max_calculation_time,
                                                                                   level_number=k,
                                                                                   save_solutions_txt=True,
                                                                                   only_if_not_yet_calculated=only_if_not_yet_calculated)
                if len(solutions) == 0:
                    print('*'*100)
                    print(level.name, 'no solution')
                    print('*'*100)
                t3 = time()
                nb_iterations_list.append(nb_iterations)
                nb_operations_list.append(nb_operations)
                if verbose == 1 and multithreads:
                    for sol in solutions:
                        txt = txt + ' '.join(sol) + '\n'
                    if verbose >= 1:
                        txt = txt + str(t3 - t2) + 's'
                    txt = '\n' + txt + '\n'
                    if verbose > 0:
                        print(txt)
                calculations_times[k] = t3 - t2

            if multithreads:
                import threading
                l_threads = []
                for k in range(Levels.number_of_levels):  # creating the threads
                    thread = threading.Thread(target=find_solution, args=(k,))
                    l_threads.append(thread)
                n_threads = len(l_threads)
                print(f'number of threads : {n_threads}\n\n')
                for thread in l_threads:  # starting all the threads
                    thread.start()
                for thread in l_threads:  # waiting for all threads to end
                    thread.join()
            else:
                for k in range(Levels.number_of_levels):
                    find_solution(k)
                    sleep(1e-5)
        txt = ''
        for k in range(Levels.number_of_levels):
            level = Levels.get_level(k, fast_solution_finding)
            name = level.name
            try:
                txt += ''.join(('Level ', str(k), ' : ', name, '\n'))
                txt += str(level.fastest_solution) + '\n\n'
            except:
                print(txt, ('Level ', str(k), ' : ', name, '\n'))
                raise
        if save_as_txt:
            # solutions/ directory is ignored when pushed on github
            if do_it_fast:
                sol_file_name = 'solutions/solutions.txt'
            else:
                sol_file_name = 'solutions/calculated_solutions.txt'
            with open(sol_file_name, 'w') as f:
                f.write(txt)
        if verbose == 1 and multithreads:
            t1 = time()
            if verbose >= 1:
                print(t1 - t0, 's')
        if not do_it_fast:
            return calculations_times, nb_iterations_list, nb_operations_list
        else:
            a = [1 for i in range(Levels.number_of_levels)]
            return a, a, a


def test_levels(test_random_levels=False):
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 15})
    
    print('\nCheck levels duplications')
    all_mazes_list = []
    all_mazes_set = set()
    for level_function in Levels.levels_modules_list:
        maze = level_function.f()
        all_mazes_set.add(maze.name)
        all_mazes_list.append(maze)
    if len(all_mazes_set) != len(Levels.levels_modules_list):
        print("Some levels are duplicated in the list Levels.levels_modules_list")
    levels_folder_names_list = [x for x in dir(lvls) if x[:6] == 'level_']
    levels_used_names_list = [str(level_module).split('\\')[-1].split('.')[0] for level_module in Levels.levels_modules_list]
    print(len(levels_folder_names_list), 'levels')
    print(set(levels_folder_names_list) - set(levels_used_names_list), 'not used')
    
    print('\nCheck if "random" is specified when needed')
    for level_function in Levels.levels_modules_list:
        maze = level_function.f()
        if maze.fastest_solution is None:
            continue
        if maze.random:
            continue
        if maze.fastest_solution != level_function.f().fastest_solution:
            print(maze.name)
            

    print('\nTrying all solutions')
    for maze in all_mazes_list:
        assert not maze.name in ['', 'TODO', 'todo', 'temp']
        if maze.fastest_solution is not None:
            r = maze.try_solution(maze.fastest_solution)
            if r != 2:
                print(maze.name, 'wrong solution')
        elif not maze.random:
            if maze.name not in ['Panex', 'Superflip']:
                print(maze.name, 'no solution')

    print('\nSaving solutions')
    Levels.save_solutions_txt(do_it_fast=True, verbose=0)

    print('\nCalculating solutions lenghts')
    solutions_lenghts = []
    for maze in all_mazes_list:
        if maze.fastest_solution is not None:
            solutions_lenghts.append(len(maze.fastest_solution.split(' ')))
    plt.figure(figsize=(10, 5))
    x_list = [i for i in range(len(solutions_lenghts))]
    plt.plot(x_list, solutions_lenghts, lw=0.3, color='k')
    plt.scatter(x_list, solutions_lenghts, lw=0.1, color='r')
    plt.xlabel('Level number')
    plt.ylabel('Number of actions in the solution')
    plt.grid()
    plt.show()
    
    print('\nTesting some chosen levels')
    solutions = lvls.level_cartesian.f().find_all_solutions(verbose=2,
                                                     nb_iterations_print=10**4,
                                                     stop_at_first_solution=False)
    assert len(solutions[0]) == 1
    sol = solutions[0][0]
    print("Cartesian")
    assert lvls.level_cartesian.f().fastest_solution == ' '.join(sol)
    print("Arithmetic")
    assert len(lvls.level_arithmetic.f().find_all_solutions()) != 0
    print("Numeration")
    assert len(lvls.level_numeration.f().find_all_solutions()) != 0
    print("3 cycle")
    assert len(lvls.level_3_cycle.f().find_all_solutions()) != 0
    print("Graceful random tree")
    assert len(lvls.level_graceful_random_tree.f().find_all_solutions()) != 0

    if test_random_levels:
        print('\nTesting random levels')
        from numpy import array, median
        for aux_level in Levels.aux_level_function_list:
            print(aux_level().name)
            solution_length, number_of_solutions = calculates_random_level_solution_length(
                aux_level)
            if solution_length == []:
                print('*')
                continue
            print('len', len(solution_length))
            print('solutions length')
            print('min', min(solution_length))
            print('avg', sum(solution_length) / len(solution_length))
            print('med', median(array(solution_length)))
            print('max', max(solution_length))
            print('number of solutions')
            print('min', min(number_of_solutions))
            print('avg', sum(number_of_solutions) / len(number_of_solutions))
            print('med', median(array(number_of_solutions)))
            print('max', max(number_of_solutions))
            bins_list = [i for i in range(max(solution_length) + 1)]
            plt.figure(figsize=(10, 5))
            plt.hist(solution_length, bins=bins_list)
            plt.xticks(bins_list)
            plt.show()
            print('')
    
    # worlds_level_list = []
    # for world_name in Levels.Worlds.keys():
    #     for level_function in Levels.Worlds[world_name]:
    #         worlds_level_list.append(level_function().name)
            
    # for level_function in Levels.levels_modules_list:
    #     name = level_function().name
    #     if not name in worlds_level_list:
    #         print(name)
            
    # worlds_level_set = set(worlds_level_list)
    # duplicates = set([item for item in worlds_level_list if worlds_level_list.count(item) > 1])
    # if all_level_set != worlds_level_set or duplicates != set():
    #     print(duplicates)
    #     print('')
    #     print(all_level_set - worlds_level_set)
    #     print('')
    #     print(worlds_level_set - all_level_set)
    
    print('\nEnd of the tests')


def calculates_random_level_solution_length(aux_level_function):
    from os import listdir as os_listdir
    from os.path import exists as os_path_exists
    from Maze import Maze
    folder = f'levels/{aux_level_function().name}'
    solution_length = []
    number_of_solutions = []
    if os_path_exists(folder):
        for file_name in os_listdir(folder):
            level = Maze.get_random_level_from_file(
                aux_level_function, file_name)
            solutions = level.find_all_solutions(
                verbose=0, stop_at_first_solution=False)[0]
            try:
                solution_length.append(len(solutions[0]))
                number_of_solutions.append(len(solutions))
            except IndexError:
                level.find_all_solutions(
                    verbose=1, stop_at_first_solution=False, nb_iterations_print=1)
                print(file_name)
                raise
    return solution_length, number_of_solutions


if __name__ == "__main__":
    pass

    test_levels()

    # import os
    
    # if not os.path.exists('temp'):
    #     os.mkdir('temp')
    
    # dico_i_level_name = {}
    # for i, level_funtion in enumerate(Levels.levels_modules_list):
    #     dico_i_level_name[level_funtion().name] = i
    
    # with open('temp/level_numbers.txt', 'w') as fw:
    #     for name in sorted(dico_i_level_name.keys()):
    #         i = dico_i_level_name[name]
    #         fw.write(f'{name: <25} {i}\n')
    
    # # # fast_solution_finding=True
    
    # level = lvls.level_harmonious_star.f()
    # solutions = level.find_all_solutions(verbose=3, save_solutions_txt=True,
    #                                       DFS=False,
    #                                       initial_try=())
    # print('\n')
    # print(len(solutions[0]))
    # print('\n')
    # for sol in solutions[0]:
    #     print(' '.join(sol))
        
    #    D0 S1 D1    D2 S3 D3 D4 D5 D6 D7
    # S0 D0 S1 D1    D2 S3 D3 D4 D5 D6 D7
    #    D0 S1 D1 S2 D2 S3 D3 D4 D5 D6 D7
    # S0 D0 S1 D1 S2 D2 S3 D3 D4 D5 D6 D7
    
        
    
#     sol_list = """S1 D0 S10 D0 D5 S4 D6 S9 D6 D5 D9 S6 D3 S17 D3 D9 S1 D0 D10 S13 D10 D0 D15
# S1 D0 S10 D0 D5 S4 D6 S9 D6 D5 D9 S6 D3 S17 D3 D9 S1 D0 S10 S11 D10 S12 D10 D0 D15""".split("\n")

#     nsol = 0
#     for sol in sol_list:
#         if level.try_solution(sol) == 2:
#             nsol += 1
#             print(sol)
#     print(nsol)
    
#     for sol in sol_list:
#         sol = sol.split(' ')
#         sol = [a for a in sol if 'S' in a]
#         sol = ' '.join(sol)
#         print(sol)
    
    # print(level.try_solution(level.fastest_solution, verbose=2))
    
    # #print(level.fastest_solution.count('D'))
    
    # all_roots_names = set()
    # for level_function in Levels.levels_modules_list:
    #     level = level_function()
    #     level_roots_names = level.roots_names_set
    #     if level_roots_names - all_roots_names != set():
    #         print(level.name, level_roots_names - all_roots_names)
    #         all_roots_names = all_roots_names | level_roots_names
    
    
    