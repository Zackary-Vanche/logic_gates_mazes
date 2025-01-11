from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

def aux(door_trees_list = [[i for i in range(2**8)] for j in range(8)],
                                   exit_number=None): # exit_number isn't usde but should remain as an argument

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]
    
    def get_tree(i):
        i_min = max(0, i-5)
        i_max = i+1
        Slist_i = Slist[i_min:i_max]
        tree_list = []
        for j in door_trees_list[i]:
            str_j = format(j, f'0{len(Slist)}b')[::-1]
            bin_j = 0
            for k in range(i_min, i_max):
                bin_j += int(str_j[k]) * 2**(k-i_min)
            if bin_j not in tree_list:
                tree_list.append(bin_j)
        return Tree(['IN', Tree.tree_list_BIN(len(Slist_i))] + [[None]]*len(tree_list),
                     name=f'T{i}',
                     switches = Slist_i + tree_list,
                     cut_expression=True,
                     cut_expression_separator=')',
                     random_switches_bin_list=Slist_i)
    
    ex = 0.5
    ey = 0.6
    ey0 = 0.925
    
    R0 = Room(name='R0',
              position = [0, 0, ex, ey0],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [1, 0, ex, ey],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [1, 1, ex, ey0],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [0, 1, ex, ey],
              switches_list = [S3])
    R4 = Room(name='R4',
              position = [0, 2, ex, ey0],
              switches_list = [S4])
    R5 = Room(name='R5',
              position = [1, 2, ex, ey],
              switches_list = [S5])
    R6 = Room(name='R6',
              position = [1, 3, ex, ey0],
              switches_list = [S6])
    R7 = Room(name='R7',
              position = [0, 3, ex, ey],
              switches_list = [S7])
    RE = Room(name='RE',
              position=[0, 4, 1.5, ey],
              is_exit=True)   # E pour exit ou end
    
    rd0 = [1/2, ey/ey0/2]
    rd1 = [1/2, 1]
    ra1 = [1/2, 0]
    
    D0 = Door(two_way=0,
                tree=get_tree(0),
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=rd0)
    D1 = Door(two_way=0,
                tree=get_tree(1),
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=rd1,
                relative_arrival_coordinates=ra1)
    D2 = Door(two_way=0,
                tree=get_tree(2),
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=rd0)
    D3 = Door(two_way=0,
                tree=get_tree(3),
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=rd1,
                relative_arrival_coordinates=ra1)
    D4 = Door(two_way=0,
                tree=get_tree(4),
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=rd0)
    D5 = Door(two_way=0,
                tree=get_tree(5),
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=rd1,
                relative_arrival_coordinates=ra1)
    D6 = Door(two_way=0,
                tree=get_tree(6),
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=rd0)
    D7 = Door(two_way=0,
                tree=get_tree(7),
                room_departure=R7,
                room_arrival=RE,
                relative_arrival_coordinates=[1/6, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE], #, R11, R12, R13, R14, R15, R16, R17, R18, R19
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7], # , D11, D12, D13, D14, D15, D16, D17, D18, D19
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Boustrophedon',
                 door_window_size=600,
                 keep_proportions=False,
                 y_separation=40,
                 border=40,
                 random=True,
                 random_long=False)
    
    return level

get_color = Levels_colors_list.RANDOM

def f():
    return Maze.get_random_level_from_file(aux)