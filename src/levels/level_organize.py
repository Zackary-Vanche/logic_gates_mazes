from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[1])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[1])
    T6 = Tree(tree_list=["DIFF",
                         Tree.tree_list_SUM(2),
                         Tree.tree_list_SUM(2),
                         ['SUM', Tree.tree_list_PROD(2), [None]],
                         ['SUM', Tree.tree_list_PROD(2), [None]],
                         [None],
                         Tree.tree_list_SUM(2),
                         ],
                name='T6',
                switches=[S0, 6,
                          S0, 7,
                          3, S1, 2,
                          3, S1, 5,
                          S2,
                          S2, 1,
                          ],
                cut_expression_depth_1=True)
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S0])

    dx = 2
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, 3.5*dy+ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R2 = Room(name='R2',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S2])
    R4 = Room(name='R4',
                position=[2*dx, 0*dy, ex, 3.5*dy+ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[1*dx, 3*dy, ex, ey],
              is_exit=True)

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
                room_departure=R0,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R1,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[1, 1])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution="D2 S2 D5 D6 D1 S1 D4 D6 D0 S0 D3 D6 D7",
                 level_color=get_color(),
                 name='Organize',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.1, sa=0.25, li=0.6)
    lcolor.surrounding_color = [255, 255, 255]
    return lcolor