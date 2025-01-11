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
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')

    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)

    T0 = Tree(tree_list=Tree.tree_list_NONO(8),
              name='T0',
              switches=[SN2, SN1, SN1, S0, S1, S2, S3, S4])
    T1 = Tree(tree_list=Tree.tree_list_NONO(8),
              name='T1',
              switches=[SN2, SN1, SN1, S5, S6, S7, S8, S9])
    T2 = Tree(tree_list=Tree.tree_list_NONO(8),
              name='T2',
              switches=[SN2, SN1, SN2, S10, S11, S12, S13, S14])
    T3 = Tree(tree_list=Tree.tree_list_NONO(7),
              name='T3',
              switches=[SN1, SN1, S15, S16, S17, S18, S19])
    T4 = Tree(tree_list=Tree.tree_list_NONO(7),
              name='T4',
              switches=[SN1, SN1, S20, S21, S22, S23, S24])
    T5 = Tree(tree_list=['AND',
                         Tree.tree_list_NONO(8),
                         Tree.tree_list_NONO(8),
                         Tree.tree_list_NONO(7),
                         Tree.tree_list_NONO(7),
                         Tree.tree_list_NONO(8),
                         Tree.tree_list_NONO(8),
                         Tree.tree_list_NONO(7)],
              name='T5',
              switches=[SN2, SN1, SN1, S0, S5, S10, S15, S20,
                        SN2, SN1, SN1, S1, S6, S11, S16, S21,
                        SN1, SN1, S2, S7, S12, S17, S22,
                        SN1, SN2, S3, S8, S13, S18, S23,
                        SN2, SN1, SN1, S4, S9, S14, S19, S24,
                        SN2, SN2, SN1, S4, S8, S12, S16, S20,
                        SN1, SN2, S0, S6, S12, S18, S24],
              cut_expression=True,
              cut_expression_separator=')')

    R0 = Room(name='R0',
              position=[0, 0, 5, 1],
              switches_list=[S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
              position=[1, 2, 5, 1],
              switches_list=[S5, S6, S7, S8, S9])
    R2 = Room(name='R2',
              position=[0, 4, 5, 1],
              switches_list=[S10, S11, S12, S13, S14])
    R3 = Room(name='R3',
              position=[1, 6, 5, 1],
              switches_list=[S15, S16, S17, S18, S19])
    R4 = Room(name='R4',
              position=[0, 8, 5, 1],
              switches_list=[S20, S21, S22, S23, S24])
    R5 = Room(name='R5',
              position=[1, 10, 1, 1],
              switches_list=[])
    RE = Room(name='RE',
              position=[3, 10, 3, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 1])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=[1, 1],
              relative_arrival_coordinates=[1, 1])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_departure_coordinates=[0, 1],
              relative_arrival_coordinates=[0, 1])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=RE,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, 1 / 2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution='S0 S4 D0 S6 S8 D1 S10 S13 S14 D2 S16 D3 S22 D4 D5',
                 level_color=get_color(),
                 name='Nonogram',
                 door_window_size=400,
                 keep_proportions=False)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.3, sa=1, li=0.22)