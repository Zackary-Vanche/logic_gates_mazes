from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def level_chromagraph(): 
    
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
    
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    
    Slist=Slist_0+Slist_1+Slist_2+Slist_3+Slist_4
    
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
    V5 = Tree(tree_list=Tree.tree_list_SUM(5),
          name='V5',
          switches=[V0, V1, V2, V3, V4,])

    V6 = Tree(tree_list=Tree.tree_list_DIFF(2),
          name='V6',
          switches=[V0, V1])
    V7 = Tree(tree_list=Tree.tree_list_DIFF(2),
          name='V7',
          switches=[V1, V2])
    V8 = Tree(tree_list=Tree.tree_list_DIFF(2),
          name='V8',
          switches=[V1, V3])
    V9 = Tree(tree_list=Tree.tree_list_SUP(2),
          name='V9',
          switches=[V1, V4])
    V10 = Tree(tree_list=Tree.tree_list_DIFF(2),
          name='V10',
          switches=[V2, V4])
    V11 = Tree(tree_list=Tree.tree_list_DIFF(2),
          name='V11',
          switches=[V3, V4])

    T0 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T0',
                switches=[V5, 4])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V6])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V7])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V8])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V9])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V10])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[V11])
    T7 = Tree(tree_list=Tree.tree_list_AND(6)+[Tree.tree_list_NAND(2)],
                name='T7',
                switches=[V6, V7, V8, V9, V10, V11, S2, S3])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    
    ex0 = 1.5

    R0 = Room(name='R0',
              position=[0*dx, 1*dy-ey-0.2, ex0, 2*ex0/5],
              switches_list=Slist,
              inside_color=Color.color_hls(sa=0),
              surrounding_color=Color.IVORY)
    R1 = Room(name='R1',
              position=[0*dx, 2*dy, ex, ey],
              switches_list=[],
              inside_color=Color.color_hls(hu=0, sa=0.5),
              surrounding_color=Color.IVORY)
    R2 = Room(name='R2',
              position=[1*dx, 2*dy, ex, ey],
              switches_list=[],
              inside_color=Color.color_hls(hu=0.6, sa=0.5),
              surrounding_color=Color.IVORY)
    R3 = Room(name='R3',
              position=[2*dx, 1*dy, ex, ey],
              switches_list=[],
              inside_color=Color.color_hls(hu=0.4, sa=0.5),
              surrounding_color=Color.IVORY)
    R4 = Room(name='R4',
              position=[2*dx, 3*dy, ex, ey],
              switches_list=[],
              inside_color=Color.color_hls(hu=0.4, sa=0.5),
              surrounding_color=Color.IVORY)
    R5 = Room(name='R5',
              position=[3*dx, 2*dy, ex, ey],
              switches_list=[],
              inside_color=Color.color_hls(hu=0, sa=0.5),
              surrounding_color=Color.IVORY)
    RE = Room(name='RE',
              position=[0*dx, 3*dy, ex, ey],
              is_exit=True,
              inside_color=Color.color_hls(sa=0),
              surrounding_color=Color.IVORY)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R4,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R5,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R5,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R5,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=RE,
                inside_color=Color.color_hls(sa=0),
                surrounding_color=Color.IVORY)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution="S0 S3 S8 D0 D7",
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Chromagraph',
                 keep_proportions=True,
                 door_window_size=360,
                 uniform_surrounding_colors=False,
                 uniform_inside_room_color=False)
    
    return level