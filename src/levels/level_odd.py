from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_odd():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    tree_list_0 = Tree.tree_list_AND(5)
    tree_list_5 = Tree.tree_list_NOR(2)
    tree_list_4 = Tree.tree_list_from_str('FT')
    tree_list_6 = Tree.tree_list_from_str('TF')
    tree_list_1 = Tree.tree_list_from_str('FTF')
    tree_list_2 = Tree.tree_list_from_str('FFT')
    tree_list_3 = Tree.tree_list_from_str('TTTF')

    T0 = Tree(tree_list=tree_list_0,  name='T0', switches=[S0, S1, S2, S3, S4])
    T1 = Tree(tree_list=tree_list_1,  name='T1', switches=[S0, S1, S4])
    T2 = Tree(tree_list=tree_list_2,  name='T2', switches=[S0, S2, S4])
    T3 = Tree(tree_list=tree_list_3,  name='T3', switches=[S0, S1, S3, S4])
    T4 = Tree(tree_list=tree_list_4,  name='T4', switches=[S0, S4])
    T5 = Tree(tree_list=tree_list_5,  name='T5', switches=[S0, S4])
    T6 = Tree(tree_list=tree_list_6,  name='T6', switches=[S0, S4])

    position_R0 = [3, 3, 2, 2]
    position_R1 = [3, 0, 2, 2]
    position_R2 = [0, 6.5, 2, 2]
    position_R3 = [6, 6.5, 2, 2]
    position_RE = [3, 6, 2, 2]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0, S4])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2])
    R3 = Room(name='R3', position=position_R3, switches_list=[S3])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    a = 0
    b = 1

    relative_departure_coordinates_D2 = [a, b]
    relative_arrival_coordinates_D2 = [b, a]
    relative_departure_coordinates_D3 = [b, b]
    relative_arrival_coordinates_D3 = [a, a]
    relative_departure_coordinates_D4 = [a, a]
    relative_arrival_coordinates_D4 = [a, a]
    relative_departure_coordinates_D5 = [b, a]
    relative_arrival_coordinates_D5 = [b, a]
    relative_departure_coordinates_D6 = [b, b]
    relative_arrival_coordinates_D6 = [a, b]

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=RE)
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R0,
              room_arrival=R1)
    D2 = Door(two_way=True,
              tree=T2, name='D2',
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D2,
              relative_arrival_coordinates=relative_arrival_coordinates_D2)
    D3 = Door(two_way=True,
              tree=T3, name='D3',
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D3,
              relative_arrival_coordinates=relative_arrival_coordinates_D3)
    D4 = Door(two_way=True,
              tree=T4, name='D4',
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D4,
              relative_arrival_coordinates=relative_arrival_coordinates_D4)
    D5 = Door(two_way=True,
              tree=T5, name='D5',
              room_departure=R1,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D5,
              relative_arrival_coordinates=relative_arrival_coordinates_D5)
    D6 = Door(two_way=True,
              tree=T6, name='D6',
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=relative_departure_coordinates_D6,
              relative_arrival_coordinates=relative_arrival_coordinates_D6)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S4 D2 D4 S1 D4 D2 S4 D1 D5 S3 D5 D1 S0 D3 D6 S2 D6 D3 S4 D0',
                 level_color=Levels_colors_list.PURPLE,
                 name='Odd',
                 border=60,
                 door_window_size=340,
                 keep_proportions=True)

    return level