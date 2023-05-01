from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from os.path import exists as os_path_exists
from Color import Color

def level_rotation_bis(): 
    
    v = 1

    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')

    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17', value=v)
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]
    
    

    T0 = Tree(tree_list=['IN'] + [Tree.tree_list_BIN(12)]*4,
                empty=True,
                name='T0',
                switches=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11,
                          S12, S13, S22, S23, S14, S15, S18, S19, S16, S17, S20, S21,
                          S16, S17, S14, S15, S18, S19, S22, S23, S20, S21, S12, S13,
                          S20, S21, S12, S13, S16, S17, S14, S15, S18, S19, S22, S23],
                cut_expression=True)
    T1 = Tree(tree_list=['EQU'] + [Tree.tree_list_BIN(12)]*2,
                empty=True,
                name='T1',
                switches=Slist,
                cut_expression=True)
    T2 = Tree(tree_list=[None],
                empty=True,
                name='T2',
                switches=[1])
    filename = 'levels/Rotation_bis_random_exits.txt'
    if os_path_exists(filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            l = rd_choice(lines)
        T3 = Tree(tree_list=Tree.tree_list_from_str(l)[:12],
                    empty=True,
                    name='T3',
                    switches=Slist[:12])
    else:
        T3 = Tree(tree_list=[None],
                    empty=True,
                    name='T3',
                    switches=[1])

    R0 = Room(name='R0',
                position=[3, 3, 2, 6],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11])
    R1 = Room(name='R1',
                position=[0, 3, 2, 6],
                switches_list=[S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23])
    R2 = Room(name='R2',
                position=[0, 0, 2, 2],
                switches_list=[])
    RE = Room(name='RE',
              position=[3, 0, 2, 2],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[0, 0])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=RE)
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.18, sa=0.6, li=0.2)
    lcolor.background_color = Color.BRIGHT_YELLOW
    lcolor.letters_color = Color.BLACK
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Rotation_bis',
                 keep_proportions=True,
                 door_window_size=1000)
    
    return level
