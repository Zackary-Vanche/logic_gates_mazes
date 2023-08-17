from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_baguenaudier():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    SN1 = Switch(value=1)

    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[SN1])
    T1 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='T1',
              switches=[S0, S1])
    T2 = Tree(tree_list=Tree.tree_list_from_str('FFT TTF'),
              name='T2',
              switches=[S0, S1, S2,
                        S0, S1, S2],
              cut_expression=True)
    T3 = Tree(tree_list=Tree.tree_list_from_str('FFFT TTTF'),
              name='T3',
              switches=[S0, S1, S2, S3,
                        S0, S1, S2, S3],
              cut_expression=True)
    T4 = Tree(tree_list=Tree.tree_list_from_str('FFFFT TTTTF'),
              name='T4',
              switches=[S0, S1, S2, S3, S4,
                        S0, S1, S2, S3, S4],
              cut_expression=True)
    T5 = Tree(tree_list=Tree.tree_list_from_str('FFFFFT TTTTTF'),
              name='T5',
              switches=[S0, S1, S2, S3, S4, S5,
                        S0, S1, S2, S3, S4, S5],
              cut_expression=True)
    T6 = Tree(tree_list=Tree.tree_list_from_str('FFFFFFT TTTTTTF'),
              name='T6',
              switches=[S0, S1, S2, S3, S4, S5, S6,
                        S0, S1, S2, S3, S4, S5, S6],
              cut_expression=True)
    T7 = Tree(tree_list=Tree.tree_list_AND(8),
              name='T7',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7],
              cut_expression=True)

    ex = 1
    ey = 1

    R0 = Room(name='R0',
              position=[2, 2, ex, ey],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=[0, 0, ex, ey],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=[0, 2, ex, ey],
              switches_list=[S2])
    R3 = Room(name='R3',
              position=[0, 4, ex, ey],
              switches_list=[S3])
    R4 = Room(name='R4',
              position=[2, 4, ex, ey],
              switches_list=[S4])
    R5 = Room(name='R5',
              position=[4, 4, ex, ey],
              switches_list=[S5])
    R6 = Room(name='R6',
              position=[4, 2, ex, ey],
              switches_list=[S6])
    R7 = Room(name='R7',
              position=[4, 0, ex, ey],
              switches_list=[S7])
    RE = Room(name='RE',
              position=[2, 0, ex, ey],
              is_exit=True)  # E pour exit ou end

    p = 0.4

    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[p, 0],
              relative_arrival_coordinates=[1, 1])
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1 / 2 - p],
              relative_arrival_coordinates=[1, 1 / 2])
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1 - p],
              relative_arrival_coordinates=[1, 0])
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_departure_coordinates=[1 / 2 - p, 1],
              relative_arrival_coordinates=[1 / 2, 0])
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R0,
              room_arrival=R5,
              relative_departure_coordinates=[1 - p, 1],
              relative_arrival_coordinates=[0, 0])
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R0,
              room_arrival=R6,
              relative_departure_coordinates=[1, 1 / 2 + p],
              relative_arrival_coordinates=[0, 1 / 2])
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R0,
              room_arrival=R7,
              relative_departure_coordinates=[1, p],
              relative_arrival_coordinates=[0, 1])
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2 + p, 0],
              relative_arrival_coordinates=[1 / 2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution='S0 D0 S1 D0 D2 S3 D2 S0 D0 S1 D0 D3 S4 D3 S0 D1 S2 D1 D0 S1 D0 D5 S6 D5 S0 D0 S1 D0 D2 S3 D2 S0 D0 S1 D0 D3 S4 D3 S0 D1 S2 D1 D0 S1 D0 D6 S7 D6 S0 D0 S1 D0 D2 S3 D2 S0 D1 S2 D1 S0 D4 S5 D4 S0 D1 S2 D1 D0 S1 D0 D3 S4 D3 S0 D1 S2 D1 D0 S1 D0 D7',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=1, li=0.9),
                 name='Baguenaudier',
                 door_window_size=450,
                 keep_proportions=False,
                 y_separation=65,
                 border=50)

    return level