from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

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
    
    T0 = Tree(tree_list=["INFOREQU", Tree.tree_list_SUM(6), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, 2])
    
    T1 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T1',
                switches=[S0, S1])
    T2 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T2',
                switches=[S1, S2])
    T3 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T3',
                switches=[S2, S3])
    T4 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T4',
                switches=[S1, S4])
    T5 = Tree(tree_list=Tree.tree_list_OR(2),
                name='T5',
                switches=[S1, S5])
    
    T6 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T6',
                switches=[S6, S7, S8, S9, S10, S11])
    
    T7 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T7',
                switches=[S0, S1])
    T8 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T8',
                switches=[S1, S2])
    T9 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T9',
                switches=[S2, S3])
    T10 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T10',
                switches=[S1, S4])
    T11 = Tree(tree_list=Tree.tree_list_NAND(2),
                name='T11',
                switches=[S1, S5])
    
    T12 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T12',
                switches=[S12, S13, S14, S15, S16, S17])

    dx = 1.4
    dy = 1
    ex = dx-0.5
    ey = dy-0.5
    
    ay = 0.1

    R0 = Room(name='R0',
                position=[0*dx, 1*dy-ey-ay, 4*dx+ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5])
    
    R1 = Room(name='R1',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R2 = Room(name='R2',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S7])
    R3 = Room(name='R3',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S8])
    R4 = Room(name='R4',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[S9])
    R5 = Room(name='R5',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S10])
    R6 = Room(name='R6',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S11])
    
    R7 = Room(name='R7',
                position=[3*dx, 4*dy, ex, ey],
                switches_list=[S12])
    R8 = Room(name='R8',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[S13])
    R9 = Room(name='R9',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S14])
    R10 = Room(name='R10',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S15])
    R11 = Room(name='R11',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S16])
    R12 = Room(name='R12',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[S17])
    
    RE = Room(name='RE',
              position=[0*dx, 4*dy+ey+ay, 4*dx+ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R5,
                relative_departure_coordinates=[(ex/2)/(4*dx+ex), 1/2])
    
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
                room_departure=R2,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R6)
    
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R11)
    
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R8,
                room_arrival=R11)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R8,
                room_arrival=R12)
    
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R12,
                room_arrival=RE,
                relative_arrival_coordinates=[(4*dx+ex/2)/(4*dx+ex), 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution="S1 S3 D0 S10 D4 S7 D1 S6 D1 D2 S8 D3 S9 D3 D2 D5 S11 D6 S16 D10 S13 D7 S12 D7 D8 S14 D9 S15 D9 D8 D11 S17 D12",
                 level_color=get_color(),
                 name='Cross graph two dominating set',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.35, sa=0.35, li=0.15)
    lcolor.surroungind_color = Color.color_hls(hu=0.35, sa=1, li=0.8)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor