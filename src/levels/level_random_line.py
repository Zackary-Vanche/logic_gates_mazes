from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

n_switches = 6

def aux(door_trees_list = [[i for i in range(2**n_switches)] for j in range(6)],
                          exit_number=None):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    
    Slist = [S0, S1, S2, S3, S4, S5]
    
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
    
    dy = 2
    ey = 0.75
    
    R0 = Room(name='R0',
              position = [0, 0, 1, ey],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [0, dy, 1, ey],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [0, 2*dy, 1, ey],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [0, 3*dy, 1, ey],
              switches_list = [S3])
    R4 = Room(name='R4',
              position = [0, 4*dy, 1, ey],
              switches_list = [S4])
    R5 = Room(name='R5',
              position = [0, 5*dy, 1, ey],
              switches_list = [S5])
    RE = Room(name='RE',
              position=[0, 6*dy, 1, ey],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.5
    
    D0 = Door(two_way=True,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=True,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D2 = Door(two_way=True,
              tree=get_tree(2),
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp)
    D3 = Door(two_way=True,
                tree=get_tree(3),
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D4 = Door(two_way=True,
                tree=get_tree(4),
                room_departure=R4,
                room_arrival=R5,
                relative_position=rp)
    if exit_number is None:
        D5 = Door(two_way=True,
                  tree=get_tree(5),
                  room_departure=R5,
                  room_arrival=RE,
                  relative_position=rp)
    else:
        D5 = Door(two_way=True,
                  tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                            name='T5',
                            switches = Slist + [exit_number],
                            cut_expression=True),
                  room_departure=R5,
                  room_arrival=RE,
                  relative_position=rp)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Line',
                 door_window_size=300,
                 keep_proportions=False,
                 y_separation=40,
                 border=40,
                 random=True)
    
    return level

def f():
    return Maze.get_random_level_from_file(aux)