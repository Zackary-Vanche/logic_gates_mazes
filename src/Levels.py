from time import time, sleep
from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from inspect import signature

from levels.level_3_cycle import level_3_cycle
from levels.level_3sat import level_3sat
from levels.level_4_colors_theorem import level_4_colors_theorem
from levels.level_alice_and_bob import level_alice_and_bob
from levels.level_alternation import level_alternation
from levels.level_arithmetic import level_arithmetic
from levels.level_backward import level_backward
from levels.level_baguenaudier import level_baguenaudier
from levels.level_bamboos import level_bamboos
from levels.level_baobab import level_baobab
from levels.level_beech import level_beech
from levels.level_betweenness import level_betweenness
from levels.level_binary import level_binary
from levels.level_bipartite import level_bipartite
from levels.level_bis_repetita import level_bis_repetita
from levels.level_birch import level_birch
#from levels.level_black_knight_puzzle import level_black_knight_puzzle
from levels.level_blind_alleys import level_blind_alleys
from levels.level_bloodline import level_bloodline
from levels.level_bonsai import level_bonsai
from levels.level_boolean import level_boolean
from levels.level_box import level_box
from levels.level_branches import level_branches
from levels.level_bridges import level_bridges
from levels.level_bubble_sort import level_bubble_sort
from levels.level_cardinal_directions import level_cardinal_directions
from levels.level_cartesian import level_cartesian
from levels.level_cattle import level_cattle
from levels.level_cedar import level_cedar
from levels.level_cellular_automaton import level_cellular_automaton
from levels.level_central_symmetry import level_central_symmetry
from levels.level_chessboard import level_chessboard
from levels.level_chinese_postman_problem import level_chinese_postman_problem
from levels.level_choice import level_choice
from levels.level_chromatic import level_chromatic
from levels.level_circle import level_circle
from levels.level_circuit import level_circuit
from levels.level_classified import level_classified
from levels.level_cocktail_sort import level_cocktail_sort
from levels.level_code import level_code
from levels.level_coloring import level_coloring
from levels.level_combinatorics import level_combinatorics
from levels.level_compact import level_compact
from levels.level_congruence import level_congruence
from levels.level_conjunctive_normal_form import level_conjunctive_normal_form
from levels.level_connect_the_dots import level_connect_the_dots
from levels.level_connectivity import level_connectivity
from levels.level_crossroad import level_crossroad
from levels.level_crystal import level_crystal
from levels.level_cube import level_cube
from levels.level_cubic import level_cubic
from levels.level_cycle_sort import level_cycle_sort
from levels.level_cypress import level_cypress
from levels.level_dead_ends import level_dead_ends
from levels.level_diagonal import level_diagonal
from levels.level_dichotomy import level_dichotomy
from levels.level_desire_path import level_desire_path
from levels.level_dominating_set import level_dominating_set
from levels.level_doppelganger import level_doppelganger
from levels.level_draw import level_draw
from levels.level_euclidean_algorithm import level_euclidean_algorithm
from levels.level_edelweiss import level_edelweiss
from levels.level_egyptian_fractions import level_egyptian_fractions
from levels.level_electricity import level_electricity
from levels.level_elementary import level_elementary
from levels.level_elm import level_elm
from levels.level_entropy import level_entropy
from levels.level_equation import level_equation
from levels.level_eratosthenes import level_eratosthenes
from levels.level_error import level_error
from levels.level_eulerian import level_eulerian
from levels.level_exact_cover import level_exact_cover
from levels.level_expand_and_simplify import level_expand_and_simplify
from levels.level_expedition import level_expedition
from levels.level_ferrers_diagram import level_ferrers_diagram
from levels.level_fibonacci_sequence import level_fibonacci_sequence
from levels.level_fir import level_fir
from levels.level_first_guarini_s_problem import level_first_guarini_s_problem
from levels.level_five import level_five
from levels.level_flash_back import level_flash_back
from levels.level_fluid import level_fluid
from levels.level_forest import level_forest
from levels.level_fortification import level_fortification
from levels.level_fractal import level_fractal
from levels.level_gingko_biloba import level_gingko_biloba
from levels.level_gnome_sort import level_gnome_sort
from levels.level_grid import level_grid
from levels.level_hamiltonian import level_hamiltonian
from levels.level_harmony import level_harmony
from levels.level_heapsort import level_heapsort
from levels.level_hello_world import level_hello_world
from levels.level_herd import level_herd
from levels.level_hitting_set import level_hitting_set
from levels.level_honeycomb import level_honeycomb
from levels.level_house import level_house
from levels.level_hungarian_rings import level_hungarian_rings
from levels.level_hut import level_hut
from levels.level_impasse import level_impasse
from levels.level_independent_set import level_independent_set
from levels.level_infinity import level_infinity
from levels.level_initiation import level_initiation
from levels.level_insertion_sort import level_insertion_sort
from levels.level_inside_out import level_inside_out
from levels.level_integer_factorization import level_integer_factorization
from levels.level_integer_partition import level_integer_partition
from levels.level_intersection import level_intersection
from levels.level_inversions import level_inversions
from levels.level_invert import level_invert
from levels.level_iris import level_iris
from levels.level_jail import level_jail
from levels.level_journey import level_journey
from levels.level_jungle import level_jungle
from levels.level_k import level_k
from levels.level_knapsack import level_knapsack
from levels.level_knight import level_knight
from levels.level_leaves import level_leaves
from levels.level_lights_out import level_lights_out
from levels.level_linear import level_linear
from levels.level_line_and_columns import level_line_and_columns
from levels.level_longest_path import level_longest_path
from levels.level_loop import level_loop
from levels.level_love import level_love
from levels.level_magic_square import level_magic_square  # kakuro
from levels.level_magnolia import level_magnolia
from levels.level_manhattan_distance import level_manhattan_distance
from levels.level_mansion import level_mansion
from levels.level_maple import level_maple
from levels.level_mastermind import level_mastermind
from levels.level_matrix import level_matrix
from levels.level_max_cut import level_max_cut
from levels.level_meanders import level_meanders
from levels.level_melencolia_1 import level_melencolia_1
from levels.level_merge_sort import level_merge_sort
from levels.level_min_cut import level_min_cut
from levels.level_minimum_spanning_tree import level_minimum_spanning_tree
from levels.level_mols import level_mols
from levels.level_moore_neighborhood import level_moore_neighborhood
from levels.level_naturals import level_naturals
from levels.level_network import level_network
from levels.level_no_three_in_line import level_no_three_in_line
from levels.level_nonogram import level_nonogram
from levels.level_numeration import level_numeration
from levels.level_oak import level_oak
from levels.level_octahedron import level_octahedron
from levels.level_odd import level_odd
from levels.level_odd_even_sort import level_odd_even_sort
from levels.level_orchard import level_orchard
from levels.level_orchid import level_orchid
from levels.level_order import level_order
from levels.level_oval_track_puzzle import level_oval_track_puzzle
from levels.level_palace import level_palace
from levels.level_palm_tree import level_palm_tree
from levels.level_pancake_sorting import level_pancake_sorting
from levels.level_panex import level_panex
from levels.level_parallel import level_parallel
from levels.level_parking import level_parking
from levels.level_partition import level_partition
from levels.level_passage import level_passage
from levels.level_path import level_path
from levels.level_peirce_s_arrow import level_peirce_s_arrow
from levels.level_peony import level_peony
from levels.level_permutate import level_permutate
from levels.level_permutations import level_permutations
from levels.level_pigeonhole_sort import level_pigeonhole_sort
from levels.level_pine import level_pine
from levels.level_platonic import level_platonic
from levels.level_playground import level_playground
from levels.level_podium import level_podium
from levels.level_point_of_no_return import level_point_of_no_return
from levels.level_pong import level_pong
from levels.level_poppy import level_poppy
from levels.level_power_down import level_power_down
from levels.level_prime_number import level_prime_number
from levels.level_prison import level_prison
from levels.level_product import level_product
from levels.level_puzzle import level_puzzle
from levels.level_pyramid import level_pyramid
from levels.level_pythagorean import level_pythagorean
from levels.level_quick_sort import level_quick_sort
from levels.level_rainforest import level_rainforest
from levels.level_rampart import level_rampart
from levels.level_random_K2 import level_random_K2
from levels.level_random_K33 import level_random_K33
from levels.level_random_K5 import level_random_K5
from levels.level_random_binary_tree import level_random_binary_tree
from levels.level_random_boustrophedon import level_random_boustrophedon
from levels.level_random_bull import level_random_bull
from levels.level_random_butterfly import level_random_butterfly
from levels.level_random_come_back import level_random_come_back
from levels.level_random_cuboctahedron import level_random_cuboctahedron
from levels.level_random_gemini import level_random_gemini
from levels.level_random_ladder import level_random_ladder
from levels.level_random_line import level_random_line
from levels.level_random_petersen import level_random_petersen
from levels.level_random_simple import level_random_simple
from levels.level_random_star import level_random_star
from levels.level_random_starting_point import level_random_starting_point
from levels.level_random_turning import level_random_turning
from levels.level_random_w6 import level_random_w6
from levels.level_recurrence import level_recurrence
from levels.level_relay import level_relay
from levels.level_river import level_river
from levels.level_roadblock import level_roadblock
from levels.level_roses_are_red import level_roses_are_red
from levels.level_rotation import level_rotation
from levels.level_rotation_bis import level_rotation_bis
from levels.level_route import level_route
from levels.level_secret import level_secret
from levels.level_second import level_second
from levels.level_second_guarini_s_problem import level_second_guarini_s_problem
from levels.level_selection_sort import level_selection_sort
from levels.level_separation import level_separation
from levels.level_shared import level_shared
from levels.level_sheffer_stroke import level_sheffer_stroke
from levels.level_shortcut import level_shortcut
from levels.level_shortest_path import level_shortest_path
from levels.level_shuffled import level_shuffled
from levels.level_sign import level_sign
from levels.level_silex import level_silex
from levels.level_singletons import level_singletons
from levels.level_small import level_small
from levels.level_sunflower import level_sunflower
from levels.level_sneckdown import level_sneckdown
from levels.level_solitaire import level_solitaire
from levels.level_sorted import level_sorted
from levels.level_spaceship import level_spaceship
from levels.level_spare import level_spare
from levels.level_spider import level_spider
from levels.level_spy import level_spy
from levels.level_square import level_square
from levels.level_stairs import level_stairs
from levels.level_strange import level_strange
from levels.level_sudoku import level_sudoku
from levels.level_sujiko import level_sujiko
from levels.level_sum import level_sum
from levels.level_superpermutation import level_superpermutation
from levels.level_syracuse import level_syracuse
from levels.level_takuzu import level_takuzu
from levels.level_taxicab_number import level_taxicab_number
from levels.level_temple import level_temple
from levels.level_tesseract import level_tesseract
from levels.level_tetractys import level_tetractys
from levels.level_tetrahedron import level_tetrahedron
from levels.level_tetris import level_tetris
from levels.level_the_4_queens import level_the_4_queens
from levels.level_the_8_queens import level_the_8_queens
from levels.level_the_4th_dimension import level_the_4th_dimension
from levels.level_tour import level_tour
from levels.level_towers import level_towers
from levels.level_town import level_town
from levels.level_trail import level_trail
from levels.level_travelling_salesman import level_travelling_salesman
from levels.level_traversal import level_traversal
from levels.level_tree import level_tree
from levels.level_triangulate import level_triangulate
from levels.level_trivial import level_trivial
from levels.level_tulip import level_tulip
from levels.level_variable import level_variable
from levels.level_village import level_village
from levels.level_violets_are_blue import level_violets_are_blue
from levels.level_von_neumann_neighborhood import level_von_neumann_neighborhood
from levels.level_vortex import level_vortex
from levels.level_voyage import level_voyage
from levels.level_walk import level_walk
from levels.level_walls import level_walls
from levels.level_wasted import level_wasted
from levels.level_water_lily import level_water_lily
from levels.level_water_pouring import level_water_pouring
from levels.level_wave import level_wave
from levels.level_weights import level_weights
from levels.level_wheel import level_wheel
from levels.level_willow import level_willow
from levels.level_wind_compass import level_wind_compass
from levels.level_wander import level_wander
from levels.level_worms import level_worms
from levels.level_young_tableaux import level_young_tableaux
from levels.level_yoyo import level_yoyo
from levels.level_zebra import level_zebra

