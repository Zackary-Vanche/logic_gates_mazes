from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list
from numpy import cos, sin, pi

n_switches = 5
n_doors = 26

def aux(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
                        exit_number=None,
                        exit_door=None):

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
    
    def pos(i):
        a = pi/2 + 2*i*pi/5
        return [cos(a)-ex/2, sin(a)-ey/2, ex, ey]
    
    exE = 0.6
    eyE = 0.6
    
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
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    rp1 = 0.25
    rp2 = 0.25
    rpE = 0.55
    
    D0 = Door(two_way=False,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp1)
    D1 = Door(two_way=False,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp1)
    D2 = Door(two_way=False,
              tree=get_tree(2),
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp2)
    D3 = Door(two_way=False,
              tree=get_tree(3),
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp2)
    D4 = Door(two_way=False,
              tree=get_tree(4),
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp2)
    D5 = Door(two_way=False,
              tree=get_tree(5),
              room_departure=R3,
              room_arrival=R0,
              relative_position=rp2)
    D6 = Door(two_way=False,
              tree=get_tree(6),
              room_departure=R0,
              room_arrival=R4,
              relative_position=rp1)
    D7 = Door(two_way=False,
              tree=get_tree(7),
              room_departure=R4,
              room_arrival=R0,
              relative_position=rp1)
    D8 = Door(two_way=False,
              tree=get_tree(8),
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp1)
    D9 = Door(two_way=False,
              tree=get_tree(9),
              room_departure=R2,
              room_arrival=R1,
              relative_position=rp1)
    D10 = Door(two_way=False,
               tree=get_tree(10),
               room_departure=R1,
               room_arrival=R3,
               relative_position=rp2)
    D11 = Door(two_way=False,
               tree=get_tree(11),
               room_departure=R3,
               room_arrival=R1,
               relative_position=rp2)
    D12 = Door(two_way=False,
               tree=get_tree(12),
               room_departure=R1,
               room_arrival=R4,
               relative_position=rp2)
    D13 = Door(two_way=False,
               tree=get_tree(13),
               room_departure=R4,
               room_arrival=R1,
               relative_position=rp2)
    D14 = Door(two_way=False,
               tree=get_tree(14),
               room_departure=R2,
               room_arrival=R3,
               relative_position=rp1)
    D15 = Door(two_way=False,
               tree=get_tree(15),
               room_departure=R3,
               room_arrival=R2,
               relative_position=rp1)
    D16 = Door(two_way=False,
               tree=get_tree(16),
               room_departure=R2,
               room_arrival=R4,
               relative_position=rp2)
    D17 = Door(two_way=False,
               tree=get_tree(17),
               room_departure=R4,
               room_arrival=R2,
               relative_position=rp2)
    D18 = Door(two_way=False,
               tree=get_tree(18),
               room_departure=R3,
               room_arrival=R4,
               relative_position=rp1)
    D19 = Door(two_way=False,
               tree=get_tree(19),
               room_departure=R4,
               room_arrival=R3,
               relative_position=rp1)
    if exit_number is None:
        T20 = get_tree(20)
        T21 = get_tree(21)
        T22 = get_tree(22)
        T23 = get_tree(23)
        T24 = get_tree(24)
    else:
        assert exit_door != None
        T20 = Tree([None],
                   name='T20',
                   switches = [exit_door==20],
                   cut_expression=True)
        T21 = Tree([None],
                   name='T21',
                   switches = [exit_door==21],
                   cut_expression=True)
        T22 = Tree([None],
                   name='T22',
                   switches = [exit_door==22],
                   cut_expression=True)
        T23 = Tree([None],
                   name='T23',
                   switches = [exit_door==23],
                   cut_expression=True)
        T24 = Tree([None],
                   name='T24',
                   switches = [exit_door==24],
                   cut_expression=True)
    D20 = Door(two_way=False,
               tree=T20,
               room_departure=R0,
               room_arrival=RE,
               relative_position=rpE)
    D21 = Door(two_way=False,
               tree=T21,
               room_departure=R1,
               room_arrival=RE,
               relative_position=rpE)
    D22 = Door(two_way=False,
               tree=T22,
               room_departure=R2,
               room_arrival=RE,
               relative_position=rpE)
    D23 = Door(two_way=False,
               tree=T23,
               room_departure=R3,
               room_arrival=RE,
               relative_position=rpE)
    D24 = Door(two_way=False,
               tree=T24,
               room_departure=R4,
               room_arrival=RE,
               relative_position=rpE)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - K5',
                 random=True,
                 door_window_size=500,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random_several_exit=True,
                 exit_doors_indexes=[20, 21, 22, 23, 24])
    
    return level

get_color = Levels_colors_list.RANDOM

def f():
    return Maze.get_random_level_from_file(aux)
    