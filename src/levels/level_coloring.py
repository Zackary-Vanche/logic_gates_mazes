from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Level_color import Level_color
from Color import Color
from numpy import cos, sin, pi
from random import random as rd_random

n_switches = 5
n_doors = 16

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
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19]

    tree_list_0 = ['DIFF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)]

    V0 = Tree(tree_list=tree_list_0,
                    name='V0',
                    switches=[S0, S1, S10, S11])
    V1 = Tree(tree_list=tree_list_0,
                    name='V1',
                    switches=[S2, S3, S12, S13])
    V2 = Tree(tree_list=tree_list_0,
                    name='V2',
                    switches=[S4, S5, S14, S15])
    V3 = Tree(tree_list=tree_list_0,
                    name='V3',
                    switches=[S6, S7, S16, S17])
    V4 = Tree(tree_list=tree_list_0,
                    name='V4',
                    switches=[S8, S9, S18, S19])
    V5 = Tree(tree_list=tree_list_0,
                    name='V5',
                    switches=[S0, S1, S4, S5])
    V6 = Tree(tree_list=tree_list_0,
                    name='V6',
                    switches=[S4, S5, S8, S9])
    V7 = Tree(tree_list=tree_list_0,
                    name='V7',
                    switches=[S8, S9, S2, S3])
    V8 = Tree(tree_list=tree_list_0,
                    name='V8',
                    switches=[S2, S3, S6, S7])
    V9 = Tree(tree_list=tree_list_0,
                    name='V9',
                    switches=[S6, S7, S0, S1])
    V10 = Tree(tree_list=tree_list_0,
                    name='V10',
                    switches=[S10, S11, S12, S13])
    V11 = Tree(tree_list=tree_list_0,
                    name='V11',
                    switches=[S12, S13, S14, S15])
    V12 = Tree(tree_list=tree_list_0,
                    name='V12',
                    switches=[S14, S15, S16, S17])
    V13 = Tree(tree_list=tree_list_0,
                    name='V13',
                    switches=[S16, S17, S18, S19])
    V14 = Tree(tree_list=tree_list_0,
                    name='V14',
                    switches=[S18, S19, S10, S11])
    V15 = Tree(tree_list=['INFOREQU', Tree.tree_list_SUM(20), [None]],
                    name='V15',
                    switches=Slist + [6])
    
    T0 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T0',
                    switches=[V0, V15])
    T1 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T1',
                    switches=[V1, V15])
    T2 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T2',
                    switches=[V2, V15])
    T3 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T3',
                    switches=[V3, V15])
    T4 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T4',
                    switches=[V4, V15])
    T5 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T5',
                    switches=[V5, V15])
    T6 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T6',
                    switches=[V6, V15])
    T7 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T7',
                    switches=[V7, V15])
    T8 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T8',
                    switches=[V8, V15])
    T9 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T9',
                    switches=[V9, V15])
    T10 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T10',
                    switches=[V10, V15])
    T11 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T11',
                    switches=[V11, V15])
    T12 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T12',
                    switches=[V12, V15])
    T13 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T13',
                    switches=[V13, V15])
    T14 = Tree(tree_list=Tree.tree_list_AND(2),
                    name='T14',
                    switches=[V14, V15])
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14]
    
    T15 = Tree(tree_list=['AND',Tree.tree_list_AND(15),] + [Tree.tree_list_NAND(2)]*10 + [
                          [None],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)],
                          ['INF', ['SUM'] + [Tree.tree_list_BIN(2)]*5, ['SUM'] + [Tree.tree_list_BIN(2)]*5],
                              ],
                name='T15',
                switches=Vlist + Slist + [V15,
                                          S0, S1, S10, S11,
                                          S2, S3, S12, S13,
                                          S4, S5, S8, S9,
                                          S12, S13, S10, S11,
                                          ] + Slist,
                cut_expression_depth_1=True)
    
    dx = 1.6
    dy = 1.2
    ex = dx/2
    ey = dy/2
    
    def position(i):
        alpha = -2*2*pi/7
        if i >= 5:
            r = 1.7
            a = 2*i*pi/5 + alpha
            return [r*cos(a)*dx-ex/2, r*sin(a)*dy-ey/2, ex, ey]
        else:
            r = 1
            a = 2*i*pi/5 + 2*pi/5 + alpha
            return [r*cos(a)*dx-ex/2, r*sin(a)*dy-ey/2, ex, ey]
    exE = ex*0.8
    eyE = ey*0.8
    position_RE = [-exE/2, -eyE/2, exE, eyE]
    
    possible_switches_values = [[0, 0], [0, 1], [1, 0]]

    def get_random_inside_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.35, sa=0.5)
    
    def get_random_surrounding_color():
        hu = rd_random()
        return Color.color_hls(hu, li=0.8, sa=1)

    R0 = Room(name='R0',
                position=position(0),
                switches_list=[S0, S1],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R1 = Room(name='R1',
                position=position(1),
                switches_list=[S2, S3],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R2 = Room(name='R2',
                position=position(2),
                switches_list=[S4, S5],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R3 = Room(name='R3',
                position=position(3),
                switches_list=[S6, S7],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R4 = Room(name='R4',
                position=position(4),
                switches_list=[S8, S9],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R5 = Room(name='R5',
                position=position(5),
                switches_list=[S10, S11],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R6 = Room(name='R6',
                position=position(6),
                switches_list=[S12, S13],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R7 = Room(name='R7',
                position=position(7),
                switches_list=[S14, S15],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R8 = Room(name='R8',
                position=position(8),
                switches_list=[S16, S17],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    R9 = Room(name='R9',
                position=position(9),
                switches_list=[S18, S19],
                possible_switches_values=possible_switches_values,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True,
              inside_color = get_random_inside_color(),
              surrounding_color=get_random_surrounding_color())
    
    rp0 = 0.375
    rp1 = 0.4
    rp2 = 0.65

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R5,
                relative_position=rp0,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R6,
                relative_position=rp0,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R7,
                relative_position=rp0,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R8,
                relative_position=rp0,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R9,
                relative_position=rp0,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R2,
                relative_position=rp1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R4,
                relative_position=rp1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R1,
                relative_position=rp1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R3,
                relative_position=rp1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R0,
                relative_position=rp1,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R7,
                relative_position=rp2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R7,
                room_arrival=R8,
                relative_position=rp2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R9,
                relative_position=rp2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R9,
                room_arrival=R5,
                relative_position=rp2,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R0,
                room_arrival=RE,
                relative_position=0.54,
                inside_color = get_random_inside_color(),
                surrounding_color=get_random_surrounding_color())
    
    hu = 0
    lcolor = Level_color(background_color=Color.color_hls(hu, 0, 0.4),
                         room_color=Color.color_hls(hu, 0.2, 0),
                         letters_color=Color.WHITE,
                         contour_color=Color.color_hls(hu=0.9, li=0.6, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.TOTAL_YELLOW)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution="S1 D0 S10 D0 D5 S4 D6 S9 D6 D5 D9 S6 D3 S17 D3 D9 S1 D0 S10 S11 D10 S12 D10 D0 D15",
                 level_color=lcolor,
                 name='Coloring',
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
    #     print(f'''    T{i} = Tree(tree_list=Tree.tree_list_AND(2),
    #                 name='T{i}',
    #                 switches=[V{i}])''')
    
    return level