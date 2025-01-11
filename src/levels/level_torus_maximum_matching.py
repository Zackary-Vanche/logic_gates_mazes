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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]
    
    #    R0******
    #    D0    D1
    # D5 R1 D2 R2 D5 RE
    #    D3    D4    * 
    # D7 R3 D6 R4 D7 *
    #    D0    D1

    T0 = Tree(Tree.tree_list_NOT,
                name='T0',
                switches=[S0])
    T1 = Tree(Tree.tree_list_NOT,
                name='T1',
                switches=[S1])
    T2 = Tree(Tree.tree_list_NOT,
                name='T2',
                switches=[S2])
    T3 = Tree(Tree.tree_list_NOT,
                name='T3',
                switches=[S3])
    T4 = Tree(Tree.tree_list_NOT,
                name='T4',
                switches=[S4])
    T5 = Tree(Tree.tree_list_NOT,
                name='T5',
                switches=[S5])
    T6 = Tree(Tree.tree_list_NOT,
                name='T6',
                switches=[S6])
    T7 = Tree(Tree.tree_list_NOT,
                name='T7',
                switches=[S7])
    T8 = Tree(["AND",
               Tree.tree_list_XOR(4),
               Tree.tree_list_XOR(4),
               Tree.tree_list_XOR(4),
               Tree.tree_list_XOR(4),
               ["EQU", Tree.tree_list_SUM(len(Slist)), [None]]],
                name='T8',
                switches=[S0, S2, S3, S5,
                          S1, S1, S4, S5,
                          S0, S3, S6, S7,
                          S1, S4, S6, S7] + Slist + [2])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, ey-(dx+ex)/2, dx+ex, (dx+ex)/2],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
              position=[2*dx, 1*dy, ex, dy+ey])
    RE = Room(name='RE',
              position=[3*dx, 1*dy, ex, dy+ey],
              is_exit=True)
    
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(dx+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(dx+ex/2)/(dx+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5,
                relative_arrival_coordinates=[1/2, ey/2/(dy+ey)])
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R4)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R5,
                relative_arrival_coordinates=[1/2, (dy+ey/2)/(dy+ey)])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution="S0 S4 D1 D5 D8",
                 level_color=get_color(),
                 name='Torus maximum matching',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.3, li=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.3, sa=0.8, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.1, sa=0.8, li=0.8)
    return lcolor