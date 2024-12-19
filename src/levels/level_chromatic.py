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
    
    tree_list_0 = Tree.tree_list_XOR(2)

    V0 = Tree(tree_list=tree_list_0,
                    name='V0',
                    switches=[S0, S1])
    V1 = Tree(tree_list=tree_list_0,
                    name='V1',
                    switches=[S1, S2])
    V2 = Tree(tree_list=tree_list_0,
                    name='V2',
                    switches=[S2, S3])
    V3 = Tree(tree_list=tree_list_0,
                    name='V3',
                    switches=[S3, S4])
    V4 = Tree(tree_list=tree_list_0,
                    name='V4',
                    switches=[S4, S5])
    V5 = Tree(tree_list=tree_list_0,
                    name='V5',
                    switches=[S5, S0])
    V6 = Tree(tree_list=tree_list_0,
                    name='V6',
                    switches=[S0, S3])
    V7 = Tree(tree_list=tree_list_0,
                    name='V7',
                    switches=[S1, S4])
    V8 = Tree(tree_list=tree_list_0,
                    name='V8',
                    switches=[S2, S5])
    
    T0 = Tree(tree_list=Tree.tree_list_AND(9),
                name='T0',
                switches=[V0, V1, V2, V3, V4, V5, V6, V7, V8],
               cut_expression_depth_1=False)
    T1 = Tree(tree_list=[None],
                    name='T1',
                    switches=[V0])
    T2 = Tree(tree_list=[None],
                    name='T2',
                    switches=[V1])
    T3 = Tree(tree_list=[None],
                    name='T3',
                    switches=[V2])
    T4 = Tree(tree_list=[None],
                    name='T4',
                    switches=[V3])
    T5 = Tree(tree_list=[None],
                    name='T5',
                    switches=[V4])
    T6 = Tree(tree_list=[None],
                    name='T6',
                    switches=[V5])
    T7 = Tree(tree_list=[None],
                    name='T7',
                    switches=[V6])
    T8 = Tree(tree_list=[None],
                    name='T8',
                    switches=[V7])
    T9 = Tree(tree_list=[None],
                    name='T9',
                    switches=[V8])
    T10 = Tree(tree_list=['INF', Tree.tree_list_SUM(3), Tree.tree_list_SUM(3)],
                name='T10',
                switches=[S0, S1, S2, S3, S4, S5],
               cut_expression_depth_1=False)
    
    def position(i):
        n = 8.5
        alpha = i*2*np.pi/n - np.pi/2 + 2*np.pi/n
        r = 1 + 1*i/7
        ex = 0.25 + 0.75*i/7
        ey = 0.25 + 0.55*i/7
        return [1.5*r*np.cos(alpha), r*np.sin(alpha), ex, ey]
    
    def get_random_inside_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.8, sa=0.25)
    
    def get_random_surrounding_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.5, sa=1)

    R0 = Room(name='R0',
                position=position(7),
                switches_list=[S0, S1, S2, S3, S4, S5],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R1 = Room(name='R1',
                position=position(0),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R2 = Room(name='R2',
                position=position(1),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R3 = Room(name='R3',
                position=position(2),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R4 = Room(name='R4',
                position=position(3),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R5 = Room(name='R5',
                position=position(4),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R6 = Room(name='R6',
                position=position(5),
                switches_list=[],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    RE = Room(name='RE',
              position=position(6),
              is_exit=True,
              inside_color = get_random_inside_color(),
              surrounding_color=get_random_surrounding_color())
    
    rp = 0.25
    
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0.9, 0.9],
                relative_arrival_coordinates=[0.1, 0.1],
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R4,
                relative_position=rp,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R5,
                relative_position=rp,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R6,
                relative_position=rp,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=RE,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    
    hu = 0.16
    lcolor = Level_color(background_color=Color.color_hls(hu, 0, 0.4),
                         room_color=Color.color_hls(hu, 0.7, 0.2),
                         letters_color=Color.WHITE,
                         contour_color=Color.TOTAL_YELLOW,
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.TOTAL_YELLOW)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S1 S3 S5 D0 D6 D10",
                 level_color=lcolor,
                 name='Chromatic',
                 keep_proportions=True,
                 door_window_size=300,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    # for i, door in enumerate(level.doors_list):
    #     r0 = door.room_departure
    #     r1 = door.room_arrival
    #     if r1.is_exit:
    #         continue
    #     s0, = r0.switches_list
    #     s1, = r1.switches_list
    #     print(f'''    V{i} = Tree(tree_list=tree_list_0,
    #                 name='V{i}',
    #                 switches=[{s0.name}, {s1.name}])''')
    # for i, door in enumerate(level.doors_list):
    #     print(f'''    T{i} = Tree(tree_list=[None],
    #                 name='T{i}',
    #                 switches=[V{i}])''')
    
    return level