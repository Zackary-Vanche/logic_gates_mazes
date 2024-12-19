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
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    
    SN1 = Switch(name='1', value=1)
    SN3 = Switch(name='3', value=3)
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V0',
              switches=[S0, S1, S2, S3])
    V1 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V1',
              switches=[S4, S5, S6, S7])
    V2 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V2',
              switches=[S8, S9, S10, S11])
    V3 = Tree(tree_list=Tree.tree_list_BIN(4),
              name='V3',
              switches=[S12, S13, S14, S15])
    
    tree_list_INF = ['INF', [None], [None]]
    tree_list_3 = ['POW', [None], [None]]
    tree_list_SUM = ['SUM', tree_list_3, tree_list_3]
    tree_list_EQU = ['EQU', tree_list_SUM, tree_list_SUM]

    T0 = Tree(tree_list=[None],
              name='T0',
              switches = [SN1])
    T1 = Tree(tree_list=tree_list_INF,
              name='T1',
              switches = [V0, V1])
    T2 = Tree(tree_list=tree_list_INF,
              name='T2',
              switches = [V0, V2])
    T3 = Tree(tree_list=['AND',
                             tree_list_INF,
                             tree_list_EQU],
              name='T3',
              switches = [V2,
                          V3,
                          V0,
                          SN3,
                          V1,
                          SN3,
                          V2,
                          SN3,
                          V3,
                          SN3],
              cut_expression=True)
    
    h = 5
    e = 0.5    

    R0 = Room(name='R0',
              position = [0, 0, e, h],
              switches_list = [S0, S1, S2, S3])
    R1 = Room(name='R1',
              position = [1, 0, e, h],
              switches_list = [S4, S5, S6, S7])
    R2 = Room(name='R2',
              position = [2, 0, e, h],
              switches_list = [S8, S9, S10, S11])
    R3 = Room(name='R3',
              position = [3, 0, e, h],
              switches_list = [S12, S13, S14, S15])
    RE = Room(name='RE',
              position=[4, 0, e, h],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=RE)
    
    [R0, R1, R2, R3]
    [D0, D1, D2, D3]
    [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution='S0 D0 S6 S7 D1 S8 S11 D2 S13 S15 D3',
                 level_color=Levels_colors_list.YELLOW_AND_BLACK,
                 name='Taxicab number',
                 door_window_size=410,
                 keep_proportions=False)

    return level