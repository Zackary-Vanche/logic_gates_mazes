from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def f():
    v = 1

    # pancakes
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    # count
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')

    # pancakes
    # 0
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    # 1
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13')
    # 2
    S14 = Switch(name='S14')
    S15 = Switch(name='S15', value=v)
    # 3
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17', value=v)
    # count
    S18 = Switch(name='S18', value=v)
    S19 = Switch(name='S19', value=v)

    SN0 = Switch(name='0', value=0)
    SN1 = Switch(name='1', value=1)
    SN2 = Switch(name='2', value=2)
    SN3 = Switch(name='3', value=3)

    # def tree_list_EQU_BIN(nequ, nbin):
    #     return ['EQU'] + [Tree.tree_list_BIN(nbin)] * nequ
    
    tree_list_0 = ['EQU', [None], Tree.tree_list_BIN(8)]

    nbin = 2

    Slist0 = [S0, S1, S2, S3, S4, S5, S6, S7]
    Slist1 = [S16, S17, S14, S15, S12, S13, S10, S11]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
              name='V0',
              switches=Slist0)

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[V0,
                        S12, S13, S10, S11,
                        S14, S15, S16, S17],
              cut_expression=True,
              cut_expression_separator=']')
    T1 = Tree(tree_list=tree_list_0,
              name='T1',
              switches=[V0,
                        S14, S15, S12, S13, S10, S11,
                        S16, S17],
              cut_expression=True,
              cut_expression_separator=']')
    T2 = Tree(tree_list=tree_list_0,
              name='T2',
              switches=[V0] + Slist1,
              cut_expression=True,
              cut_expression_separator=']')

    T3 = Tree(tree_list=['EQU',
                         ['SUM',
                          Tree.tree_list_BIN(2),
                          [None]],
                         Tree.tree_list_BIN(2)],
              name='T3',
              switches=[S8, S9, SN1, S18, S19],
              cut_expression=True,
              cut_expression_separator=']')

    T4 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(10)] * 2,
              name='T4',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9,
                        S10, S11, S12, S13, S14, S15, S16, S17, S18, S19])

    T5 = Tree(tree_list=['DIFF'] + [Tree.tree_list_BIN(2)] * 4,
              name='T5',
              switches=[S10, S11, S12, S13, S14, S15, S16, S17])

    T5 = Tree(tree_list=[None],
              name='T5',
              switches=[SN1])

    T6 = Tree(tree_list=['AND'] + [['EQU', [None], Tree.tree_list_BIN(nbin)]] * 4,
              name='T6',
              switches=[SN0, S0, S1,
                        SN3, S2, S3,
                        SN2, S4, S5,
                        SN1, S6, S7],
              cut_expression=True,
              cut_expression_separator=')')

    # T6 = Tree(tree_list=[None],
    #           
    #           name='T6',
    #           switches = [SN1])

    R0 = Room(name='R0',
              position=[-0.5, 2, 2, 5],
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
              position=[2.75, 4, 0.5, 3],
              switches_list=[])
    R2 = Room(name='R2',
              position=[4.5, 2, 2, 5],
              switches_list=[S10, S11, S12, S13, S14, S15, S16, S17, S18, S19])
    R3 = Room(name='R3',
              position=[2.75, 3.25, 0.5, 0.5],
              switches_list=[])
    RE = Room(name='RE',
              position=[2, 2, 2, 0.5],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 2.5 / 5],
              relative_arrival_coordinates=[0, 0.5 / 3])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 3.5 / 5],
              relative_arrival_coordinates=[0, 1.5 / 3])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, 4.5 / 5],
              relative_arrival_coordinates=[0, 2.5 / 3])

    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=[1, 1 / 2],
              relative_arrival_coordinates=[0, 3.5 / 5])

    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=[0, 1.5 / 5],
              relative_arrival_coordinates=[1, 1 / 2])

    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_departure_coordinates=[0, 1 / 2],
              relative_arrival_coordinates=[1, 1.5 / 5])

    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R3,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2, 0],
              relative_arrival_coordinates=[1 / 2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S0 S1 S3 S4 S9 D2 D3 S10 S11 S12 S13 S14 S15 S16 S17 S18 D4 D5 S1 S5 S8 S9 D1 D3 S11 S15 S18 S19 D4 D5 S0 S2 S4 S6 S8 D2 D3 S10 S12 S14 S16 S18 D4 D6',
                 level_color=get_color(),
                 name='Pancake sorting',
                 door_window_size=300,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(0.05, sa=0.4, li=0.4)