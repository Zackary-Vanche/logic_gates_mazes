from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists
from Color import Color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    tree_list_1 = Tree.tree_list_from_str('TF')
    
    T0 = Tree(tree_list=tree_list_1,
              name='T0',
              switches=[S0, S1])

    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches=[S0, S2])

    T2 = Tree(tree_list=tree_list_1,
              name='T2',
              switches=[S1, S3])
    T3 = Tree(tree_list=tree_list_1,
              name='T3',
              switches=[S3, S1])
    
    T4 = Tree(tree_list=tree_list_1,
              name='T4',
              switches=[S1, S4])
    T5 = Tree(tree_list=tree_list_1,
              name='T5',
              switches=[S4, S1])

    T6 = Tree(tree_list=tree_list_1,
              name='T6',
              switches=[S2, S4])
    T7 = Tree(tree_list=tree_list_1,
              name='T7',
              switches=[S4, S2])

    T8 = Tree(tree_list=tree_list_1,
              name='T8',
              switches=[S2, S5])
    T9 = Tree(tree_list=tree_list_1,
              name='T9',
              switches=[S5, S2])

    T10 = Tree(tree_list=tree_list_1,
               name='T10',
               switches=[S3, S6])
    T11 = Tree(tree_list=tree_list_1,
               name='T11',
               switches=[S6, S3])

    T12 = Tree(tree_list=tree_list_1,
               name='T12',
               switches=[S4, S6])
    T13 = Tree(tree_list=tree_list_1,
               name='T13',
               switches=[S6, S4])

    T14 = Tree(tree_list=tree_list_1,
               name='T14',
               switches=[S4, S7])
    T15 = Tree(tree_list=tree_list_1,
               name='T15',
               switches=[S7, S4])

    T16 = Tree(tree_list=tree_list_1,
               name='T16',
               switches=[S5, S7])
    T17 = Tree(tree_list=tree_list_1,
               name='T17',
               switches=[S7, S5])

    T18 = Tree(tree_list=Tree.tree_list_AND(3),
               name='T18',
               switches=[S3, S5, S6])

    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
              position=[0, 2, ex, ey],
              switches_list=[S0])
    R1 = Room(name='R1',
                position=[1, 2, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[0, 1, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[2, 2, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[1, 1, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[0, 0, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[2, 1, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[1, 0, ex, ey],
                switches_list=[S7])
    RE = Room(name='RE',
              position=[2, 0, ex, ey],
              is_exit=True)
    
    epsilon = 1/4

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              name='D1',
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=[1, epsilon],
              relative_arrival_coordinates=[0, epsilon])
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R3,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1-epsilon],
              relative_arrival_coordinates=[1, 1-epsilon])
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R1,
              room_arrival=R4,
              relative_departure_coordinates=[epsilon, 1],
              relative_arrival_coordinates=[epsilon, 0])
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R4,
              room_arrival=R1,
              relative_departure_coordinates=[1-epsilon, 0],
              relative_arrival_coordinates=[1-epsilon, 1])
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R2,
              room_arrival=R4,
              relative_departure_coordinates=[1, epsilon],
              relative_arrival_coordinates=[0, epsilon])
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R4,
              room_arrival=R2,
              relative_departure_coordinates=[0, 1-epsilon],
              relative_arrival_coordinates=[1, 1-epsilon])
    D8 = Door(two_way=False,
              tree=T8,
              name='D8',
              room_departure=R2,
              room_arrival=R5,
              relative_departure_coordinates=[epsilon, 1],
              relative_arrival_coordinates=[epsilon, 0])
    D9 = Door(two_way=False,
              tree=T9,
              name='D9',
              room_departure=R5,
              room_arrival=R2,
              relative_departure_coordinates=[1-epsilon, 0],
              relative_arrival_coordinates=[1-epsilon, 1])
    D10 = Door(two_way=False,
               tree=T10,
               name='D10',
               room_departure=R3,
               room_arrival=R6,
               relative_departure_coordinates=[epsilon, 1],
               relative_arrival_coordinates=[epsilon, 0])
    D11 = Door(two_way=False,
               tree=T11,
               name='D11',
               room_departure=R6,
               room_arrival=R3,
               relative_departure_coordinates=[1-epsilon, 0],
               relative_arrival_coordinates=[1-epsilon, 1])
    D12 = Door(two_way=False,
               tree=T12,
               name='D12',
               room_departure=R4,
               room_arrival=R6,
               relative_departure_coordinates=[1, epsilon],
               relative_arrival_coordinates=[0, epsilon])
    D13 = Door(two_way=False,
               tree=T13,
               name='D13',
               room_departure=R6,
               room_arrival=R4,
               relative_departure_coordinates=[0, 1-epsilon],
               relative_arrival_coordinates=[1, 1-epsilon])
    D14 = Door(two_way=False,
               tree=T14,
               name='D14',
               room_departure=R4,
               room_arrival=R7,
               relative_departure_coordinates=[epsilon, 1],
               relative_arrival_coordinates=[epsilon, 0])
    D15 = Door(two_way=False,
               tree=T15,
               name='D15',
               room_departure=R7,
               room_arrival=R4,
               relative_departure_coordinates=[1-epsilon, 0],
               relative_arrival_coordinates=[1-epsilon, 1])
    D16 = Door(two_way=False,
               tree=T16,
               name='D16',
               room_departure=R5,
               room_arrival=R7,
               relative_departure_coordinates=[1, epsilon],
               relative_arrival_coordinates=[0, epsilon])
    D17 = Door(two_way=False,
               tree=T17,
               name='D17',
               room_departure=R7,
               room_arrival=R5,
               relative_departure_coordinates=[0, 1-epsilon],
               relative_arrival_coordinates=[1, 1-epsilon])
    D18 = Door(two_way=False,
               tree=T18,
               name='D18',
               room_departure=R6,
               room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.25, sa=0.3, li=0.3)
    # lcolor.background_color = Color.DARK_GREEN
    lcolor.surrounding_color = Color.BRIGHT_BLUE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18],
                 fastest_solution='S0 D1 S2 D8 S5 D16 S7 D15 S4 D5 S1 D2 S3 D10 S6 D18',
                 level_color=lcolor,
                 name='Meanders',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

