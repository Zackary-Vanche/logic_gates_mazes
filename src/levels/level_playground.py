from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f():
    S0 = Switch(name='S0', value=1)

    T0 = Tree(tree_list=Tree.tree_list_NOT,
              name='T0',
              switches=[S0])

    R0 = Room(name='R0',
              position=[1.25, 0, 1, 1],
              switches_list=[S0])
    RE = Room(name='RE',
              position=[0, 1.25, 1, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_position=0.55)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution='S0 D0',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.16, sa=0.5, li=0.51),
                 name='Playground',
                 door_window_size=300,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)

    return level