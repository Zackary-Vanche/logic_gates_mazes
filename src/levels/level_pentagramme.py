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
    
    T0 = Tree(tree_list=["EQU", Tree.tree_list_SUM(10), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, 5])
    
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

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[-1*dx-ex, 0*dy, 3*dx+3*ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S10])
    R2 = Room(name='R2',
                position=[-1*dx, 2*dy, ex, ey],
                switches_list=[S11])
    R3 = Room(name='R3',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S12])
    R4 = Room(name='R4',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S13])
    R5 = Room(name='R5',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S14])
    RE = Room(name='RE',
              position=[-1*dx, 1*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    
    Rl = [R1, R2]
    if door_directions_list[0]:
        Rl = Rl[::-1]
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R1, R3]
    if door_directions_list[1]:
        Rl = Rl[::-1]
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R1, R4]
    if door_directions_list[2]:
        Rl = Rl[::-1]
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R1, R5]
    if door_directions_list[3]:
        Rl = Rl[::-1]
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R3]
    if door_directions_list[4]:
        Rl = Rl[::-1]
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R4]
    if door_directions_list[5]:
        Rl = Rl[::-1]
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R5]
    if door_directions_list[6]:
        Rl = Rl[::-1]
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R3, R4]
    if door_directions_list[7]:
        Rl = Rl[::-1]
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=Rl[0],
                room_arrival=Rl[1],
                relative_position=0.35)
    Rl = [R3, R5]
    if door_directions_list[8]:
        Rl = Rl[::-1]
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R4, R5]
    if door_directions_list[9]:
        Rl = Rl[::-1]
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=Rl[0],
                room_arrival=Rl[1])

    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Pentagramme',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    
    filename = current_folder+'/pentagramme_door_directions_list.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            door_directions_list = rd_choice(lines).replace('\n', '')
            door_directions_list = [int(i) for i in door_directions_list]
    
    # door_directions_list = [0 for i in range(10)]
    
    return aux(door_directions_list)

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.05, sa=0.2, li=0.25)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor