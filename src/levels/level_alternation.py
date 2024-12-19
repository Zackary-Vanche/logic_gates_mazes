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
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=1)
    S4 = Switch(name='S4')
    
    tree_list_0 = Tree.tree_list_XNOR(2)
    
    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_0,
                name='T1',
                switches=[S1, S2])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[S2, S3])
    T3 = Tree(tree_list=tree_list_0,
                name='T3',
                switches=[S3, S4])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S4])
    
    def position(i):
        alpha = i*2*np.pi/6
        return [np.cos(alpha), np.sin(alpha), 0.5, 0.5]

    R0 = Room(name='R0',
                position=position(0),
                switches_list=[S0])
    R1 = Room(name='R1',
                position=position(1),
                switches_list=[S1])
    R2 = Room(name='R2',
                position=position(2),
                switches_list=[S2])
    R3 = Room(name='R3',
                position=position(3),
                switches_list=[S3])
    R4 = Room(name='R4',
                position=position(4),
                switches_list=[S4])
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
                room_arrival=RE)
    
    hu = 0.25
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.2, 0.4),
                         room_color=Color.color_hls(hu, 0.4, 0.4),
                         letters_color=Color.WHITE,
                         contour_color=Color.KHAKI,
                         inside_room_color=Color.BLACK,
                         surrounding_color=Color.TOTAL_YELLOW)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 D0 S1 D1 S2 D2 S3 D3 S4 D4",
                 level_color=lcolor,
                 name='Alternation',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level