from levels.level_random_K2 import aux_level_random_K2
from levels.level_random_K5 import aux_level_random_K5
from levels.level_random_K33 import aux_level_random_K33
from levels.level_random_star import aux_level_random_star
from levels.level_random_starting_point import aux_level_random_starting_point
from levels.level_random_turning import aux_level_random_turning
from levels.level_random_line import aux_level_random_line
from levels.level_random_binary_tree import aux_level_random_binary_tree
from levels.level_random_w6 import aux_level_random_w6
from levels.level_random_bull import aux_level_random_bull
from levels.level_random_butterfly import aux_level_random_butterfly
from levels.level_random_come_back import aux_level_random_come_back
from levels.level_random_gemini import aux_level_random_gemini
from levels.level_random_ladder import aux_level_random_ladder
from levels.level_random_boustrophedon import aux_level_random_boustrophedon
from levels.level_random_simple import aux_level_random_simple
from levels.level_random_petersen import aux_level_random_petersen
from levels.level_random_cuboctahedron import aux_level_random_cuboctahedron

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
                             level_trivial,
                             level_choice,
                             level_hello_world,
                             level_playground,
                             level_initiation,
                             level_cardinal_directions,
                             level_linear,
                             level_expand_and_simplify,
                             level_variable,
                             level_order,
                             level_loop,
                             level_backward,
                             level_boolean,
                             level_alternation,
                             level_yoyo,
                             level_power_down,
                             level_orchard,
                             level_crossroad,
                             level_bis_repetita,
                             level_shared,
                             level_spy,
                             level_leaves,
                             level_binary,
                             level_tetrahedron,
                             level_bonsai,
                             level_numeration,
                             level_square,
                             level_point_of_no_return,
                             level_cubic,
                             level_cube,
                             level_3sat,
                             level_sum,
                             level_product,
                             level_inside_out,
                             level_chromatic,
                             level_octahedron,
                             level_fluid,
                             level_congruence,
                             level_infinity,
                             level_forest,
                             level_equation,
                             level_von_neumann_neighborhood,
                             level_moore_neighborhood,
                             level_pong,
                             level_bipartite,
                             level_bloodline,
                             level_hamiltonian,
                             level_sorted,
                             level_sheffer_stroke,
                             level_peirce_s_arrow,
                             level_longest_path,
                             level_shortest_path,
                             level_hitting_set,
                             level_independent_set,
                             level_dominating_set,
                             level_circle,
                             level_exact_cover,
                             level_connectivity,
                             level_rainforest,
                             level_secret,
                             level_odd,
                             level_jungle,
                             level_min_cut,
                             level_max_cut,
                             level_hut,
                             level_arithmetic,
                             level_triangulate,
                             level_recurrence,
                             level_stairs,
                             level_sunflower,
                             level_naturals,
                             level_3_cycle,
                             level_blind_alleys,
                             level_wasted,
                             level_doppelganger,
                             level_meanders,
                             level_shortcut,
                             level_wind_compass,
                             level_prime_number,
                             level_poppy,
                             level_peony,
                             level_magnolia,
                             level_iris,
                             level_orchid,
                             level_tulip,
                             level_compact,
                             level_village,
                             level_town,
                             level_fibonacci_sequence,
                             level_palace,
                             level_random_simple,
                             level_random_boustrophedon,
                             level_parallel,
                             level_eratosthenes,
                             level_random_bull,
                             level_pythagorean,
                             level_random_butterfly,
                             level_elementary,
                             level_young_tableaux,
                             level_rotation,
                             level_superpermutation,
                             level_singletons,
                             level_relay,
                             level_circuit,
                             level_network,
                             level_pyramid,
                             level_invert,
                             level_permutate,
                             level_desire_path,
                             level_integer_partition,
                             level_ferrers_diagram,
                             level_integer_factorization,
                             level_chessboard,
                             level_silex,
                             level_roses_are_red,
                             level_edelweiss,
                             level_violets_are_blue,
                             level_walk,
                             level_trail,
                             level_path,
                             level_entropy,
                             level_bubble_sort,
                             level_odd_even_sort,
                             level_cocktail_sort,
                             level_pigeonhole_sort,
                             level_dichotomy,
                             level_wheel,
                             level_random_star,
                             level_intersection,
                             level_partition,
                             level_second,
                             level_insertion_sort,
                             level_gnome_sort,
                             level_knapsack,
                             level_love,
                             level_palm_tree,
                             level_podium,
                             level_willow,
                             level_beech,
                             level_birch,
                             level_elm,
                             level_maple,
                             level_pine,
                             level_merge_sort,
                             level_cycle_sort,
                             level_sneckdown,
                             level_selection_sort,
                             level_random_K2,
                             level_egyptian_fractions,
                             level_roadblock,
                             level_passage,
                             level_impasse,
                             level_route,
                             level_baobab,
                             level_code,
                             level_random_binary_tree,
                             level_spider,
                             level_cedar,
                             level_oak,
                             level_fir,
                             level_traversal,
                             level_journey,
                             level_expedition,
                             level_voyage,
                             level_taxicab_number,
                             level_platonic,
                             level_jail,
                             level_prison,
                             level_small,
                             level_strange,
                             level_water_lily,
                             level_harmony,
                             level_worms,
                             level_wander,
                             level_k,
                             level_the_4_queens,
                             level_mansion,
                             level_alice_and_bob,
                             level_walls,
                             level_rampart,
                             level_fortification,
                             level_rotation_bis,
                             level_nonogram,
                             level_crystal,
                             level_mastermind,
                             level_tetris,
                             level_central_symmetry,
                             level_lights_out,
                             level_weights,
                             level_tetractys,
                             level_line_and_columns,
                             level_baguenaudier,
                             level_spare,
                             level_4_colors_theorem,
                             level_bamboos,
                             level_gingko_biloba,
                             level_cypress,
                             level_grid,
                             level_flash_back,
                             level_spaceship,
                             level_connect_the_dots,
                             level_the_8_queens,
                             level_magic_square,
                             level_melencolia_1,
                             level_matrix,
                             level_river,
                             level_cattle,
                             level_herd,
                             level_vortex,
                             level_tree,
                             level_dead_ends,
                             level_conjunctive_normal_form,
                             level_betweenness,
                             level_fractal,
                             level_euclidean_algorithm,
                             level_tesseract,
                             level_random_turning,
                             level_branches,
                             level_oval_track_puzzle,
                             level_cartesian,
                             level_random_line,
                             level_eulerian,
                             level_random_starting_point,
                             level_sujiko,
                             level_electricity,
                             level_random_w6,
                             level_pancake_sorting,
                             level_random_ladder,
                             level_wave,
                             level_box,
                             level_error,
                             level_house,
                             level_the_4th_dimension,
                             level_draw,
                             level_random_come_back,
                             level_permutations,
                             level_inversions,
                             level_random_K5,
                             level_takuzu,
                             level_random_K33,
                             level_travelling_salesman,
                             level_random_petersen,
                             level_no_three_in_line,
                             level_manhattan_distance,
                             level_tour,
                             level_minimum_spanning_tree,
                             level_honeycomb,
                             level_random_gemini,
                             level_random_cuboctahedron,
                             level_knight,
                             level_coloring,
                             level_first_guarini_s_problem,
                             level_second_guarini_s_problem,
                             level_diagonal,
                             level_sudoku,
                             level_temple,
                             level_syracuse,
                             level_quick_sort,
                             level_five,
                             level_shuffled,
                             level_heapsort,
                             level_sign,
                             level_combinatorics,
                             level_hungarian_rings,
                             level_water_pouring,
                             level_puzzle,
                             level_solitaire,
                             level_mols,
                             level_separation,
                             level_panex,
                             level_classified,
                             level_towers,
                             level_zebra,
                             level_bridges,
                             level_chinese_postman_problem,
                             level_cellular_automaton,
                             level_parking,
                             #level_panex,
                             #level_superflip,
                             ]
    
    Worlds = {'The Hidden Country':[level_von_neumann_neighborhood,
                                    level_cubic,
                                    level_spy,
                                    level_hitting_set,
                                    level_independent_set,
                                    level_dominating_set,
                                    level_exact_cover,
                                    level_connectivity,
                                    level_secret,
                                    level_moore_neighborhood,
                                    level_triangulate,
                                    level_min_cut,
                                    level_max_cut,
                                    level_entropy,
                                    level_branches,
                                    level_tree,
                                    level_tesseract,
                                    level_electricity,
                                    level_wave,
                                    level_travelling_salesman,
                                    level_bridges,
                                    level_chinese_postman_problem,
                                   ],
              'The Tree-House':[level_orchard,
                                level_binary,
                                level_forest,
                                level_jungle,
                                level_rainforest,
                             ],
              'The Wooden World':[level_bonsai,
                                  level_poppy,
                                  level_peony,
                                  level_magnolia,
                                  level_iris,
                                  level_orchid,
                                  level_tulip,
                                  level_roses_are_red,
                                  level_edelweiss,
                                  level_violets_are_blue,
                                  level_love,
                                  level_palm_tree,
                                  level_podium,
                                  level_intersection,
                                  level_sunflower,
                                  level_willow,
                                  level_beech,
                                  level_birch,
                                  level_elm,
                                  level_maple,
                                  level_pine,
                                  level_baobab,
                                  level_minimum_spanning_tree,
                                  level_weights,
                                  level_honeycomb,
                                  level_cedar,
                                  level_oak,
                                  level_fir,
                                  level_bamboos,
                                  level_gingko_biloba,
                                  level_cypress],
              'The Travel':[level_tetrahedron,
                            level_meanders,
                            level_shortcut,
                            level_octahedron,
                            level_cube,
                            level_desire_path,
                            level_hamiltonian,
                            level_wind_compass,
                            level_singletons,
                            level_walk,
                            level_trail,
                            level_path,
                            level_sneckdown,
                            level_roadblock,
                            level_passage,
                            level_impasse,
                            level_route,
                            level_traversal,
                            level_journey,
                            level_expedition,
                            level_voyage,
                            level_water_lily,
                            level_harmony,
                            level_worms,
                            level_wander,
                            level_tour,
                            level_central_symmetry,
                            level_tetractys,
                            level_connect_the_dots,
                            level_eulerian,
                            level_separation,
                            ],
              'The Accidental Realm':[level_random_simple,
                                      level_random_boustrophedon,
                                      level_random_bull,
                                      level_random_butterfly,
                                      level_random_star,
                                      level_random_K2,
                                      level_random_binary_tree,
                                      level_random_turning,
                                      level_random_line,
                                      level_random_starting_point,
                                      level_random_w6,
                                      level_random_ladder,
                                      level_random_come_back,
                                      level_random_K5,
                                      level_random_K33,
                                      level_random_petersen,
                                      level_random_gemini,
                                      level_random_cuboctahedron,
                                      ],
              'The Digital Maze':[level_sheffer_stroke,
                                  level_peirce_s_arrow,
                                  level_relay,
                                  level_circuit,
                                  level_network,
                                  level_pyramid,
                                  ],
              'The Permutation Universe':[level_circle,
                                          level_elementary,
                                          level_invert,
                                          level_permutate,
                                          level_bubble_sort,
                                          level_odd_even_sort,
                                          level_cocktail_sort,
                                          level_3_cycle,
                                          level_spare,
                                          level_pigeonhole_sort,
                                          level_insertion_sort,
                                          level_gnome_sort,
                                          level_merge_sort,
                                          level_cycle_sort,
                                          level_selection_sort,
                                          level_quick_sort,
                                          level_grid,
                                          level_heapsort,
                                          level_spaceship,
                                          level_vortex,
                                          level_line_and_columns,
                                          level_permutations,
                                          level_inversions,
                                          level_pancake_sorting,
                                          level_oval_track_puzzle,
                                          level_box,
                                          level_error,
                                          level_puzzle,
                                          level_panex,
                                          level_hungarian_rings,
                                          level_cellular_automaton,
                                          level_parking,
                                          #level_panex,
                                          #level_superflip,
                                          ],
              'The Rotations Dimension':[level_wasted,
                                         level_rotation,
                                         level_rotation_bis,
                                         level_the_4th_dimension,
                                        ],
              'The Deduction Course':[level_dichotomy,
                                      level_mastermind,
                                      ],
              'The Numerals':[level_sum,
                              level_numeration,
                              level_inside_out,
                              level_equation,
                              level_bloodline,
                              level_arithmetic,
                              level_product,
                              level_congruence,
                              level_prime_number,
                              level_pythagorean,
                              level_sorted,
                              level_fibonacci_sequence,
                              level_young_tableaux,
                              level_integer_partition,
                              level_ferrers_diagram,
                              level_integer_factorization,
                              level_eratosthenes,
                              level_partition,
                              level_second,
                              level_egyptian_fractions,
                              level_strange,
                              level_taxicab_number,
                              level_euclidean_algorithm,
                              level_magic_square,
                              level_melencolia_1,
                              level_matrix,
                              level_takuzu,
                              level_sujiko,
                              level_diagonal,
                              level_sudoku,
                              level_mols,
                              ],
              "The Decisions":[level_boolean,
                               level_alternation,
                               level_3sat,
                               level_point_of_no_return,
                               level_chromatic,
                               level_stairs,
                               level_longest_path,
                               level_shortest_path,
                               level_tetris,
                               level_knapsack,
                               level_wheel,
                               level_betweenness,
                               level_4_colors_theorem,
                               level_nonogram,
                               level_no_three_in_line,
                               level_superpermutation,
                               level_conjunctive_normal_form,
                               level_manhattan_distance,
                               level_coloring,
                               level_zebra,
                               level_five,
                               level_shuffled,
                               level_sign,
                               level_combinatorics,
                             ],
              "The Chess Experts":[level_chessboard,
                                   level_the_4_queens,
                                   level_k,
                                   level_the_8_queens,
                                   level_knight,
                                   level_first_guarini_s_problem,
                                   level_second_guarini_s_problem,
                                   ],
              "The Nature":[level_trivial,
                            level_choice,
                            level_hello_world,
                            level_playground,
                            level_initiation,
                            level_cardinal_directions,
                            level_linear,
                            level_expand_and_simplify,
                            level_variable,
                            level_order,
                            level_loop,
                            level_yoyo,
                            level_power_down,
                            level_bis_repetita,
                            level_shared,
                            level_odd,
                            level_parallel,
                            level_leaves,
                            level_recurrence,
                            level_blind_alleys,
                            level_alice_and_bob,
                            level_walls,
                            level_rampart,
                            level_fortification,
                            level_river,
                            level_cattle,
                            level_herd,
                            level_small,
                            level_platonic,
                            level_baguenaudier,
                            level_lights_out,
                            level_cartesian,
                            level_compact,
                            level_temple,
                            level_water_pouring,
                            level_solitaire,
                            level_syracuse,
                            level_classified,
                            level_towers,
                            ],
              "The Ruins":[level_backward,
                           level_square,
                           level_fluid,
                           level_crossroad,
                           level_silex,
                           level_infinity,
                           level_spider,
                           level_hut,
                           level_town,
                           level_village,
                           level_palace,
                           level_mansion,
                           level_crystal,
                           level_jail,
                           level_prison,
                           level_dead_ends,
                           level_fractal,
                           level_house,
                           level_draw,],
              "The Zigzags":[level_pong,
                             level_naturals,
                             level_bipartite,
                             level_doppelganger,
                             level_flash_back,
                             level_code,
                             ]
              }
    
    worlds_names = list(Worlds.keys())
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
        aux_level_random_simple,
        aux_level_random_bull,
        aux_level_random_butterfly,
        aux_level_random_star,
        aux_level_random_K2,
        aux_level_random_binary_tree,
        aux_level_random_line,
        aux_level_random_turning,
        aux_level_random_w6,
        aux_level_random_boustrophedon,
        aux_level_random_come_back,
        aux_level_random_starting_point,
        aux_level_random_ladder,
        aux_level_random_K5,
        aux_level_random_K33,
        aux_level_random_petersen,
        aux_level_random_cuboctahedron,
        aux_level_random_gemini,
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
    solutions = level_cartesian().find_all_solutions(verbose=2,
                                                     nb_iterations_print=10**4,
                                                     stop_at_first_solution=False)
    assert len(solutions[0]) == 1
    sol = solutions[0][0]
    assert level_cartesian().fastest_solution == ' '.join(sol)
    assert level_arithmetic().find_all_solutions()[0] != 0
    assert level_numeration().find_all_solutions()[0] != 0
    assert level_3_cycle().find_all_solutions()[0] != 0
    
    print('Check levels duplications')
    all_level_set = set()
    for level_function in Levels.levels_functions_list:
        all_level_set.add(level_function().name)
    if len(all_level_set) != len(Levels.levels_functions_list):
        print("Some levels are duplicated in the list Levels.levels_functions_list")
    
    worlds_level_list = []
    for world_name in Levels.Worlds.keys():
        for level_function in Levels.Worlds[world_name]:
            worlds_level_list.append(level_function().name)
            
    for level_function in Levels.levels_functions_list:
        name = level_function().name
        if not name in worlds_level_list:
            print(name)
            
    worlds_level_set = set(worlds_level_list)
    duplicates = set([item for item in worlds_level_list if worlds_level_list.count(item) > 1])
    if all_level_set != worlds_level_set or duplicates != set():
        print(duplicates)
        print('')
        print(all_level_set - worlds_level_set)
        print('')
        print(worlds_level_set - all_level_set)
    
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

    # test_levels()

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
    
    level = level_fortification()
    solutions = level.find_all_solutions(verbose=3, save_solutions_txt=True)
    print('\n')
    print(len(solutions[0]))
    print('\n')
    # with open('cellular_automaton_solutions.txt', 'w') as fw:
    for sol in solutions[0]:
        print(' '.join(sol))
        # fw.write(' '.join(sol))
        # fw.write('\n')
    
        
    
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
    
    
    