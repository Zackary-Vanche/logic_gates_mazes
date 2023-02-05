from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_mols():

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
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    S45 = Switch(name='S45')
    S46 = Switch(name='S46')
    S47 = Switch(name='S47')
    S48 = Switch(name='S48')
    S49 = Switch(name='S49')
    S50 = Switch(name='S50')
    S51 = Switch(name='S51')
    S52 = Switch(name='S52')
    S53 = Switch(name='S53')
    S54 = Switch(name='S54')
    S55 = Switch(name='S55')
    S56 = Switch(name='S56')
    S57 = Switch(name='S57')
    S58 = Switch(name='S58')
    S59 = Switch(name='S59')
    S60 = Switch(name='S60')
    S61 = Switch(name='S61')
    S62 = Switch(name='S62')
    S63 = Switch(name='S63')
    S64 = Switch(name='S64')
    S65 = Switch(name='S65')
    S66 = Switch(name='S66')
    S67 = Switch(name='S67')
    S68 = Switch(name='S68')
    S69 = Switch(name='S69')
    S70 = Switch(name='S70')
    S71 = Switch(name='S71')

    Slist = [
     S0, S1, S2, S3, S4, S5,
     S6, S7, S8, S9, S10, S11,
     S12, S13, S14, S15, S16, S17,
     S18, S19, S20, S21, S22, S23,

     S24, S25, S26, S27, S28, S29,
     S30, S31, S32, S33, S34, S35,
     S36, S37, S38, S39, S40, S41,
     S42, S43, S44, S45, S46, S47,

     S48, S49, S50, S51, S52, S53,
     S54, S55, S56, S57, S58, S59,
     S60, S61, S62, S63, S64, S65,
     S66, S67, S68, S69, S70, S71]

    def Slist_i(i):
        return Slist[i * 6:i * 6 + 6]

    def Slist_transverse(i):
        l = []
        for j in range(0, 6, 2):
            for k in range(3*i, 3*i+4):
                l.append(Slist_i(k)[j])
                l.append(Slist_i(k)[j+1])
        return l

    Slist12 = []
    for i in range(12):
        for j in range(3):
            Slist12.extend(Slist[j*24:j*24+24][2*i:2*i+2])
    assert len(Slist12) == len(Slist), len(Slist12)
    Slist12.extend([0, 1+4, 2+4*2, 3+4*3])

    tree_list0 = ['DIFF'] + [Tree.tree_list_BIN(2)]*3 + [[None]]
    tree_list3 = ['AND'] + [['DIFF'] + [Tree.tree_list_BIN(2)]*4]*3 + [tree_list0]
    tree_list4 = ['AND', tree_list0, ['INF', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)]]

    T0 = Tree(tree_list=tree_list0,
              empty=True,
              name='T0',
              switches=Slist_i(0) + [0])
    T1 = Tree(tree_list=tree_list0,
              empty=True,
              name='T1',
              switches=Slist_i(1) + [1])
    T2 = Tree(tree_list=tree_list0,
              empty=True,
              name='T2',
              switches=Slist_i(2) + [2])
    T3 = Tree(tree_list=tree_list3,
              empty=True,
              name='T3',
              switches=Slist_transverse(0) + Slist_i(3) + [3],
              cut_expression=True)
    T4 = Tree(tree_list=tree_list4,
              empty=True,
              name='T4',
              switches=Slist_i(4) + [0] + [S0, S1, S24, S25])
    T5 = Tree(tree_list=tree_list0,
              empty=True,
              name='T5',
              switches=Slist_i(5) + [1])
    T6 = Tree(tree_list=tree_list0,
              empty=True,
              name='T6',
              switches=Slist_i(6) + [2])
    T7 = Tree(tree_list=tree_list3,
              empty=True,
              name='T7',
              switches=Slist_transverse(1) + Slist_i(7) + [3],
              cut_expression=True)
    T8 = Tree(tree_list=tree_list4,
              empty=True,
              name='T8',
              switches=Slist_i(8) + [0] + [S24, S25, S48, S49])
    T9 = Tree(tree_list=tree_list0,
              empty=True,
              name='T9',
              switches=Slist_i(9) + [1])
    T10 = Tree(tree_list=tree_list0,
               empty=True,
               name='T10',
               switches=Slist_i(10) + [2])
    T11 = Tree(tree_list=tree_list3,
               empty=True,
               name='T11',
               switches=Slist_transverse(2) + Slist_i(11) + [3],
               cut_expression=True)
    tree_list = ['DIFF'] + [Tree.tree_list_BIN(6)]*12 + [[None]]*4
    Slistp = [S2, S3, S5, S7, S11, S13, S17, S19, S23, S29, S31, S37, S41, S43, S47, S53, S59, S61, S67, S71]
    T12 = Tree(tree_list=['AND',
                          tree_list,
                          ['EQU', [None], ['MOD', Tree.tree_list_BIN(20), [None]]]],
               empty=True,
               name='T12',
               switches=Slist12 + [7] + Slistp + [11],
               cut_expression=True)

    ex = 0.4
    ey = 3
    dx = 0.9
    dy = ey + 0.6

    def get_room(i):
        return Room(name=f'R{i}',
                    position=[i//2*dx, int(i%4 in [1, 2])*dy, ex, ey],
                    switches_list=Slist_i(i))

    R0 = get_room(0)
    R1 = get_room(1)
    R2 = get_room(2)
    R3 = get_room(3)
    R4 = get_room(4)
    R5 = get_room(5)
    R6 = get_room(6)
    R7 = get_room(7)
    R8 = get_room(8)
    R9 = get_room(9)
    R10 = get_room(10)
    R11 = get_room(11)
    R12 = get_room(12)
    RE = Room(name='RE',
              position=[6*dx, dy, ex, ey],
    is_exit = True)  # E pour exit ou end

    rdc1 = [1, 1]
    rac1 = [0, 0]
    rdc2 = [1, 0]
    rac2 = [0, 1]
    rp = 0.55

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=rdc1,
              relative_arrival_coordinates=rac1,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=rdc2,
              relative_arrival_coordinates=rac2,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_departure_coordinates=rdc1,
              relative_arrival_coordinates=rac1,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_departure_coordinates=rdc2,
              relative_arrival_coordinates=rac2,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=R9)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R9,
              room_arrival=R10,
              relative_departure_coordinates=rdc1,
              relative_arrival_coordinates=rac1,
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R10,
               room_arrival=R11)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R11,
               room_arrival=R12,
              relative_departure_coordinates=rdc2,
              relative_arrival_coordinates=rac2)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R12,
               room_arrival=RE)

    rp = 1 / 2

    lcolor = Levels_colors_list.FROM_HUE(hu=0.9, sa=0.6, li=0.65)
    lcolor.surrounding_color=Color.WHITE_PINK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution='S0 S3 S4 S5 D0 S7 S8 S9 D1 S12 S13 S16 D2 S20 S23 D3 S25 S26 S27 S28 D4 S30 S31 S33 D5 S36 S40 S41 D6 S43 S44 D7 S48 S49 S51 S52 D8 S56 S57 S59 D9 S60 S61 S62 D10 S68 S71 D11 D12',
                 level_color=lcolor,
                 name='MOLS',
                 door_window_size=900,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level
