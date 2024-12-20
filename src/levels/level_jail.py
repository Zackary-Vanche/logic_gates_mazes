from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import random

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

    Slist = [S5, S6, S7, S8, S9]

    V0 = Tree(tree_list=['MOD', Tree.tree_list_SUM(len(Slist)), [None]],
          name='V0',
          switches=Slist + [2])
    V1 = Tree(tree_list=Tree.tree_list_EQU(2),
          name='V1',
          switches=[V0, 1])
    
    tree_list = ["AND",
                 ["EQU", [None], [None]],
                 [None]]
    tree_list = ["EQU", [None], [None]]

    T0 = Tree(tree_list=tree_list,
        name='T0',
        switches=[S0, S5])
    T1 = Tree(tree_list=tree_list,
        name='T1',
        switches=[S1, S6])
    T2 = Tree(tree_list=tree_list,
        name='T2',
        switches=[S0, S5])
    T3 = Tree(tree_list=tree_list,
        name='T3',
        switches=[S2, S7])
    T4 = Tree(tree_list=tree_list,
        name='T4',
        switches=[S1, S6])
    T5 = Tree(tree_list=tree_list,
        name='T5',
        switches=[S3, S8])
    T6 = Tree(tree_list=tree_list,
        name='T6',
        switches=[S2, S7])
    T7 = Tree(tree_list=tree_list,
        name='T7',
        switches=[S3, S8])
    T8 = Tree(tree_list=tree_list,
        name='T8',
        switches=[S2, S7])
    T9 = Tree(tree_list=tree_list,
        name='T9',
        switches=[S4, S9])
    T10 = Tree(tree_list=tree_list,
        name='T10',
        switches=[S3, S8])
    T11 = Tree(tree_list=tree_list,
        name='T11',
        switches=[S4, S9])
    T12 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T12',
                switches=[S0, S5])
    T13 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T13',
                switches=[S1, S6])
    T14 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T14',
                switches=[S2, S7])
    T15 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T15',
                switches=[S3, S8])
    T16 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T16',
                switches=[S4, S9])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[V1])

    dx = 1.4
    dy = 1
    ex = 1.05
    ey = 0.5
    
    hu = random()
    li = 0.6
    sa = 0.4
    color0 = Color.color_hls(hu, li=li, sa=sa)
    color1 = Color.color_hls(hu+1/4, li=li, sa=sa)
    color2 = Color.color_hls(hu+1/2, li=li, sa=sa)
    color3 = Color.color_hls(hu+3/4, li=li, sa=sa)

    R0 = Room(name='R0',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S0],
                inside_color=color0)
    R1 = Room(name='R1',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[S1],
                inside_color=color0)
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S2],
                inside_color=color0)
    R3 = Room(name='R3',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[S3],
                inside_color=color0)
    R4 = Room(name='R4',
                position=[-1*dx, 6*dy, ex, ey],
                switches_list=[S4],
                inside_color=color0)
    R5 = Room(name='R5',
                position=[3*dx, -1*dy, ex, ey],
                switches_list=[S5],
                inside_color=color1)
    R6 = Room(name='R6',
                position=[6*dx, 3*dy, ex, ey],
                switches_list=[S6],
                inside_color=color1)
    R7 = Room(name='R7',
                position=[-1*dx, 2*dy, ex, ey],
                switches_list=[S7],
                inside_color=color1)
    R8 = Room(name='R8',
                position=[2*dx, 6*dy, ex, ey],
                switches_list=[S8],
                inside_color=color1)
    R9 = Room(name='R9',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S9],
                inside_color=color1)
    RE = Room(name='RE',
              position=[1*dx, 0*dy, ex, ey],
              is_exit=True,
              inside_color=Color.color_hls(0, li=li, sa=0))

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R5,
                room_arrival=R1,
                relative_position=0.75,
                inside_color=color2)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R6,
                room_arrival=R0,
                relative_position=0.5,
                inside_color=color2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R5,
                room_arrival=R2,
                relative_position=0.3,
                inside_color=color2)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R7,
                room_arrival=R0,
                relative_position=0.775,
                inside_color=color2)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R6,
                room_arrival=R3,
                relative_position=0.75,
                inside_color=color2)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R8,
                room_arrival=R1,
                relative_position=0.5,
                inside_color=color2)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R7,
                room_arrival=R3,
                relative_position=0.35,
                inside_color=color2)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R8,
                room_arrival=R2,
                relative_position=0.8,
                inside_color=color2)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R7,
                room_arrival=R4,
                relative_position=0.5,
                inside_color=color2)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R2,
                relative_position=0.35,
                inside_color=color2)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R8,
                room_arrival=R4,
                relative_position=0.5,
                inside_color=color2)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R9,
                room_arrival=R3,
                relative_position=0.5,
                inside_color=color2)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=R5,
                inside_color=color3)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R6,
                inside_color=color3)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R7,
                inside_color=color3)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=R8,
                inside_color=color3)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R4,
                room_arrival=R9,
                inside_color=color3)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R0,
                room_arrival=RE,
                inside_color=Color.color_hls(0, li=li, sa=0))

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17],
                 fastest_solution="S0 D12 S5 D0 S1 D13 S6 D4 S3 D15 S8 D10 S4 D16 S9 D9 S2 D14 S7 D3 D17",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Jail',
                 keep_proportions=True,
                 door_window_size=300,
                 uniform_inside_room_color=False)
    
    return level