from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
from random import choice as rd_choice

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]

    T0 = Tree(tree_list=Tree.tree_list_from_str(''.join(rd_choice('TF') for _ in range(len(Slist)))),
                    name='T0',
                    switches=Slist,
                    cut_expression_depth_1=True)
    T1 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T1',
                    switches=[S0, S1])
    T2 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T2',
                    switches=[S1, S2])
    T3 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T3',
                    switches=[S2, S3])
    T4 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T4',
                    switches=[S3, S4])
    T5 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T5',
                    switches=[S4, S5])
    T6 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T6',
                    switches=[S5, S6])
    T7 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T7',
                    switches=[S6, S7])
    T8 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T8',
                    switches=[S7, S8])
    T9 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T9',
                    switches=[S8, S9])
    T10 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T10',
                    switches=[S9, S10])
    T11 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T11',
                    switches=[S0, S2])
    T12 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T12',
                    switches=[S2, S4])
    T13 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T13',
                    switches=[S4, S6])
    T14 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T14',
                    switches=[S6, S8])
    T15 = Tree(tree_list=Tree.tree_list_XOR(2),
                    name='T15',
                    switches=[S8, S10])

    dx = 1
    dy = 5
    ex = 1
    ey = 4

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[5*dx, 0*dy, ex, ey],
                switches_list=[S5])
    R6 = Room(name='R6',
                position=[6*dx, 1*dy, ex, ey],
                switches_list=[S6])
    R7 = Room(name='R7',
                position=[7*dx, 0*dy, ex, ey],
                switches_list=[S7])
    R8 = Room(name='R8',
                position=[8*dx, 1*dy, ex, ey],
                switches_list=[S8])
    R9 = Room(name='R9',
                position=[9*dx, 0*dy, ex, ey],
                switches_list=[S9])
    R10 = Room(name='R10',
                position=[10*dx, 1*dy, ex, ey],
                switches_list=[S10])
    RE = Room(name='RE',
              position=[-1*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=True,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=RE)
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R1)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R5,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R6,
                room_arrival=R7)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R7,
                room_arrival=R8)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R8,
                room_arrival=R9)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R9,
                room_arrival=R10)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R0,
                room_arrival=R2)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R4)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R4,
                room_arrival=R6)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R8)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R8,
                room_arrival=R10)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Town',
                 keep_proportions=True,
                 door_window_size=310,
                 random=True)
    
    # for i, door in enumerate(level.doors_list):
    #     r0 = door.room_departure
    #     r1 = door.room_arrival
    #     if r1.is_exit:
    #         continue
    #     s0, = r0.switches_list
    #     s1, = r1.switches_list
    #     print(f'''    T{i} = Tree(tree_list=Tree.tree_list_XOR(2),
    #                 name='T{i}',
    #                 switches=[{s0.name}, {s1.name}])''')
    
    return level

def get_color():
    hu = 0.1
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.25, sa=0.05),
                         room_color=Color.color_hls(hu, li=0.5, sa=0.05),
                         letters_color=Color.WHITE,
                         contour_color=Color.color_hls(hu, li=0.25, sa=1),
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.color_hls(hu, li=0.25, sa=1))
    return lcolor