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
             lvls.level_initiation,
             lvls.level_linear,
             lvls.level_electronic,
             lvls.level_variable,
                [lvls.level_expand_and_simplify,
                 mkc(lvls.level_orchard,
                     lvls.level_forest,
                     lvls.level_jungle,
                     lvls.level_rainforest,),
                 mkc(lvls.level_two_way_switch,
                     lvls.level_eliminate,
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
                 ],
                mkc(lvls.level_loop,
                    mkc(lvls.level_crossroad,
                        mkc(lvls.level_yoyo,
                            lvls.level_power_down,
                            lvls.level_boolean,
                            lvls.level_alternation),
                        mkc(lvls.level_backward,
                            lvls.level_square,
                            lvls.level_binary,
                            lvls.level_ebb_and_flow,
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
                            lvls.level_fractal,),
                        mkc(lvls.level_hut,
                            lvls.level_village,
                            lvls.level_palace,
                            lvls.level_mansion,
                            lvls.level_town,),
                        mkc(lvls.level_order,
                            [lvls.level_blind_alleys,
                             lvls.level_dead_ends,
                             lvls.level_keys,]),
                        )),
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
                  [lvls.level_easy,
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
                              lvls.level_connect_the_dots,
                              lvls.level_equality,),
                          mkc(lvls.level_hamiltonian,
                              lvls.level_eulerian,),
                          mkc(lvls.level_random_travelling_salesman,
                              lvls.level_random_bottleneck_travelling_salesman,
                              lvls.level_travelling_salesman),
                          mkc(lvls.level_shortest_path,
                              lvls.level_minimize,
                              lvls.level_longest_path,
                              lvls.level_maximize),]),
                      mkc(lvls.level_hamiltonian_path,
                          lvls.level_traceable_path,
                          lvls.level_pentagramme,
                          lvls.level_k5_eulerian_circuit,
                          lvls.level_octahedron_eulerian_circuit),
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
                    [lvls.level_sapling,
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
                         mkc(lvls.level_spanning,
                             lvls.level_rising_sun,),
                         mkc(lvls.level_sunflower,
                            lvls.level_minimum_spanning_tree,
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
                              mkc(lvls.level_tetractys,
                                  lvls.level_bamboos,
                                  lvls.level_gingko_biloba,
                                  lvls.level_cypress),
                              lvls.level_fir,]),
                         ),],],   
                     [lvls.level_domination_number,
                         [lvls.level_matching,
                          [lvls.level_chromatic,
                          mkc(lvls.level_leaves,
                              lvls.level_branches,
                              lvls.level_tree_skin,
                              lvls.level_tree_bark,),
                          [lvls.level_rainbow,
                           [lvls.level_cubic,
                            mkc(lvls.level_colorful,
                                lvls.level_molecule,
                                lvls.level_von_neumann_neighborhood,
                                mkc(lvls.level_moore_neighborhood,
                                    mkc(lvls.level_wheel,
                                        lvls.level_coloring,
                                        lvls.level_zero_3_vertex_clique,
                                        lvls.level_ramsey_theorem,
                                        lvls.level_4_colors_theorem,),
                                mkc(lvls.level_exact_cover,
                                    lvls.level_articulation_point,)),
                                mkc(lvls.level_min_cut,
                                    lvls.level_max_flow,),),
                            mkc(lvls.level_tetrahedron_edges_coloring,
                                lvls.level_cube_edges_coloring,
                                lvls.level_octahedron_edges_coloring,
                                lvls.level_k5_edges_coloring,
                                lvls.level_k6_edges_coloring,
                                lvls.level_petersen_graph_edges_coloring),
                            mkc(lvls.level_torus_maximum_matching,
                                lvls.level_tetrahedron_maximum_matching,
                                lvls.level_octahedron_maximum_matching,
                                lvls.level_cube_maximum_matching,
                                lvls.level_toroid_maximum_matching,
                                lvls.level_moser_graph_maximum_matching,
                                lvls.level_herringbone,
                                lvls.level_perfect_matching,
                                lvls.level_3_dimensional_matching,),
                            ]],
                          [lvls.level_shared,
                           mkc(lvls.level_points,
                               lvls.level_dots,),
                           mkc(lvls.level_spy,
                               mkc(lvls.level_fish_graph_dominating_set,
                                   lvls.level_random_dominating_set,
                                   lvls.level_dominating_set,
                                   lvls.level_cross_graph_two_dominating_set,
                                   lvls.level_secret,
                                   mkc(lvls.level_rook_s_graph_dominating_set,
                                       lvls.level_bishop_s_graph_dominating_set,
                                       lvls.level_king_s_graph_dominating_set,
                                       lvls.level_grid_graph_dominating_set,
                                       lvls.level_knight_s_graph_dominating_set),
                                   [lvls.level_domatic_number],),
                               mkc(lvls.level_hitting_set,
                                   lvls.level_independent_set),
                               ),
                           mkc(lvls.level_the_4_queens,
                               lvls.level_k,
                               lvls.level_the_8_queens,
                               lvls.level_no_three_in_line,
                               lvls.level_combinatorics,),
                           lvls.level_graph_realization_problem,],
                          ]],
                         mkc(lvls.level_claw_graph,
                             lvls.level_paw_graph,
                             [lvls.level_diamond_graph,
                              mkc(lvls.level_butterfly_graph,
                                  lvls.level_sierpinski,
                                  lvls.level_the_fourth_triangle,
                                  lvls.level_hexagon,
                                  lvls.level_octahedral_graph,
                                  lvls.level_hexagonal_bipyramid,
                                  lvls.level_K7,),
                             lvls.level_isomorphism,
                             mkc(lvls.level_self_complementary_graph,
                                 lvls.level_split,
                                 lvls.level_fracture)]),
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
                               lvls.level_harmonious_star)],],
                         ],
                     ],
                mkc(lvls.level_inside_out,
                    [lvls.level_sorted,
                    mkc(lvls.level_invert,
                        [lvls.level_permutate,
                         lvls.level_inverse_permutation,
                         mkc(lvls.level_necklace,
                             lvls.level_necklaces_enumeration,
                             lvls.level_necklace_splitting,),
                         lvls.level_superpermutation,
                        [lvls.level_decomposition,
                         [lvls.level_claw_graph_permutations,
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
                         lvls.level_inversions,
                         mkc(lvls.level_3_cycle,
                             lvls.level_flip,
                             lvls.level_elementary,
                             lvls.level_permutations,
                              mkc(lvls.level_spare,
                                   mkc(lvls.level_classified,
                                      lvls.level_baguenaudier,
                                      lvls.level_towers,
                                      [lvls.level_puzzle,
                                       mkc(lvls.level_solitaire,
                                           lvls.level_water_pouring,),
                                       mkc(lvls.level_panex,
                                           [lvls.level_vortex,
                                               mkc(lvls.level_oval_track_puzzle,
                                                   lvls.level_hungarian_rings,
                                                   lvls.level_spaceship,),
                                               lvls.level_cellular_automaton,
                                                mkc(lvls.level_valleys,
                                                    lvls.level_mountains,),
                                                mkc(lvls.level_organize,
                                                    lvls.level_parking,)])]),
                                  mkc(lvls.level_first_guarini_s_problem,
                                      lvls.level_second_guarini_s_problem,),
                                  mkc(lvls.level_temple,
                                      lvls.level_box,
                                      lvls.level_error,),)),
                         mkc(lvls.level_wasted,
                            lvls.level_rotation,
                            lvls.level_rotation_bis,
                            lvls.level_the_4th_dimension,),
                        lvls.level_order_of_a_permutation,]],
                         mkc(lvls.level_lights_out,
                             lvls.level_line_and_columns,
                             lvls.level_grid),
                         ],),
                    mkc(lvls.level_alice_and_bob,
                        lvls.level_river,
                        lvls.level_cattle,
                        lvls.level_herd,),
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
                        lvls.level_ploutos,
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
                         lvls.level_zebra,
                         lvls.level_five,
                         lvls.level_shuffled,)
                    ],
                  mkc(lvls.level_water_tower,
                      lvls.level_betweenness,
                      lvls.level_nonogram,
                      lvls.level_tetris,),
                  mkc(lvls.level_guess,
                      lvls.level_hypothesis,
                      lvls.level_dichotomy,
                      lvls.level_mastermind,),
                  ]],
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
                    # if fast_solution_finding and len(signature(Levels.levels_modules_list[level_number].f).parameters) > 0:
                    #     Levels.levels_list[level_number] = Levels.levels_modules_list[level_number].f(True)
                    # else:
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

