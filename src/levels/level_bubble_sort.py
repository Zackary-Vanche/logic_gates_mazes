from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def level_bubble_sort(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=rd_choice([0, 1]))
    S4 = Switch(name='S4', value=rd_choice([0, 1]))
    S5 = Switch(name='S5', value=rd_choice([0, 1]))
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9', value=rd_choice([0, 1]))
    S10 = Switch(name='S10', value=rd_choice([0, 1]))
    S11 = Switch(name='S11', value=rd_choice([0, 1]))
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15', value=rd_choice([0, 1]))
    S16 = Switch(name='S16', value=rd_choice([0, 1]))
    S17 = Switch(name='S17', value=rd_choice([0, 1]))
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21', value=rd_choice([0, 1]))
    S22 = Switch(name='S22', value=rd_choice([0, 1]))
    S23 = Switch(name='S23', value=rd_choice([0, 1]))
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27', value=rd_choice([0, 1]))
    S28 = Switch(name='S28', value=rd_choice([0, 1]))
    S29 = Switch(name='S29', value=rd_choice([0, 1]))
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33', value=rd_choice([0, 1]))
    S34 = Switch(name='S34', value=rd_choice([0, 1]))
    S35 = Switch(name='S35', value=rd_choice([0, 1]))

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35]

    Slist0 = Slist[0:3]
    Slist1 = Slist[3:6]
    Slist2 = Slist[6:9]
    Slist3 = Slist[9:12]
    Slist4 = Slist[12:15]
    Slist5 = Slist[15:18]
    Slist6 = Slist[18:21]
    Slist7 = Slist[21:24]
    Slist8 = Slist[24:27]
    Slist9 = Slist[27:30]
    Slist10 = Slist[30:33]
    Slist11 = Slist[33:36]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist3)),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist4)),
          name='V4',
          switches=Slist4)
    V5 = Tree(tree_list=Tree.tree_list_BIN(len(Slist5)),
          name='V5',
          switches=Slist5)
    V6 = Tree(tree_list=Tree.tree_list_BIN(len(Slist6)),
          name='V6',
          switches=Slist6)
    V7 = Tree(tree_list=Tree.tree_list_BIN(len(Slist7)),
          name='V7',
          switches=Slist7)
    V8 = Tree(tree_list=Tree.tree_list_BIN(len(Slist8)),
          name='V8',
          switches=Slist8)
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist9)),
          name='V9',
          switches=Slist9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist10)),
          name='V10',
          switches=Slist10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist11)),
          name='V11',
          switches=Slist11)
    
    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11]
    Vlist_odd = [V1, V3, V5, V7, V9, V11]

    valuelist = []
    for V in Vlist_odd:
        valuelist.append(V.get_value())
    
    def get_tree(i):
        if i==0:
            return Tree(tree_list=['EQU', [None], [None]],
                        name=f'T{i}',
                        switches=[V0, V1])
        elif i%2 == 0:
            return Tree(tree_list=['EQU', [None], [None]],
                        name=f'T{i}',
                        switches=[Vlist[i], Vlist[i+1]])
        elif i < 11:
            return Tree(tree_list=['EQU',
                                   [None],
                                   ['MIN', [None], [None]]],
                        name=f'T{i}',
                        switches=[Vlist[i], Vlist[i-1], Vlist[i+2]])
        elif i==11:
            return Tree(tree_list=['EQUSET'] + [[None]]*12,
                        name=f'T{i}',
                        switches=Vlist_odd + valuelist,
                        cut_expression_depth_1=True)
    T12 = Tree(tree_list=['INFOREQU'] + [[None]]*6,
                name='T12',
                switches=Vlist_odd)

    dx = 3
    dy = 4.5
    ex = 1
    ey = 3
    
    ax = -2

    R0 = Room(name='R0',
                position=[4*dx, 0*dy+ax, ex, ey],
                switches_list=Slist0)
    R1 = Room(name='R1',
                position=[5*dx, 0*dy+ax, ex, ey],
                switches_list=Slist1)
    R2 = Room(name='R2',
                position=[5*dx, 1*dy+ax, ex, ey],
                switches_list=Slist2)
    R3 = Room(name='R3',
                position=[4*dx, 1*dy+ax, ex, ey],
                switches_list=Slist3)
    R4 = Room(name='R4',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist4)
    R5 = Room(name='R5',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=Slist5)
    R6 = Room(name='R6',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist6)
    R7 = Room(name='R7',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist7)
    R8 = Room(name='R8',
                position=[1*dx, 1*dy+ax, ex, ey],
                switches_list=Slist8)
    R9 = Room(name='R9',
                position=[0*dx, 1*dy+ax, ex, ey],
                switches_list=Slist9)
    R10 = Room(name='R10',
                position=[0*dx, 0*dy+ax, ex, ey],
                switches_list=Slist10)
    R11 = Room(name='R11',
                position=[1*dx, 0*dy+ax, ex, ey],
                switches_list=Slist11)
    RE = Room(name='RE',
              position=[2*dx, -dy, dx+ex, ey],
              is_exit=True)

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
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=get_tree(6),
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=get_tree(7),
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=get_tree(8),
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=get_tree(9),
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=get_tree(10),
                name='D10',
                room_departure=R10,
                room_arrival=R11)
    D11 = Door(two_way=False,
                tree=get_tree(11),
                name='D11',
                room_departure=R11,
                room_arrival=R0)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R11,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Bubble sort',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level