from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list
from numpy import cos, sin, pi

n_switches = 5
n_doors = 16

def aux_level_random_petersen(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
                        exit_number=None):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    Slist = [S0, S1, S2, S3, S4]
    
    assert len(Slist) == n_switches
    
    def get_tree(i):
        return Tree(['IN', Tree.tree_list_BIN(len(Slist))] + [[None]]*len(door_trees_list[i]),
                     empty=True,
                     name=f'T{i}',
                     switches = Slist + door_trees_list[i],
                     cut_expression=True)
    
    ex = 0.3
    ey = 0.3
    
    exs = 0.125
    eys = 0.125
    
    def pos(i):
        if i >= 5:
            a = pi/2 + 2*i*pi/5
            return [cos(a)-exs/2, sin(a)-eys/2, exs, eys]
        else:
            r = 1
            a = pi/2 + 2*i*pi/5 + pi/5
            return [r*cos(a)-ex/2, r*sin(a)-ey/2, ex, ey]
    exE = 0.4
    eyE = 0.4
    
    position_RE = [-exE/2, -eyE/2, exE, eyE]
    
    R0 = Room(name='R0',
              position = pos(0),
              switches_list = [S0])
    R1 = Room(name='R1',
              position = pos(1),
              switches_list = [S1])
    R2 = Room(name='R2',
              position = pos(2),
              switches_list = [S2])
    R3 = Room(name='R3',
              position = pos(3),
              switches_list = [S3])
    R4 = Room(name='R4',
              position = pos(4),
              switches_list = [S4])
    R5 = Room(name='R5',
              position = pos(5),
              switches_list = [])
    R6 = Room(name='R6',
              position = pos(6),
              switches_list = [])
    R7 = Room(name='R7',
              position = pos(7),
              switches_list = [])
    R8 = Room(name='R8',
              position = pos(8),
              switches_list = [])
    R9 = Room(name='R9',
              position = pos(9),
              switches_list = [])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    rp = 0.5
    rp0 = 0.33
    
    D0 = Door(two_way=True,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp0)
    D1 = Door(two_way=True,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp0)
    D2 = Door(two_way=True,
              tree=get_tree(2),
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp0)
    D3 = Door(two_way=True,
              tree=get_tree(3),
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp0)
    D4 = Door(two_way=True,
              tree=get_tree(4),
              room_departure=R4,
              room_arrival=R0,
              relative_position=rp0)
    D5 = Door(two_way=True,
              tree=get_tree(5),
              room_departure=R0,
              room_arrival=R5,
              relative_position=rp)
    D6 = Door(two_way=True,
              tree=get_tree(6),
              room_departure=R1,
              room_arrival=R6,
              relative_position=rp)
    D7 = Door(two_way=True,
              tree=get_tree(7),
              room_departure=R2,
              room_arrival=R7,
              relative_position=rp)
    D8 = Door(two_way=True,
              tree=get_tree(8),
              room_departure=R3,
              room_arrival=R8,
              relative_position=rp)
    D9 = Door(two_way=True,
              tree=get_tree(9),
              room_departure=R4,
              room_arrival=R9,
              relative_position=rp)
    D10 = Door(two_way=True,
               tree=get_tree(10),
               room_departure=R5,
               room_arrival=R7,
               relative_position=rp)
    D11 = Door(two_way=True,
               tree=get_tree(11),
               room_departure=R7,
               room_arrival=R9,
               relative_position=rp)
    D12 = Door(two_way=True,
               tree=get_tree(12),
               room_departure=R9,
               room_arrival=R6,
               relative_position=rp)
    D13 = Door(two_way=True,
               tree=get_tree(13),
               room_departure=R6,
               room_arrival=R8,
               relative_position=rp)
    D14 = Door(two_way=True,
               tree=get_tree(14),
               room_departure=R8,
               room_arrival=R5,
               relative_position=rp)
    if exit_number is None:
        D15 = Door(two_way=True,
                   tree=get_tree(15),
                   room_departure=R5,
                   room_arrival=RE,
                   relative_position=0.45)
    else:
        D15 = Door(two_way=True,
                   tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                             empty=True,
                             name='T15',
                             switches = Slist + [exit_number],
                             cut_expression=True),
                   room_departure=R5,
                   room_arrival=RE,
                   relative_position=0.45)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Petersen',
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level

def level_random_petersen():
    return Maze.get_random_level_from_file(aux_level_random_petersen)