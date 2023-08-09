from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_spaceship():
    
    v = 1

    S0 = Switch(name='S0')

    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')

    S7 = Switch(name='S7')
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9')

    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11', value=v)
    S12 = Switch(name='S12')

    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15', value=v)
    
    tree_list_0 = ['AND', Tree.tree_list_not, ['EQU', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]]
    tree_list_1 = ['AND', [None], ['EQU', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]]

    T0 = Tree(tree_list=Tree.tree_list_not,
              empty=True, name='T0',
              switches=[S0])
    T1 = Tree(tree_list=tree_list_0,
              empty=True, name='T1',
              switches=[S0, S1, S2, S3, S4, S5, S6])
    T2 = Tree(tree_list=tree_list_0,
              empty=True, name='T2',
              switches=[S0, S4, S5, S6, S10, S11, S12])
    T3 = Tree(tree_list=tree_list_0,
              empty=True, name='T3',
              switches=[S0, S10, S11, S12, S13, S14, S15])
    T4 = Tree(tree_list=[None],
              empty=True, name='T4',
              switches=[S0])
    T5 = Tree(tree_list=tree_list_1,
              empty=True, name='T5',
              switches=[S0, S7, S8, S9, S1, S2, S3])
    T6 = Tree(tree_list=tree_list_1,
              empty=True, name='T6',
              switches=[S0, S1, S2, S3, S10, S11, S12])
    T7 = Tree(tree_list=tree_list_1,
              empty=True, name='T7',
              switches=[S0, S10, S11, S12, S4, S5, S6])
    T8 = Tree(tree_list=tree_list_1,
              empty=True, name='T8',
              switches=[S0, S4, S5, S6, S13, S14, S15])
    T9 = Tree(tree_list=['EQUSET'] + [Tree.tree_list_BIN(3)]*5 + [[None]]*5,
              empty=True,
              name='T9',
              switches=[S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15,
                         0, 1, 2, 3, 4],
               cut_expression=True)
    T10 = Tree(tree_list=Tree.tree_list_from_str('1001110000010100'),
               empty=True,
               name='T10',
               switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15])
    
    ax = 1.9
    ay = 1
    ex = 1.9
    ey = 1

    position_R0 = [7.5*ax,  0*ay, 1*ex, 2*ey]
    position_R1 = [7*ax,  5*ay, 2*ex, 4*ey]
    position_R2 = [3.5*ax,  9*ay, 2*ex, 2*ey]
    position_R3 = [9.25*ax,  0*ay, 2*ex, 2*ey]
    position_R4 = [2*ax,  3.5*ay, 2*ex, 2*ey]
    position_R5 = [4.8*ax,  0*ay, 2*ex, 2*ey]
    position_RE = [7*ax,  -4.5*ay, 2*ex, 3*ey]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1, S2, S3])
    R2 = Room(name='R2', position=position_R2, switches_list=[S4, S5, S6])
    R3 = Room(name='R3', position=position_R3, switches_list=[S7, S8, S9])
    R4 = Room(name='R4', position=position_R4, switches_list=[S10, S11, S12])
    R5 = Room(name='R5', position=position_R5, switches_list=[S13, S14, S15])
    RE = Room(name='RE', position=position_RE, is_exit=True)

    D0 = Door(two_way=False,
              tree=T0,
              name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/2, 1],
              relative_arrival_coordinates=[1/2, 0],
              relative_position=0.25)
    D1 = Door(two_way=False,
              tree=T1,
              name='D1',
              room_departure=R1,
              room_arrival=R2,
              relative_position=0.6)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=R4,
              relative_position=0.4)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R4,
              room_arrival=R5)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R0,
              room_arrival=R3,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, 1/2])
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R3,
              room_arrival=R1)
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R1,
              room_arrival=R4,
              relative_position=0.3)
    D7 = Door(two_way=False,
              tree=T7,
              name='D7',
              room_departure=R4,
              room_arrival=R2,
              relative_position=0.4)
    D8 = Door(two_way=False,
              tree=T8,
              name='D8',
              room_departure=R2,
              room_arrival=R5,
              relative_position=0.25)
    D9 = Door(two_way=False,
              tree=T9,
              name='D9',
              room_departure=R5,
              room_arrival=R0,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, 1/2])
    D10 = Door(two_way=False,
               tree=T10,
               name='D10',
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates=[1/2, 0],
               relative_arrival_coordinates=[1/2, 1])

    color = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.3, li=0.4)
    color.surrounding_color=Color.TOTAL_YELLOW
    color.contour_color=Color.TOTAL_YELLOW
    color.letters_color=Color.TOTAL_YELLOW
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution='D0 S1 D1 S5 D2 S10 S11 S12 D3 S15 D9 S0 D4 S7 S8 D5 S1 S3 D6 S10 S11 S12 D7 S4 S5 D8 S14 D9 D4 S7 S9 D5 S1 S2 S3 D6 S10 S11 D7 S5 D8 S13 S14 D9 S0 D0 S1 D1 S5 D2 S10 D3 S14 D9 D0 S2 D1 S4 D2 S11 D3 S13 D9 S0 D4 S9 D5 S1 S2 D6 S11 D7 S4 S5 D8 S14 S15 D9 S0 D0 S1 D1 S4 S5 D2 S10 S12 D3 S13 S14 S15 D9 D0 S1 S2 D1 S4 S6 D2 S10 S11 S12 D3 S13 D9 D0 S1 S3 D1 S4 S5 S6 D2 S10 D3 S13 S14 D9 S0 D10',
                 level_color=color,
                 name='Spaceship',
                 border=50,
                 door_window_size=650,
                 keep_proportions=False)
    return level
