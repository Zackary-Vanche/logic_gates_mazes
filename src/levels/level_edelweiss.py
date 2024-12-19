from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from numpy import cos, sin, pi
from Color import Color

def f(fast_solution_finding=False): 

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

    T0 = Tree(tree_list=['AND',
                         ['DIFF', Tree.tree_list_SUM(4), [None]],
                         ['EQU', Tree.tree_list_SUM(10), [None]]] + [['EQU', Tree.tree_list_SUM(3), [None]]]*5,
                name='T0',
                switches=[S1, S2, S3, S4, 3,
                          S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, 5,
                          S0, S1, S5, 2,
                          S1, S2, S6, 2,
                          S2, S3, S7, 1,
                          S3, S4, S8, 2,
                          S4, S0, S9, 1,
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
    T11 = Tree(tree_list=Tree.tree_list_AND(6),
                name='T11',
                switches=[S10, S11, S12, S13, S14, S15])

    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5
    
    def pos(i):
        alpha = i*2*pi/5 + pi*0.05
        return [dx*cos(alpha), dy*sin(alpha), ex, ey]

    R0 = Room(name='R0',
                position=[1.55*dx, -1*dy, 1.25*ex, 5*ey],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9])
    R1 = Room(name='R1',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S10],
                surrounding_color=Color.TOTAL_YELLOW)
    R2 = Room(name='R2',
                position=pos(0),
                switches_list=[S11])
    R3 = Room(name='R3',
                position=pos(1),
                switches_list=[S12])
    R4 = Room(name='R4',
                position=pos(2),
                switches_list=[S13])
    R5 = Room(name='R5',
                position=pos(3),
                switches_list=[S14])
    R6 = Room(name='R6',
                position=pos(4),
                switches_list=[S15])
    RE = Room(name='RE',
              position=[-1.5*dx, -0.5*dy, ex, ey],
              is_exit=True)
    
    if fast_solution_finding:
        for room in [R1, R2, R3, R4, R5, R6]:
            room.possible_switches_values = [[1]]

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R6,
                relative_departure_coordinates=[0.5/1.5, 0.5/5])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                surrounding_color=Color.TOTAL_YELLOW)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3,
                surrounding_color=Color.TOTAL_YELLOW)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4,
                surrounding_color=Color.TOTAL_YELLOW)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R5,
                surrounding_color=Color.TOTAL_YELLOW)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R1,
                room_arrival=R6,
                surrounding_color=Color.TOTAL_YELLOW)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R2,
                room_arrival=R3)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R4)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R5)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R5,
                room_arrival=R6)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R6,
                room_arrival=R2)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.6)
    lcolor.surrounding_color = Color.WHITE
    lcolor.background_color = Color.color_hls(hu=0.4, li=0.1, sa=0.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 uniform_surrounding_colors=False,
                 fastest_solution="S0 S1 S3 S6 S8 D0 S15 D9 S14 D4 S10 D1 S11 D1 D2 S12 D7 S13 D11",
                 level_color=lcolor,
                 name='Edelweiss',
                 keep_proportions=True,
                 door_window_size=340)
    
    return level