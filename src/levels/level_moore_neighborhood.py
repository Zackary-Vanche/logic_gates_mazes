from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_moore_neighborhood(): 

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

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]
    Slist_5 = [S10, S11]
    Slist_6 = [S12, S13]
    Slist_7 = [S14, S15]
    Slist_8 = [S16, S17]
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
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_7)),
          name='V7',
          switches=Slist_7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_8)),
          name='V8',
          switches=Slist_8)

    Vlist = [V0, V1, V2,
             V3, V4, V5,
             V6, V7, V8]
    
    def tree_list(n):
        if n == 1:
            t = Tree.tree_list_DIFF(2)
        else:
            t = ['AND'] + [Tree.tree_list_DIFF(2)]*n
        return t 
    
    T0 = Tree(tree_list=[None],
              name='T0',
              switches=[1])
    T1 = Tree(tree_list=tree_list(1),
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list(1),
                name='T2',
                switches=[V1, V2,])
    T3 = Tree(tree_list=tree_list(2),
                name='T3',
                switches=[V0, V3,
                          V1, V3])
    T4 = Tree(tree_list=tree_list(4),
                name='T4',
                switches=[V0, V4,
                          V1, V4,
                          V2, V4,
                          V3, V4])
    T5 = Tree(tree_list=tree_list(3),
                name='T5',
                switches=[V1, V5,
                          V2, V5,
                          V4, V5])
    T6 = Tree(tree_list=tree_list(2),
                name='T6',
                switches=[V3, V6,
                          V4, V6])
    T7 = Tree(tree_list=tree_list(4),
                name='T7',
                switches=[V3, V7,
                          V4, V7,
                          V5, V7,
                          V6, V7])
    T8 = Tree(tree_list=tree_list(3),
                name='T8',
                switches=[V4, V8,
                          V5, V8,
                          V7, V8])
    T9 = Tree(tree_list=['AND',
                         ['INF', Tree.tree_list_SUM(9), [None]],
                         ['INF', [None], [None]]],
                name='T9',
                switches=Vlist + [10, V1, V3])
    
    Slist = [S0, S1,
             S2, S3,
             S4, S5,
             S6, S7,
             S8, S9,
             S10, S11,
             S12, S13,
             S14, S15,
             S16, S17]
    
    ex = 1.5
    ey = 1
    dx = 2.5
    dy = 2

    R0 = Room(name='R0',
              position=[-ex/2, 0, 2*ex, 3],
              switches_list=[])
    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0, S1])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S2, S3])
    R2 = Room(name='R2',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[S4, S5])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S6, S7])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S8, S9])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S10, S11])
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S12, S13])
    R7 = Room(name='R7',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S14, S15])
    R8 = Room(name='R8',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S16, S17])
    R9 = Room(name='R9',
                position=[0.5*dx, 3*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[1.5*dx, 3*dy, ex, ey],
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
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.4, li=0.8)
    lcolor.room_color = Color.GREY_150
    lcolor.surrounding_color = Color.WHITE
    lcolor.contour_color = Color.WHITE
    lcolor.letters_color = Color.WHITE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9],
                 fastest_solution="D0 S2 D1 D2 S7 D3 S8 S9 D4 S11 D5 D6 S14 D7 D8 D9",
                 level_color=lcolor,
                 name='Moore neighborhood',
                 keep_proportions=True,
                 door_window_size=440)
    
    return level