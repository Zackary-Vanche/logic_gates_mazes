from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list
from numpy import cos, sin, pi
from random import random as random_random
from random import randint as random_randint

n_switches = 5
n_doors = 11

def aux_level_random_wheel(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
                           exit_number=None):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    Slist = [S0, S1, S2, S3, S4]
    
    assert len(Slist) == n_switches
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist)),
              name='V0',
              switches = Slist)
    
    def get_tree(i):
        return Tree(['IN', [None]] + [[None]]*len(door_trees_list[i]),
                     name=f'T{i}',
                     switches = [V0] + door_trees_list[i],
                     cut_expression=True,
                     cut_expression_separator=')')
    
    ex = 0.2
    ey = 0.2
    
    a0 = 2*pi*random_random()
    
    def pos(i):
        a = a0 + 2*i*pi/5
        return [cos(a), sin(a), ex, ey]
    
    a = a0 +2*random_randint(0, 4)*pi/5 + pi/5
    posE = [cos(a), sin(a), ex, ey]
    
    R0 = Room(name='R0',
              position = [0, 0, ex, ey],
              switches_list = [])
    R1 = Room(name='R1',
              position = pos(1),
              switches_list = [S0])
    R2 = Room(name='R2',
              position = pos(2),
              switches_list = [S1])
    R3 = Room(name='R3',
              position = pos(3),
              switches_list = [S2])
    R4 = Room(name='R4',
              position = pos(4),
              switches_list = [S3])
    R5 = Room(name='R5',
              position = pos(5),
              switches_list = [S4])
    RE = Room(name='RE',
              position=posE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=True,
              tree=get_tree(1),
              room_departure=R0,
              room_arrival=R2)
    D2 = Door(two_way=True,
              tree=get_tree(2),
              room_departure=R0,
              room_arrival=R3)
    D3 = Door(two_way=True,
              tree=get_tree(3),
              room_departure=R0,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=get_tree(4),
              room_departure=R0,
              room_arrival=R5)
    D5 = Door(two_way=True,
              tree=get_tree(5),
              room_departure=R1,
              room_arrival=R2)
    D6 = Door(two_way=True,
              tree=get_tree(6),
              room_departure=R2,
              room_arrival=R3)
    D7 = Door(two_way=True,
              tree=get_tree(7),
              room_departure=R3,
              room_arrival=R4)
    D8 = Door(two_way=True,
              tree=get_tree(8),
              room_departure=R4,
              room_arrival=R5)
    D9 = Door(two_way=True,
              tree=get_tree(9),
              room_departure=R5,
              room_arrival=R1)
    if exit_number is None:
        D10 = Door(two_way=True,
                  tree=get_tree(10),
                  room_departure=R0,
                  room_arrival=RE,
                  relative_position=0.3)
    else:
        D10 = Door(two_way=True,
                  tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                            name='T10',
                            switches = Slist + [exit_number],
                            cut_expression=True),
                  room_departure=R0,
                  room_arrival=RE,
                  relative_position=0.3)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Wheel',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)
    
    return level

def level_random_wheel():
    return Maze.get_random_level_from_file(aux_level_random_wheel)