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
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V0',
          switches=[S2, S3, S4])
    V1 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V1',
          switches=[S5, S6, S7])

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=Tree.tree_list_XOR(2),
                name='T1',
                switches=[S0, S1])
    T2 = Tree(tree_list=Tree.tree_list_XNOR(2),
                name='T2',
                switches=[S0, S1])
    T3 = Tree(tree_list=["OR"] + [["AND",
                                   [None],
                                   Tree.tree_list_EQUSET(4)]]*4 + [["AND",
                                                                    Tree.tree_list_NOT,
                                                                    Tree.tree_list_EQUSET(4)]]*5,
                name='T3',
                switches=[S0, V0, V1, 0, 2,
                          S0, V0, V1, 2, 4,
                          S0, V0, V1, 3, 5,
                          S0, V0, V1, 6, 7,
                          #################
                          S0, V0, V1, 1, 3,
                          S0, V0, V1, 2, 3,
                          S0, V0, V1, 4, 5,
                          S0, V0, V1, 5, 6,
                          S0, V0, V1, 5, 7,
                          ],
                cut_expression_depth_1=True)
    T4 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T4',
                switches=[V0, V1])
    T5 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T5',
                switches=[V0, 1])

    ex = 1
    ey = 1.25
    dx = ex
    dy = ey
    
    ey0 = 1/ey
    eye = 1/ey
    
    hue_min = 0
    hue_max = 1/3
    li = 0.3
    sa = 0.4
    
    inside_color_list = []
    for i in range(12):
        inside_color_list.append(Color.color_hls(i*(hue_max-hue_min)/12+hue_min, li=li, sa=sa))
        
    surrounding_color_list = []
    for i in range(11, -1, -1):
        surrounding_color_list.append(Color.color_hls(i*(hue_max-hue_min)/12+hue_min, li=0.7, sa=1))

    R0 = Room(name='R0',
                position=[2*dx, 2*dy, 3*ex, ey0],
                switches_list=[],
                inside_color=inside_color_list[0],
                surrounding_color=surrounding_color_list[0])
    R1 = Room(name='R1',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S0],
                inside_color=inside_color_list[2],
                surrounding_color=surrounding_color_list[2])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S1],
                inside_color=inside_color_list[4],
                surrounding_color=surrounding_color_list[4])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, 3*ey],
                switches_list=[S2, S3, S4],
                inside_color=inside_color_list[6],
                surrounding_color=surrounding_color_list[6])
    R4 = Room(name='R4',
                position=[6*dx, 1*dy, ex, 3*ey],
                switches_list=[S5, S6, S7],
                inside_color=inside_color_list[8],
                surrounding_color=surrounding_color_list[8])
    RE = Room(name='RE',
              position=[2.5*dx, 4*dy-eye, 2*ex, eye],
              is_exit=True,
              inside_color=inside_color_list[11],
              surrounding_color=surrounding_color_list[11])

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[2.5/3, ey/2/ey0],
                inside_color=inside_color_list[1],
                surrounding_color=surrounding_color_list[1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                inside_color=inside_color_list[3],
                surrounding_color=surrounding_color_list[3])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_arrival_coordinates=[1/2, 0.5/3],
                inside_color=inside_color_list[5],
                surrounding_color=surrounding_color_list[5])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 0.5/3],
                relative_arrival_coordinates=[1/2, 0.5/3],
                inside_color=inside_color_list[7],
                surrounding_color=surrounding_color_list[7])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R0,
                relative_arrival_coordinates=[2.5/3, ey/2/ey0],
                inside_color=inside_color_list[9],
                surrounding_color=surrounding_color_list[9])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[2.5/3, 1/2],
                inside_color=inside_color_list[10],
                surrounding_color=surrounding_color_list[10])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5,],
                 fastest_solution="D0 S0 D1 S1 D2 S3 D3 S6 D4 D0 S0 D1 S1 D2 S2 D3 S5 D4 D0 S0 D1 S1 D2 S3 S4 D3 S6 S7 D4 D0 S0 D1 S1 D2 S3 D3 S6 D4 D0 S0 D1 S1 D2 S2 D3 S5 D4 D0 S0 D1 S1 D2 S2 S3 D3 S5 S6 D4 D0 S0 D1 S1 D2 S3 S4 D3 S6 S7 D4 D0 S0 D1 S1 D2 S3 D3 S6 D4 D5",
                 level_color=get_color(),
                 name='Walls',
                 keep_proportions=True,
                 door_window_size=350,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level

def get_color():
    hue_min = 0
    hue_max = 1/3
    li = 0.3
    sa = 0.4
    lcolor = Levels_colors_list.FROM_HUE(hu=(hue_max+hue_min)/2, sa=sa, li=0.3)
    return lcolor