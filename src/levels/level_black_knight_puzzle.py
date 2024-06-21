from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_black_knight_puzzle(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    # black knight
    # 0
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    # 0
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    
    # knight
    # 1
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11')
    # 0
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    
    # knight
    # 1
    S15 = Switch(name='S15', value=1)
    S16 = Switch(name='S16')
    # 1
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    
    # knight
    # 1
    S20 = Switch(name='S20', value=1)
    S21 = Switch(name='S21')
    # 2
    S22 = Switch(name='S22')
    S23 = Switch(name='S23', value=1)
    S24 = Switch(name='S24')
    
    # knight
    # 1
    S25 = Switch(name='S25', value=1)
    S26 = Switch(name='S26')
    # 3
    S27 = Switch(name='S27', value=1)
    S28 = Switch(name='S28', value=1)
    S29 = Switch(name='S29')
    
    # tower
    # 1
    S30 = Switch(name='S30', value=1)
    S31 = Switch(name='S31')
    # 4
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34', value=1)
    
    # tower
    # 1
    S35 = Switch(name='S35', value=1)
    S36 = Switch(name='S36')
    # 5
    S37 = Switch(name='S37', value=1)
    S38 = Switch(name='S38')
    S39 = Switch(name='S39', value=1)
    
    # tower
    # 2
    S40 = Switch(name='S40')
    S41 = Switch(name='S41', value=1)
    # 4
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44', value=1)
    
    # tower
    # 2
    S45 = Switch(name='S45')
    S46 = Switch(name='S46', value=1)
    # 5
    S47 = Switch(name='S47', value=1)
    S48 = Switch(name='S48')
    S49 = Switch(name='S49', value=1)
    
    # bishop
    # 0
    S50 = Switch(name='S50')
    S51 = Switch(name='S51')
    # 1
    S52 = Switch(name='S52', value=1)
    S53 = Switch(name='S53')
    S54 = Switch(name='S54')
    
    # bishop
    # 0
    S55 = Switch(name='S55')
    S56 = Switch(name='S56')
    # 2
    S57 = Switch(name='S57')
    S58 = Switch(name='S58', value=1)
    S59 = Switch(name='S59')
    
    # bishop
    # 0
    S60 = Switch(name='S60')
    S61 = Switch(name='S61')
    # 3
    S62 = Switch(name='S62', value=1)
    S63 = Switch(name='S63', value=1)
    S64 = Switch(name='S64')
    
    # bishop
    # 0
    S65 = Switch(name='S65')
    S66 = Switch(name='S66')
    # 4
    S67 = Switch(name='S67')
    S68 = Switch(name='S68')
    S69 = Switch(name='S69', value=1)

    Slist_0 = [S0, S1, S2, S3, S4]
    Slist_1 = [S5, S6, S7, S8, S9]
    Slist_2 = [S10, S11, S12, S13, S14]
    Slist_3 = [S15, S16, S17, S18, S19]
    Slist_4 = [S20, S21, S22, S23, S24]
    Slist_5 = [S25, S26, S27, S28, S29]
    Slist_6 = [S30, S31, S32, S33, S34]
    Slist_7 = [S35, S36, S37, S38, S39]
    Slist_8 = [S40, S41, S42, S43, S44]
    Slist_9 = [S45, S46, S47, S48, S49]
    Slist_10 = [S50, S51, S52, S53, S54]
    Slist_11 = [S55, S56, S57, S58, S59]
    Slist_12 = [S60, S61, S62, S63, S64]
    Slist_13 = [S65, S66, S67, S68, S69]
    
    tree_list_BIN_5 = Tree.tree_list_BIN(5)
    
    V0 = Tree(tree_list=tree_list_BIN_5,
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=tree_list_BIN_5,
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=tree_list_BIN_5,
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=tree_list_BIN_5,
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=tree_list_BIN_5,
          name='V4',
          switches=Slist_4)
    V5 = Tree(tree_list=tree_list_BIN_5,
          name='V5',
          switches=Slist_5)
    V6 = Tree(tree_list=tree_list_BIN_5,
          name='V6',
          switches=Slist_6)
    V7 = Tree(tree_list=tree_list_BIN_5,
          name='V7',
          switches=Slist_7)
    V8 = Tree(tree_list=tree_list_BIN_5,
          name='V8',
          switches=Slist_8)
    V9 = Tree(tree_list=tree_list_BIN_5,
          name='V9',
          switches=Slist_9)
    V10 = Tree(tree_list=tree_list_BIN_5,
          name='V10',
          switches=Slist_10)
    V11 = Tree(tree_list=tree_list_BIN_5,
          name='V11',
          switches=Slist_11)
    V12 = Tree(tree_list=tree_list_BIN_5,
          name='V12',
          switches=Slist_12)
    V13 = Tree(tree_list=tree_list_BIN_5,
          name='V13',
          switches=Slist_13)

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13]
    
    l = [i+4*j for i in range(0, 3) for j in range(0, 6) if not (i, j) in [(2, 0), (2, 1), (2, 2), (2, 3)]]
    Vlist_14 = Vlist + l
    assert len(Vlist_14) == 28
    V14 = Tree(tree_list=['EQUSET'] + [[None]]*28,
          name='V14',
          switches=Vlist_14)
    
    V14 = Tree(tree_list=['EQUSET'] + [[None]]*28,
          name='V14',
          switches=Vlist_14)
    
    V15 = Tree(tree_list=['DIFF'] + [[None]]*13,
          name='V15',
          switches=[V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13])
    
    tree_list_0 = ['AND',
                   [None],
                   [None],
                   ['EQUSET',
                    ['ABS', ['SUM', Tree.tree_list_BIN(2), ['MINUS', Tree.tree_list_BIN(2)]]],
                    ['ABS', ['SUM', Tree.tree_list_BIN(3), ['MINUS', Tree.tree_list_BIN(3)]]],
                    [None],
                    [None],
                   ]]
    
    tree_list_1 = ['EQU', [None], [None]]

    # knights
    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V14, V15, 
                          S0, S1,
                          S5, S6,
                          S2, S3, S4,
                          S7, S8, S9,
                          1, 2])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V14, V15, 
                          S0, S1,
                          S10, S11,
                          S2, S3, S4,
                          S12, S13, S14,
                          1, 2])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[V0, V2])
    T4 = Tree(tree_list=tree_list_0,
                name='T4', 
                switches=[V14, V15, 
                          S0, S1,
                          S15, S16,
                          S2, S3, S4,
                          S17, S18, S19,
                          1, 2])
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[V0, V3])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[V14, V15, 
                          S0, S1,
                          S20, S21,
                          S2, S3, S4,
                          S22, S23, S24,
                          1, 2])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[V0, V4])
    T8 = Tree(tree_list=tree_list_0,
                name='T8',
                switches=[V14, V15, 
                          S0, S1,
                          S25, S26,
                          S2, S3, S4,
                          S27, S28, S29,
                          1, 2])
    T9 = Tree(tree_list=tree_list_1,
                name='T9',
                switches=[V0, V5])
    
    # towers
    T10 = Tree(tree_list=tree_list_0,
                name='T10',
                switches=[V14, V15, 
                          S0, S1,
                          S30, S31,
                          S2, S3, S4,
                          S32, S33, S34,
                          0, 1])
    T11 = Tree(tree_list=tree_list_1,
                name='T11',
                switches=[V0, V6])
    T12 = Tree(tree_list=tree_list_0,
                name='T12',
                switches=[V14, V15, 
                          S0, S1,
                          S35, S36,
                          S2, S3, S4,
                          S37, S38, S39,
                          0, 1])
    T13 = Tree(tree_list=tree_list_1,
                name='T13',
                switches=[V0, V7])
    T14 = Tree(tree_list=tree_list_0,
                name='T14',
                switches=[V14, V15, 
                          S0, S1,
                          S40, S41,
                          S2, S3, S4,
                          S42, S43, S44,
                          0, 1])
    T15 = Tree(tree_list=tree_list_1,
                name='T15',
                switches=[V0, V8])
    T16 = Tree(tree_list=tree_list_0,
                name='T16',
                switches=[V14, V15, 
                          S0, S1,
                          S45, S46,
                          S2, S3, S4,
                          S47, S48, S49,
                          0, 1])
    T17 = Tree(tree_list=tree_list_1,
                name='T17',
                switches=[V0, V9])
    
    # bishops
    T18 = Tree(tree_list=tree_list_0,
                name='T18',
                switches=[V14, V15, 
                          S0, S1,
                          S50, S51,
                          S2, S3, S4,
                          S52, S53, S54,
                          1, 1])
    T19 = Tree(tree_list=tree_list_1,
                name='T19',
                switches=[V0, V10])
    T20 = Tree(tree_list=tree_list_0,
                name='T20',
                switches=[V14, V15, 
                          S0, S1,
                          S55, S56,
                          S2, S3, S4,
                          S57, S58, S59,
                          1, 1])
    T21 = Tree(tree_list=tree_list_1,
                name='T21',
                switches=[V0, V11])
    T22 = Tree(tree_list=tree_list_0,
                name='T22',
                switches=[V14, V15, 
                          S0, S1,
                          S60, S61,
                          S2, S3, S4,
                          S62, S63, S64,
                          1, 1])
    T23 = Tree(tree_list=tree_list_1,
                name='T23',
                switches=[V0, V12])
    T24 = Tree(tree_list=tree_list_0,
                name='T24',
                switches=[V14, V15, 
                          S0, S1,
                          S65, S66,
                          S2, S3, S4,
                          S67, S68, S69,
                          1, 1])
    T25 = Tree(tree_list=tree_list_1,
                name='T25',
                switches=[V0, V13])
    T26 = Tree(tree_list=Tree.tree_list_from_str('FFTFT'),
                name='T26',
                switches=Slist_1)

    dx = 1
    dy = 1.5
    ex = 0.95
    ey = 0.5
    ay = 3*ey
    
    delta_y = ex
    ya = -ay-delta_y
    yb = ey+delta_y
    
    """
    possible_switches_updating = [bin(i)[2:].ljust(5, '0') for i in l]
    possible_switches_updating = [[*string] for string in possible_switches_updating]
    possible_switches_updating = [[int(nbin) for nbin in lbin] for lbin in possible_switches_updating]
    for lbin in possible_switches_updating:
        lbin.reverse()"""

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 8*dx+ex, ey],
                switches_list=Slist_0,
                #possible_switches_updating=possible_switches_updating
                )
    R1 = Room(name='R1',
                position=[5*dx, ya, ex, ay],
                switches_list=Slist_1,
                #possible_switches_updating=possible_switches_updating
                )
    R2 = Room(name='R2',
                position=[3*dx, ya, ex, ay],
                switches_list=Slist_2,
                #possible_switches_updating=possible_switches_updating
                )
    R3 = Room(name='R3',
                position=[2*dx, ya, ex, ay],
                switches_list=Slist_3,
                #possible_switches_updating=possible_switches_updating
                )
    R4 = Room(name='R4',
                position=[1*dx, ya, ex, ay],
                switches_list=Slist_4,
                #possible_switches_updating=possible_switches_updating
                )
    R5 = Room(name='R5',
                position=[0*dx, ya, ex, ay],
                switches_list=Slist_5,
                #possible_switches_updating=possible_switches_updating
                )
    R6 = Room(name='R6',
                position=[8*dx, yb, ex, ay],
                switches_list=Slist_6,
                #possible_switches_updating=possible_switches_updating
                )
    R7 = Room(name='R7',
                position=[7*dx, yb, ex, ay],
                switches_list=Slist_7,
                #possible_switches_updating=possible_switches_updating
                )
    R8 = Room(name='R8',
                position=[6*dx, yb, ex, ay],
                switches_list=Slist_8,
                #possible_switches_updating=possible_switches_updating
                )
    R9 = Room(name='R9',
                position=[5*dx, yb, ex, ay],
                switches_list=Slist_9,
                #possible_switches_updating=possible_switches_updating
                )
    R10 = Room(name='R10',
                position=[3*dx, yb, ex, ay],
                switches_list=Slist_10,
                #possible_switches_updating=possible_switches_updating
                )
    R11 = Room(name='R11',
                position=[2*dx, yb, ex, ay],
                switches_list=Slist_11,
                #possible_switches_updating=possible_switches_updating
                )
    R12 = Room(name='R12',
                position=[1*dx, yb, ex, ay],
                switches_list=Slist_12,
                #possible_switches_updating=possible_switches_updating
                )
    R13 = Room(name='R13',
                position=[0*dx, yb, ex, ay],
                switches_list=Slist_13,
                #possible_switches_updating=possible_switches_updating
                )
    RE = Room(name='RE',
              position=[7*dx, ya, 1*dx+ex, ay],
              is_exit=True)
    
    
    r0x = 8*dx+ex
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(5*dx+ex/4)/r0x, 0],
                relative_arrival_coordinates=[1/4, 1],)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 1],
                relative_arrival_coordinates=[(5*dx+3*ex/4)/r0x, 0],)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[(3*dx+ex/4)/r0x, 0],
                relative_arrival_coordinates=[1/4, 1],)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 1],
                relative_arrival_coordinates=[(3*dx+3*ex/4)/r0x, 0],)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[(2*dx+ex/4)/r0x, 0],
                relative_arrival_coordinates=[1/4, 1],)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 1],
                relative_arrival_coordinates=[(2*dx+3*ex/4)/r0x, 0],)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[(1*dx+ex/4)/r0x, 0],
                relative_arrival_coordinates=[1/4, 1],)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 1],
                relative_arrival_coordinates=[(1*dx+3*ex/4)/r0x, 0],)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[(0*dx+ex/4)/r0x, 0],
                relative_arrival_coordinates=[1/4, 1],)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 1],
                relative_arrival_coordinates=[(0*dx+3*ex/4)/r0x, 0],)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[(8*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R6,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(8*dx+3*ex/4)/r0x, 1],)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R0,
                room_arrival=R7,
                relative_departure_coordinates=[(7*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(7*dx+3*ex/4)/r0x, 1],)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R0,
                room_arrival=R8,
                relative_departure_coordinates=[(6*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(6*dx+3*ex/4)/r0x, 1],)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=R9,
                relative_departure_coordinates=[(5*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R9,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(5*dx+3*ex/4)/r0x, 1],)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R0,
                room_arrival=R10,
                relative_departure_coordinates=[(3*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R10,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(3*dx+3*ex/4)/r0x, 1],)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R0,
                room_arrival=R11,
                relative_departure_coordinates=[(2*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R11,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(2*dx+3*ex/4)/r0x, 1],)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R0,
                room_arrival=R12,
                relative_departure_coordinates=[(1*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R12,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(1*dx+3*ex/4)/r0x, 1],)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R0,
                room_arrival=R13,
                relative_departure_coordinates=[(0*dx+ex/4)/r0x, 1],
                relative_arrival_coordinates=[1/4, 0],)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R13,
                room_arrival=R0,
                relative_departure_coordinates=[3/4, 0],
                relative_arrival_coordinates=[(0*dx+3*ex/4)/r0x, 1],)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[(7.5*dx+ex/2)/r0x, 0],
                relative_arrival_coordinates=[1/2 ,1],)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='Black knight puzzle',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level