# ANSI escape codes

def ansi_print(txt, color_code=None, bg_color_code=None, style_code=None):
    # Code ANSI de base pour réinitialiser tout effet
    reset = '\x1b[0m'
    
    # Les codes pour les couleurs de texte (de 30 à 37 pour les couleurs de base)
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'gray': '90',
        'bright_red': '91',
        'bright_green': '92',
        'bright_yellow': '93',
        'bright_blue': '94',
        'bright_magenta': '95',
        'bright_cyan': '96',
        'bright_white': '97'
    }

    # Les codes pour les couleurs de fond (de 40 à 47 pour les couleurs de base)
    bg_colors = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
        'gray': '100',
        'bright_red': '101',
        'bright_green': '102',
        'bright_yellow': '103',
        'bright_blue': '104',
        'bright_magenta': '105',
        'bright_cyan': '106',
        'bright_white': '107'
    }

    # Les codes pour les styles (gras, italique, etc.)
    styles = {
        'bold': '1',
        'underline': '4',
        'blink': '5',
        'inverse': '7',
        'hidden': '8'
    }
    
    # Construction du code ANSI final
    codes = []
    
    if color_code and color_code in colors:
        codes.append(colors[color_code])
    
    if bg_color_code and bg_color_code in bg_colors:
        codes.append(bg_colors[bg_color_code])
    
    if style_code and style_code in styles:
        codes.append(styles[style_code])
    
    # Construction de la chaîne ANSI
    final_code = '\x1b[' + ';'.join(codes) + 'm' if codes else ''
    
    # Affichage du texte avec les codes ANSI appliqués
    print(final_code + txt + reset)

