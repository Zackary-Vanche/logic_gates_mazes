from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color

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
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    
    V0 = Tree(tree_list=Tree.tree_list_AND(9),
              name='V0',
              switches=[S14, S15, S16, S17, S18, S19, S20, S21, S22])
    V1 = Tree(tree_list=Tree.tree_list_NOR(9),
              name='V1',
              switches=[S14, S15, S16, S17, S18, S19, S20, S21, S22])
    
    tree_list_1 = Tree.tree_list_from_str('FT TT')

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],],
                name='T0',
                switches=[S0, S1, 1,
                          S0, S2, S3, 2,
                          S2, S4, 2,
                          S1, S5, S6, 2,
                          S3, S5, S7, S8, 2,
                          S4, S7, S9, 2,
                          S8, S10, S11, S12, 2,
                          S9, S10, S13, 2,
                          S11, S13, 2,],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[S23, S0, S23, S24])
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[S23, S1, S23, S25])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[S23, S2, S23, S26])
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[S23, S3, S23, S27])
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[S23, S4, S23, S28])
    T6 = Tree(tree_list=tree_list_1,
                name='T6',
                switches=[S23, S5, S23, S29])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[S23, S6, S23, S30])
    T8 = Tree(tree_list=tree_list_1,
                name='T8',
                switches=[S23, S7, S23, S31])
    T9 = Tree(tree_list=tree_list_1,
                name='T9',
                switches=[S23, S8, S23, S32])
    T10 = Tree(tree_list=tree_list_1,
                name='T10',
                switches=[S23, S9, S23, S33])
    T11 = Tree(tree_list=tree_list_1,
                name='T11',
                switches=[S23, S10, S23, S34])
    T12 = Tree(tree_list=tree_list_1,
                name='T12',
                switches=[S23, S11, S23, S35])
    T13 = Tree(tree_list=tree_list_1,
                name='T13',
                switches=[S23, S12, S23, S36])
    T14 = Tree(tree_list=tree_list_1,
                name='T14',
                switches=[S23, S13, S23, S37])
    T15 = Tree(tree_list=Tree.tree_list_AND(2),
                name='T15',
                switches=[S23, V0])
    T16 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['INF', Tree.tree_list_BIN(14), Tree.tree_list_BIN(14)]],
                name='T16',
                switches=[S24, S25, 1,
                          S24, S26, S27, 2,
                          S26, S28, 2,
                          S25, S29, S30, 2,
                          S27, S29, S31, S32, 2,
                          S28, S31, S33, 2,
                          S32, S34, S35, S36, 2,
                          S33, S34, S37, 2,
                          S35, S37, 2,
                          S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13,
                          S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37],
                cut_expression_depth_1=True)
    T17 = Tree(tree_list=Tree.tree_list_from_str('FT'),
                name='T17',
                switches=[S23, V1])

    dx = 1
    dy = 1
    ex = dx
    ey = dy
    
    R0 = Room(name='R0',
                position=[-2*dx, 4*dy, 4*ex, 3*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13])
    R1 = Room(name='R1',
                position=[3*dx, 6*dy, ex, ey],
                switches_list=[S14])
    R2 = Room(name='R2',
                position=[5*dx, 6*dy, ex, ey],
                switches_list=[S15])
    R3 = Room(name='R3',
                position=[7*dx, 6*dy, ex, ey],
                switches_list=[S16])
    R4 = Room(name='R4',
                position=[3*dx, 4*dy, ex, ey],
                switches_list=[S17])
    R5 = Room(name='R5',
                position=[5*dx, 4*dy, ex, ey],
                switches_list=[S18])
    R6 = Room(name='R6',
                position=[7*dx, 4*dy, ex, ey],
                switches_list=[S19])
    R7 = Room(name='R7',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S23])
    R8 = Room(name='R8',
                position=[5*dx, 2*dy, ex, ey],
                switches_list=[S20])
    R9 = Room(name='R9',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=[S21])
    R10 = Room(name='R10',
                position=[5*dx, 0*dy, ex, ey],
                switches_list=[S22])
    R11 = Room(name='R11',
                position=[-2*dx, 0*dy, 4*ex, 3*ey],
                switches_list=[S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37])
    RE = Room(name='RE',
              position=[3*dx, 0*dy, ex, ey],
              is_exit=True)
    
    e = 0.25
    Ra = Room(name='',
                position=[-2*dx+e/2, 3*dy+ey/5, 4*ex-e, ey/5],
                switches_list=[])
    Rb = Room(name='',
                position=[-2*dx+e/2, 3*dy+3*ey/5, 4*ex-e, ey/5],
                switches_list=[])
    
    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[3.5/4, 2.5/3])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R4)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R5)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R8)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=R9)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R8,
                room_arrival=R9)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R8,
                room_arrival=R10)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R8,
                room_arrival=R7)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R9,
                room_arrival=R10)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R11,
                relative_arrival_coordinates=[3.5/4, 2.5/3])
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R11,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R7,
                room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, Ra, Rb, RE,],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17],
                 fastest_solution='''S0 S2 S4 S5 S6 S8 S9 S11 S13 D0 S14 D1 S15 D3 S16 D5 S19 D10 S21 D14 S22 D12 S20 D9 S18 D6 S17 D7 S23 D15 S25 S26 S27 S28 S29 S33 S35 S36 S37 D16 S14 D2 S17 D6 S18 D4 S15 D3 S16 D5 S19 D10 S21 D14 S22 D12 S20 D13 S23 D17''',
                 level_color=get_color(),
                 name='Sneckdown',
                 keep_proportions=True,
                 door_window_size=260)
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
    #     print(', '.join([f'S{int(door.name.replace("D", ''))-1}' for door in door_list])+', 2,')
    return level

def get_color():
    hu = 0
    sa = 0
    li = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.ORANGE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.PURE_ORANGE)
    return lcolor