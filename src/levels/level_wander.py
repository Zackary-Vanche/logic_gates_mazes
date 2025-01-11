from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
import numpy as np

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
    S25 = Switch(name='S25')
    
    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ],
                name='T0',
                switches=[S0, S1, 2,
                          S0, S2, S3, 1,
                          S1, S4, S5, 2,],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],],
                name='T1',
                switches=[S2, S6, S7, 1,
                          S3, S4, S8, S9, 2,
                          S5, S10, S11, 2,],
                cut_expression_depth_1=True)
    T2 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],],
                name='T2',
                switches=[S6, S12, 2,
                          S7, S8, S13, S14, 2,
                          S9, S10, S15, S16, 2,
                          S11, S17, 2,],
                cut_expression_depth_1=True)
    T3 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],],
                name='T3',
                switches=[S12, S13, S18, 2,
                          S14, S15, S19, S20, 2,
                          S16, S17, S21, 2,
                          S18, S19, S22, 2,
                          S20, S21, S23, 2,
                          S22, S23, 2,],
                cut_expression_depth_1=True)

    T4 = Tree(tree_list=[None],
                    name='T4',
                    switches=[S0])
    T5 = Tree(tree_list=[None],
                    name='T5',
                    switches=[S1])
    T6 = Tree(tree_list=[None],
                    name='T6',
                    switches=[S2])
    T7 = Tree(tree_list=[None],
                    name='T7',
                    switches=[S3])
    T8 = Tree(tree_list=[None],
                    name='T8',
                    switches=[S4])
    T9 = Tree(tree_list=[None],
                    name='T9',
                    switches=[S5])
    T10 = Tree(tree_list=[None],
                    name='T10',
                    switches=[S6])
    T11 = Tree(tree_list=[None],
                    name='T11',
                    switches=[S7])
    T12 = Tree(tree_list=[None],
                    name='T12',
                    switches=[S8])
    T13 = Tree(tree_list=[None],
                    name='T13',
                    switches=[S9])
    T14 = Tree(tree_list=[None],
                    name='T14',
                    switches=[S10])
    T15 = Tree(tree_list=[None],
                    name='T15',
                    switches=[S11])
    T16 = Tree(tree_list=[None],
                    name='T16',
                    switches=[S12])
    T17 = Tree(tree_list=[None],
                    name='T17',
                    switches=[S13])
    T18 = Tree(tree_list=[None],
                    name='T18',
                    switches=[S14])
    T19 = Tree(tree_list=[None],
                    name='T19',
                    switches=[S15])
    T20 = Tree(tree_list=[None],
                    name='T20',
                    switches=[S16])
    T21 = Tree(tree_list=[None],
                    name='T21',
                    switches=[S17])
    T22 = Tree(tree_list=[None],
                    name='T22',
                    switches=[S18])
    T23 = Tree(tree_list=[None],
                    name='T23',
                    switches=[S19])
    T24 = Tree(tree_list=[None],
                    name='T24',
                    switches=[S20])
    T25 = Tree(tree_list=[None],
                    name='T25',
                    switches=[S21])
    T26 = Tree(tree_list=[None],
                    name='T26',
                    switches=[S22])
    T27 = Tree(tree_list=[None],
                    name='T27',
                    switches=[S23])
    
    T28 = Tree(tree_list=['AND'] + [['EQU', Tree.tree_list_SUM(3), [None]]]*2 + [[None], [None]],
                    name='T28',
                    switches=[#S0, S2, S6, 2,
                              S1, S5, S11, 2,
                              S12, S18, S22, 2,
                              #S17, S21, S23, 2,
                              S24, S25,
                              ],
                    cut_expression_depth_1=True)

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[4*dx, 2*dy+ey, 2*ex, dy+ey],
                switches_list=[S0, S1, S2, S3, S4, S5])
    R1 = Room(name='R1',
                position=[5*dx+ex, 2*dy+ey, 2*ex, dy+ey],
                switches_list=[S6, S7, S8, S9, S10, S11])
    R2 = Room(name='R2',
                position=[5*dx+ex, 0*dy+ey, 2*ex, dy+ey],
                switches_list=[S12, S13, S14, S15, S16, S17])
    R3 = Room(name='R3',
                position=[4*dx, 0*dy+ey, 2*ex, dy+ey],
                switches_list=[S18, S19, S20, S21, S22, S23])
    R4 = Room(name='R4',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[])
    R10 = Room(name='R10',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[])
    R11 = Room(name='R11',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R12 = Room(name='R12',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R13 = Room(name='R13',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S24])
    R14 = Room(name='R14',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R15 = Room(name='R15',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R16 = Room(name='R16',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R17 = Room(name='R17',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R18 = Room(name='R18',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R19 = Room(name='R19',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S25])
    a = 0.98*np.sqrt(2)
    RE = Room(name='RE',
              position=[5*dx+(1-a)*ex/2,
                        2*dy+(1-a)*ey/2,
                        a*ex,
                        a*ey],
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
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R7,
                relative_departure_coordinates=[1/4, 1/2])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R8)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R9)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=R10)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R7,
                room_arrival=R11)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R8,
                room_arrival=R11)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R12)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R9,
                room_arrival=R12)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R13)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R10,
                room_arrival=R14)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R11,
                room_arrival=R14)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R11,
                room_arrival=R15)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R12,
                room_arrival=R15)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R12,
                room_arrival=R16)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R13,
                room_arrival=R16)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R14,
                room_arrival=R17)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R15,
                room_arrival=R17)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R15,
                room_arrival=R18)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R16,
                room_arrival=R18)
    D26 = Door(two_way=True,
                tree=T26,
                name='D26',
                room_departure=R17,
                room_arrival=R19)
    D27 = Door(two_way=True,
                tree=T27,
                name='D27',
                room_departure=R18,
                room_arrival=R19)
    D28 = Door(two_way=True,
                tree=T28,
                name='D28',
                room_departure=R5,
                room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28],
                 fastest_solution='S0 S1 S4 D0 S6 S9 S10 S11 D1 S12 S13 S14 S17 D2 S19 S21 S22 S23 D3 D10 D16 D17 D18 D23 D26 S25 D27 D25 D21 S24 D15 D14 D13 D8 D5 D4 D28',
                 level_color=get_color(),
                 name='Wander',
                 keep_proportions=True,
                 door_window_size=300)
    
    # for door in level.doors_list:
    #     if door.room_arrival.is_exit:
    #         continue
    #     i = int(door.name.replace('D', ''))
    #     j = int(door.room_departure.name.replace('R', ''))
    #     k = int(door.room_arrival.name.replace('R', ''))
    #     print(f'''    T{i} = Tree(tree_list=[None],
    #                 name='T{i}',
    #                 switches=[S{i-4}])''')
    
    # for room in level.rooms_list:
    #     if room.is_exit:
    #         continue
    #     if room.name == 'R0':
    #         continue
    #     door_list = room.two_way_doors_list + room.departure_doors_list
    #     print(f"['EQU', Tree.tree_list_SUM({len(door_list)}), [None]],")
    # for room in level.rooms_list:
    #     if room.is_exit:
    #         continue
    #     if room.name == 'R0':
    #         continue
    #     door_list = room.two_way_doors_list + room.departure_doors_list
    #     print(', '.join([f'S{int(door.name.replace("D", ''))-4}' for door in door_list])+', 2,')
    
    return level

def get_color():
    hu = 0.3
    sa = 0.3
    li = 0.7
    lcolor = Level_color(background_color=Color.color_hls(hu, li*0.5 , sa),
                         room_color=Color.color_hls(hu, li*0.3, 0.8 * sa),
                         letters_color=Color.color_hls(hu=0.72, li=0.95, sa=0.9),
                         contour_color=Color.KHAKI,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.KHAKI)
    return lcolor