from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f():
    v = 1

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8')

    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11')

    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14', value=v)

    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16')
    S17 = Switch(name='S17', value=v)

    S18 = Switch(name='S18')
    S19 = Switch(name='S19', value=v)
    S20 = Switch(name='S20', value=v)
    
    Slist_0 = [S0, S1, S2]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
              name='V0',
              switches=Slist_0)

    tree_list_EQU = ['EQU', [None], [None]]

    T0 = Tree(tree_list=tree_list_EQU,
              name='T0',
              switches=[V0, 0])
    T1 = Tree(tree_list=tree_list_EQU,
              name='T1',
              switches=[V0, 1])
    T2 = Tree(tree_list=tree_list_EQU,
              name='T2',
              switches=[V0, 2])
    T3 = Tree(tree_list=tree_list_EQU,
              name='T3',
              switches=[V0, 3])
    T4 = Tree(tree_list=tree_list_EQU,
              name='T4',
              switches=[V0, 4])

    T5 = Tree(tree_list=tree_list_EQU,
              name='T5',
              switches=[V0, 0])
    T6 = Tree(tree_list=tree_list_EQU,
              name='T6',
              switches=[V0, 1])
    T7 = Tree(tree_list=tree_list_EQU,
              name='T7',
              switches=[V0, 2])
    T8 = Tree(tree_list=tree_list_EQU,
              name='T8',
              switches=[V0, 3])
    T9 = Tree(tree_list=tree_list_EQU,
              name='T9',
              switches=[V0, 4])

    T10 = Tree(tree_list=tree_list_EQU,
               name='T10',
               switches=[V0, 0])
    T11 = Tree(tree_list=tree_list_EQU,
               name='T11',
               switches=[V0, 1])
    T12 = Tree(tree_list=tree_list_EQU,
               name='T12',
               switches=[V0, 2])
    T13 = Tree(tree_list=tree_list_EQU,
               name='T13',
               switches=[V0, 3])
    T14 = Tree(tree_list=tree_list_EQU,
               name='T14',
               switches=[V0, 4])

    T15 = Tree(tree_list=['EQUSET'] + [Tree.tree_list_BIN(3)] * 6 + [[None]] * 6,
               name='T15',
               switches=[S3, S4, S5,
                         S6, S7, S8,
                         S9, S10, S11,
                         S12, S13, S14,
                         S15, S16, S17,
                         S18, S19, S20,
                         1,
                         2,
                         3,
                         4,
                         5,
                         6],
               cut_expression=True)

    T16 = Tree(tree_list=['EQU', Tree.tree_list_BIN(3 * 7), [None]],
               name='T16',
               switches=[S0, S1, S2,
                         S3, S4, S5,
                         S6, S7, S8,
                         S9, S10, S11,
                         S12, S13, S14,
                         S15, S16, S17,
                         S18, S19, S20,
                         Switch(value=342384)])

    ex = 0.75
    ey = 0.75
    deltay = 1 - ey

    R0 = Room(name='R0',
              position=[0, 0, ex, 12],
              switches_list=[S0, S1, S2, ])
    R1 = Room(name='R1',
              position=[2, 1 + deltay, 4, ey],
              switches_list=[S3, S4, S5, ])
    R2 = Room(name='R2',
              position=[2, 3 + deltay, 4, ey],
              switches_list=[S6, S7, S8, ])
    R3 = Room(name='R3',
              position=[2, 5 + deltay, 4, ey],
              switches_list=[S9, S10, S11, ])
    R4 = Room(name='R4',
              position=[2, 7 + deltay, 4, ey],
              switches_list=[S12, S13, S14, ])
    R5 = Room(name='R5',
              position=[2, 9 + deltay, 4, ey],
              switches_list=[S15, S16, S17, ])
    R6 = Room(name='R6',
              position=[2, 11 + deltay, 4, ey],
              switches_list=[S18, S19, S20, ])
    R7 = Room(name='R7',
              position=[7 + 1 - ex, 0, ex, 12],
              switches_list=[])
    RE = Room(name='RE',
              position=[3+1/8, -1, 2, 1],
              is_exit=True)  # E pour exit ou end

    rp = 1 / 2

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 3.5 / 12],
              relative_arrival_coordinates=[0, 1 / 2])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=[1, 5.5 / 12],
              relative_arrival_coordinates=[0, 1 / 2])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=[1, 7.5 / 12],
              relative_arrival_coordinates=[0, 1 / 2])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=[1, 9.5 / 12],
              relative_arrival_coordinates=[0, 1 / 2])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=[1, 11.5 / 12],
              relative_arrival_coordinates=[0, 1 / 2])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R4,
              room_arrival=R5,
              relative_position=rp)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R5,
              room_arrival=R6,
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R2,
               room_arrival=R7,
               relative_position=rp,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, 1.5 / 12])
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R3,
               room_arrival=R7,
               relative_position=rp,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, 3.5 / 12])
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R4,
               room_arrival=R7,
               relative_position=rp,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, 5.5 / 12])
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R5,
               room_arrival=R7,
               relative_position=rp,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, 7.5 / 12])
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R6,
               room_arrival=R7,
               relative_position=rp,
               relative_departure_coordinates=[1, 1 / 2],
               relative_arrival_coordinates=[0, 9.5 / 12])
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R7,
               room_arrival=R0,
               relative_position=rp,
               relative_departure_coordinates=[0, 0.6 / 12],
               relative_arrival_coordinates=[1, 0.6 / 12])
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R0,
               room_arrival=RE,
               relative_position=rp,
               relative_departure_coordinates=[1, 0],
               relative_arrival_coordinates=[0, 1 / 2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution='D0 S3 S4 D5 S6 S7 D10 D15 S0 D1 S7 D6 S10 D11 D15 S0 D0 S3 D5 S6 D10 D15 S1 D2 S9 S11 D7 S12 S14 D12 D15 S0 D3 S14 D8 S17 D13 D15 S0 D2 S9 D7 S12 D12 D15 S0 S1 D1 S6 S7 S8 D6 S9 S10 S11 D11 D15 S0 D0 S4 S5 D5 S7 S8 D10 D15 S1 D2 S10 S11 D7 S13 S14 D12 D15 S0 S1 D1 S6 S7 S8 D6 S9 S10 S11 D11 D15 S0 S2 D4 S15 S16 S17 D9 S18 S19 S20 D14 D15 S0 S1 S2 D3 S14 D8 S17 D13 D15 S0 D2 S9 S11 D7 S12 S14 D12 D15 S0 S1 D1 S7 D6 S10 D11 D15 S0 D0 S3 S4 D5 S6 S7 D10 D15 D16',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.175, sa=0.9, li=0.7),
                 name='Inversions',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level