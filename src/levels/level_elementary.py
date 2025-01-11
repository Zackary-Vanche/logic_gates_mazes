from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')

    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5')

    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=1)

    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9', value=1)
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V0',
              switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V1',
              switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V2',
              switches=[S4, S5])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V3',
              switches=[S6, S7])
    V4 = Tree(tree_list=Tree.tree_list_BIN(2),
              name='V4',
              switches=[S8, S9])

    tree_list_036 = ['EQU', [None], [None]]

    tree_list_147 = ['EQU', [None], [None]]

    tree_list_258 = ['EQUSET'] + [[None]]*8

    switches_list_258 = [V1, V2, V3, V4, 0, 1, 2, 3]

    T0 = Tree(tree_list=tree_list_036,
              name='T0',
              switches=[V0, 1])
    T1 = Tree(tree_list=tree_list_147,
              name='T1',
              switches=[V1, V2])
    T2 = Tree(tree_list=tree_list_258,
              name='T2',
              switches=switches_list_258)
    T3 = Tree(tree_list=tree_list_036,
              name='T3',
              switches=[V0, 2])
    T4 = Tree(tree_list=tree_list_147,
              name='T4',
              switches=[V2, V3])
    T5 = Tree(tree_list=tree_list_258,
              name='T5',
              switches=switches_list_258)
    T6 = Tree(tree_list=tree_list_036,
              name='T6',
              switches=[V0, 3])
    T7 = Tree(tree_list=tree_list_147,
              name='T7',
              switches=[V3, V4])
    T8 = Tree(tree_list=tree_list_258,
              name='T8',
              switches=switches_list_258)
    T9 = Tree(tree_list=['EQU', Tree.tree_list_BIN(10), [None]],
              name='T9',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, 110])

    epsilon = 0.1

    R0 = Room(name='R0',
              position=[0, 2, 1, 1],
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[2, 0, 1, 1],
              switches_list=[S2, S3])
    R2 = Room(name='R2',
              position=[3, 1, 1, 1],
              switches_list=[S4, S5])
    R3 = Room(name='R3',
              position=[3, 3, 1, 1],
              switches_list=[S6, S7])
    R4 = Room(name='R4',
              position=[2, 4, 1, 1],
              switches_list=[S8, S9])
    RE = Room(name='RE',
              position=[0, 4, 1, 1],
              is_exit=True)  # E pour exit ou end
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1 - epsilon, epsilon],
              relative_arrival_coordinates=[1 - epsilon, epsilon])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R0,
              relative_position=0.6)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R2,
              relative_position=0.6)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R3)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_position=0.6)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R0,
              room_arrival=R3,
              relative_position=0.6)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=[1 - epsilon, 1 - epsilon],
              relative_arrival_coordinates=[1 - epsilon, 1 - epsilon])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R4,
              room_arrival=R0)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution='S0 D0 S2 D1 S4 S5 D4 S6 D7 S8 S9 D8 D0 S2 S3 D1 S4 D4 S7 D5 D0 S2 D1 S4 D2 S0 S1 D9',
                 level_color=get_color(),
                 name='Elementary',
                 door_window_size=500,
                 keep_proportions=False,
                 y_separation=40,
                 border=40,
                 random=False)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.15, sa=1, li=0.9)