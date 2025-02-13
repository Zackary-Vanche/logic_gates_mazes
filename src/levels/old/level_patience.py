from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color

def f(): 
    
    Slist = [Switch(name=f"S{i}") for i in range(23*3)]
    Sl_list = [Slist[3*i:3*i+3] for i in range(23)]
    Slist_0 = Sl_list[0]
    Slist_1 = Sl_list[1]
    Slist_2 = Sl_list[2]
    Slist_3 = Sl_list[3]
    Slist_4 = Sl_list[4]
    Slist_5 = Sl_list[5]
    Slist_6 = Sl_list[6]
    Slist_7 = Sl_list[7]
    Slist_8 = Sl_list[8]
    Slist_9 = Sl_list[9]
    Slist_10 = Sl_list[10]
    Slist_11 = Sl_list[11]
    Slist_12 = Sl_list[12]
    Slist_13 = Sl_list[13]
    Slist_14 = Sl_list[14]
    Slist_15 = Sl_list[15]
    Slist_16 = Sl_list[16]
    Slist_17 = Sl_list[17]
    Slist_18 = Sl_list[18]
    Slist_19 = Sl_list[19]
    Slist_20 = Sl_list[20]
    Slist_21 = Sl_list[21]
    Slist_22 = Sl_list[22]
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
    V9 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_9)),
          name='V9',
          switches=Slist_9)
    V10 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_10)),
          name='V10',
          switches=Slist_10)
    V11 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_11)),
          name='V11',
          switches=Slist_11)
    V12 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_12)),
          name='V12',
          switches=Slist_12)
    V13 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_13)),
          name='V13',
          switches=Slist_13)
    V14 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_14)),
          name='V14',
          switches=Slist_14)
    V15 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_15)),
          name='V15',
          switches=Slist_15)
    V16 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_16)),
          name='V16',
          switches=Slist_16)
    V17 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_17)),
          name='V17',
          switches=Slist_17)
    V18 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_18)),
          name='V18',
          switches=Slist_18)
    V19 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_19)),
          name='V19',
          switches=Slist_19)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[1])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[1])
    ##################################################
    ##################################################
    T6 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T6',
                switches=[V6, 0])
    T7 = Tree(tree_list=["AND", Tree.tree_list_DIFF(2), Tree.tree_list_EQU(2)],
                name='T7',
                switches=[V6, 0, V7, 0])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[1])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[1])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[1])
    ##################################################
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[1])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[1])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[1])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[1])
    ##################################################
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[1])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[1])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[1])
    ##################################################
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[1])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[1])
    ##################################################
    T20 = Tree(tree_list=[None],
                name='T20',
                switches=[1])
    ##################################################
    ##################################################
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[1])
    # T22 = Tree(tree_list=[None],
    #             name='T22',
    #             switches=[1])
    # T23 = Tree(tree_list=[None],
    #             name='T23',
    #             switches=[1])

    dx = 1
    dy = 3
    ex = 0.9
    ey = 3
    eye = 0.6
    
    dxmax = 14*dx
    ax = dxmax/5
    
    epsilony = 0.2

    R0 = Room(name='R0',
                position=[0*dx, 1*dy+(ey-eye)/2, dxmax+ex, eye],
                switches_list=[])
    ##################################################
    ##################################################
    R1 = Room(name='R1',
                position=[0*ax, 0*dy, ex, ey],
                switches_list=Slist_0)
    R2 = Room(name='R2',
                position=[1*ax, 0*dy, ex, ey],
                switches_list=Slist_1)
    R3 = Room(name='R3',
                position=[2*ax, 0*dy, ex, ey],
                switches_list=Slist_2)
    R4 = Room(name='R4',
                position=[3*ax, 0*dy, ex, ey],
                switches_list=Slist_3)
    R5 = Room(name='R5',
                position=[4*ax, 0*dy, ex, ey],
                switches_list=Slist_4)
    ##################################################
    R6 = Room(name='R6',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    R7 = Room(name='R7',
                position=[1*dx, 2*dy+epsilony, ex, ey],
                switches_list=Slist_6)
    R8 = Room(name='R8',
                position=[2*dx, 2*dy+2*epsilony, ex, ey],
                switches_list=Slist_7)
    R9 = Room(name='R9',
                position=[3*dx, 2*dy+3*epsilony, ex, ey],
                switches_list=Slist_8)
    R10 = Room(name='R10',
                position=[4*dx, 2*dy+4*epsilony, ex, ey],
                switches_list=Slist_9)
    ##################################################
    R11 = Room(name='R11',
                position=[5*dx, 2*dy, ex, ey],
                switches_list=Slist_10)
    R12 = Room(name='R12',
                position=[6*dx, 2*dy+epsilony, ex, ey],
                switches_list=Slist_11)
    R13 = Room(name='R13',
                position=[7*dx, 2*dy+2*epsilony, ex, ey],
                switches_list=Slist_12)
    R14 = Room(name='R14',
                position=[8*dx, 2*dy+3*epsilony, ex, ey],
                switches_list=Slist_13)
    ##################################################
    R15 = Room(name='R15',
                position=[9*dx, 2*dy, ex, ey],
                switches_list=Slist_14)
    R16 = Room(name='R16',
                position=[10*dx, 2*dy+epsilony, ex, ey],
                switches_list=Slist_15)
    R17 = Room(name='R17',
                position=[11*dx, 2*dy+2*epsilony, ex, ey],
                switches_list=Slist_16)
    ##################################################
    R18 = Room(name='R18',
                position=[12*dx, 2*dy, ex, ey],
                switches_list=Slist_17)
    R19 = Room(name='R19',
                position=[13*dx, 2*dy+epsilony, ex, ey],
                switches_list=Slist_18)
    ##################################################
    R20 = Room(name='R20',
                position=[14*dx, 2*dy, ex, ey],
                switches_list=Slist_19)
    ##################################################
    # R21 = Room(name='R21',
    #             position=[6*ax, 0*dy, ex, ey],
    #             switches_list=Slist_21)
    # R22 = Room(name='R22',
    #             position=[dxmax, 0*dy, ex, ey],
    #             switches_list=Slist_22)
    ##################################################
    RE = Room(name='RE',
              position=[5*ax, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[ex/2/(dxmax+ex), 0],
                relative_arrival_coordinates=[1/2, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                # relative_departure_coordinates=[(ax+ex/2)/(dxmax+ex), 0],
                # relative_arrival_coordinates=[1/2, 1]
                )
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                # relative_departure_coordinates=[(2*ax+ex/2)/(dxmax+ex), 0],
                # relative_arrival_coordinates=[1/2, 1]
                )
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                # relative_departure_coordinates=[(3*ax+ex/2)/(dxmax+ex), 0],
                # relative_arrival_coordinates=[1/2, 1]
                )
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                # relative_departure_coordinates=[(4*ax+ex/2)/(dxmax+ex), 0],
                # relative_arrival_coordinates=[1/2, 1]
                )
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[(4*ax+ex/2)/(dxmax+ex), 0]
                )
    
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[ex/2/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[(dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=[(2*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=[(3*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=R10,
                relative_departure_coordinates=[(4*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R0,
                room_arrival=R11,
                relative_departure_coordinates=[(5*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=R12,
                relative_departure_coordinates=[(6*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R0,
                room_arrival=R13,
                relative_departure_coordinates=[(7*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R0,
                room_arrival=R14,
                relative_departure_coordinates=[(8*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R0,
                room_arrival=R15,
                relative_departure_coordinates=[(9*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=R16,
                relative_departure_coordinates=[(10*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R0,
                room_arrival=R17,
                relative_departure_coordinates=[(11*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R0,
                room_arrival=R18,
                relative_departure_coordinates=[(12*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R0,
                room_arrival=R19,
                relative_departure_coordinates=[(13*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R0,
                room_arrival=R20,
                relative_departure_coordinates=[(14*dx+ex/2)/(dxmax+ex), 1],
                relative_arrival_coordinates=[1/2, 0])
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[(5*ax+ex/2)/(dxmax+ex), 0],
                relative_arrival_coordinates=[1/2, 1])
    # D21 = Door(two_way=False,
    #             tree=T21,
    #             name='D21',
    #             room_departure=R0,
    #             room_arrival=R21,
    #             relative_departure_coordinates=[(6*ax+ex/2)/(dxmax+ex), 0],
    #             relative_arrival_coordinates=[1/2, 1])
    # D22 = Door(two_way=False,
    #             tree=T22,
    #             name='D22',
    #             room_departure=R21,
    #             room_arrival=R22)
    # D23 = Door(two_way=False,
    #             tree=T23,
    #             name='D23',
    #             room_departure=R22,
    #             room_arrival=R0,
    #             relative_departure_coordinates=[1/2, 1],
    #             relative_arrival_coordinates=[(dxmax+ex/2)/(dxmax+ex), 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4,
                             R5, R6, R7, R8, R9,
                             R10, R11, R12, R13, R14,
                             R15, R16, R17, R18, R19,
                             R20,
                             # R21, R22,
                             RE],
                 doors_list=[D0, D1, D2, D3, D4,
                             D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14,
                             D15, D16, D17, D18, D19,
                             D20, D21,
                             # D21, D22, D23
                             ],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Patience',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.25
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.7, sa=0.3),
                         room_color=Color.color_hls(hu, li=0.3, sa=0.4),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.9, li=0.1, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.9, li=0.1, sa=1))
    return lcolor