from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists

current_folder = '/'.join(__file__.split('\\')[:-1])

def aux(door_directions_list): 

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
    
    T0 = Tree(tree_list=["AND",
                         ["EQU", Tree.tree_list_SUM(10), [None]],
                         ] + [["EQU", Tree.tree_list_SUM(4), [None]]]*5,
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, 5,
                          S0, S1, S2, S3, 2,
                          S0, S4, S5, S6, 2,
                          S1, S4, S7, S8, 2,
                          S2, S5, S7, S9, 2,
                          S3, S6, S8, S9, 2,
                          ],
                cut_expression_depth_1=True)
    
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S0])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[S1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[S2])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S3])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S4])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S5])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S6])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S7])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S8])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S9])
    
    T11 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T11',
                switches=[S10, S11, S12, S13, S14])
    
    T12 = Tree(tree_list=Tree.tree_list_NOT,
                name='T12',
                switches=[S0])
    T13 = Tree(tree_list=Tree.tree_list_NOT,
                name='T13',
                switches=[S1])
    T14 = Tree(tree_list=Tree.tree_list_NOT,
                name='T14',
                switches=[S2])
    T15 = Tree(tree_list=Tree.tree_list_NOT,
                name='T15',
                switches=[S3])
    T16 = Tree(tree_list=Tree.tree_list_NOT,
                name='T16',
                switches=[S4])
    T17 = Tree(tree_list=Tree.tree_list_NOT,
                name='T17',
                switches=[S5])
    T18 = Tree(tree_list=Tree.tree_list_NOT,
                name='T18',
                switches=[S6])
    T19 = Tree(tree_list=Tree.tree_list_NOT,
                name='T19',
                switches=[S7])
    T20 = Tree(tree_list=Tree.tree_list_NOT,
                name='T20',
                switches=[S8])
    T21 = Tree(tree_list=Tree.tree_list_NOT,
                name='T21',
                switches=[S9])
    
    T22 = Tree(tree_list=Tree.tree_list_AND(5),
                name='T22',
                switches=[S15, S16, S17, S18, S19])

    ex = 3
    ey = 3
    dx = 4
    dy = 6
    ax = ex+0.1
    dx0 = -1*dx-ax
    ex0 = 3*dx+ex-dx0
    ey0 = ex0/10
    dy0 = (ey-ey0)/2

    R0 = Room(name='R0',
                position=[dx0, dy0, ex0, ey0],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S10])
    R2 = Room(name='R2',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R3 = Room(name='R3',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S12])
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S13])
    R5 = Room(name='R5',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[S14])
    
    
    R6 = Room(name='R6',
                position=[-1*dx-ax, 1*dy, ex, ey],
                switches_list=[S15])
    R7 = Room(name='R7',
                position=[0*dx-ax, 2*dy, ex, ey],
                switches_list=[S16])
    R8 = Room(name='R8',
                position=[-1*dx-ax, 3*dy, ex, ey],
                switches_list=[S17])
    R9 = Room(name='R9',
                position=[-3*dx-ax, 2*dy, ex, ey],
                switches_list=[S18])
    R10 = Room(name='R10',
                position=[-3*dx-ax, 1*dy, ex, ey],
                switches_list=[S19])
    RE = Room(name='RE',
              position=[-3*dx-ax, dy0, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    
    Rl1 = [R1, R2]
    if door_directions_list[0]:
        Rl1 = Rl1[::-1]     
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=Rl1[0],
                room_arrival=Rl1[1])
    Rl2 = [R1, R3]
    if door_directions_list[1]:
        Rl2 = Rl2[::-1]     
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=Rl2[0],
                room_arrival=Rl2[1])
    Rl3 = [R1, R4]
    if door_directions_list[2]:
        Rl3 = Rl3[::-1]     
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=Rl3[0],
                room_arrival=Rl3[1])
    Rl4 = [R1, R5]
    if door_directions_list[3]:
        Rl4 = Rl4[::-1]     
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=Rl4[0],
                room_arrival=Rl4[1])
    Rl5 = [R2, R3]
    if door_directions_list[4]:
        Rl5 = Rl5[::-1]     
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=Rl5[0],
                room_arrival=Rl5[1])
    Rl6 = [R2, R4]
    if door_directions_list[5]:
        Rl6 = Rl6[::-1]     
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=Rl6[0],
                room_arrival=Rl6[1])
    Rl7 = [R2, R5]
    if door_directions_list[6]:
        Rl7 = Rl7[::-1]     
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=Rl7[0],
                room_arrival=Rl7[1])
    Rl8 = [R3, R4]
    if door_directions_list[7]:
        Rl8 = Rl8[::-1]     
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=Rl8[0],
                room_arrival=Rl8[1])
    Rl9 = [R3, R5]
    if door_directions_list[8]:
        Rl9 = Rl9[::-1]     
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=Rl9[0],
                room_arrival=Rl9[1])
    Rl10 = [R4, R5]
    if door_directions_list[9]:
        Rl10 = Rl10[::-1]     
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=Rl10[0],
                room_arrival=Rl10[1])
    
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=R6)
    
    Rl12 = [R6, R7]
    if door_directions_list[0]:
        Rl12 = Rl12[::-1]     
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=Rl12[0],
                room_arrival=Rl12[1])
    Rl13 = [R6, R8]
    if door_directions_list[1]:
        Rl13 = Rl13[::-1]     
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=Rl13[0],
                room_arrival=Rl13[1])
    Rl14 = [R6, R9]
    if door_directions_list[2]:
        Rl14 = Rl14[::-1]     
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=Rl14[0],
                room_arrival=Rl14[1])
    Rl15 = [R6, R10]
    if door_directions_list[3]:
        Rl15 = Rl15[::-1]     
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=Rl15[0],
                room_arrival=Rl15[1])
    Rl16 = [R7, R8]
    if door_directions_list[4]:
        Rl16 = Rl16[::-1]     
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=Rl16[0],
                room_arrival=Rl16[1])
    Rl17 = [R7, R9]
    if door_directions_list[5]:
        Rl17 = Rl17[::-1]     
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=Rl17[0],
                room_arrival=Rl17[1])
    Rl18 = [R7, R10]
    if door_directions_list[6]:
        Rl18 = Rl18[::-1]     
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=Rl18[0],
                room_arrival=Rl18[1])
    Rl19 = [R8, R9]
    if door_directions_list[7]:
        Rl19 = Rl19[::-1]     
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=Rl19[0],
                room_arrival=Rl19[1])
    Rl20 = [R8, R10]
    if door_directions_list[8]:
        Rl20 = Rl20[::-1]     
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=Rl20[0],
                room_arrival=Rl20[1])
    Rl21 = [R9, R10]
    if door_directions_list[9]:
        Rl21 = Rl21[::-1]     
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=Rl21[0],
                room_arrival=Rl21[1])
    
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R6,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='K5 eulerian circuit',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    
    filename = current_folder+'/k5_eulerian_circuit_door_directions_list.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            door_directions_list = rd_choice(lines).replace('\n', '')
            door_directions_list = [int(i) for i in door_directions_list]
    #                       0  1  2  3  4  5  6  7  8  9  10
    # door_directions_list = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
    
    return aux(door_directions_list)

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.65, sa=0.2, li=0.25)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor