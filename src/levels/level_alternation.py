from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
import numpy as np

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7')
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9')
    
    tree_list_1 = ["AND", Tree.tree_list_XNOR(2), Tree.tree_list_XNOR(2)]
    
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[S0, S5, S5, S6])
    T2 = Tree(tree_list=tree_list_1,
                name='T2',
                switches=[S1, S6, S6, S7])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[S2, S7, S7, S8])
    T4 = Tree(tree_list=tree_list_1,
                name='T4',
                switches=[S3, S8, S8, S9])
    T5 = Tree(tree_list=["AND", Tree.tree_list_XNOR(2), [None]],
                name='T5',
                switches=[S4, S9, S9])
    
    ex = 0.6
    ey = 0.5
    
    def position(i):
        alpha = i*2*np.pi/6
        return [np.cos(alpha), np.sin(alpha), ex, ey]
    
    R0 = Room(name='R0',
                position=[0, 0, ex, ey],
                switches_list=[S0, S1, S2, S3, S4])
    R1 = Room(name='R1',
                position=position(0),
                switches_list=[S5])
    R2 = Room(name='R2',
                position=position(1),
                switches_list=[S6])
    R3 = Room(name='R3',
                position=position(2),
                switches_list=[S7])
    R4 = Room(name='R4',
                position=position(3),
                switches_list=[S8])
    R5 = Room(name='R5',
                position=position(4),
                switches_list=[S9])
    RE = Room(name='RE',
              position=position(5),
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 S2 S4 D0 S5 D1 S6 D2 S7 D3 S8 D4 S9 D5",
                 level_color=get_color(),
                 name='Alternation',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.25
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.2, 0.4),
                         room_color=Color.color_hls(hu, 0.4, 0.4),
                         letters_color=Color.WHITE,
                         contour_color=Color.KHAKI,
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.TOTAL_YELLOW)
    return lcolor