from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8]

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(5), [None]],
                          ['EQU', Tree.tree_list_SUM(3), [None]],
                          ['EQU', Tree.tree_list_SUM(3), [None]],
                         ['INFOREQU', Tree.tree_list_SUM(2), Tree.tree_list_SUM(2)],],
                name='T0',
                switches=[S0, S1, S2, S3, S4, 3,
                          S0, S1, S3, 2,
                          S1, S2, S4, 1,
                          S0, S2, S3, S4,
                          ],
                cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=Tree.tree_list_AND(4),
                name='T6',
                switches=[S5, S6, S7, S8])

    dx = 1.5
    dy = 1
    ex = 0.9
    ey = 1

    R0 = Room(name='R0',
                position=[0*dx, 6*dy, 4*dx+ex, ey],
                switches_list=[S0, S1, S2, S3, S4,])
    R1 = Room(name='R1',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[S5])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy-ey/4, ex, ey],
                switches_list=[S6])
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S7])
    R4 = Room(name='R4',
                position=[4*dx, 2*dy-ey/4, ex, ey],
                switches_list=[S8])
    RE = Room(name='RE',
              position=[2*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R3)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S0 S3 S4 D0 S5 D1 S6 D4 S7 D5 S8 D5 D6",
                 level_color=get_color(),
                 name='Bonsai',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor=Levels_colors_list.FROM_HUE(hu=0.4, sa=0.2, li=0.5)
    return lcolor