from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
import numpy as np
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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
    
    tree_list_0 = ['DIFF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)]

    V0 = Tree(tree_list=tree_list_0,
                    name='V0',
                    switches=[S0, S1, S2, S3])
    V1 = Tree(tree_list=tree_list_0,
                    name='V1',
                    switches=[S0, S1, S4, S5])
    V2 = Tree(tree_list=tree_list_0,
                    name='V2',
                    switches=[S0, S1, S6, S7])
    V3 = Tree(tree_list=tree_list_0,
                    name='V3',
                    switches=[S0, S1, S8, S9])
    V4 = Tree(tree_list=tree_list_0,
                    name='V4',
                    switches=[S0, S1, S10, S11])
    V5 = Tree(tree_list=tree_list_0,
                    name='V5',
                    switches=[S2, S3, S4, S5])
    V6 = Tree(tree_list=tree_list_0,
                    name='V6',
                    switches=[S4, S5, S6, S7])
    V7 = Tree(tree_list=tree_list_0,
                    name='V7',
                    switches=[S6, S7, S8, S9])
    V8 = Tree(tree_list=tree_list_0,
                    name='V8',
                    switches=[S8, S9, S10, S11])
    V9 = Tree(tree_list=tree_list_0,
                    name='V9',
                    switches=[S10, S11, S2, S3])
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9,]

    T0 = Tree(tree_list=[None],
                    name='T0',
                    switches=[V0])
    T1 = Tree(tree_list=[None],
                    name='T1',
                    switches=[V1])
    T2 = Tree(tree_list=[None],
                    name='T2',
                    switches=[V2])
    T3 = Tree(tree_list=[None],
                    name='T3',
                    switches=[V3])
    T4 = Tree(tree_list=[None],
                    name='T4',
                    switches=[V4])
    T5 = Tree(tree_list=[None],
                    name='T5',
                    switches=[V5])
    T6 = Tree(tree_list=[None],
                    name='T6',
                    switches=[V6])
    T7 = Tree(tree_list=[None],
                    name='T7',
                    switches=[V7])
    T8 = Tree(tree_list=[None],
                    name='T8',
                    switches=[V8])
    T9 = Tree(tree_list=[None],
                    name='T9',
                    switches=[V9])
    T10 = Tree(tree_list=Tree.tree_list_AND(len(Vlist)),
                    name='T10',
                    switches=Vlist)
    T11 = Tree(tree_list=['INFOREQU', Tree.tree_list_SUM(len(Slist)), [None]],
                name='T11',
                switches=Slist + [5])
    T12 = Tree(tree_list=['DIFF', ['SUM'] + [Tree.tree_list_BIN(2)] * 6,[None]],
                name='T12',
                switches=Slist + [8])
    T13 = Tree(tree_list=['AND',
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],],
                name='T13',
                switches=Slist)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    def position(i):
        i = i-1
        alpha = i*2*np.pi/5 - np.pi/10
        return [dx*np.cos(alpha), dy*np.sin(alpha), ex, ey]
    [dx2, dy2, ex2, ey2] = position(2)
    [dx5, dy5, ex5, ey5] = position(5)
    exe = 0.8
    dye = dy2 - dx5
    
    def get_random_inside_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.15, sa=1)
    
    def get_random_surrounding_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.6, sa=1)
    
    R0 = Room(name='R0',
                position=[0, 0, ex, ey],
                switches_list=[S0, S1],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R1 = Room(name='R1',
                position=position(1),
                switches_list=[S2, S3],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R2 = Room(name='R2',
                position=position(2),
                switches_list=[S4, S5],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R3 = Room(name='R3',
                position=position(3),
                switches_list=[S6, S7],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R4 = Room(name='R4',
                position=position(4),
                switches_list=[S8, S9],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R5 = Room(name='R5',
                position=position(5),
                switches_list=[S10, S11],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R6 = Room(name='R6',
                position=[dx5+exe, dy5, ex, ey],
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R7 = Room(name='R7',
                position=[dx5+2*exe, dy5, ex, ey],
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R8 = Room(name='R8',
                position=[dx5+2*exe, (dy5+dy2)/2, ex, ey],
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    RE = Room(name='RE',
              position=[dx5+2*exe, dy2, ex, ey],
              is_exit=True,
              inside_color = get_random_inside_color(),
              surrounding_color=get_random_surrounding_color())

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R5,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R3,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R4,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R5,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R6,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R7,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R8,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=RE,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution="S1 D2 S6 D2 D0 S2 S3 D9 S10 D10 D11 D12 D13",
                 level_color=get_color(),
                 name='Wheel',
                 keep_proportions=True,
                 door_window_size=300,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    # for i, door in enumerate(level.doors_list):
    #     r0 = door.room_departure
    #     r1 = door.room_arrival
    #     if r1.is_exit:
    #         continue
    #     s0, s1 = r0.switches_list
    #     s2, s3 = r1.switches_list
    #     print(f'''    V{i} = Tree(tree_list=tree_list_0,
    #                 name='V{i}',
    #                 switches=[{s0.name}, {s1.name}, {s2.name}, {s3.name}])''')
    # for i, door in enumerate(level.doors_list):
    #     print(f'''    T{i} = Tree(tree_list=[None],
    #                 name='T{i}',
    #                 switches=[V{i}])''')
    
    return level

def get_color():
    hu = 0
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.6, sa=0),
                         room_color=Color.color_hls(hu, li=0.2, sa=0),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.6, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.TOTAL_YELLOW)
    return lcolor