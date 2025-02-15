from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice

current_folder = '/'.join(__file__.split('\\')[:-1])

def aux(one_way_door_index): 

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
    
    T0 = Tree(tree_list=["INFOREQU", Tree.tree_list_SUM(12), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, 6])
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
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S10])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S11])
    T13 = Tree(tree_list=Tree.tree_list_AND(7),
                name='T13',
                switches=[S12, S13, S14, S15, S16, S17, S18])

    dx = 1
    dy = 1
    ex = 0.3
    ey = 0.3
    
    r = 1

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, dx, dy],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    R1 = Room(name='R1',
                position=[1.5*dx, 0*dy, ex, ey],
                switches_list=[S12],
                possible_switches_values=[[1]])
    R2 = Room(name='R2',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S13],
                possible_switches_values=[[1]])
    R3 = Room(name='R3',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S14],
                possible_switches_values=[[1]])
    R4 = Room(name='R4',
                position=[0*dx, 1.5*dy, ex, ey],
                switches_list=[S15],
                possible_switches_values=[[1]])
    R5 = Room(name='R5',
                position=[3*dx, 1.5*dy, ex, ey],
                switches_list=[S16],
                possible_switches_values=[[1]])
    R6 = Room(name='R6',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S17],
                possible_switches_values=[[1]])
    R7 = Room(name='R7',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S18],
                possible_switches_values=[[1]])
    RE = Room(name='RE',
              position=[3*dx-r+ex, 0*dy, r, r],
              is_exit=True)
    
    

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(dx-ex/2)/dx, ey/2/dy])
    ###############################
    Rl = [R1, R2]
    rd_shuffle(Rl)
    D1 = Door(two_way=not 0 in one_way_door_index,
                tree=T1,
                name='D1',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R1, R3]
    rd_shuffle(Rl)
    D2 = Door(two_way=not 1 in one_way_door_index,
                tree=T2,
                name='D2',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R3]
    rd_shuffle(Rl)
    D3 = Door(two_way=not 2 in one_way_door_index,
                tree=T3,
                name='D3',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R4]
    rd_shuffle(Rl)
    D4 = Door(two_way=not 3 in one_way_door_index,
                tree=T4,
                name='D4',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R6]
    rd_shuffle(Rl)
    D5 = Door(two_way=not 4 in one_way_door_index,
                tree=T5,
                name='D5',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R7]
    rd_shuffle(Rl)
    D6 = Door(two_way=not 5 in one_way_door_index,
                tree=T6,
                name='D6',
                room_departure=Rl[0],
                room_arrival=Rl[1],
                relative_position=0.35)
    Rl = [R3, R5]
    rd_shuffle(Rl)
    D7 = Door(two_way=not 6 in one_way_door_index,
                tree=T7,
                name='D7',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R3, R6]
    rd_shuffle(Rl)
    D8 = Door(two_way=not 7 in one_way_door_index,
                tree=T8,
                name='D8',
                room_departure=Rl[0],
                room_arrival=Rl[1],
                relative_position=0.35)
    Rl = [R3, R7]
    rd_shuffle(Rl)
    D9 = Door(two_way=not 8 in one_way_door_index,
                tree=T9,
                name='D9',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R4, R6]
    rd_shuffle(Rl)
    D10 = Door(two_way=not 9 in one_way_door_index,
                tree=T10,
                name='D10',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R5, R7]
    rd_shuffle(Rl)
    D11 = Door(two_way=not 10 in one_way_door_index,
                tree=T11,
                name='D11',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R6, R7]
    rd_shuffle(Rl)
    D12 = Door(two_way=not 11 in one_way_door_index,
                tree=T12,
                name='D12',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    ###############################
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R1,
                room_arrival=RE,
                relative_arrival_coordinates=[1/3, ey/2/dy])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Rising sun',
                 keep_proportions=True,
                 door_window_size=310,
                 random=True)
        
    return level

