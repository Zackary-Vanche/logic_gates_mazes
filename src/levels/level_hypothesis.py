from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import random as rd_random

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
    Sa = Switch(name='?', value=rd_choice([0, 1, 2, 3]))

    V0 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V0',
          switches=[S0, S1])
    V1 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V1',
          switches=[S3, S4])
    V2 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V2',
          switches=[S6, S7])
    V3 = Tree(tree_list=Tree.tree_list_BIN(2),
          name='V3',
          switches=[S9, S10])
    
    tree_list_1 = ["AND", [None], Tree.tree_list_EQU(2)]

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[S2, V0, Sa])
    
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[S5, V1, Sa])
    
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[1])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[1])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[S8, V2, Sa])
    
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[1])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[1])
    T10 = Tree(tree_list=tree_list_1,
                name='T10',
                switches=[S11, V3, Sa])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    exe = 1
    eye = 1

    R0 = Room(name='R0',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R2 = Room(name='R2',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S3, S4])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R4 = Room(name='R4',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S6, S7])
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S8])
    R6 = Room(name='R6',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S9, S10])
    R7 = Room(name='R7',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S11])
    RE = Room(name='RE',
                  position=[1*dx-exe/2+ex/2, 1*dy-eye/2+ey/2, exe, eye],
                  is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=RE,
                relative_position=0.4)
    
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=RE,
                relative_position=0.4)
    
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R5)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=RE,
                relative_position=0.4)
    
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R6)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R7)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=RE,
                relative_position=0.4)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Hypothesis',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE_light_background(hu=rd_random(), sa=0.35, li=0.1)