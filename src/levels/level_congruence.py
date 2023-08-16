from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_congruence():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(6),
              empty=True,
              name='V0',
              switches=[S0, S1, S2, S3, S4, S5])

    tree_list_0 = ['EQU',
                   ['MOD',
                    [None],
                    [None]],
                   [None]]

    T0 = Tree(tree_list=['AND', tree_list_0, tree_list_0],
              empty=True,
              name='T0',
              switches=[V0,
                        7,
                        6,
                        V0,
                        8,
                        7],
              cut_expression_depth_1=True)
    
    # tree_list_0 = ['EQU',
    #                ['MOD',
    #                 Tree.tree_list_BIN(6),
    #                 [None]],
    #                [None]]

    # T0 = Tree(tree_list=['AND', tree_list_0, tree_list_0],
    #           empty=True,
    #           name='T0',
    #           switches=[S0, S1, S2, S3, S4, S5,
    #                     7,
    #                     6,
    #                     S0, S1, S2, S3, S4, S5,
    #                     8,
    #                     7],
    #           cut_expression_depth_1=True)

    R0 = Room(name='R0',
              position=[0, 0, 0.5, 6],
              switches_list=[S0, S1, S2, S3, S4, S5])
    RE = Room(name='RE',
              position=[1.25, 0.5, 5.25, 5],
              is_exit=True)  # E pour exit ou end

    p = 1 / 2

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1, p],
              relative_arrival_coordinates=[0, p])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution='S0 S1 S2 S4 S5 D0',
                 level_color=Levels_colors_list.FROM_HUE(0.83, sa=0.3, li=0.6),
                 name='Congruence',
                 door_window_size=380,
                 keep_proportions=True)

    return level