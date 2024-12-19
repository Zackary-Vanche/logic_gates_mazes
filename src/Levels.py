from time import time, sleep
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from inspect import signature

import levels as lvls

class Levels:

    """    
    Problème du couplage maximal (Maximum Matching Problem) :
        Trouver un couplage (ensemble d'arêtes non adjacentes) de taille maximale dans un graphe.

    k_center

    k-mean

    Domatic partition

    Maximum coverage problem
    
    Random bin packing
    
    """

    levels_functions_list = [ 
        lvls.level_trivial.f,
        lvls.level_choice.f,
        lvls.level_hello_world.f,
        lvls.level_playground.f,
        lvls.level_initiation.f,
        lvls.level_cardinal_directions.f,
        lvls.level_linear.f,
        lvls.level_expand_and_simplify.f,
        lvls.level_domination_number.f,
        lvls.level_variable.f,
        lvls.level_order.f,
        lvls.level_loop.f,
        lvls.level_backward.f,
        lvls.level_boolean.f,
        lvls.level_alternation.f,
        lvls.level_yoyo.f,
        lvls.level_power_down.f,
        lvls.level_orchard.f,
        lvls.level_crossroad.f,
        lvls.level_bis_repetita.f,
        lvls.level_shared.f,
        lvls.level_boustrophedon.f,
        lvls.level_spy.f,
        lvls.level_leaves.f,
        lvls.level_binary.f,
        lvls.level_tetrahedron.f,
        lvls.level_bonsai.f,
        lvls.level_numeration.f,
        lvls.level_square.f,
        lvls.level_point_of_no_return.f,
        lvls.level_cubic.f,
        lvls.level_cube.f,
        lvls.level_3sat.f,
        lvls.level_sum.f,
        lvls.level_product.f,
        lvls.level_inside_out.f,
        lvls.level_chromatic.f,
        lvls.level_chromagraph.f,
        lvls.level_octahedron.f,
        lvls.level_fluid.f,
        lvls.level_congruence.f,
        lvls.level_infinity.f,
        lvls.level_forest.f,
        lvls.level_equation.f,
        lvls.level_von_neumann_neighborhood.f,
        lvls.level_moore_neighborhood.f,
        lvls.level_pong.f,
        lvls.level_bipartite.f,
        lvls.level_bloodline.f,
        lvls.level_hamiltonian.f,
        lvls.level_sorted.f,
        lvls.level_sheffer_stroke.f,
        lvls.level_peirce_s_arrow.f,
        lvls.level_longest_path.f,
        lvls.level_shortest_path.f,
        lvls.level_hitting_set.f,
        lvls.level_independent_set.f,
        lvls.level_dominating_set.f,
        lvls.level_one_third.f,
        lvls.level_quaternary.f,
        lvls.level_circle.f,
        lvls.level_exact_cover.f,
        lvls.level_connectivity.f,
        lvls.level_rainforest.f,
        lvls.level_secret.f,
        lvls.level_odd.f,
        lvls.level_molecule.f,
        lvls.level_water_tower.f,
        lvls.level_jungle.f,
        lvls.level_min_cut.f,
        lvls.level_max_cut.f,
        lvls.level_hut.f,
        lvls.level_arithmetic.f,
        lvls.level_tetrahedron_edges_coloring.f,
        lvls.level_triangulate.f,
        lvls.level_recurrence.f,
        lvls.level_stairs.f,
        lvls.level_sunflower.f,
        lvls.level_naturals.f,
        lvls.level_3_cycle.f,
        lvls.level_blind_alleys.f,
        lvls.level_wasted.f,
        lvls.level_doppelganger.f,
        lvls.level_meanders.f,
        lvls.level_shortcut.f,
        lvls.level_wind_compass.f,
        lvls.level_prime_number.f,
        lvls.level_points.f,
        lvls.level_poppy.f,
        lvls.level_peony.f,
        lvls.level_magnolia.f,
        lvls.level_iris.f,
        lvls.level_orchid.f,
        lvls.level_tulip.f,
        lvls.level_substract.f,
        lvls.level_remove.f,
        lvls.level_deduct.f,
        lvls.level_decrease.f,
        lvls.level_compact.f,
        lvls.level_village.f,
        lvls.level_town.f,
        lvls.level_fibonacci_sequence.f,
        lvls.level_palace.f,
        lvls.level_random_simple.f,
        lvls.level_parallel.f,
        lvls.level_eratosthenes.f,
        lvls.level_dots.f,
        lvls.level_random_bull.f,
        lvls.level_pythagorean.f,
        lvls.level_random_butterfly.f,
        lvls.level_elementary.f,
        lvls.level_young_tableaux.f,
        lvls.level_rotation.f,
        lvls.level_superpermutation.f,
        lvls.level_singletons.f,
        lvls.level_relay.f,
        lvls.level_circuit.f,
        lvls.level_network.f,
        lvls.level_pyramid.f,
        lvls.level_invert.f,
        lvls.level_permutate.f,
        lvls.level_desire_path.f,
        lvls.level_integer_partition.f,
        lvls.level_ferrers_diagram.f,
        lvls.level_integer_factorization.f,
        lvls.level_chessboard.f,
        lvls.level_silex.f,
        lvls.level_roses_are_red.f,
        lvls.level_edelweiss.f,
        lvls.level_violets_are_blue.f,
        lvls.level_walk.f,
        lvls.level_trail.f,
        lvls.level_path.f,
        lvls.level_entropy.f,
        lvls.level_bubble_sort.f,
        lvls.level_odd_even_sort.f,
        lvls.level_cocktail_sort.f,
        lvls.level_pigeonhole_sort.f,
        lvls.level_diminish.f,
        lvls.level_withdraw.f,
        lvls.level_withhold.f,
        lvls.level_detract.f,
        lvls.level_dichotomy.f,
        lvls.level_wheel.f,
        lvls.level_random_star.f,
        lvls.level_intersection.f,
        lvls.level_partition.f,
        lvls.level_second.f,
        lvls.level_insertion_sort.f,
        lvls.level_gnome_sort.f,
        lvls.level_knapsack.f,
        lvls.level_love.f,
        lvls.level_palm_tree.f,
        lvls.level_podium.f,
        lvls.level_willow.f,
        lvls.level_beech.f,
        lvls.level_birch.f,
        lvls.level_elm.f,
        lvls.level_maple.f,
        lvls.level_pine.f,
        lvls.level_the_answer.f,
        lvls.level_merge_sort.f,
        lvls.level_cycle_sort.f,
        lvls.level_sneckdown.f,
        lvls.level_selection_sort.f,
        lvls.level_random_K2.f,
        lvls.level_egyptian_fractions.f,
        lvls.level_roadblock.f,
        lvls.level_passage.f,
        lvls.level_impasse.f,
        lvls.level_route.f,
        lvls.level_baobab.f,
        lvls.level_code.f,
        lvls.level_random_binary_tree.f,
        lvls.level_spider.f,
        lvls.level_cedar.f,
        lvls.level_oak.f,
        lvls.level_fir.f,
        lvls.level_traversal.f,
        lvls.level_journey.f,
        lvls.level_expedition.f,
        lvls.level_voyage.f,
        lvls.level_taxicab_number.f,
        lvls.level_platonic.f,
        lvls.level_jail.f,
        lvls.level_prison.f,
        lvls.level_small.f,
        lvls.level_strange.f,
        lvls.level_water_lily.f,
        lvls.level_harmony.f,
        lvls.level_worms.f,
        lvls.level_wander.f,
        lvls.level_k.f,
        lvls.level_the_4_queens.f,
        lvls.level_mansion.f,
        lvls.level_alice_and_bob.f,
        lvls.level_walls.f,
        lvls.level_rampart.f,
        lvls.level_fortification.f,
        lvls.level_rotation_bis.f,
        lvls.level_butterfly_graph.f,
        lvls.level_sierpinski.f,
        lvls.level_the_fourth_triangle.f,
        lvls.level_hexagon.f,
        lvls.level_octahedral_graph.f,
        lvls.level_hexagonal_bipyramid.f,
        lvls.level_triangles.f,
        lvls.level_nonogram.f,
        lvls.level_crystal.f,
        lvls.level_mastermind.f,
        lvls.level_tetris.f,
        lvls.level_central_symmetry.f,
        lvls.level_lights_out.f,
        lvls.level_weights.f,
        lvls.level_tetractys.f,
        lvls.level_line_and_columns.f,
        lvls.level_baguenaudier.f,
        lvls.level_spare.f,
        lvls.level_4_colors_theorem.f,
        lvls.level_bamboos.f,
        lvls.level_gingko_biloba.f,
        lvls.level_cypress.f,
        lvls.level_cube_edges_coloring.f,
        lvls.level_octahedron_edges_coloring.f,
        lvls.level_grid.f,
        lvls.level_flash_back.f,
        lvls.level_spaceship.f,
        lvls.level_connect_the_dots.f,
        lvls.level_the_8_queens.f,
        lvls.level_magic_square.f,
        lvls.level_melencolia_1.f,
        lvls.level_matrix.f,
        lvls.level_river.f,
        lvls.level_cattle.f,
        lvls.level_herd.f,
        lvls.level_petersen_graph_edges_coloring.f,
        lvls.level_vortex.f,
        lvls.level_tree.f,
        lvls.level_dead_ends.f,
        lvls.level_conjunctive_normal_form.f,
        lvls.level_betweenness.f,
        lvls.level_fractal.f,
        lvls.level_euclidean_algorithm.f,
        lvls.level_tesseract.f,
        lvls.level_random_turning.f,
        lvls.level_branches.f,
        lvls.level_oval_track_puzzle.f,
        lvls.level_cartesian.f,
        lvls.level_random_line.f,
        lvls.level_eulerian.f,
        lvls.level_random_starting_point.f,
        lvls.level_sujiko.f,
        lvls.level_electricity.f,
        lvls.level_random_w6.f,
        lvls.level_pancake_sorting.f,
        lvls.level_random_ladder.f,
        lvls.level_wave.f,
        lvls.level_box.f,
        lvls.level_error.f,
        lvls.level_house.f,
        lvls.level_the_4th_dimension.f,
        lvls.level_draw.f,
        lvls.level_random_come_back.f,
        lvls.level_permutations.f,
        lvls.level_inversions.f,
        lvls.level_random_K5.f,
        lvls.level_takuzu.f,
        lvls.level_random_K33.f,
        lvls.level_travelling_salesman.f,
        lvls.level_random_petersen.f,
        lvls.level_no_three_in_line.f,
        lvls.level_manhattan_distance.f,
        lvls.level_tour.f,
        lvls.level_minimum_spanning_tree.f,
        lvls.level_honeycomb.f,
        lvls.level_random_gemini.f,
        lvls.level_random_cuboctahedron.f,
        lvls.level_knight.f,
        lvls.level_coloring.f,
        lvls.level_first_guarini_s_problem.f,
        lvls.level_second_guarini_s_problem.f,
        lvls.level_diagonal.f,
        lvls.level_sudoku.f,
        lvls.level_temple.f,
        lvls.level_syracuse.f,
        lvls.level_quick_sort.f,
        lvls.level_five.f,
        lvls.level_shuffled.f,
        lvls.level_heapsort.f,
        lvls.level_sign.f,
        lvls.level_combinatorics.f,
        lvls.level_hungarian_rings.f,
        lvls.level_water_pouring.f,
        lvls.level_puzzle.f,
        lvls.level_solitaire.f,
        lvls.level_mols.f,
        lvls.level_separation.f,
        lvls.level_panex.f,
        lvls.level_classified.f,
        lvls.level_towers.f,
        lvls.level_zebra.f,
        lvls.level_bridges.f,
        lvls.level_chinese_postman_problem.f,
        lvls.level_cellular_automaton.f,
        lvls.level_parking.f,
                             ]
    
    # Worlds = {'The Hidden Country':[level_von_neumann_neighborhood,
    #                                 level_cubic,
    #                                 level_spy,
    #                                 level_hitting_set,
    #                                 level_independent_set,
    #                                 level_dominating_set,
    #                                 level_exact_cover,
    #                                 level_connectivity,
    #                                 level_secret,
    #                                 level_moore_neighborhood,
    #                                 level_triangulate,
    #                                 level_water_tower,
    #                                 level_min_cut,
    #                                 level_max_cut,
    #                                 level_entropy,
    #                                 level_branches,
    #                                 level_tree,
    #                                 level_tesseract,
    #                                 level_electricity,
    #                                 level_wave,
    #                                 level_travelling_salesman,
    #                                 level_bridges,
    #                                 level_chinese_postman_problem,
    #                                ],
    #           'The Tree-House':[level_orchard,
    #                             level_binary,
    #                             level_forest,
    #                             level_jungle,
    #                             level_rainforest,
    #                          ],
    #           'The Wooden World':[level_bonsai,
    #                               level_poppy,
    #                               level_peony,
    #                               level_magnolia,
    #                               level_iris,
    #                               level_orchid,
    #                               level_tulip,
    #                               level_roses_are_red,
    #                               level_edelweiss,
    #                               level_violets_are_blue,
    #                               level_love,
    #                               level_palm_tree,
    #                               level_podium,
    #                               level_intersection,
    #                               level_sunflower,
    #                               level_willow,
    #                               level_beech,
    #                               level_birch,
    #                               level_elm,
    #                               level_maple,
    #                               level_pine,
    #                               level_baobab,
    #                               level_minimum_spanning_tree,
    #                               level_weights,
    #                               level_honeycomb,
    #                               level_cedar,
    #                               level_oak,
    #                               level_fir,
    #                               level_bamboos,
    #                               level_gingko_biloba,
    #                               level_cypress],
    #           'The Travel':[level_tetrahedron,
    #                         level_meanders,
    #                         level_shortcut,
    #                         level_octahedron,
    #                         level_cube,
    #                         level_desire_path,
    #                         level_hamiltonian,
    #                         level_wind_compass,
    #                         level_singletons,
    #                         level_walk,
    #                         level_trail,
    #                         level_path,
    #                         level_sneckdown,
    #                         level_roadblock,
    #                         level_passage,
    #                         level_impasse,
    #                         level_route,
    #                         level_traversal,
    #                         level_journey,
    #                         level_expedition,
    #                         level_voyage,
    #                         level_water_lily,
    #                         level_harmony,
    #                         level_worms,
    #                         level_wander,
    #                         level_tour,
    #                         level_central_symmetry,
    #                         level_tetractys,
    #                         level_connect_the_dots,
    #                         level_eulerian,
    #                         level_separation,
    #                         ],
    #           'The Accidental Realm':[level_random_simple,
    #                                   level_random_bull,
    #                                   level_random_butterfly,
    #                                   level_random_star,
    #                                   level_random_K2,
    #                                   level_random_binary_tree,
    #                                   level_random_turning,
    #                                   level_random_line,
    #                                   level_random_starting_point,
    #                                   level_random_w6,
    #                                   level_random_ladder,
    #                                   level_random_come_back,
    #                                   level_random_K5,
    #                                   level_random_K33,
    #                                   level_random_petersen,
    #                                   level_random_gemini,
    #                                   level_random_cuboctahedron,
    #                                   ],
    #           'The Digital Maze':[level_sheffer_stroke,
    #                               level_peirce_s_arrow,
    #                               level_relay,
    #                               level_circuit,
    #                               level_network,
    #                               level_pyramid,
    #                               ],
    #           'The Permutation Universe':[level_circle,
    #                                       level_elementary,
    #                                       level_invert,
    #                                       level_permutate,
    #                                       level_bubble_sort,
    #                                       level_odd_even_sort,
    #                                       level_cocktail_sort,
    #                                       level_3_cycle,
    #                                       level_spare,
    #                                       level_pigeonhole_sort,
    #                                       level_insertion_sort,
    #                                       level_gnome_sort,
    #                                       level_merge_sort,
    #                                       level_cycle_sort,
    #                                       level_selection_sort,
    #                                       level_quick_sort,
    #                                       level_grid,
    #                                       level_heapsort,
    #                                       level_spaceship,
    #                                       level_vortex,
    #                                       level_line_and_columns,
    #                                       level_permutations,
    #                                       level_inversions,
    #                                       level_pancake_sorting,
    #                                       level_oval_track_puzzle,
    #                                       level_box,
    #                                       level_error,
    #                                       level_puzzle,
    #                                       level_panex,
    #                                       level_hungarian_rings,
    #                                       level_cellular_automaton,
    #                                       level_parking,
    #                                       #level_panex,
    #                                       #level_superflip,
    #                                       ],
    #           'The Rotations Dimension':[level_wasted,
    #                                      level_rotation,
    #                                      level_rotation_bis,
    #                                      level_the_4th_dimension,
    #                                     ],
    #           'The Deduction Course':[level_dichotomy,
    #                                   level_mastermind,
    #                                   ],
    #           'The Numerals':[level_sum,
    #                           level_points,
    #                           level_numeration,
    #                           level_inside_out,
    #                           level_equation,
    #                           level_dots,
    #                           level_bloodline,
    #                           level_arithmetic,
    #                           level_product,
    #                           level_congruence,
    #                           level_one_third,
    #                           level_prime_number,
    #                           level_pythagorean,
    #                           level_sorted,
    #                           level_fibonacci_sequence,
    #                           level_quaternary,
    #                           level_young_tableaux,
    #                           level_integer_partition,
    #                           level_ferrers_diagram,
    #                           level_integer_factorization,
    #                           level_eratosthenes,
    #                           level_partition,
    #                           level_second,
    #                           level_the_answer,
    #                           level_egyptian_fractions,
    #                           level_strange,
    #                           level_taxicab_number,
    #                           level_euclidean_algorithm,
    #                           level_magic_square,
    #                           level_melencolia_1,
    #                           level_matrix,
    #                           level_takuzu,
    #                           level_sujiko,
    #                           level_diagonal,
    #                           level_sudoku,
    #                           level_mols,
    #                           ],
    #           "The substractions":[level_substract,
    #                                level_remove,
    #                                level_deduct,
    #                                level_decrease,
    #                                level_diminish,
    #                                level_withdraw,
    #                                level_withhold,
    #                                level_detract,],
    #           "The Decisions":[level_boolean,
    #                            level_alternation,
    #                            level_3sat,
    #                            level_point_of_no_return,
    #                            level_chromatic,
    #                            level_chromagraph,
    #                            level_stairs,
    #                            level_longest_path,
    #                            level_shortest_path,
    #                            level_tetris,
    #                            level_knapsack,
    #                            level_wheel,
    #                            level_betweenness,
    #                            level_4_colors_theorem,
    #                            level_nonogram,
    #                            level_no_three_in_line,
    #                            level_superpermutation,
    #                            level_conjunctive_normal_form,
    #                            level_manhattan_distance,
    #                            level_coloring,
    #                            level_zebra,
    #                            level_five,
    #                            level_shuffled,
    #                            level_sign,
    #                            level_combinatorics,
    #                          ],
    #           "The Chess Experts":[level_chessboard,
    #                                level_the_4_queens,
    #                                level_k,
    #                                level_the_8_queens,
    #                                level_knight,
    #                                level_first_guarini_s_problem,
    #                                level_second_guarini_s_problem,
    #                                ],
    #           "The Nature":[level_trivial,
    #                         level_choice,
    #                         level_hello_world,
    #                         level_playground,
    #                         level_initiation,
    #                         level_cardinal_directions,
    #                         level_linear,
    #                         level_expand_and_simplify,
    #                         level_variable,
    #                         level_order,
    #                         level_loop,
    #                         level_yoyo,
    #                         level_boustrophedon,
    #                         level_power_down,
    #                         level_bis_repetita,
    #                         level_domination_number,
    #                         level_shared,
    #                         level_odd,
    #                         level_molecule,
    #                         level_parallel,
    #                         level_leaves,
    #                         level_recurrence,
    #                         level_blind_alleys,
    #                         level_alice_and_bob,
    #                         level_walls,
    #                         level_rampart,
    #                         level_fortification,
    #                         level_river,
    #                         level_cattle,
    #                         level_herd,
    #                         level_small,
    #                         level_platonic,
    #                         level_baguenaudier,
    #                         level_lights_out,
    #                         level_cartesian,
    #                         level_compact,
    #                         level_temple,
    #                         level_water_pouring,
    #                         level_solitaire,
    #                         level_syracuse,
    #                         level_classified,
    #                         level_towers,
    #                         level_tetrahedron_edges_coloring,
    #                         level_cube_edges_coloring,
    #                         level_octahedron_edges_coloring,
    #                         level_petersen_graph_edges_coloring,
    #                         ],
    #           "The Ruins":[level_backward,
    #                        level_square,
    #                        level_fluid,
    #                        level_crossroad,
    #                        level_silex,
    #                        level_infinity,
    #                        level_spider,
    #                        level_hut,
    #                        level_town,
    #                        level_village,
    #                        level_palace,
    #                        level_mansion,
    #                        level_crystal,
    #                        level_jail,
    #                        level_prison,
    #                        level_dead_ends,
    #                        level_fractal,
    #                        level_house,
    #                        level_draw,],
    #           "The Zigzags":[level_pong,
    #                          level_naturals,
    #                          level_bipartite,
    #                          level_doppelganger,
    #                          level_flash_back,
    #                          level_code,
    #                          ],
    #           "The triangular globe":[level_butterfly_graph,
    #                                   level_sierpinski,
    #                                   level_the_fourth_triangle,
    #                                   level_hexagon,
    #                                   level_octahedral_graph,
    #                                   level_hexagonal_bipyramid,
    #                                   level_triangles,]
    #           }
    
    # worlds_names = list(Worlds.keys())
    # ['The Hidden Country',
    #  'The Tree-house',
    #  'The Journey',
    #  'The Accidental Realm',
    #  'The Digital Maze',
    #  'The Permutation Universe',
    #  'The Rotations Dimension',
    #  'The Deduction Course',
    #  'The Numerals',
    #  'The Decisions',
    #  'The Chess Experts',
    #  'The Nature',
    #  'The Ruins',
    #  'The Zigzags']
    # levels_functions_list = Worlds[worlds_names[3]]

    # levels_names_dico = {}
    # for i in range(len(levels_functions_list)):
    #     level = levels_functions_list[i]()
    #     name = level.name
    #     levels_names_dico[name] = i
    # print(levels_names_dico)

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
        lvls.level_random_ladder.aux,
        lvls.level_random_K5.aux,
        lvls.level_random_K33.aux,
        lvls.level_random_petersen.aux,
        lvls.level_random_cuboctahedron.aux,
        lvls.level_random_gemini.aux,
    ]

    number_of_levels = len(levels_functions_list)

    levels_list = [None for k in range(number_of_levels)]

    def get_level(level_number, fast_solution_finding=False, get_new_level=False):
        if get_new_level:
            Levels.levels_list[level_number] = Levels.levels_functions_list[level_number](
            )
        else:
            try:
                level_number = level_number % Levels.number_of_levels
                if Levels.levels_list[level_number] is None:
                    if fast_solution_finding and len(signature(Levels.levels_functions_list[level_number]).parameters) > 0:
                        Levels.levels_list[level_number] = Levels.levels_functions_list[level_number](
                            True)
                    else:
                        Levels.levels_list[level_number] = Levels.levels_functions_list[level_number](
                        )
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

    print('Trying all solutions')
    for level_function in Levels.levels_functions_list:
        level = level_function()
        assert not level.name in ['', 'TODO', 'todo', 'temp']
        if level.fastest_solution is not None:
            r = level.try_solution(level.fastest_solution)
            if r != 2:
                print(level.name, 'wrong solution')
        elif not level.random:
            if level.name not in ['Panex', 'Superflip']:
                print(level.name, 'no solution')

    print('Saving solutions')
    Levels.save_solutions_txt(do_it_fast=True, verbose=0)

    print('Calculating solutions lenghts')
    solutions_lenghts = []
    for level_function in Levels.levels_functions_list:
        level = level_function()
        if level.fastest_solution is not None:
            solutions_lenghts.append(len(level.fastest_solution.split(' ')))
    plt.figure(figsize=(15, 15))
    x_list = [i for i in range(len(solutions_lenghts))]
    plt.plot(x_list, solutions_lenghts, lw=0.3, color='k')
    plt.scatter(x_list, solutions_lenghts, lw=0.1, color='r')
    plt.xlabel('Level number')
    plt.ylabel('Number of actions in the solution')
    plt.grid()
    plt.show()

    if test_random_levels:
        print('Testing random levels')
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
            plt.figure(figsize=(30, 5))
            plt.hist(solution_length, bins=bins_list)
            plt.xticks(bins_list)
            plt.show()
            print('')

    print('Testing some chosen levels')
    solutions = lvls.level_cartesian.f().find_all_solutions(verbose=2,
                                                     nb_iterations_print=10**4,
                                                     stop_at_first_solution=False)
    assert len(solutions[0]) == 1
    sol = solutions[0][0]
    assert lvls.level_cartesian.f().fastest_solution == ' '.join(sol)
    assert lvls.level_arithmetic.f().find_all_solutions()[0] != 0
    assert lvls.level_numeration.f().find_all_solutions()[0] != 0
    assert lvls.level_3_cycle.f().find_all_solutions()[0] != 0
    
    print('Check levels duplications')
    all_level_set = set()
    for level_function in Levels.levels_functions_list:
        all_level_set.add(level_function().name)
    if len(all_level_set) != len(Levels.levels_functions_list):
        print("Some levels are duplicated in the list Levels.levels_functions_list")
    
    # worlds_level_list = []
    # for world_name in Levels.Worlds.keys():
    #     for level_function in Levels.Worlds[world_name]:
    #         worlds_level_list.append(level_function().name)
            
    # for level_function in Levels.levels_functions_list:
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
    
    print('End of the tests')


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
    # for i, level_funtion in enumerate(Levels.levels_functions_list):
    #     dico_i_level_name[level_funtion().name] = i
    
    # with open('temp/level_numbers.txt', 'w') as fw:
    #     for name in sorted(dico_i_level_name.keys()):
    #         i = dico_i_level_name[name]
    #         fw.write(f'{name: <25} {i}\n')
    
    # # # fast_solution_finding=True
    
    # level = level_triangles()
    # level = level_detract()
    # level = level_the_fourth_triangle()
    # level = level_octahedral_graph()
    # level = level_hexagonal_bipyramid()
    # level = level_vertex()
    # level = level_boustrophedon()
    # solutions = level.find_all_solutions(verbose=3, save_solutions_txt=True)
    # print('\n')
    # print(len(solutions[0]))
    # # print('\n')
    # # # with open('cellular_automaton_solutions.txt', 'w') as fw:
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
    # for level_function in Levels.levels_functions_list:
    #     level = level_function()
    #     level_roots_names = level.roots_names_set
    #     if level_roots_names - all_roots_names != set():
    #         print(level.name, level_roots_names - all_roots_names)
    #         all_roots_names = all_roots_names | level_roots_names
    
    
    