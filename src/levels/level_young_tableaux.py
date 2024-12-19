from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
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

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    Slist_5 = [S20, S21, S22, S23]
    
    Sll = [Slist_0, Slist_1, Slist_2, Slist_3, Slist_4, Slist_5]
    
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

    def get_tree(i):
        Sl = Sll[i]
        Slt = [Sl[0], Sl[1],
               Sl[0], Sl[2],
               Sl[1], Sl[3],
               Sl[2], Sl[3]]
        tree_list = ["AND"] + [Tree.tree_list_SUPOREQU(2)]*4
        if i == 0:
            return Tree(tree_list=tree_list,
                        name=f'T{i}',
                        switches=Slt,
                        cut_expression_depth_1=False)
        else:
            return Tree(tree_list=tree_list + [Tree.tree_list_INF(2)],
                        name=f'T{i}',
                        switches=Slt + [Vlist[i-1], Vlist[i]],
                        cut_expression_depth_1=False)

    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)

    dx = 1.3
    dy = 1
    ex = 1
    ey = 1
    
    def get_position(i):
        if i%2 == 0:
            r = 2
        else:
            r = 0.75
        theta = 2*pi
        alpha = 0
        n = 7
        return [dx*r*cos(i*theta/n-alpha), dy*r*sin(i*theta/n-alpha), ex, ey]
    
    def get_room(i):
        return Room(name=f'R{i}',
                    position=get_position(i),
                    switches_list=Sll[i])
    R0 = get_room(0)
    R1 = get_room(1)
    R2 = get_room(2)
    R3 = get_room(3)
    R4 = get_room(4)
    R5 = get_room(5)
    RE = Room(name='RE',
              position=get_position(6),
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
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.1, li=0.5)
    lcolor.surrounding_color = Color.TOTAL_RED
    lcolor.contour_color = Color.TOTAL_RED

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="D0 S4 D1 S8 S9 D2 S12 S14 D3 S16 S17 S18 D4 S20 S21 S22 S23 D5",
                 level_color=lcolor,
                 name='Young tableaux',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level