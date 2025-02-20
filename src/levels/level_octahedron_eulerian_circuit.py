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
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11,
             S12, S13, S14, S15, S16, S17,
             S18, S19, S20, S21, S22, S23]

    dx = 1
    dy = 1
    ex = 1
    ey = 1
    epsilony = 0.5
    ax = 2
    dx0 = -1*dx-ax
    ex0 = 4*dx+ex-dx0
    ey0 = ex0/12
    dy0 = (ey-ey0)/2-2*dy
    
    R0 = Room(name='R0',
                position=[dx0, dy0, ex0, ey0],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S12])
    R2 = Room(name='R2',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S13])
    R3 = Room(name='R3',
                position=[4*dx, 4*dy, ex, ey],
                switches_list=[S14])
    R4 = Room(name='R4',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S15])
    R5= Room(name='R5',
                position=[2*dx, 1.5*dy-epsilony, ex, ey],
                switches_list=[S16])
    R6 = Room(name='R6',
                position=[2*dx, 2.5*dy+epsilony, ex, ey],
                switches_list=[S17])

    R7 = Room(name='R7',
                position=[0*dx-ax, 0*dy, ex, ey],
                switches_list=[S18])
    R8 = Room(name='R8',
                position=[-4*dx-ax, 0*dy, ex, ey],
                switches_list=[S19])
    R9 = Room(name='R9',
                position=[-4*dx-ax, 4*dy, ex, ey],
                switches_list=[S20])
    R10 = Room(name='R10',
                position=[0*dx-ax, 4*dy, ex, ey],
                switches_list=[S21])
    R11 = Room(name='R11',
                position=[-2*dx-ax, 1.5*dy-epsilony, ex, ey],
                switches_list=[S22])
    R12 = Room(name='R12',
                position=[-2*dx-ax, 2.5*dy+epsilony, ex, ey],
                switches_list=[S23])
    RE = Room(name='RE',
              position=[-4*dx-ax, dy0, ex, ey],
              is_exit=True)
    
    Dl = []
    
    #                0  1  2  3  4  5  6  7  8  9 10 11
    Rd_index_list = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]
    Ra_index_list = [1, 3, 4, 5, 2, 4, 5, 3, 4, 5, 4, 5]
    
    Rl = [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, RE]
    
    # 0
    D0 = Door(two_way=False,
              tree=Tree(tree_list=["AND",
                                   ["EQU", Tree.tree_list_SUM(12), [None]],
                                   ] + [["EQU", Tree.tree_list_SUM(4), [None]]]*6,
                        name='T0',
                        switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, 6,
                                  S0, S1, S2, S3, 2,
                                  S0, S4, S5, S6, 2,
                                  S4, S7, S8, S9, 2,
                                  S1, S7, S10, S11, 2,
                                  S2, S5, S8, S10, 2,
                                  S3, S6, S9, S11, 2,],
                        cut_expression_depth_1=True),
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    Dl.append(D0)
    # 1 -> 12
    for iD in range(1, 12+1):
        iS = iD-1
        iRd = Rd_index_list[iS]+1
        iRa = Ra_index_list[iS]+1
        if door_directions_list[iS]:
            iRd, iRa = iRa, iRd
        D = Door(two_way=False,
                 tree=Tree(tree_list=[None],
                           name=f'T{iD}',
                           switches=[Slist[iS]]),
                 name=f'D{iD}',
                 room_departure=Rl[iRd],
                 room_arrival=Rl[iRa])
        Dl.append(D)
    # 13
    D13 = Door(two_way=False,
               tree=Tree(tree_list=Tree.tree_list_AND(6),
                         name='T13',
                         switches=[S12, S13, S14, S15, S16, S17]),
               name='D13',
               room_departure=R1,
               room_arrival=R7)
    Dl.append(D13)
    # 14 -> 25
    # 1 -> 12
    for iD in range(14, 25+1):
        iS = iD-14
        iRd = Rd_index_list[iS]+7
        iRa = Ra_index_list[iS]+7
        if door_directions_list[iS]:
            iRd, iRa = iRa, iRd
        D = Door(two_way=False,
                 tree=Tree(tree_list=Tree.tree_list_NOT,
                           name=f'T{iD}',
                           switches=[Slist[iS]]),
                 name=f'D{iD}',
                 room_departure=Rl[iRd],
                 room_arrival=Rl[iRa])
        Dl.append(D)
    # 26
    D26 = Door(two_way=False,
               tree=Tree(tree_list=Tree.tree_list_AND(6),
                         name='T26',
                         switches=[S18, S19, S20, S21, S22, S23]),
               name='D26',
               room_departure=R7,
               room_arrival=RE)
    Dl.append(D26)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=Rl,
                 doors_list=Dl,
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Octahedron eulerian circuit',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level

def f():
    
    filename = current_folder+'/octahedron_eulerian_circuit_door_directions_list.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            door_directions_list = rd_choice(lines).replace('\n', '')
            door_directions_list = [int(i) for i in door_directions_list]
    #door_directions_list = [0 for i in range(12)]
    
    return aux(door_directions_list)

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.8, sa=0.2, li=0.25)
    lcolor.background_color, lcolor.room_color = lcolor.room_color, lcolor.background_color
    return lcolor