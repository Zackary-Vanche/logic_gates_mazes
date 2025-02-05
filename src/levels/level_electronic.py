from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
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

    T0 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T0',
                switches=[S0, S1],
              easy_logical_expression_PN="^ S0 S1\n= | & ¬S0 S1 & S0 ¬S1")
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T2',
                switches=[S2, S3],
              easy_logical_expression_PN="^ S2 S3\n= | & ¬S2 S3 & S2 ¬S3")
    T3 = Tree(tree_list=Tree.tree_list_NOT,
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T4',
                switches=[S4, S5],
              easy_logical_expression_PN="¬^ S4 S5\n= | & ¬S4 ¬S5 & S4 S5")
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T6',
                switches=[S6, S7],
              easy_logical_expression_PN="¬^ S6 S7\n= | & ¬S6 ¬S7 & S6 S7")
    T7 = Tree(tree_list=Tree.tree_list_NOT,
                name='T7',
                switches=[S6])
    dx = 1
    dy = 1
    ex = 0.65
    ey = 0.65

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, dy+ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[1*dx, 1*dy, ex, dy+ey],
                switches_list=[S2, S3])
    R3 = Room(name='R3',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx, 0*dy, ex, dy+ey],
                switches_list=[S4, S5])
    R5 = Room(name='R5',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[3*dx, 1*dy, ex, dy+ey],
                switches_list=[S6, S7])
    R7 = Room(name='R7',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[4*dx, 0*dy, ex, 2*dy+ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_arrival_coordinates=[1/2, (dy+ey/2)/(dy+ey)])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_arrival_coordinates=[1/2, ey/2/(dy+ey)])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6,
                relative_arrival_coordinates=[1/2, (dy+ey/2)/(dy+ey)])
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=RE,
                relative_arrival_coordinates=[1/2, ey/2/(2*dy+ey)])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution="S0 D0 D1 S3 D2 D3 S4 S5 D4 D5 D6 D7",
                 level_color=get_color(),
                 name='Electronic',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE_light_background(hu=0.15, li=0.1, sa=0.4)
    lcolor.surrounding_color = Color.color_hls(hu=0.25, li=0.8, sa=1)
    lcolor.contour_color = Color.color_hls(hu=0.25, li=0.8, sa=1)
    return lcolor