from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f():
    
    S0 = Switch(name='S0', value=1)
    S1 = Switch(name='S1', value=1)
    S2 = Switch(name='S2', value=1)
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    SN = Switch(name='1', value=1)
    
    T0 = Tree(tree_list=['AND',
                         Tree.tree_list_NAND(2),
                         Tree.tree_list_NAND(2)],
                name='T0',
                switches = [S6, S7,
                            S7, S8])
    T1 = Tree(tree_list=['AND',
                         Tree.tree_list_NAND(2),
                         Tree.tree_list_NAND(2)],
                name='T1',
                switches = [S0, S1,
                            S1, S2])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches = [SN])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches = [SN])
    
    T4 = Tree(tree_list=['AND', 
                         Tree.tree_list_XOR(3), 
                         Tree.tree_list_XOR(3), 
                         Tree.tree_list_XOR(3)],
                name='T4',
                switches = [S0, S3, S6,
                            S1, S4, S7,
                            S2, S5, S8])
    T5 = Tree(tree_list=['OR',
                         Tree.tree_list_XOR(3),
                         Tree.tree_list_from_str('FFF')],
                name='T5',
                switches = [S3, S4, S5,
                            S3, S4, S5])
    
    T6 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T6',
                switches = [S6, S7, S8])
    
    R0 = Room(name='R0',
                position = [9, 2, 1, 4],
                switches_list = [S3, S4, S5])
    R1 = Room(name='R1',
                position = [3, 0, 5, 1],
                switches_list = [S0, S1, S2])
    R2 = Room(name='R2',
                position = [3, 7, 5, 1],
                switches_list = [S6, S7, S8])
    R3 = Room(name='R3',
                position = [6, 3, 1, 2],
                switches_list = [])
    R4 = Room(name='R4',
                position = [3, 3, 1, 2],
                switches_list = [])
    RE = Room(name='RE',
              position=[0, 3, 1, 2],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
                tree=T0,
                room_departure=R4,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                room_departure=R4,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                room_departure=R1,
                room_arrival=R0)
    D3 = Door(two_way=False,
                tree=T3,
                room_departure=R2,
                room_arrival=R0)
    
    D4 = Door(two_way=False,
                tree=T4,
                room_departure=R0,
                room_arrival=R3)
    D5 = Door(two_way=False,
                tree=T5,
                room_departure=R3,
                room_arrival=R4)
    D6 = Door(two_way=False,
                tree=T6,
                room_departure=R4,
                room_arrival=RE)
    
    level = Maze(start_room_index=0, 
              exit_room_index=-1, 
              rooms_list=[R0, R1, R2, R3, R4, RE], 
              doors_list = [D0, D1, D2, D3, D4, D5, D6],
              fastest_solution="D4 D5 D0 S1 D2 S4 D4 D5 D1 S7 D3 S4 D4 D5 D0 S0 D2 S3 D4 D5 D1 S6 S7 D3 S3 S4 D4 D5 D0 S1 S2 D2 S4 S5 D4 D5 D1 S8 D3 S5 D4 D5 D0 S1 D2 S4 D4 D5 D1 S7 D3 S4 D4 D5 D6",
              level_color=get_color(),
              name='River',
              keep_proportions=False,
              door_window_size=500,
              y_separation=100)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.6, sa=0.5, li=0.6)
    lcolor.room_color = Color.color_hls(hu=0.4, sa=0.5, li=0.25)
    lcolor.inside_room_color = Color.IVORY
    lcolor.surrounding_color = Color.color_hls(hu=0.6, sa=1, li=0.8)
    lcolor.contour_color = Color.color_hls(hu=0.6, sa=1, li=0.8)
    return lcolor
    