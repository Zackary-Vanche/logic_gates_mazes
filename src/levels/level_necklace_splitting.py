from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def aux(l): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
    Slist_7 = [S14, S15]
    Slist_8 = [S16, S17]
    Slist_9 = [S18, S19]
    Slist_10 = [S20, S21]
    Slist_11 = [S22, S23]
    Slist_12 = [S24, S25]
    Slist_13 = [S26, S27]
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_5)),
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_6)),
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
          name='V8',
          switches=Slist_8)
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_9)),
          name='V9',
          switches=Slist_9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_10)),
          name='V10',
          switches=Slist_10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_11)),
          name='V11',
          switches=Slist_11)
    V12 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_12)),
          name='V12',
          switches=Slist_12)
    V13 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_13)),
          name='V13',
          switches=Slist_13)

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13]
    
    tree_list_T13 = ["EQU",
                     ["SUM"] + [["PROD", Tree.tree_list_EQU(2), [None]]]*len(Vlist),
                     [None]]
    Slist_T13 = []
    for i, V in enumerate(Vlist):
        Slist_T13.extend([V, 1, l[i]])
    Slist_T13.append(int(sum(l)/2))
        
    T13 = Tree(tree_list=tree_list_T13,
                name='T13',
                switches=Slist_T13)

    def get_tree(i):
        if i == 0:
            return Tree(tree_list=Tree.tree_list_INFOREQU(2),
                        name=f'T{i}',
                        switches=[V0, 2])
        elif i < 13:
            return Tree(tree_list=Tree.tree_list_INFOREQU(3),
                        name=f'T{i}',
                        switches=[Vlist[i-1], Vlist[i], 2])
        else:
            return T13

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=Slist_6)
    R7 = Room(name='R7',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_7)
    R8 = Room(name='R8',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_8)
    R9 = Room(name='R9',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_9)
    R10 = Room(name='R10',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_10)
    R11 = Room(name='R11',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_11)
    R12 = Room(name='R12',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_12)
    R13 = Room(name='R13',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=Slist_13)
    RE = Room(name='RE',
              position=[4*dx, 2*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=get_tree(0),
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=get_tree(1),
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=get_tree(2),
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=get_tree(3),
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=get_tree(4),
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=get_tree(5),
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=get_tree(6),
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=get_tree(7),
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=get_tree(8),
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=get_tree(9),
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=get_tree(10),
                name='D10',
                room_departure=R10,
                room_arrival=R11)
    D11 = Door(two_way=False,
                tree=get_tree(11),
                name='D11',
                room_departure=R11,
                room_arrival=R12)
    D12 = Door(two_way=False,
                tree=get_tree(12),
                name='D12',
                room_departure=R12,
                room_arrival=R13)
    D13 = Door(two_way=False,
                tree=get_tree(13),
                name='D13',
                room_departure=R13,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Necklace splitting',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    filename = 'levels/necklace_splitting_random_list.txt'
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        l = rd_choice(lines)
    l = l.replace(' ', '').replace('\n', '')
    l = list(l)
    l = [int(x) for x in l]
    return aux(l)

def get_color():
    hu = 0.1
    sa = 0.6
    li = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.YELLOW,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.YELLOW)
    return lcolor