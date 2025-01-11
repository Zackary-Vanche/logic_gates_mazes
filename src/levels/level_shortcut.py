from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
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
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]
    
    def tree_list_aux(n):
        return ['EQU', Tree.tree_list_SUM(n), [None]]

    T0 = Tree(tree_list=['AND',
                         ['EQU', Tree.tree_list_SUM(12), [None]],
                         Tree.tree_list_OR(2),
                         Tree.tree_list_OR(2),
                         tree_list_aux(3),
                         tree_list_aux(3),
                         tree_list_aux(3),
                         tree_list_aux(3),
                         tree_list_aux(2),
                         tree_list_aux(2),
                         ['DIFF', Tree.tree_list_SUM(4), [None]]
                         ],
                name='T0',
                switches=Slist + [7,
                         S0, S1,
                         S0, S2,
                         S1, S3, S4, 2,
                         S2, S3, S5, 2,
                         S4, S6, S7, 2,
                         S5, S6, S8, 2,
                         S7, S9, 2,
                         S8, S9, 2,
                         S3, S4, S5, S6, 2,
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
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[1])

    dx = 11/8
    dy = 1
    ex = 1
    ey = 1
    ay = 0.75

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 12*ex, ey],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[4*dx, 2*dy+ay, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[4*dx, 4*dy+ay, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[6*dx, 2*dy+2*ay, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[6*dx, 4*dy+2*ay, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[8*dx, 2*dy+3*ay, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[8*dx, 4*dy+3*ay, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0*dx, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(2*dx+ex/2)/(12*ex), 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R4)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R3,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R6)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R5,
                room_arrival=R7)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R6,
                room_arrival=R8)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R7,
                room_arrival=R8)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R2,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution="S0 S3 S4 S5 S7 S8 S9 D0 D1 D11",
                 level_color=get_color(),
                 name='Shortut',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.45
    sa = 0.3
    li = 0.7
    lcolor = Level_color(background_color=Color.color_hls(hu, li*0.5 , 0.8*sa),
                         room_color=Color.color_hls(hu, li*0.3, sa),
                         letters_color=Color.WHITE,
                         contour_color=Color.KHAKI,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.KHAKI)
    return lcolor