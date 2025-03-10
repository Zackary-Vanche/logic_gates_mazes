from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    S4 = Switch(name='S4', value=1)
    S5 = Switch(name='S5')
    S6 = Switch(name='S6', value=1)
    S7 = Switch(name='S7')
    
    S8 = Switch(name='S8', value=1)
    S9 = Switch(name='S9')
    S10 = Switch(name='S10', value=1)
    S11 = Switch(name='S11', value=1)
    
    S12 = Switch(name='S12', value=1)
    S13 = Switch(name='S13', value=1)
    S14 = Switch(name='S14', value=1)
    S15 = Switch(name='S15')
    
    S16 = Switch(name='S16', value=1)
    S17 = Switch(name='S17', value=1)
    S18 = Switch(name='S18', value=1)
    S19 = Switch(name='S19', value=1)

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    
    Slist = Slist_0 + Slist_1 + Slist_2 + Slist_3 + Slist_4
    
    tree_list_BIN_4 = Tree.tree_list_BIN(4)
    
    V0 = Tree(tree_list=tree_list_BIN_4,
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=tree_list_BIN_4,
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=tree_list_BIN_4,
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=tree_list_BIN_4,
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=tree_list_BIN_4,
          name='V4',
          switches=Slist_4)
    
    V5 = Tree(tree_list=['AND'] + [Tree.tree_list_OR(2)]*10,
          name='V5',
          switches=Slist)
    
    V6 = Tree(tree_list=['DIFF'] + [[None]]*4,
          name='V6',
          switches=[V1, V2, V3, V4])
    
    l = [1+4*1, 3+4*1, 1+4*3, 3+4*3]
    
    tree_list_0 = ['AND',
                   [None],
                   [None],
                   ['EQUSET',
                    ['ABS', ['SUM', Tree.tree_list_BIN(2), ['MINUS', Tree.tree_list_BIN(2)]]],
                    ['ABS', ['SUM', Tree.tree_list_BIN(2), ['MINUS', Tree.tree_list_BIN(2)]]],
                    [None],
                    [None],
                   ]]
    tree_list_1 = ['EQU', [None], [None]]

    T0 = Tree(tree_list=tree_list_0,
                name='T0',
                switches=[V5, V6,
                          S0, S1,
                          S4, S5,
                          S2, S3,
                          S6, S7,
                          1, 2
                          ])
    T1 = Tree(tree_list=tree_list_1,
                name='T1',
                switches=[V0, V1])
    T2 = Tree(tree_list=tree_list_0,
                name='T2',
                switches=[V5, V6,
                          S0, S1,
                          S8, S9,
                          S2, S3,
                          S10, S11,
                          1, 2
                          ])
    T3 = Tree(tree_list=tree_list_1,
                name='T3',
                switches=[V0, V2])
    T4 = Tree(tree_list=tree_list_0,
                name='T4',
                switches=[V5, V6,
                          S0, S1,
                          S12, S13,
                          S2, S3,
                          S14, S15,
                          1, 2
                          ])
    T5 = Tree(tree_list=tree_list_1,
                name='T5',
                switches=[V0, V3])
    T6 = Tree(tree_list=tree_list_0,
                name='T6',
                switches=[V5, V6,
                          S0, S1,
                          S16, S17,
                          S2, S3,
                          S18, S19,
                          1, 2
                          ])
    T7 = Tree(tree_list=tree_list_1,
                name='T7',
                switches=[V0, V4])
    T8 = Tree(tree_list=['AND', Tree.tree_list_from_str('FFFFTTTTTFTF')] + [['DIFF', Tree.tree_list_BIN(2), [None]]]*4 + [[None]],
                name='T8',
                switches=[S0, S1, S2, S3,
                          S4, S5,
                          S8, S9,
                          S12, S13,
                          S16, S17,
                          S6, S7, 2,
                          S10, S11, 2,
                          S14, S15, 2,
                          S18, S19, 2,
                          V6
                          ])

    R0 = Room(name='R0',
                position=[1, 3, 5, 1],
                switches_list=Slist_0,
                surrounding_color=Color.BRIGHT_BROWN)
    R1 = Room(name='R1',
                position=[0, 0, 2, 2],
                switches_list=Slist_1,
                surrounding_color=Color.WHITE)
    R2 = Room(name='R2',
                position=[5, 0, 2, 2],
                switches_list=Slist_2,
                surrounding_color=Color.WHITE)
    R3 = Room(name='R3',
                position=[1, 5, 2, 2],
                switches_list=Slist_3,
                surrounding_color=Color.BLACK)
    R4 = Room(name='R4',
                position=[4, 5, 2, 2],
                switches_list=Slist_4,
                surrounding_color=Color.BLACK)
    RE = Room(name='RE',
              position=[3, 0, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1.5/5, 1/2],
                relative_arrival_coordinates=[1.5/2, 1.5/2],
                surrounding_color=Color.BLACK)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[0.5/2, 1.5/2],
                relative_arrival_coordinates=[0.5/5, 1/2],
                surrounding_color=Color.BLACK)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[3.5/5, 1/2],
                relative_arrival_coordinates=[0.5/2, 1.5/2],
                surrounding_color=Color.BLACK)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[1.5/2, 1.5/2],
                relative_arrival_coordinates=[4.5/5, 1/2],
                surrounding_color=Color.BLACK)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[1.5/5, 1/2],
                relative_arrival_coordinates=[1.5/2, 0.5/2])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[0.5/2, 0.5/2],
                relative_arrival_coordinates=[0.5/5, 1/2])
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R4,
                relative_departure_coordinates=[3.5/5, 1/2],
                relative_arrival_coordinates=[0.5/2, 0.5/2])
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[1.5/2, 0.5/2],
                relative_arrival_coordinates=[4.5/5, 1/2])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution='S0 S3 D4 S13 S14 S15 D5 S1 D2 S9 S10 D3 S0 S2 D0 S4 S5 S7 D1 S3 D6 S16 S19 D7 S0 D0 S4 S7 D1 S1 D2 S9 S10 S11 D3 S3 D6 S16 S17 S19 D7 S1 D4 S13 S14 D5 S0 D2 S8 S9 S11 D3 S3 D4 S12 S15 D5 S0 S2 S3 D6 S17 S18 D7 S1 D0 S5 S6 S7 D1 S2 D4 S12 S13 S15 D5 S1 D0 S5 S6 D1 S3 D2 S8 S11 D3 S1 D6 S17 S18 S19 D7 S0 S2 D8',
                 level_color=get_color(),
                 uniform_surrounding_colors=False,
                 name="First Guarini's puzzle",
                 keep_proportions=True,
                 door_window_size=400)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.1, sa=0.4, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=0.1, sa=1, li=0.85)
    return lcolor