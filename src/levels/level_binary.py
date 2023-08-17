from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_binary():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')

    T0 = Tree(tree_list=[None], name='T0', switches=[S6])
    T1 = Tree(tree_list=[None], name='T1', switches=[S3])
    T2 = Tree(tree_list=[None], name='T2', switches=[S4])
    T3 = Tree(tree_list=[None], name='T3', switches=[S0])
    T4 = Tree(tree_list=[None], name='T4', switches=[S1])
    T5 = Tree(tree_list=[None], name='T5', switches=[S2])
    T6 = Tree(tree_list=Tree.tree_list_AND(7),
              name='T6',
              switches=[S0, S1, S2, S3, S4, S5, S6])

    position_R0 = [3, 2.9, 2, 2]
    position_R1 = [1, 0, 2, 2]
    position_R2 = [5, 0, 2, 2]
    position_R3 = [0, 3, 2, 2]
    position_R4 = [6, 3, 2, 2]
    position_R5 = [0, 6, 2, 2]
    position_R6 = [6, 6, 2, 2]
    position_RE = [3, 6, 2, 2]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2])
    R3 = Room(name='R3', position=position_R3, switches_list=[S3])
    R4 = Room(name='R4', position=position_R4, switches_list=[S4])
    R5 = Room(name='R5', position=position_R5, switches_list=[S5])
    R6 = Room(name='R6', position=position_R6, switches_list=[S6])
    RE = Room(name='RE', position=position_RE, is_exit=True)
    # E pour exit ou end

    D0 = Door(two_way=True,
              tree=T0,
              name='D0',
              room_departure=R3,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=T1,
              name='D1',
              room_departure=R4,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=T2,
              name='D2',
              room_departure=R0,
              room_arrival=R3)
    D3 = Door(two_way=True,
              tree=T3,
              name='D3',
              room_departure=R0,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=T4,
              name='D4',
              room_departure=R3,
              room_arrival=R5)
    D5 = Door(two_way=True,
              tree=T5,
              name='D5',
              room_departure=R4,
              room_arrival=R6)
    D6 = Door(two_way=True,
              tree=T6,
              name='D6',
              room_departure=R0,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S0 D3 S4 D3 D2 S3 D2 D3 D1 S2 D1 D5 S6 D5 D3 D2 D0 S1 D0 D4 S5 D4 D2 D6',
                 level_color=Levels_colors_list.BLUE_GREEN,
                 name='Binary',
                 door_window_size=340)

    return level