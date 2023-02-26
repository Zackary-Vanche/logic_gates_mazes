from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_pythagorean():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    SN2 = Switch(value=2, name='2')
    
    tree_list_pow = ['POW', Tree.tree_list_BIN(3), [None]]
    tree_list_sum = ['SUM', tree_list_pow, tree_list_pow]
    tree_list_equ = ['EQU', tree_list_sum, tree_list_pow]
    tree_list_inf = ['INF', Tree.tree_list_BIN(3), Tree.tree_list_BIN(3)]
    tree_list_or = ['AND'] + [Tree.tree_list_OR(3)]*3
    
    T0 = Tree(tree_list=tree_list_equ,
              empty=True,
              name='T0',
              switches = [S0, S1, S2, SN2,
                          S3, S4, S5, SN2,
                          S6, S7, S8, SN2])
    T1 = Tree(tree_list=['AND', tree_list_inf, tree_list_or],
              empty=True,
              name='T1',
              switches = [S0, S1, S2,
                          S3, S4, S5,
                          S0, S1, S2, S3, S4, S5, S6, S7, S8])
    
    R0 = Room(name='R0',
              position = [0, 0, 3, 3],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
              position=[0, 4, 1, 1])
    RE = Room(name='RE',
              position=[2, 4, 1, 1],
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=[1/6, 5/6])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=RE)
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, RE], 
             doors_list=[D0, D1], 
             fastest_solution='S0 S1 S5 S6 S8 D0 D1',
             level_color=Levels_colors_list.FROM_HUE(0.15, sa=1, li=0.25),
             name='Pythagorean',
             door_window_size = 800,
             keep_proportions = True)
    
    return level