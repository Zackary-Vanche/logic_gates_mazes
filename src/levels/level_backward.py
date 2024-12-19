from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    tree_list_0 = Tree.tree_list_from_str('TF')
    tree_list_1 = ['AND', ['NOT', [None]], Tree.tree_list_AND(2)]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_1,
              name='T1',
              switches=[S0, S1, S2],
              easy_logical_expression_PN="& ¬ S0 ( & S1 S2 )\n= & ( ¬ S0 S1 S2 )")

    R0 = Room(name='R0',
              position=[3, 2, 2, 2],
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=[0, 1, 2, 2],
              switches_list=[S2])
    RE = Room(name='RE',
              position=[6, 3, 2, 2],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[0, 1/2],
              relative_arrival_coordinates=[0.98, 0.98])
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[0.98, 0.98],
              relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution='S0 D0 S2 D0 S0 S1 D1',
                 level_color=Levels_colors_list.BROWN,
                 name='Backward',
                 door_window_size=350)

    return level