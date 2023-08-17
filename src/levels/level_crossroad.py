from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_crossroad():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    tree_list_0 = [None]  # S0
    tree_list_1 = [None]  # S1
    tree_list_2 = [None]  # S2
    tree_list_3 = [None]  # S3
    tree_list_4 = [None]  # S4
    tree_list_5 = Tree.tree_list_AND(6)

    T0 = Tree(tree_list=tree_list_0,  name='T0', switches=[S0])
    T1 = Tree(tree_list=tree_list_1,  name='T1', switches=[S1])
    T2 = Tree(tree_list=tree_list_2,  name='T2', switches=[S2])
    T3 = Tree(tree_list=tree_list_3,  name='T3', switches=[S3])
    T4 = Tree(tree_list=tree_list_4,  name='T4', switches=[S4])
    T5 = Tree(tree_list=tree_list_5,  name='T5', switches=[S0, S1, S2, S3, S4, S5])

    position_R0 = [2.5, 5, 1.75, 1.75]
    position_R1 = [0, 2.5, 1.75, 1.75]
    position_R2 = [2.5, 0, 1.75, 1.75]
    position_R3 = [5, 2.5, 1.75, 1.75]
    position_RE = [5, 0, 1, 1.5]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0, S2])
    R1 = Room(name='R1', position=position_R1, switches_list=[S5])
    R2 = Room(name='R2', position=position_R2, switches_list=[S4])
    R3 = Room(name='R3', position=position_R3, switches_list=[S1, S3])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False, tree=T0, name='D0', room_departure=R0, room_arrival=R1)
    D1 = Door(two_way=False, tree=T1, name='D1', room_departure=R3, room_arrival=R0)
    D2 = Door(two_way=False, tree=T2, name='D2', room_departure=R0, room_arrival=R2,
              relative_departure_coordinates=[1 / 2, 0.9],
              relative_arrival_coordinates=[1 / 2, 0.9])
    D3 = Door(two_way=False, tree=T3, name='D3', room_departure=R1, room_arrival=R3,
              relative_departure_coordinates=[0.1, 1 / 2],
              relative_arrival_coordinates=[0.1, 1 / 2])
    D4 = Door(two_way=False, tree=T4, name='D4', room_departure=R2, room_arrival=R3)
    D5 = Door(two_way=False, tree=T5, name='D5', room_departure=R3, room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution='S0 S2 D2 S4 D4 S1 S3 D1 D0 S5 D3 D5',
                 level_color=Levels_colors_list.YELLOW,
                 name='Crossroad',
                 border=30,
                 door_window_size=470)

    return level