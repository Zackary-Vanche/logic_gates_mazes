from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

n_switches = 4
n_doors = 12

def aux(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
                           exit_number=None):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    Slist = [S0, S1, S2, S3]
    
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
    
    dx = 1
    dy = 1
    ex = 0.6
    ey = 0.6
    
    R0 = Room(name='R0',
              position=[1.5*dx, 0*dy, ex, ey],
              switches_list = [])
    R1 = Room(name='R1',
              position=[0*dx, 0.75*dy, ex, ey],
              switches_list = [S0])
    R2 = Room(name='R2',
              position=[1*dx, 1*dy, ex, ey],
              switches_list = [S1])
    R3 = Room(name='R3',
              position=[2*dx, 1*dy, ex, ey],
              switches_list = [S2])
    R4 = Room(name='R4',
              position=[3*dx, 0.75*dy, ex, ey],
              switches_list = [S3])
    R5 = Room(name='R5',
              position=[1*dx, 2*dy, ex, ey],
              switches_list = [])
    R6 = Room(name='R6',
              position=[2*dx, 2*dy, ex, ey],
              switches_list = [])
    RE = Room(name='RE',
              position=[1.5*dx, -1*dy, ex, ey],
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
              room_departure=R1,
              room_arrival=R5)
    D5 = Door(two_way=True,
              tree=get_tree(5),
              room_departure=R2,
              room_arrival=R5)
    D6 = Door(two_way=True,
              tree=get_tree(6),
              room_departure=R3,
              room_arrival=R6)
    D7 = Door(two_way=True,
              tree=get_tree(7),
              room_departure=R4,
              room_arrival=R6)
    D8 = Door(two_way=True,
              tree=get_tree(8),
              room_departure=R1,
              room_arrival=R2)
    D9 = Door(two_way=True,
              tree=get_tree(9),
              room_departure=R3,
              room_arrival=R4)
    D10 = Door(two_way=True,
              tree=get_tree(10),
              room_departure=R5,
              room_arrival=R6)
    if exit_number is None:
        D11 = Door(two_way=True,
                  tree=get_tree(11),
                  room_departure=R0,
                  room_arrival=RE)
    else:
        D11 = Door(two_way=True,
                  tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                            name='T11',
                            switches = Slist + [exit_number],
                            cut_expression=True),
                  room_departure=R0,
                  room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Random - Moser spindle',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)
    
    return level

get_color = Levels_colors_list.RANDOM

def f():
    return Maze.get_random_level_from_file(aux)