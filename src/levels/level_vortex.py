from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3', value=1)
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    SN3 = Switch(value=3)

    T0 = Tree(tree_list=[None],
              name='T0',
              switches = [S0])
    T1 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T1',
              switches = [S1, S2])
    T2 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T2',
              switches = [S2, S3])
    T3 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T3',
              switches = [S3, S4])
    T4 = Tree(tree_list=['AND',
                         ['EQU',
                          ['SUM'] + [[None]]*7,
                          [None]],
                         [None]],
              name='T4',
              switches = [S1, S2, S3, S4, S5, S6, S7, SN3,
                          S0])
    T5 = Tree(tree_list=Tree.tree_list_NOT,
              name='T5',
              switches = [S0])
    T6 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T6',
              switches = [S4, S5])
    T7 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T7',
              switches = [S5, S6])
    T8 = Tree(tree_list=Tree.tree_list_XNOR(2),
              name='T8',
              switches = [S6, S7])
    T9 = Tree(tree_list=['AND',
                         ['EQU',
                          ['SUM'] + [[None]]*7,
                          [None]],
                         Tree.tree_list_NOT],
              name='T9',
              switches = [S1, S2, S3, S4, S5, S6, S7, SN3,
                          S0])
    T10 = Tree(tree_list=Tree.tree_list_from_str('TFFFFTTT'),
               name='T10',
               switches = [S0, S1, S2, S3, S4, S5, S6, S7])

    R0 = Room(name='R0',
              position = [2, 2, 1, 1],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [0, 4, 1, 1],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [0, 2, 1, 1],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [0, 0, 1, 1],
              switches_list = [S3])
    R4 = Room(name='R4',
              position = [2, 0, 1, 1],
              switches_list = [S4])
    R5 = Room(name='R5',
              position = [4, 0, 1, 1],
              switches_list = [S5])
    R6 = Room(name='R6',
              position = [4, 2, 1, 1],
              switches_list = [S6])
    R7 = Room(name='R7',
              position = [4, 4, 1, 1],
              switches_list = [S7])
    RE = Room(name='RE',
              position=[1.5, 4, 2, 1],
              is_exit=True)   # E pour exit ou end

    rp = 1/2
    rdc = [1/2, 1/2]
    rac = [1/2, 1/2]

    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R4,
                room_arrival=R0,
                relative_position=rp,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0])
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R0,
                room_arrival=R4,
                relative_position=rp,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 0])
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R4,
                room_arrival=R5,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D7 = Door(two_way=False,
                tree=T7,
                room_departure=R5,
                room_arrival=R6,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D8 = Door(two_way=False,
                tree=T8,
                room_departure=R6,
                room_arrival=R7,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D9 = Door(two_way=False,
                tree=T9,
                room_departure=R7,
                room_arrival=R0,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)
    D10 = Door(two_way=False,
                tree=T10,
                room_departure=R0,
                room_arrival=RE,
                relative_position=rp,
                relative_departure_coordinates=rdc,
                relative_arrival_coordinates=rac)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution="S0 D0 D1 D2 S3 D3 S4 D4 S0 D5 S4 D6 D7 D8 S7 D9 S0 D0 D1 S2 D2 D3 S4 D4 S0 D5 S4 D6 D7 S6 D8 D9 S0 D0 S1 D1 D2 D3 S4 D4 S0 D5 S4 D6 S5 D7 D8 D9 S0 D10",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.85, sa=1, li=0.9),
                 name='Vortex',
                 door_window_size=300,
                 keep_proportions=True,
                 y_separation=66,
                 border=50)

    return level