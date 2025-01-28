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

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Sl_list = [Slist_0, Slist_1, Slist_2, Slist_3, Slist_4, Slist_5]
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
    
    Vlist = [V0, V1, V2, V3, V4, V5]
    
    # # A B C 
    # A   0 2
    # B 1   4
    # C 3 5  
    
    # # A B C 
    # A   2 3
    # B 5   6
    # C 4 1 
    
    V6 = Tree(tree_list=Tree.tree_list_SUM(4),
          name='V6',
          switches=[V0, V1, V2, V3])
    V7 = Tree(tree_list=Tree.tree_list_SUM(4),
          name='V7',
          switches=[V0, V1, V4, V5])
    V8 = Tree(tree_list=Tree.tree_list_SUM(4),
          name='V8',
          switches=[V2, V3, V4, V5])

    dx = 0.75
    dy = 1.25
    ex = 0.5
    ey = 0.5/3

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy+ey, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 1*dy-ey, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_5)
    RE = Room(name='RE',
              position=[2*dx, 0.5*dy, ex, ey],
              is_exit=True)
    Ra = Room(name='',
              position=[0*dx, 0.5*dy-ex/2+ey/2, ex, ex],
              is_exit=True)
    
    tree_list_not_EQU = ['NOT', Tree.tree_list_EQU(3)]
    
    def get_tree(i):
        if i == 0:
            return Tree(tree_list=tree_list_not_EQU,
                        name='T0',
                        switches=Slist_0)
        elif i < 5:
            return Tree(tree_list=["AND",
                                   tree_list_not_EQU,
                                   Tree.tree_list_DIFF(i+1)],
                        name=f'T{i}',
                        switches=Sl_list[i]+Vlist[:i+1],
                        cut_expression_depth_1=True)
        else:
            return Tree(tree_list=['AND',
                                   tree_list_not_EQU,
                                   Tree.tree_list_DIFF(i+1),
                                   Tree.tree_list_EQU(3),
                                   Tree.tree_list_INF(2),
                                   Tree.tree_list_INF(2),
                                   Tree.tree_list_INF(2),
                                   Tree.tree_list_INF(3)],
                        name='T5',
                        switches=Sl_list[i]+Vlist[:i+1]+[V6, V7, V8,
                                                         V0, V1,
                                                         V2, V3,
                                                         V4, V5,
                                                         V0, V2, V4],
                        cut_expression_depth_1=True)

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
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, Ra, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 D0 S4 S5 D1 S7 D2 S9 S11 D3 S12 S13 D4 S17 D5",
                 level_color=get_color(),
                 name='Magic circles',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.85, sa=0.3, li=0.35)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, li=0.5, sa=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.9, li=0.5, sa=0.8)
    return lcolor