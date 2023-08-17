from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_alice_and_bob():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')

    T0 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T0',
              switches=[S3, S4])
    T1 = Tree(tree_list=Tree.tree_list_XOR(2),
              name='T1',
              switches=[S3, S4])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S0])
    T3 = Tree(tree_list=Tree.tree_list_not,
              name='T3',
              switches=[S0])
    T4 = Tree(tree_list=Tree.tree_list_OR(2),
              name='T4',
              switches=[S1, S2])
    T5 = Tree(tree_list=Tree.tree_list_OR(2),
              name='T5',
              switches=[S1, S2])
    T6 = Tree(tree_list=Tree.tree_list_from_str("FFTF"),
              name='T6',
              switches=[S1, S2, S3, S4])

    R0 = Room(name='R0',
              position=[2, 2, 1, 1],
              switches_list=[S0])
    R1 = Room(name='R1',
              position=[0, 0, 1, 1],
              switches_list=[S1])
    R2 = Room(name='R2',
              position=[4, 2, 1, 1],
              switches_list=[S2])
    R3 = Room(name='R3',
              position=[0, 2, 1, 1],
              switches_list=[S3])
    R4 = Room(name='R4',
              position=[4, 0, 1, 1],
              switches_list=[S4])
    RE = Room(name='RE',
              position=[2, 0, 1, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R1,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R3,
              room_arrival=R0)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R4,
              room_arrival=R0)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R4,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution="S0 D0 S1 D2 S3 D4 S0 D1 S2 D3 S4 D5 S0 D0 S1 D2 S3 D4 S0 D1 D3 S4 D5 S0 D0 D2 S3 D4 S0 D1 S2 D3 D6",
                 level_color=Levels_colors_list.FROM_HUE(0.57, sa=0.6, li=0.49),
                 name='Alice and Bob',
                 door_window_size=550,
                 group='pure maze')

    return level