def f():
    
    one_way_door_index = rd_choice([
         (0, 2, 3, 4, 6, 7),
         (0, 2, 3, 4, 6, 8),
         (0, 2, 3, 4, 6, 11),
         (0, 2, 3, 4, 7, 8),
         (0, 2, 3, 4, 7, 10),
         (0, 2, 3, 4, 8, 10),
         (0, 2, 3, 4, 8, 11),
         (0, 2, 3, 4, 10, 11),
         (0, 2, 3, 5, 6, 7),
         (0, 2, 3, 5, 6, 8),
         (0, 2, 3, 5, 6, 11),
         (0, 2, 3, 5, 7, 8),
         (0, 2, 3, 5, 7, 10),
         (0, 2, 3, 5, 8, 10),
         (0, 2, 3, 5, 8, 11),
         (0, 2, 3, 5, 10, 11),
         (0, 2, 3, 6, 7, 11),
         (0, 2, 3, 6, 8, 11),
         (0, 2, 3, 7, 8, 11),
         (0, 2, 3, 7, 10, 11),
         (0, 2, 3, 8, 10, 11),
         (0, 2, 4, 5, 6, 7),
         (0, 2, 4, 5, 6, 8),
         (0, 2, 4, 5, 6, 11),
         (0, 2, 4, 5, 7, 8),
         (0, 2, 4, 5, 7, 10),
         (0, 2, 4, 5, 8, 10),
         (0, 2, 4, 5, 8, 11),
         (0, 2, 4, 5, 10, 11),
         (0, 2, 4, 6, 7, 9),
         (0, 2, 4, 6, 7, 11),
         (0, 2, 4, 6, 8, 9),
         (0, 2, 4, 6, 8, 11),
         (0, 2, 4, 6, 9, 11),
         (0, 2, 4, 7, 8, 9),
         (0, 2, 4, 7, 8, 11),
         (0, 2, 4, 7, 9, 10),
         (0, 2, 4, 7, 10, 11),
         (0, 2, 4, 8, 9, 10),
         (0, 2, 4, 8, 9, 11),
         (0, 2, 4, 8, 10, 11),
         (0, 2, 4, 9, 10, 11),
         (0, 2, 5, 6, 7, 9),
         (0, 2, 5, 6, 8, 9),
         (0, 2, 5, 6, 9, 11),
         (0, 2, 5, 7, 8, 9),
         (0, 2, 5, 7, 9, 10),
         (0, 2, 5, 8, 9, 10),
         (0, 2, 5, 8, 9, 11),
         (0, 2, 5, 9, 10, 11),
         (0, 2, 6, 7, 9, 11),
         (0, 2, 6, 8, 9, 11),
         (0, 2, 7, 8, 9, 11),
         (0, 2, 7, 9, 10, 11),
         (0, 2, 8, 9, 10, 11),
         (0, 3, 4, 5, 6, 7),
         (0, 3, 4, 5, 6, 8),
         (0, 3, 4, 5, 6, 11),
         (0, 3, 4, 5, 7, 8),
         (0, 3, 4, 5, 7, 10),
         (0, 3, 4, 5, 8, 10),
         (0, 3, 4, 5, 8, 11),
         (0, 3, 4, 5, 10, 11),
         (0, 3, 4, 6, 7, 8),
         (0, 3, 4, 6, 8, 11),
         (0, 3, 4, 7, 8, 10),
         (0, 3, 4, 8, 10, 11),
         (0, 3, 5, 6, 7, 8),
         (0, 3, 5, 6, 7, 11),
         (0, 3, 5, 7, 8, 10),
         (0, 3, 5, 7, 8, 11),
         (0, 3, 5, 7, 10, 11),
         (0, 3, 6, 7, 8, 11),
         (0, 3, 7, 8, 10, 11),
         (0, 4, 5, 6, 7, 8),
         (0, 4, 5, 6, 7, 9),
         (0, 4, 5, 6, 7, 11),
         (0, 4, 5, 6, 8, 9),
         (0, 4, 5, 6, 9, 11),
         (0, 4, 5, 7, 8, 9),
         (0, 4, 5, 7, 8, 10),
         (0, 4, 5, 7, 8, 11),
         (0, 4, 5, 7, 9, 10),
         (0, 4, 5, 7, 10, 11),
         (0, 4, 5, 8, 9, 10),
         (0, 4, 5, 8, 9, 11),
         (0, 4, 5, 9, 10, 11),
         (0, 4, 6, 7, 8, 9),
         (0, 4, 6, 7, 8, 11),
         (0, 4, 6, 8, 9, 11),
         (0, 4, 7, 8, 9, 10),
         (0, 4, 7, 8, 10, 11),
         (0, 4, 8, 9, 10, 11),
         (0, 5, 6, 7, 8, 9),
         (0, 5, 6, 7, 9, 11),
         (0, 5, 7, 8, 9, 10),
         (0, 5, 7, 8, 9, 11),
         (0, 5, 7, 9, 10, 11),
         (0, 6, 7, 8, 9, 11),
         (0, 7, 8, 9, 10, 11),
         (1, 2, 3, 4, 6, 7),
         (1, 2, 3, 4, 6, 8),
         (1, 2, 3, 4, 6, 11),
         (1, 2, 3, 4, 7, 8),
         (1, 2, 3, 4, 7, 10),
         (1, 2, 3, 4, 8, 10),
         (1, 2, 3, 4, 8, 11),
         (1, 2, 3, 4, 10, 11),
         (1, 2, 3, 5, 6, 7),
         (1, 2, 3, 5, 6, 8),
         (1, 2, 3, 5, 6, 11),
         (1, 2, 3, 5, 7, 8),
         (1, 2, 3, 5, 7, 10),
         (1, 2, 3, 5, 8, 10),
         (1, 2, 3, 5, 8, 11),
         (1, 2, 3, 5, 10, 11),
         (1, 2, 3, 6, 7, 11),
         (1, 2, 3, 6, 8, 11),
         (1, 2, 3, 7, 8, 11),
         (1, 2, 3, 7, 10, 11),
         (1, 2, 3, 8, 10, 11),
         (1, 2, 4, 5, 6, 7),
         (1, 2, 4, 5, 6, 8),
         (1, 2, 4, 5, 6, 11),
         (1, 2, 4, 5, 7, 8),
         (1, 2, 4, 5, 7, 10),
         (1, 2, 4, 5, 8, 10),
         (1, 2, 4, 5, 8, 11),
         (1, 2, 4, 5, 10, 11),
         (1, 2, 4, 6, 7, 9),
         (1, 2, 4, 6, 7, 11),
         (1, 2, 4, 6, 8, 9),
         (1, 2, 4, 6, 8, 11),
         (1, 2, 4, 6, 9, 11),
         (1, 2, 4, 7, 8, 9),
         (1, 2, 4, 7, 8, 11),
         (1, 2, 4, 7, 9, 10),
         (1, 2, 4, 7, 10, 11),
         (1, 2, 4, 8, 9, 10),
         (1, 2, 4, 8, 9, 11),
         (1, 2, 4, 8, 10, 11),
         (1, 2, 4, 9, 10, 11),
         (1, 2, 5, 6, 7, 9),
         (1, 2, 5, 6, 8, 9),
         (1, 2, 5, 6, 9, 11),
         (1, 2, 5, 7, 8, 9),
         (1, 2, 5, 7, 9, 10),
         (1, 2, 5, 8, 9, 10),
         (1, 2, 5, 8, 9, 11),
         (1, 2, 5, 9, 10, 11),
         (1, 2, 6, 7, 9, 11),
         (1, 2, 6, 8, 9, 11),
         (1, 2, 7, 8, 9, 11),
         (1, 2, 7, 9, 10, 11),
         (1, 2, 8, 9, 10, 11),
         (1, 3, 4, 5, 6, 7),
         (1, 3, 4, 5, 6, 8),
         (1, 3, 4, 5, 6, 11),
         (1, 3, 4, 5, 7, 8),
         (1, 3, 4, 5, 7, 10),
         (1, 3, 4, 5, 8, 10),
         (1, 3, 4, 5, 8, 11),
         (1, 3, 4, 5, 10, 11),
         (1, 3, 4, 6, 7, 8),
         (1, 3, 4, 6, 8, 11),
         (1, 3, 4, 7, 8, 10),
         (1, 3, 4, 8, 10, 11),
         (1, 3, 5, 6, 7, 8),
         (1, 3, 5, 6, 7, 11),
         (1, 3, 5, 7, 8, 10),
         (1, 3, 5, 7, 8, 11),
         (1, 3, 5, 7, 10, 11),
         (1, 3, 6, 7, 8, 11),
         (1, 3, 7, 8, 10, 11),
         (1, 4, 5, 6, 7, 8),
         (1, 4, 5, 6, 7, 9),
         (1, 4, 5, 6, 7, 11),
         (1, 4, 5, 6, 8, 9),
         (1, 4, 5, 6, 9, 11),
         (1, 4, 5, 7, 8, 9),
         (1, 4, 5, 7, 8, 10),
         (1, 4, 5, 7, 8, 11),
         (1, 4, 5, 7, 9, 10),
         (1, 4, 5, 7, 10, 11),
         (1, 4, 5, 8, 9, 10),
         (1, 4, 5, 8, 9, 11),
         (1, 4, 5, 9, 10, 11),
         (1, 4, 6, 7, 8, 9),
         (1, 4, 6, 7, 8, 11),
         (1, 4, 6, 8, 9, 11),
         (1, 4, 7, 8, 9, 10),
         (1, 4, 7, 8, 10, 11),
         (1, 4, 8, 9, 10, 11),
         (1, 5, 6, 7, 8, 9),
         (1, 5, 6, 7, 9, 11),
         (1, 5, 7, 8, 9, 10),
         (1, 5, 7, 8, 9, 11),
         (1, 5, 7, 9, 10, 11),
         (1, 6, 7, 8, 9, 11),
         (1, 7, 8, 9, 10, 11),
         (2, 3, 4, 5, 6, 7),
         (2, 3, 4, 5, 6, 8),
         (2, 3, 4, 5, 6, 11),
         (2, 3, 4, 5, 7, 8),
         (2, 3, 4, 5, 7, 10),
         (2, 3, 4, 5, 8, 10),
         (2, 3, 4, 5, 8, 11),
         (2, 3, 4, 5, 10, 11),
         (2, 3, 4, 6, 7, 8),
         (2, 3, 4, 6, 8, 11),
         (2, 3, 4, 7, 8, 10),
         (2, 3, 4, 8, 10, 11),
         (2, 3, 5, 6, 7, 8),
         (2, 3, 5, 6, 7, 11),
         (2, 3, 5, 7, 8, 10),
         (2, 3, 5, 7, 8, 11),
         (2, 3, 5, 7, 10, 11),
         (2, 3, 6, 7, 8, 11),
         (2, 3, 7, 8, 10, 11),
         (2, 4, 5, 6, 7, 8),
         (2, 4, 5, 6, 7, 9),
         (2, 4, 5, 6, 7, 11),
         (2, 4, 5, 6, 8, 9),
         (2, 4, 5, 6, 9, 11),
         (2, 4, 5, 7, 8, 9),
         (2, 4, 5, 7, 8, 10),
         (2, 4, 5, 7, 8, 11),
         (2, 4, 5, 7, 9, 10),
         (2, 4, 5, 7, 10, 11),
         (2, 4, 5, 8, 9, 10),
         (2, 4, 5, 8, 9, 11),
         (2, 4, 5, 9, 10, 11),
         (2, 4, 6, 7, 8, 9),
         (2, 4, 6, 7, 8, 11),
         (2, 4, 6, 8, 9, 11),
         (2, 4, 7, 8, 9, 10),
         (2, 4, 7, 8, 10, 11),
         (2, 4, 8, 9, 10, 11),
         (2, 5, 6, 7, 8, 9),
         (2, 5, 6, 7, 9, 11),
         (2, 5, 7, 8, 9, 10),
         (2, 5, 7, 8, 9, 11),
         (2, 5, 7, 9, 10, 11),
         (2, 6, 7, 8, 9, 11),
         (2, 7, 8, 9, 10, 11)])
    level = aux(one_way_door_index)
    
    try:
        initial_try = tuple([f"S{i}" for i in range(12) if not i in one_way_door_index])
        # print(initial_try)
        sol = level.find_all_solutions(initial_try=initial_try, stop_at_first_solution=True)
        level.fastest_solution = ' '.join(sol[0][0])
        # print(level.fastest_solution)
    except:
        print(one_way_door_index)
        raise
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.125, sa=0.4, li=0.2)
    lcolor.background_color = Color.color_hls(hu=0.025, sa=0.4, li=0.2)
    lcolor.surrounding_color = Color.color_hls(hu=0.15, sa=1, li=0.6)
    return lcolor