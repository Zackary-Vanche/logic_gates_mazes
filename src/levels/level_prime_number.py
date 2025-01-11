from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from numpy import cos, sin, pi

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
    
    Slist = [S0, S1,
             S2, S3,
             S4, S5,
             S6, S7,
             S8, S9,
             S10, S11,]
    
    def tree_list(n):
        tree_list_aux = ['EQU',
                         ['MOD', [None], [None]],
                         [None]]
        if n == 1:
            tree_list = ['EQU',
                         tree_list_aux,
                         Tree.tree_list_NOT]
        else:
            tree_list = ['EQU',
                         ['OR'] + [tree_list_aux]*n,
                         Tree.tree_list_NOT]
        return tree_list
    
    def get_Slist(n):
        Slistn = []
        for i in range(2, n+2):
            Slistn.extend([n+2, i, 0])
        Slistn.append(Slist[n])
        return Slistn

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[S0])
    T1 = Tree(tree_list=tree_list(1),
                name='T1',
                switches=get_Slist(1))
    T2 = Tree(tree_list=tree_list(2),
                name='T2',
                switches=get_Slist(2))
    T3 = Tree(tree_list=tree_list(3),
                name='T3',
                switches=get_Slist(3))
    T4 = Tree(tree_list=tree_list(4),
                name='T4',
                switches=get_Slist(4))
    T5 = Tree(tree_list=tree_list(5),
                name='T5',
                switches=get_Slist(5))
    T6 = Tree(tree_list=tree_list(6),
                name='T6',
                switches=get_Slist(6))
    T7 = Tree(tree_list=tree_list(7),
                name='T7',
                switches=get_Slist(7))
    T8 = Tree(tree_list=tree_list(8),
                name='T8',
                switches=get_Slist(8))
    T9 = Tree(tree_list=tree_list(9),
                name='T9',
                switches=get_Slist(9))
    T10 = Tree(tree_list=tree_list(10),
                name='T10',
                switches=get_Slist(10))

    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    
    def position(i):
        alpha = 0
        r = 1.7
        a = 2*i*pi/12 + alpha
        return [r*cos(a)*dx-ex/2, r*sin(a)*dy-ey/2, ex, ey]

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R10 = Room(name='R10',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S10])
    RE = Room(name='RE',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[],
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
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R10,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10,],
                 fastest_solution="S0 D0 S1 D1 D2 S3 D3 D4 S5 D5 D6 D7 D8 S9 D9 D10",
                 level_color=get_color(),
                 name='Prime number',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.2
    sa = 0.6
    li = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.BRIGHT_ORANGE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.TOTAL_RED)
    return lcolor