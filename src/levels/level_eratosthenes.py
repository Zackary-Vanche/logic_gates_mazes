from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4', value=1)
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
    
    tree_list_2 = ['AND',
                   ['DIFF', [None], [None], [None]],
                   #['DIFF', [None], [None]],
                   ['EQU', ['MODNAN', [None], [None]], [None]]]
    
    def get_Slist(i):
        return [V0, 0, i,
                i, V0, 0]

    V0 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V0',
          switches=[S0, S1, S2])
    V1 = Tree(tree_list=Tree.tree_list_BIN(3),
          name='V1',
          switches=[S3, S4, S5,])
    V2 = Tree(tree_list=tree_list_2,
          name='V2',
          switches=get_Slist(2))
    V3 = Tree(tree_list=tree_list_2,
          name='V3',
          switches=get_Slist(3))
    V4 = Tree(tree_list=tree_list_2,
          name='V4',
          switches=get_Slist(4))
    V5 = Tree(tree_list=tree_list_2,
          name='V5',
          switches=get_Slist(5))
    V6 = Tree(tree_list=tree_list_2,
          name='V6',
          switches=get_Slist(6))
    V7 = Tree(tree_list=tree_list_2,
          name='V7',
          switches=get_Slist(7))
    V8 = Tree(tree_list=tree_list_2,
          name='V8',
          switches=get_Slist(8))
    V9 = Tree(tree_list=tree_list_2,
          name='V9',
          switches=get_Slist(9))
    V10 = Tree(tree_list=tree_list_2,
          name='V10',
          switches=get_Slist(10))
    V11 = Tree(tree_list=tree_list_2,
          name='V11',
          switches=get_Slist(11))
    V12 = Tree(tree_list=tree_list_2,
          name='V12',
          switches=get_Slist(12))
    V13 = Tree(tree_list=tree_list_2,
          name='V13',
          switches=get_Slist(13))
    V14 = Tree(tree_list=tree_list_2,
          name='V14',
          switches=get_Slist(14))
    V15 = Tree(tree_list=tree_list_2,
          name='V15',
          switches=get_Slist(15))
    
    Slist_aux = [
    S6, V2,
    S7, V3,
    S8, V4,
    S9, V5,
    S10, V6,
    S11, V7,
    S12, V8,
    S13, V9,
    S14, V10,
    S15, V11,
    S16, V12,
    S17, V13,
    S18, V14,
    S19, V15]

    T0 = Tree(tree_list=['EQU', [None], [None]],
                name='T0',
                switches=[V0, V1])
    T1 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(2), [None]],
                         ['AND'] + [['NAND', Tree.tree_list_NOT, [None]]]*(len(Slist_aux)//2)
                         ],
                name='T1',
                switches=[V0, 1, V1] + Slist_aux)
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[V2])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[V3])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[V4])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[V5])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[V6])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[V7])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[V8])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[V9])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[V10])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[V11])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[V12])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[V13])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[V14])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[V15])
    T16 = Tree(tree_list=['AND',
                          ['EQU', [None], [None]],
                          ['EQU', [None], [None]],
                          ],
                name='T16',
                switches=[V0, 5, V1, 5])

    dx = 1
    dy = 1
    ex = 0.95
    ey = 0.95
    ax1 = 0.5
    ax2 = 0.3
    ay1 = 0.3
    ay2 = 0.4

    R0 = Room(name='R0',
                position=[3*dx, 0*dy, dx+ex, ey],
                switches_list=[S0, S1, S2])
    R1 = Room(name='R1',
                position=[2*dx, 3*dy, 3*dy+ex, 1*ey],
                switches_list=[S3, S4, S5])
    R2 = Room(name='R2',
                position=[1*dx-ax1, 1*dy, ex, ey],
                switches_list=[S6])
    R3 = Room(name='R3',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S7])
    R4 = Room(name='R4',
                position=[0*dx-ax2, 3*dy, ex, ey],
                switches_list=[S8])
    R5 = Room(name='R5',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S9])
    R6 = Room(name='R6',
                position=[1*dx, 5*dy, ex, ey],
                switches_list=[S10])
    R7 = Room(name='R7',
                position=[2*dx, 5*dy+ay1, ex, ey],
                switches_list=[S11])
    R8 = Room(name='R8',
                position=[3*dx, 5*dy+ay2, ex, ey],
                switches_list=[S12])
    R9 = Room(name='R9',
                position=[4*dx, 5*dy+ay2, ex, ey],
                switches_list=[S13])
    R10 = Room(name='R10',
                position=[5*dx, 5*dy+ay1, ex, ey],
                switches_list=[S14])
    R11 = Room(name='R11',
                position=[6*dx, 5*dy, ex, ey],
                switches_list=[S15])
    R12 = Room(name='R12',
                position=[7*dx, 4*dy, ex, ey],
                switches_list=[S16])
    R13 = Room(name='R13',
                position=[7*dx+ax2, 3*dy, ex, ey],
                switches_list=[S17])
    R14 = Room(name='R14',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=[S18])
    R15 = Room(name='R15',
                position=[6*dx+ax1, 1*dy, ex, ey],
                switches_list=[S19])
    RE = Room(name='RE',
              position=[5.8*dx, 0*dy, ex, ey],
              is_exit=True)
    
    def rdc(i):
        p = 0.1
        return [p+i*(1-2*p)/5, 1/2]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(ex/2)/(dx+ex), 1/2],
                relative_arrival_coordinates=[1/6, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[1-1/6, 1/2],
                relative_arrival_coordinates=[(dx+ex/2)/(dx+ex), 1/2])
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rdc(0))
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=rdc(0))
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R4,
                relative_departure_coordinates=rdc(0))
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R5,
                relative_departure_coordinates=rdc(0))
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R6,
                relative_departure_coordinates=rdc(0))
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R1,
                room_arrival=R7,
                relative_departure_coordinates=rdc(1))
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R8,
                relative_departure_coordinates=rdc(2))
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R9,
                relative_departure_coordinates=rdc(3))
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R10,
                relative_departure_coordinates=rdc(4))
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=R11,
                relative_departure_coordinates=rdc(5))
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R1,
                room_arrival=R12,
                relative_departure_coordinates=rdc(5))
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=R13,
                relative_departure_coordinates=rdc(5))
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R1,
                room_arrival=R14,
                relative_departure_coordinates=rdc(5))
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R1,
                room_arrival=R15,
                relative_departure_coordinates=rdc(5))
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[(dx+ex/2)/(dx+ex), (ey)/(dy+ey)])
    
    hu = 0.05
    sa = 0.6
    li = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.BRIGHT_ORANGE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.TOTAL_RED)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution="S1 D0 S3 D4 S8 D4 D6 S10 D6 D8 S12 D8 D10 S14 D10 D12 S16 D12 D14 S18 D14 D1 S0 D0 S3 S4 S5 D9 S13 D9 D15 S19 D15 D1 S0 S1 S2 D0 S3 D1 S0 D16",
                 level_color=lcolor,
                 name='Sieve of Eratosthenes',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level