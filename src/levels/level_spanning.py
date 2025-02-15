from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from random import shuffle as rd_shuffle

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
    
    T0 = Tree(tree_list=["INFOREQU", Tree.tree_list_SUM(5), [None]],
                name='T0',
                switches=[S0, S1, S2, S3, S4, 3])
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
    T6 = Tree(tree_list=Tree.tree_list_AND(4),
                name='T6',
                switches=[S5, S6, S7, S8])

    dx = 1
    dy = 1
    ex = 0.7
    ey = 0.7

    R0 = Room(name='R0',
                position=[2*dx, 0*dy, ex, ex],
                switches_list=[S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S5])
    R2 = Room(name='R2',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S6])
    R3 = Room(name='R3',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S7])
    R4 = Room(name='R4',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S8])
    RE = Room(name='RE',
              position=[2*dx, 1*dy, ex, ey],
              is_exit=True)
    
    one_way_door_index = rd_choice([[0, 1],
                                    [0, 2],
                                    # 0 3
                                    [0, 4],
                                    [1, 2],
                                    [1, 3],
                                    [1, 4],
                                    [2, 3],
                                    # 2 4
                                    [3, 4]])

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
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
    Rl = [R1, R4]
    rd_shuffle(Rl)
    D3 = Door(two_way=not 2 in one_way_door_index,
                tree=T3,
                name='D3',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R2, R3]
    rd_shuffle(Rl)
    D4 = Door(two_way=not 3 in one_way_door_index,
                tree=T4,
                name='D4',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    Rl = [R3, R4]
    rd_shuffle(Rl)
    D5 = Door(two_way=not 4 in one_way_door_index,
                tree=T5,
                name='D5',
                room_departure=Rl[0],
                room_arrival=Rl[1])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Spanning',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)

    initial_try = tuple([f"S{i}" for i in range(5) if not i in one_way_door_index])
    # print(initial_try)
    sol = level.find_all_solutions(initial_try=initial_try, stop_at_first_solution=True)
    level.fastest_solution = ' '.join(sol[0][0])
    # print(level.fastest_solution)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.5, sa=0.35, li=0.25)