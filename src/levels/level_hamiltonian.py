from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color

def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')

    T0 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T0',
              switches=[S1, S2])
    T1 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T1',
              switches=[S2, S4])
    T2 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T2',
              switches=[S4, S5])
    T3 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T3',
              switches=[S5, S7])
    T4 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T4',
              switches=[S7, S8])
    T5 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T5',
              switches=[S8, S10])
    T6 = Tree(tree_list=Tree.tree_list_from_str('FT'),
              name='T6',
              switches=[S10, S11])
    T7 = Tree(tree_list=Tree.tree_list_from_str('TF'),
              name='T7',
              switches=[S1, S11])
    T8 = Tree(tree_list=Tree.tree_list_from_str('TTFF'),
              name='T8',
              switches=[S0, S1, S3, S4])
    T9 = Tree(tree_list=Tree.tree_list_from_str('TTFF'),
              name='T9',
              switches=[S3, S4, S6, S7])
    T10 = Tree(tree_list=Tree.tree_list_from_str('TTFF'),
               name='T10',
               switches=[S6, S7, S9, S10])
    T11 = Tree(tree_list=Tree.tree_list_from_str('FFTT'),
               name='T11',
               switches=[S0, S1, S9, S10])
    T12 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               name='T12',
               switches=[S2, S5])
    T13 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               name='T13',
               switches=[S5, S8])
    T14 = Tree(tree_list=Tree.tree_list_from_str('TF'),
               name='T14',
               switches=[S8, S11])
    T15 = Tree(tree_list=Tree.tree_list_from_str('FT'),
               name='T15',
               switches=[S2, S11])
    T16 = Tree(tree_list=Tree.tree_list_AND(12),
               name='T16',
               switches=[S0, S1, S2,
                         S3, S4, S5,
                         S6, S7, S8,
                         S9, S10, S11])

    a = 0.3
    c = 2 - a

    R0 = Room(name='R0',
              position=[0, 0, c, c],
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[3, 1, 1, 1],
              switches_list=[S2])
    R2 = Room(name='R2',
              position=[5 + a, 0, c, c],
              switches_list=[S3, S4])
    R3 = Room(name='R3',
              position=[5, 3, 1, 1],
              switches_list=[S5])
    R4 = Room(name='R4',
              position=[5 + a, 5 + a, c, c],
              switches_list=[S6, S7])
    R5 = Room(name='R5',
              position=[3, 5, 1, 1],
              switches_list=[S8])
    R6 = Room(name='R6',
              position=[0, 5 + a, c, c],
              switches_list=[S9, S10])
    R7 = Room(name='R7',
              position=[1, 3, 1, 1],
              switches_list=[S11])
    RE = Room(name='RE',
              position=[3.2, 3.2, 0.6, 0.6],
              switches_list=[],
              is_exit=True)

    e = 0.05
    d0 = e
    d1 = 1 - e

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=[d0, d0],
              relative_arrival_coordinates=[d1, d0])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R2,
              room_arrival=R1,
              relative_departure_coordinates=[d0, d0],
              relative_arrival_coordinates=[d1, d0])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R3,
              room_arrival=R2,
              relative_departure_coordinates=[d1, d0],
              relative_arrival_coordinates=[d1, d1])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R4,
              room_arrival=R3,
              relative_departure_coordinates=[d1, d0],
              relative_arrival_coordinates=[d1, d1])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R5,
              room_arrival=R4,
              relative_departure_coordinates=[d1, d1],
              relative_arrival_coordinates=[d0, d1])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R6,
              room_arrival=R5,
              relative_departure_coordinates=[d1, d1],
              relative_arrival_coordinates=[d0, d1])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R7,
              room_arrival=R6,
              relative_departure_coordinates=[d0, d1],
              relative_arrival_coordinates=[d0, d0])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=R7,
              relative_departure_coordinates=[d0, d1],
              relative_arrival_coordinates=[d0, d0])
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=[1, 0],
              relative_arrival_coordinates=[0, 0])
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R2,
              room_arrival=R4,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 0])
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R4,
               room_arrival=R6,
               relative_departure_coordinates=[0, 1],
               relative_arrival_coordinates=[1, 1])
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R6,
               room_arrival=R0,
               relative_departure_coordinates=[0, 0],
               relative_arrival_coordinates=[0, 1])
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R1,
               room_arrival=R3)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R3,
               room_arrival=R5)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R5,
               room_arrival=R7)
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R7,
               room_arrival=R1)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R1,
               room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution="S0 S1 D7 S11 D6 S9 S10 D5 S8 D4 S6 S7 D3 S5 D2 S3 S4 D1 S2 D16",
                 level_color=get_color(),
                 name='Hamiltonian',
                 door_window_size=400,
                 keep_proportions=False)

    return level

def get_color():
    return Level_color(background_color=Color.PSEUDO_DARK_GREEN,
                              room_color=Color.DARK_GREEN,
                              contour_color=Color.TOTAL_GREEN,
                              letters_color=Color.color_hls(hu=0.6, li=0.95, sa=0.95),
                              letter_contour_color=Color.BLACK,
                              inside_room_color=Color.color_hls(hu=0.6, li=0.95, sa=0.95),
                              surrounding_color=Color.TOTAL_GREEN)