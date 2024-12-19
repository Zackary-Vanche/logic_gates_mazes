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
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')

    Slist_0 = [S0, S1, S2]
    Slist_1 = [S3, S4, S5]
    Slist_2 = [S6, S7, S8]
    Slist_3 = [S9, S10, S11]
    Slist_4 = [S12, S13, S14]
    Slist_5 = [S15, S16, S17]
    Slist_6 = [S18, S19, S20]
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
    
    tree_list_V = ["SUM", Tree.tree_list_PROD(2), [None]]
    
    V7 = Tree(tree_list=tree_list_V,
          name='V7',
          switches=[2, V0, 1])
    V8 = Tree(tree_list=tree_list_V,
          name='V8',
          switches=[2, V1, 1])
    V9 = Tree(tree_list=tree_list_V,
          name='V9',
          switches=[2, V2, 1])
    V10 = Tree(tree_list=tree_list_V,
          name='V10',
          switches=[2, V3, 1])
    V11 = Tree(tree_list=tree_list_V,
          name='V11',
          switches=[2, V4, 1])
    V12 = Tree(tree_list=tree_list_V,
          name='V12',
          switches=[2, V5, 1])
    V13 = Tree(tree_list=tree_list_V,
          name='V13',
          switches=[2, V6, 1])
    
    tree_list_minus = ["SUM", Tree.tree_list_MAX(2), ["MINUS", Tree.tree_list_MIN(2)]]
    
    #     7
    #     8
    #     9
    #   10 11
    #  12   13
    
    V14 = Tree(tree_list=tree_list_minus,
          name='V14',
          switches=[V7, V8]*2)
    V15 = Tree(tree_list=tree_list_minus,
          name='V15',
          switches=[V8, V9]*2)
    V16 = Tree(tree_list=tree_list_minus,
          name='V16',
          switches=[V9, V10]*2)
    V17 = Tree(tree_list=tree_list_minus,
          name='V17',
          switches=[V9, V11]*2)
    V18 = Tree(tree_list=tree_list_minus,
          name='V18',
          switches=[V10, V12]*2)
    V19 = Tree(tree_list=tree_list_minus,
          name='V19',
          switches=[V11, V13]*2)

    Vlist = [V7, V8, V9, V10, V11, V12, V13,
             V14, V15, V16, V17, V18, V19]

    def get_tree(i):
        if i == 0:
            return Tree(tree_list=[None],
                        name=f'T{i}',
                        switches=[1])
        elif i < 5:
            return Tree(tree_list=Tree.tree_list_DIFF(i+1),
                        name=f'T{i}',
                        switches=[V0, V1, V2, V3, V4, V5, V6][:i+1])
        else:
            return Tree(tree_list=Tree.tree_list_EQUSET(2*len(Vlist)),
                        name=f'T{i}',
                        switches=Vlist+[i for i in range(1, len(Vlist)+1)])
        
    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)

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
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_6)
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
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
                room_arrival=RE)
    
    color=Color.color_hls(hu=0, li=0.7, sa=0.8)
    lcolor=Levels_colors_list.FROM_HUE(hu=0, sa=0.2, li=0.4)
    lcolor.surrounding_color=color
    lcolor.contour_color=color

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S1 D0 S3 S5 D1 S6 D2 S9 S10 D3 S13 S14 D4 S17 D5 D6",
                 level_color=lcolor,
                 name='Withhold',
                 keep_proportions=True,
                 door_window_size=330)
    
    return level