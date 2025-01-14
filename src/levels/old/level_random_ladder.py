from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def aux(door_trees_list = [[i for i in range(2**6)] for j in range(11)],
                            exit_number=None):
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    Slist = [S0, S1, S2, S3, S4, S5]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist)),
              name='V0',
              switches = Slist)
    
    def get_tree(i):
        try:
            return Tree(['IN', [None]] + [[None]]*len(door_trees_list[i]),
                        name=f'T{i}',
                        switches = [V0] + door_trees_list[i],
                        cut_expression=True,
                        cut_expression_separator=')')
        except:
            raise
    
    dx = 1.5
    dy = 1
    ex = 0.5
    ey = 0.5
    
    R0 = Room(name='R0',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[-0.25*dx, 2*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S2])
    
    R4 = Room(name='R4',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[S3])
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S4])
    R6 = Room(name='R6',
                position=[1.25*dx, 1*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[S5])
    
    RE = Room(name='RE',
              position=[2*dx, dy/2, ex, ey],
              is_exit=True)
    
    D0 = Door(two_way=True,
                tree=get_tree(0),
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=True,
                tree=get_tree(1),
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=get_tree(2),
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    
    D3 = Door(two_way=True,
                tree=get_tree(3),
                name='D3',
                room_departure=R4,
                room_arrival=R5)
    D4 = Door(two_way=True,
                tree=get_tree(4),
                name='D4',
                room_departure=R5,
                room_arrival=R6)
    D5 = Door(two_way=True,
                tree=get_tree(5),
                name='D5',
                room_departure=R6,
                room_arrival=R7)
    
    D6 = Door(two_way=True,
                tree=get_tree(6),
                name='D6',
                room_departure=R0,
                room_arrival=R4)
    D7 = Door(two_way=True,
                tree=get_tree(7),
                name='D7',
                room_departure=R1,
                room_arrival=R5)
    D8 = Door(two_way=True,
                tree=get_tree(8),
                name='D8',
                room_departure=R2,
                room_arrival=R6)
    D9 = Door(two_way=True,
                tree=get_tree(9),
                name='D9',
                room_departure=R3,
                room_arrival=R7)
    if exit_number is None:
        D10 = Door(two_way=True,
                    tree=get_tree(10),
                    name='D10',
                    room_departure=R7,
                    room_arrival=RE)
    else:
        D10 = Door(two_way=True,
                  tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                            name='T10',
                            switches = Slist + [exit_number],
                            cut_expression=True),
                  room_departure=R3,
                  room_arrival=RE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Ladder',
                 door_window_size=450,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)

    return level

get_color = Levels_colors_list.RANDOM

def f():
    return Maze.get_random_level_from_file(aux)
