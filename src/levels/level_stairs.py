from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_stairs():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')

    tree_list_0 = Tree.tree_list_NAND(2)
    tree_list_1 = ['AND',
                   Tree.tree_list_from_str('T F'),
                   [None]]
    tree_list_2 = ['AND',
                   Tree.tree_list_from_str('F T'),
                   [None]]
    tree_list_3 = ['AND',
                   Tree.tree_list_XOR(3),
                   [None]]
    tree_list_4 = ['AND',
                   Tree.tree_list_XORN(3),
                   [None]]
    tree_list_5 = ['AND',
                   Tree.tree_list_XOR(3),
                   [None]]
    tree_list_6 = ['AND',
                   Tree.tree_list_XORN(3),
                   [None]]
    tree_list_7 = ['AND',
                   Tree.tree_list_XOR(3),
                   [None]]
    tree_list_8 = Tree.tree_list_from_str('TF TT TT')

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[S6, S7])
    T1 = Tree(tree_list=tree_list_1,
               name='T1',
              switches=[S6, S7, S8])
    T2 = Tree(tree_list=tree_list_2,
              name='T2',
              switches=[S6, S7, S8])
    T3 = Tree(tree_list=tree_list_3,
              name='T3',
              switches=[S0, S1, S2, S8])
    T4 = Tree(tree_list=tree_list_4,
              name='T4',
              switches=[S1, S2, S3, S8])
    T5 = Tree(tree_list=tree_list_5,
              name='T5',
              switches=[S2, S3, S4, S8])
    T6 = Tree(tree_list=tree_list_6,
              name='T6',
              switches=[S3, S4, S5, S8])
    T7 = Tree(tree_list=tree_list_7,
              name='T7',
              switches=[S4, S5, S6, S8])
    T8 = Tree(tree_list=tree_list_8,
              name='T8',
              switches=[S1, S4, S1, S3, S2, S4])

    position_R0 = [0, 0, 2, 4]
    position_R1 = [1, 5.5, 1, 1.5]
    position_R2 = [4, 6, 1, 1]
    position_R3 = [8, 6, 1, 1]
    position_R4 = [4, 4, 1, 1]
    position_R5 = [8, 4, 1, 1]
    position_R6 = [4, 2, 1, 1]
    position_R7 = [8, 2, 1, 1]
    position_R8 = [4, 0, 1, 1]
    position_RE = [8, 0, 1, 1]

    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S0, S1, S2, S3, S4, S5, S6, S7])
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S8])
    R2 = Room(name='R2',
              position=position_R2,
              switches_list=[])
    R3 = Room(name='R3',
              position=position_R3,
              switches_list=[])
    R4 = Room(name='R4',
              position=position_R4,
              switches_list=[])
    R5 = Room(name='R5',
              position=position_R5,
              switches_list=[])
    R6 = Room(name='R6',
              position=position_R6,
              switches_list=[])
    R7 = Room(name='R7',
              position=position_R7,
              switches_list=[])
    R8 = Room(name='R8',
              position=position_R8,
              switches_list=[])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0, name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1/2, 0])
    D1 = Door(two_way=False,
              tree=T1, name='D1',
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2, name='D2',
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3, name='D3',
              room_departure=R3,
              room_arrival=R4)
    D4 = Door(two_way=False,
              tree=T4, name='D4',
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5, name='D5',
              room_departure=R5,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6, name='D6',
              room_departure=R6,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7, name='D7',
              room_departure=R7,
              room_arrival=R8)
    D8 = Door(two_way=False,
              tree=T8, name='D8',
              room_departure=R8,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution='S1 S3 S5 D0 S8 D1 D2 D3 D4 D5 D6 D7 D8',
                 level_color=Levels_colors_list.RED_AND_ORANGE,
                 name='Stairs',
                 door_window_size=300)

    return level