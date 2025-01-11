from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
import numpy as np

def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    T0 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='T0',
              switches=[S0, S1])
    T1 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='T1',
              switches=[S1, S2])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S2])
    T3 = Tree(tree_list=Tree.tree_list_from_str('FFF'),
              name='T3',
              switches=[S0, S1, S2])

    R0 = Room(name='R0',
              position=[0, 4, 3, 3],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=[4, 0, 3, 3],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=[5, 5, 2, 2],
              switches_list=[S2])
    RE = Room(name='RE',
              position=[3+(1-np.sqrt(2))/2, 3+(1-np.sqrt(2))/2, np.sqrt(2), np.sqrt(2)],
              is_exit=True)  # E pour exit ou end
    
    rp = 0.4

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1/6, 1/6],
              relative_arrival_coordinates=[1/6, 1/6])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=[5/6, 5/6],
              relative_arrival_coordinates=[3/4, 1/4])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp,
              relative_departure_coordinates=[1/4, 3/4],
              relative_arrival_coordinates=[5/6, 5/6])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=RE,
              relative_position=rp,
              relative_departure_coordinates=[1/4, 1/4])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution="S0 D0 S1 D1 S2 D2 S0 D0 S1 D1 S2 D3",
                 level_color=get_color(),
                 name='Bis repetita',
                 border=30,
                 door_window_size=400,
                 keep_proportions=True)

    return level

def get_color():
    return Levels_colors_list.BRIGHT_AND_DARK_BLUE