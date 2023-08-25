from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_boolean(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')

    T0 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='T0',
              switches=[S0, S1],
              easy_logical_expression_PN="^ S0 S1\n= | & ¬S0 S1 & S0 ¬S1")
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[S1])

    R0 = Room(name='R0',
                position=[0, 0, 1, 1],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[1, 1.5, 1, 1],
                switches_list=[S1])
    RE = Room(name='RE',
              position=[2, 0, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[0, 1/2])
    
    lcolor=Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.6)
    lcolor.surrounding_color = Color.WHITE
    lcolor.contour_color = Color.WHITE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution="S0 D0 S1 D1",
                 level_color=lcolor,
                 name='Boolean',
                 keep_proportions=True,
                 door_window_size=400)
    
    return level
