from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle

def level_3_cycle(): 
    
    ilist = [[0, 0,],
             [1, 0,],
             [0, 1,],
             [1, 1,]]
    rd_shuffle(ilist)

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2', value=ilist[0][0])
    S3 = Switch(name='S3', value=ilist[0][1])
    S4 = Switch(name='S4', value=ilist[1][0])
    S5 = Switch(name='S5', value=ilist[1][1])
    S6 = Switch(name='S6', value=ilist[2][0])
    S7 = Switch(name='S7', value=ilist[2][1])
    S8 = Switch(name='S8', value=ilist[3][0])
    S9 = Switch(name='S9', value=ilist[3][1])

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9]

    Slist_0 = [S0, S1]
    Slist_1 = [S2, S3]
    Slist_2 = [S4, S5]
    Slist_3 = [S6, S7]
    Slist_4 = [S8, S9]

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

    Vlist = [V1, V2, V3, V4]
    
    V5 = Tree(tree_list=["EQUSET"] + [[None]]*8,
          name='V5',
          switches=Vlist + [0, 1, 2, 3])

    tree_list_0 = ["AND", [None], ['NOT', ["EQU", [None], [None]]]]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V5, V0, 0])
    T1 = Tree(tree_list=tree_list_0,
                name='T1',
                switches=[V5, V0, 1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V5, V0, 2])
    T3 = Tree(tree_list=tree_list_0,
                name='T3',
                switches=[V5, V0, 3])
    
    tree_list_4 = ["AND", Tree.tree_list_DIFF(3), Tree.tree_list_EQU(2)]
    
    T4 = Tree(tree_list=tree_list_4,
                name='T4',
                switches=[V0, 0, 1,
                          V1, V2])
    T5 = Tree(tree_list=tree_list_4,
                name='T5',
                switches=[V0, 0, 2,
                          V1, V3])
    T6 = Tree(tree_list=tree_list_4,
                name='T6',
                switches=[V0, 0, 3,
                          V1, V4])
    
    T7 = Tree(tree_list=tree_list_4,
                name='T7',
                switches=[V0, 1, 0,
                          V2, V1])
    T8 = Tree(tree_list=tree_list_4,
                name='T8',
                switches=[V0, 1, 2,
                          V2, V3])
    T9 = Tree(tree_list=tree_list_4,
                name='T9',
                switches=[V0, 1, 3,
                          V2, V4])
    
    T10 = Tree(tree_list=tree_list_4,
                name='T10',
                switches=[V0, 2, 0,
                          V3, V1])
    T11 = Tree(tree_list=tree_list_4,
                name='T11',
                switches=[V0, 2, 1,
                          V3, V2])
    T12 = Tree(tree_list=tree_list_4,
                name='T12',
                switches=[V0, 2, 3,
                          V3, V4])
    
    T13 = Tree(tree_list=tree_list_4,
                name='T13',
                switches=[V0, 3, 0,
                          V4, V1])
    T14 = Tree(tree_list=tree_list_4,
                name='T14',
                switches=[V0, 3, 1,
                          V4, V2])
    T15 = Tree(tree_list=tree_list_4,
                name='T15',
                switches=[V0, 3, 2,
                          V4, V3])
    
    T16 = Tree(tree_list=Tree.tree_list_INFOREQU(5),
                name='T16',
                switches=[V0] + Vlist)

    dx = 2.5
    dy = 1
    ex = 0.5
    ey = 0.5
    ey0 = 0.4
    
    ay = 0.75

    R0 = Room(name='R0',
                position=[dx, -ay-ey0, dx+ex, ey0],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, 2*ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[1*dx, 2*ey+ay, ex, 2*ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 2*ey+ay, ex, 2*ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, 2*ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[dx, -2*(ay+ey0), dx+ex, ey],
              is_exit=True)
    
    rc = [1/2, 1/4]
    rp = 0.35
    rp1 = 0.25

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_arrival_coordinates=rc)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R2,
                relative_arrival_coordinates=rc,
                relative_position=rp1)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_arrival_coordinates=rc,
                relative_position=rp1)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R4,
                relative_arrival_coordinates=rc)
    
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R4,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R3,
                room_arrival=R1,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R2,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R1,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R4,
                room_arrival=R2,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R4,
                room_arrival=R3,
                relative_departure_coordinates=rc,
                relative_arrival_coordinates=rc,
                relative_position=rp)
    
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.2, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.12, li=0.4, sa=0.5)
    lcolor.surrounding_color = Color.color_hls(hu=0.12, li=0.4, sa=0.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='3-Cycle',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level