from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

n_switches = 5
n_doors = 15

def aux_level_random_come_back(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
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
    
    position_R0 = [4, 3, 2, 2]
    position_R1 = [8, 6, 2, 2]
    position_R2 = [6, 10, 2, 2]
    position_R3 = [2, 10, 2, 2]
    position_R4 = [0, 6, 2, 2]
    position_RE = [0, 3.5, 1, 1]
    
    R0 = Room(name='R0',
              position = position_R0,
              switches_list = [S0])
    R1 = Room(name='R1',
              position = position_R1,
              switches_list = [S1])
    R2 = Room(name='R2',
              position = position_R2,
              switches_list = [S2])
    R3 = Room(name='R3',
              position = position_R3,
              switches_list = [S3])
    R4 = Room(name='R4',
              position = position_R4,
              switches_list = [S4])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    rp = 0.4
    
    D0 = Door(two_way=False,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=get_tree(2),
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=get_tree(3),
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=get_tree(4),
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D5 = Door(two_way=False,
              tree=get_tree(5),
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=get_tree(6),
              room_departure=R2,
              room_arrival=R1,
              relative_position=rp)
    D7 = Door(two_way=False,
              tree=get_tree(7),
              room_departure=R3,
              room_arrival=R0,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=get_tree(8),
              room_departure=R3,
              room_arrival=R1,
              relative_position=rp)
    D9 = Door(two_way=False,
               tree=get_tree(9),
               room_departure=R3,
               room_arrival=R2,
               relative_position=rp)
    D10 = Door(two_way=False,
               tree=get_tree(10),
               room_departure=R4,
               room_arrival=R0,
               relative_position=0.45)
    D11 = Door(two_way=False,
                tree=get_tree(11),
                room_departure=R4,
                room_arrival=R1,
                relative_position=0.25)
    D12 = Door(two_way=False,
                tree=get_tree(12),
                room_departure=R4,
                room_arrival=R2,
                relative_position=0.25)
    D13 = Door(two_way=False,
                tree=get_tree(13),
                room_departure=R4,
                room_arrival=R3,
                relative_position=rp)
    if exit_number is None:
        D14 = Door(two_way=False,
                  tree=get_tree(14),
                  room_departure=R4,
                  room_arrival=RE,
                  relative_position=0.6)
    else:
        D14 = Door(two_way=False,
                  tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                            empty=True,
                            name='T14',
                            switches = Slist + [exit_number],
                            cut_expression=True),
                  room_departure=R4,
                  room_arrival=RE,
                  relative_position=0.6)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14,],#,  D15, D16, D17, D18, D19, D20],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Come back',
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True)
    
    return level

def level_random_come_back():
    return Maze.get_random_level_from_file(aux_level_random_come_back)