def test_levels(test_random_levels=False, check_color_contrasts=True):
    from tqdm import tqdm
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 15})
    
    from Color import contrast_ratio
    
    title_color = 'cyan'
    second_title_color = 'bright_white'
    error_color = 'red'
    warning_color = 'magenta'
    
    ansi_print("\nCreate maze list", color_code=title_color)
    all_mazes_list = []
    all_mazes_set = set()
    for level_function in tqdm(Levels.levels_modules_list):
        t0 = time()
        maze = level_function.f()
        if time() - t0 > 1:
            ansi_print(f"\n{maze.name} takes {round(time() - t0, 2)} seconds to load", color_code=warning_color)
        all_mazes_set.add(maze.name)
        all_mazes_list.append(maze)
        
    ansi_print("\nCheck level name duplications", color_code=title_color)
    name_list = [maze.name for maze in all_mazes_list]
    name_list.sort()
    for i in range(len(name_list)-1):
        if name_list[i] == name_list[i+1]:
            ansi_print(f'''name "{name_list[i]}" duplicated''', color=error_color)
            
    ansi_print('\nCheck levels duplications', color_code=title_color)
    if len(all_mazes_set) != len(Levels.levels_modules_list):
        ansi_print("\nSome levels are duplicated in the list Levels.levels_modules_list",
                   color_code=error_color)
    levels_folder_names_list = [x for x in dir(lvls) if x[:6] == 'level_']
    levels_used_names_list = [str(level_module).split('\\')[-1].split('.')[0] for level_module in Levels.levels_modules_list]
    print(len(levels_folder_names_list), 'levels')
    print(set(levels_folder_names_list) - set(levels_used_names_list), 'not used')
    maze_names = [maze.name for maze in all_mazes_list]
    assert len(set(maze_names)) == len(maze_names)
    
    ansi_print('\nCheck if "random" is specified when needed', color_code=title_color)
    for i in tqdm(range(len(Levels.levels_modules_list))):
        level_function = Levels.levels_modules_list[i]
        maze = all_mazes_list[i]
        if maze.fastest_solution is None:
            continue
        if maze.random:
            continue
        if maze.fastest_solution != level_function.f().fastest_solution:
            ansi_print(maze.name, color=error_color)
            
    if check_color_contrasts:
        ansi_print('\nCheck color contrasts', color_code=title_color)
        background_contrast_ratio_list = []
        room_contrast_ratio_list = []
        surrounding_contrast_ratio_list = []
        contour_contrast_ratio_list = []
        line_contrast_ratio_list = []
        for maze in all_mazes_list:
            lcolor = maze.level_color
            
            background_contrast_ratio = contrast_ratio(lcolor.background_color,
                                                       lcolor.letters_color)
            
            line_contrast_ratio = min(contrast_ratio(lcolor.background_color,
                                                     lcolor.surrounding_color),
                                      contrast_ratio(lcolor.background_color,
                                                     lcolor.contour_color))
            
            room_contrast_ratio = contrast_ratio(lcolor.room_color,
                                                 lcolor.inside_room_color)
            
            surrounding_contrast_ratio = min(contrast_ratio(lcolor.room_color,
                                                            lcolor.surrounding_color),
                                             contrast_ratio(lcolor.background_color,
                                                            lcolor.surrounding_color))
            
            contour_contrast_ratio = min(contrast_ratio(lcolor.room_color,
                                                        lcolor.contour_color),
                                         contrast_ratio(lcolor.background_color,
                                                        lcolor.contour_color))
            
            background_contrast_ratio_list.append([background_contrast_ratio, maze.name])
            line_contrast_ratio_list.append([line_contrast_ratio, maze.name])
            room_contrast_ratio_list.append([room_contrast_ratio, maze.name])
            surrounding_contrast_ratio_list.append([surrounding_contrast_ratio, maze.name])
            contour_contrast_ratio_list.append([contour_contrast_ratio, maze.name])
            # if background_contrast_ratio < threshold_contrast_ratio:
            #     print(maze.name, f"bad contrast ratio ({background_contrast_ratio}) for letters/background")
            # if room_contrast_ratio < threshold_contrast_ratio:
            #     print(maze.name, f"bad contrast ratio ({room_contrast_ratio}) for letters/room")
        background_contrast_ratio_list.sort(key=lambda x : x[0])
        line_contrast_ratio_list.sort(key=lambda x : x[0])
        room_contrast_ratio_list.sort(key=lambda x : x[0])
        surrounding_contrast_ratio_list.sort(key=lambda x : x[0])
        contour_contrast_ratio_list.sort(key=lambda x : x[0])
        # print("\nLevels with worst line/background contrast ratio:")
        # for cr in line_contrast_ratio_list:
        #     if cr[0] < 2:
        #         print([round(cr[0], 3), cr[1]])
        print("\nLevels with worst letter/background contrast ratio:")
        for cr in background_contrast_ratio_list:
            if cr[0] < 5:
                print([round(cr[0], 3), cr[1]])
        print("\nLevels with worst letter/room contrast ratio:")
        for cr in room_contrast_ratio_list:
            if cr[0] < 5:
                print([round(cr[0], 3), cr[1]])
        # print("\nLevels with worst surrounding_color contrast ratio:")
        # for i in range(10):
        #     print(surrounding_contrast_ratio_list[i])
        # print("\nLevels with worst contour_color contrast ratio:")
        # for i in range(10):
        #     print(contour_contrast_ratio_list[i])

    ansi_print('\nTrying all solutions', color_code=title_color)
    for maze in tqdm(all_mazes_list):
        assert not maze.name in ['', 'TODO', 'todo', 'temp']
        if maze.fastest_solution is not None:
            r = maze.try_solution(maze.fastest_solution)
            if r != 2:
                ansi_print(f"\n{maze.name} wrong solution",
                           color_code=error_color)
        elif not maze.random:
            print(maze.name, 'no solution')
    
    ansi_print("\nTesting level Cartesian", color_code=title_color)
    solutions = lvls.level_cartesian.f().find_all_solutions(verbose=2,
                                                     nb_iterations_print=10**4,
                                                     stop_at_first_solution=False)
    assert len(solutions[0]) == 1
    sol = solutions[0][0]
    assert lvls.level_cartesian.f().fastest_solution == ' '.join(sol)
    
    ansi_print('\nTesting random levels with no given solution', color_code=title_color)
    for maze in all_mazes_list:
        if not maze.fastest_solution is None:
            continue
        ansi_print('\n'+maze.name, color_code=second_title_color)
        if not maze.random:
            ansi_print(f"\n{maze.name} should have a given solution (it is not random)!",
                       color_code=error_color)
        max_calculation_time = 60
        t0 = time()
        n_test = 0
        while time() - t0 < 10 and n_test < 5:
            t1 = time()
            solutions_that_work, nb_iterations, nb_operations = maze.find_all_solutions(max_calculation_time=max_calculation_time,
                                                                                        stop_at_first_solution=True)
            if len(solutions_that_work) == 0:
                if time() - t1 > max_calculation_time:
                    ansi_print(f"{maze.name} solution calculation is too long.",
                               color_code=warning_color)
                else:
                    ansi_print(f"{maze.name} doesn't have a solution !",
                               color_code=error_color)
                
            n_test += 1
        
        # if time() - t0 < 0.5:
        #     ansi_print(f"{maze.name} solution calculation is really short, it could be made during maze creation.",
        #                color_code=warning_color)
        
        print(f"{n_test} test(s)")
            
    if test_random_levels:
        ansi_print('\nTesting random levels', color_code=title_color)
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
            
    ansi_print('\nSaving solutions', color_code=title_color)
    Levels.save_solutions_txt(do_it_fast=True, verbose=0)
    
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

    test_levels(check_color_contrasts=False)
    
    # level = lvls.level_traceable_path.f()
    # solutions = level.find_all_solutions(verbose=3, save_solutions_txt=True,
    #                                       DFS=False,
    #                                       initial_try=())
    # print('\n')
    # print(len(solutions[0]))
    # print('\n')
    # for sol in solutions[0]:
    #     print(' '.join(sol))
    
    