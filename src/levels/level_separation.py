from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

def level_separation(): 
    
    va = 0
    vb = 0

    S0 = Switch(name='S0', value=vb)
    S1 = Switch(name='S1', value=vb)

    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=vb)

    S4 = Switch(name='S4')
    S5 = Switch(name='S5', value=vb)

    S6 = Switch(name='S6')
    S7 = Switch(name='S7', value=vb)

    S8 = Switch(name='S8', value=va|vb)
    S9 = Switch(name='S9', value=va|vb)

    S10 = Switch(name='S10', value=vb)
    S11 = Switch(name='S11', value=va|vb)

    S12 = Switch(name='S12')
    S13 = Switch(name='S13', value=va|vb)

    S14 = Switch(name='S14', value=vb)
    S15 = Switch(name='S15', value=va)

    S16 = Switch(name='S16', value=va|vb)
    S17 = Switch(name='S17', value=va|vb)

    S18 = Switch(name='S18', value=va|vb)
    S19 = Switch(name='S19', value=va)

    S20 = Switch(name='S20', value=vb)
    S21 = Switch(name='S21', value=va)

    S22 = Switch(name='S22', value=va|vb)
    S23 = Switch(name='S23')

    S24 = Switch(name='S24', value=va)
    S25 = Switch(name='S25', value=va)

    S26 = Switch(name='S26', value=va)
    S27 = Switch(name='S27')

    S28 = Switch(name='S28', value=va)
    S29 = Switch(name='S29')

    S30 = Switch(name='S30', value=va)
    S31 = Switch(name='S31')
    
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7,
             S8, S9, S10, S11, S12, S13, S14, S15,
             S16, S17, S18, S19, S20, S21, S22, S23,
             S24, S25, S26, S27, S28, S29, S30, S31]
    
    Slist1 = []
    for S in Slist:
        if S.value:
            Slist1.append(S.name)
    print(' '.join(Slist1))

    tree_list_1 = ['NOT', ['EQU', Tree.tree_list_BIN(2), Tree.tree_list_BIN(2)]]
    
    tree_list_EQU_BIN = ['EQU'] + [Tree.tree_list_BIN(2)]*4 + [[None]]
    def tree_list_OR_EQU_BIN(n):
        return ['OR'] + [tree_list_EQU_BIN]*n
    tree_list_0 = ['AND',
                   tree_list_OR_EQU_BIN(4),
                   tree_list_OR_EQU_BIN(6),
                   tree_list_OR_EQU_BIN(6),
                   tree_list_OR_EQU_BIN(6),]

    T0 = Tree(tree_list=tree_list_0,
              empty=True,
              name='T0',
              switches=[S0, S1, S2, S3, S4, S5, S6, S7, 0,
              S8, S9, S10, S11, S12, S13, S14, S15, 0,
              S16, S17, S18, S19, S20, S21, S22, S23, 0,
              S24, S25, S26, S27, S28, S29, S30, S31, 0,
              S4, S5, S8, S9, S10, S11, S12, S13, 1,
              S12, S13, S16, S17, S18, S19, S20, S21, 1,
              S20, S21, S24, S25, S26, S27, S28, S29, 1,
              S6, S7, S10, S11, S12, S13, S14, S15, 1,
              S14, S15, S18, S19, S20, S21, S22, S23, 1,
              S22, S23, S26, S27, S28, S29, S30, S31, 1,
              S0, S1, S2, S3, S4, S5, S10, S11, 2,
              S8, S9, S10, S11, S12, S13, S18, S19, 2,
              S16, S17, S18, S19, S20, S21, S26, S27, 2,
              S2, S3, S4, S5, S6, S7, S12, S13, 2,
              S10, S11, S12, S13, S14, S15, S20, S21, 2,
              S18, S19, S20, S21, S22, S23, S28, S29, 2,
              S0, S1, S8, S9, S10, S11, S16, S17, 3,
              S8, S9, S16, S17, S18, S19, S24, S25, 3,
              S2, S3, S10, S11, S12, S13, S18, S19, 3,
              S10, S11, S18, S19, S20, S21, S26, S27, 3,
              S4, S5, S12, S13, S14, S15, S20, S21, 3,
              S12, S13, S20, S21, S22, S23, S28, S29, 3,],
              cut_expression=True)
    T1 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T1',
                      switches=[S0, S1, S2, S3])
    T2 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T2',
                      switches=[S2, S3, S4, S5])
    T3 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T3',
                      switches=[S4, S5, S6, S7])
    T4 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T4',
                      switches=[S8, S9, S10, S11])
    T5 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T5',
                      switches=[S10, S11, S12, S13])
    T6 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T6',
                      switches=[S12, S13, S14, S15])
    T7 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T7',
                      switches=[S16, S17, S18, S19])
    T8 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T8',
                      switches=[S18, S19, S20, S21])
    T9 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T9',
                      switches=[S20, S21, S22, S23])
    T10 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T10',
                      switches=[S24, S25, S26, S27])
    T11 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T11',
                      switches=[S26, S27, S28, S29])
    T12 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T12',
                      switches=[S28, S29, S30, S31])
    T13 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T13',
                      switches=[S0, S1, S8, S9])
    T14 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T14',
                      switches=[S8, S9, S16, S17])
    T15 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T15',
                      switches=[S16, S17, S24, S25])
    T16 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T16',
                      switches=[S2, S3, S10, S11])
    T17 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T17',
                      switches=[S10, S11, S18, S19])
    T18 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T18',
                      switches=[S18, S19, S26, S27])
    T19 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T19',
                      switches=[S4, S5, S12, S13])
    T20 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T20',
                      switches=[S12, S13, S20, S21])
    T21 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T21',
                      switches=[S20, S21, S28, S29])
    T22 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T22',
                      switches=[S6, S7, S14, S15])
    T23 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T23',
                      switches=[S14, S15, S22, S23])
    T24 = Tree(tree_list=tree_list_1,
                      empty=True,
                      name='T24',
                      switches=[S22, S23, S30, S31])
    T25 = Tree(tree_list=Tree.tree_list_AND(3),
                empty=True,
                name='T25',
                switches=[S30, S32, S33])
    
    ex = 0.3
    ey = 0.3
    
    dx = 0.65
    dy = 1
    
    ex0 = 1

    R0 = Room(name='R0',
              position=[ -ex0-dx+ex, 0, ex0, 3*dy-ey],
              switches_list=Slist)
    R1 = Room(name='R1',
              position=[ 0*dx, 0*dy, ex ,ey],
              switches_list=[])
    R2 = Room(name='R2',
              position=[ 0*dx, 1*dy, ex ,ey],
              switches_list=[])
    R3 = Room(name='R3',
              position=[ 0*dx, 2*dy, ex ,ey],
              switches_list=[])
    R4 = Room(name='R4',
              position=[ 0*dx, 3*dy, ex ,ey],
              switches_list=[])
    R5 = Room(name='R5',
              position=[ 1*dx, 0*dy, ex ,ey],
              switches_list=[S32])
    R6 = Room(name='R6',
              position=[ 1*dx, 1*dy, ex ,ey],
              switches_list=[])
    R7 = Room(name='R7',
              position=[ 1*dx, 2*dy, ex ,ey],
              switches_list=[])
    R8 = Room(name='R8',
              position=[ 1*dx, 3*dy, ex ,ey],
              switches_list=[])
    R9 = Room(name='R9',
              position=[ 2*dx, 0*dy, ex ,ey],
              switches_list=[S33])
    R10 = Room(name='R10',
               position=[ 2*dx, 1*dy, ex ,ey],
               switches_list=[])
    R11 = Room(name='R11',
               position=[ 2*dx, 2*dy, ex ,ey],
               switches_list=[])
    R12 = Room(name='R12',
               position=[ 2*dx, 3*dy, ex ,ey],
               switches_list=[])
    R13 = Room(name='R13',
               position=[ 3*dx, 0*dy, ex ,ey],
               switches_list=[])
    R14 = Room(name='R14',
               position=[ 3*dx, 1*dy, ex ,ey],
               switches_list=[])
    R15 = Room(name='R15',
               position=[ 3*dx, 2*dy, ex ,ey],
               switches_list=[])
    R16 = Room(name='R16',
               position=[ 3*dx, 3*dy, ex ,ey],
               switches_list=[])
    RE = Room(name='RE',
              position=[ -ex0-dx+ex, 3*dy, ex ,ey],
              is_exit=True)

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1, ey/2/(3*dy-ey)],
              relative_arrival_coordinates=[0, 1/2])
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
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R6,
                room_arrival=R7)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R7,
                room_arrival=R8)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R9,
                room_arrival=R10)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R10,
                room_arrival=R11)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R11,
                room_arrival=R12)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R13,
                room_arrival=R14)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R14,
                room_arrival=R15)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R15,
                room_arrival=R16)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R5)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R5,
                room_arrival=R9)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R9,
                room_arrival=R13)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R2,
                room_arrival=R6)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R6,
                room_arrival=R10)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R10,
                room_arrival=R14)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R3,
                room_arrival=R7)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R7,
                room_arrival=R11)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=R11,
                room_arrival=R15)
    D22 = Door(two_way=True,
                tree=T22,
                name='D22',
                room_departure=R4,
                room_arrival=R8)
    D23 = Door(two_way=True,
                tree=T23,
                name='D23',
                room_departure=R8,
                room_arrival=R12)
    D24 = Door(two_way=True,
                tree=T24,
                name='D24',
                room_departure=R12,
                room_arrival=R16)
    D25 = Door(two_way=True,
                tree=T25,
                name='D25',
                room_departure=R4,
                room_arrival=RE)
    
    fastest_solution = """S0 S1 S3 S5 S7 S8 S9 S10 S11 S13 S14 S16 S17 S18 S20 S22 D0 D1 D16 D17 D7 S33 D7 D17 D16 D1 D0 S0 S1 S3 S5 S7 S10 S14 S15 S19 S20 S21 S24 S25 S26 S28 S30 D0 D13 S32 D4 D17 D8 D9 D23 D22 D25"""

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25],
                 fastest_solution=fastest_solution,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=0.6, li=0.5),
                 name='Separation',
                 keep_proportions=True,
                 door_window_size=500,
                 y_separation=35)
    
    return level

if __name__ == "__main__":
    for i in [0, 8, 16, 24]:
        print(f'S{i}, S{i+1}, S{i+2}, S{i+3}, S{i+4}, S{i+5}, S{i+6}, S{i+7}, 0,')
    for i in [0, 8, 16,
              2, 10, 18]:
        print(f'S{i+4}, S{i+5}, S{i+8}, S{i+9}, S{i+10}, S{i+11}, S{i+12}, S{i+13}, 1,')
    for i in [0, 8, 16,
              2, 10, 18]:
        print(f'S{i}, S{i+1}, S{i+2}, S{i+3}, S{i+4}, S{i+5}, S{i+10}, S{i+11}, 2,')
    for i in [0, 8,
              2, 10,
              4, 12]:
        print(f'S{i}, S{i+1}, S{i+8}, S{i+9}, S{i+10}, S{i+11}, S{i+16}, S{i+17}, 3,')