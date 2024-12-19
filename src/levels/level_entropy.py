from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

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
    
    tree_list_1 = [None]
    
    tnot = Tree.tree_list_from_str('F')
    
    def tl(n):
        return ['AND',
                tnot,
                Tree.tree_list_from_str(' '.join(['T']*n))]

    T0 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(2)]*2,
                name='T0',
                switches=[S0, S1,
                          S8, S9])
    T1 = Tree(tree_list=tnot,
                name='T1',
                switches=[S2])
    T2 = Tree(tree_list=tl(3),
                name='T2',
                switches=[S3,
                          S2, S4, S5])
    T3 = Tree(tree_list=tl(2),
                name='T3',
                switches=[S4,
                          S2, S3])
    T4 = Tree(tree_list=tl(3),
                name='T4',
                switches=[S5,
                          S3, S4, S6])
    T5 = Tree(tree_list=tl(3),
                name='T5',
                switches=[S6,
                          S4, S5, S7])
    T6 = Tree(tree_list=tl(2),
                name='T6',
                switches=[S7,
                          S5, S6])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[S2])
    T8 = Tree(tree_list=tree_list_1,
                name='T8',
                switches=[S3])
    T9 = Tree(tree_list=tree_list_1,
                name='T9',
                switches=[S4])
    T10 = Tree(tree_list=tree_list_1,
                name='T10',
                switches=[S5])
    T11 = Tree(tree_list=tree_list_1,
                name='T11',
                switches=[S6])
    T12 = Tree(tree_list=tree_list_1,
                name='T12',
                switches=[S7])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[1])
    T14 = Tree(tree_list=['EQU',
                          ['SUM', [None], Tree.tree_list_BIN(2)],
                          Tree.tree_list_BIN(2),
                          ],
                name='T14',
                switches=[1, S0, S1, S8, S9])
    T15 = Tree(tree_list=['AND',
                          Tree.tree_list_OR(2),
                          Tree.tree_list_from_str('FT')],
                name='T15',
                switches=[S6, S7, S0, S1])
    ax = 0.3
    ay = 1.1
    ex = 0.2
    ey = 0.4
    epsilony = 0.175

    R0 = Room(name='R0',
                position=[3*ax, 1*ay-2*epsilony+ex+0.4, ex, ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[0, 2*ay-ey/2, 6*ax+ex, ey/4],
              switches_list=[])
    R2 = Room(name='R2',
                position=[0, 1*ay+epsilony, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[ax, 1*ay, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[2*ax, 1*ay-epsilony, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[4*ax, 1*ay-epsilony, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[5*ax, 1*ay, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[6*ax, 1*ay+epsilony, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[0, ey, 6*ax+ex, ey/4],
                switches_list=[])
    R9 = Room(name='R9',
                position=[3*ax, 1*ay-2*epsilony, ex, ey],
                switches_list=[S8, S9])
    RE = Room(name='RE',
              position=[(6*ax+ex)/2-ex/2, 0, ex, ey/2],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=[2/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=[3/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=[5/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=[6/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=[7/8, 0],
                relative_arrival_coordinates=[1/2, 1])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/7, 1])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R3,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[2/7, 1])
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[3/7, 1])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[4/7, 1])
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[5/7, 1])
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R8,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[6/7, 1])
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R9,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R9,
                room_arrival=R0)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.1, li=0.5)
    lcolor.surrounding_color = Color.TOTAL_RED

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0,
                             D1, D2, D3, D4, D5, D6,
                             D7, D8, D9, D10, D11, D12,
                             D13, D14,
                             D15],
                 fastest_solution='D0 D1 S2 D7 D13 S8 D14 S0 D0 D3 S4 D9 D13 S8 S9 D14 S0 S1 D0 D5 S6 D11 D15',
                 level_color=lcolor,
                 name='Entropy',
                 keep_proportions=True,
                 door_window_size=408)
    
    return level
# [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13]