from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

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
    
    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    
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

    Vlist = [V0, V1, V2, V3]
    rd_shuffle(Vlist)
    
    V_couples = [[Vlist[0], Vlist[1]],
                 [Vlist[0], Vlist[2]],
                 [Vlist[0], Vlist[3]],
                 [Vlist[1], Vlist[2]]]
    
    tree_list_V = ["SUM", Tree.tree_list_MAX(2), ["PROD", [None], Tree.tree_list_MIN(2)]]
    
    V4 = Tree(tree_list=tree_list_V,
              name='V4',
              switches=V_couples[0]+[4]+V_couples[0])
    V5 = Tree(tree_list=tree_list_V,
              name='V5',
              switches=V_couples[1]+[4]+V_couples[1])
    V6 = Tree(tree_list=tree_list_V,
              name='V6',
              switches=V_couples[2]+[4]+V_couples[2])
    V7 = Tree(tree_list=tree_list_V,
              name='V7',
              switches=V_couples[3]+[4]+V_couples[3])
    
    a_list = [0, 1, 2, 3]
    rd_shuffle(a_list)
    
    value_list = [max(a_list[0], a_list[1])+4*min(a_list[0], a_list[1]),
                  max(a_list[0], a_list[2])+4*min(a_list[0], a_list[2]),
                  max(a_list[0], a_list[3])+4*min(a_list[0], a_list[3]),
                  max(a_list[1], a_list[2])+4*min(a_list[1], a_list[2])]
    
    V8 = Tree(tree_list=Tree.tree_list_IN(5),
                name='V8',
                switches=[V4]+value_list)
    V9 = Tree(tree_list=Tree.tree_list_IN(5),
                name='V9',
                switches=[V5]+value_list)
    V10 = Tree(tree_list=Tree.tree_list_IN(5),
                name='V10',
                switches=[V6]+value_list)
    V11 = Tree(tree_list=Tree.tree_list_IN(5),
                name='V11',
                switches=[V7]+value_list)

    T0 = Tree(tree_list=Tree.tree_list_DIFF(4),
                name='T0',
                switches=[V0, V1, V2, V3])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[V8])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V9])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V10])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V11])
    T5 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T5',
                switches=[S8, V8, V9, V10, V11])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[-dx+ex, 0*dy, 2*ex, 4*ey],
                switches_list=Slist_0+Slist_1+Slist_2+Slist_3)
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, -1*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, -1*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S8])
    RE = Room(name='RE',
              position=[1*dx, 1*dy+ey, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[3/4, 2.5/4])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Paw graph',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.12, sa=0.4, li=0.25)