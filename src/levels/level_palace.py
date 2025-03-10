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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]
    
    tree_list_XOR_2 = Tree.tree_list_XOR(2)

    T0 = Tree(tree_list=tree_list_XOR_2,
                        name='T0',
                        switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_XOR_2,
                        name='T1',
                        switches=[S0, S2])
    T2 = Tree(tree_list=tree_list_XOR_2,
                        name='T2',
                        switches=[S2, S1])
    T3 = Tree(tree_list=tree_list_XOR_2,
                        name='T3',
                        switches=[S0, S3])
    T4 = Tree(tree_list=tree_list_XOR_2,
                        name='T4',
                        switches=[S3, S4])
    T5 = Tree(tree_list=tree_list_XOR_2,
                        name='T5',
                        switches=[S4, S1])
    T6 = Tree(tree_list=tree_list_XOR_2,
                        name='T6',
                        switches=[S0, S5])
    T7 = Tree(tree_list=tree_list_XOR_2,
                        name='T7',
                        switches=[S5, S6])
    T8 = Tree(tree_list=tree_list_XOR_2,
                        name='T8',
                        switches=[S6, S7])
    T9 = Tree(tree_list=tree_list_XOR_2,
                        name='T9',
                        switches=[S7, S1])
    T10 = Tree(tree_list=Tree.tree_list_from_str('FFTTTTTT'),
                name='T10',
                switches=Slist)

    dx = 1
    dy = 0.5
    ex = 0.5
    ey = 0.25

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[0.5*dx, -1*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[0*dx, -2*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1*dx, -2*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[-1*dx, -2*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[0.5*dx, -3*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[2*dx, -2*dy, ex, ey],
                switches_list=[S7])
    RE = Room(name='RE',
              position=[0.5*dx, -4*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R1)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R1)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R5)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R6,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R7,
                room_arrival=R1)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S0 D1 S2 D2 S1 D9 S7 D8 S6 D7 D6 D3 S3 D4 D5 S1 D0 D6 D7 S6 D8 D9 D0 D6 S5 D7 D8 D9 D0 S0 D3 D4 S4 D5 D9 D8 S6 D10",
                 level_color=get_color(),
                 name='Palace',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.12, sa=0.3, li=0.6)
    lcolor.surrounding_color = Color.RED
    lcolor.contour_color = Color.color_hls(hu=0.12, li=0.85, sa=1)
    return lcolor