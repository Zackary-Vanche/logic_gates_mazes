from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list
from random import randint as rd_randint

n_switches = 5
n_doors = 23

def level_sum():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    
    Slist = [S0, S1, S2, S3, S4]
    Slist_sum = [S1, S2, S3, S4]
    
    assert len(Slist) == n_switches
    
    V0 = Tree(tree_list=['SUM'] + [[None]] * 4,
              empty=True,
              name='V0',
              switches=Slist_sum)
    
    def tree_sum(i, name='T'):
        return Tree(['EQU',
                     [None],
                     [None]],
                     empty=True,
                     name=name,
                     switches = [V0, i],
                     cut_expression=True,
                     cut_expression_separator=')')
    
    def tree_open(name='T'):
        return Tree(tree_list=[None],
                    empty=True,
                    name=name,
                    switches = [1])
    
    ex = 0.5
    ey = 0.5
    
    R0 = Room(name='R0',
              position = [0, 3.25, ex, ey],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [2, 4, ex, ey],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [2, 3, ex, ey],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [2, 2, ex, ey],
              switches_list = [S3])
    R4 = Room(name='R4',
              position = [2, 1, ex, ey],
              switches_list = [S4])
    RE = Room(name='RE',
              position=[0, 2.25, ex, ey],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.6
    
    D0 = Door(two_way=False,
              tree=tree_open('T0'),
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=tree_open('T1'),
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=tree_open('T2'),
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=tree_open('T3'),
              room_departure=R0,
              room_arrival=R4,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=tree_open('T4'),
              room_departure=R1,
              room_arrival=R2)
    D5 = Door(two_way=False,
              tree=tree_open('T5'),
              room_departure=R2,
              room_arrival=R3)
    D6 = Door(two_way=False,
              tree=tree_open('T6'),
              room_departure=R3,
              room_arrival=R4)
    D7 = Door(two_way=False,
              tree=tree_sum(4, name='T7'),
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=tree_sum(3, name='T8'),
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp)
    D9 = Door(two_way=False,
              tree=tree_sum(2, name='T9'),
              room_departure=R3,
              room_arrival=R0,
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=tree_sum(1, name='T10'),
               room_departure=R4,
               room_arrival=R0,
               relative_position=rp)
    T11=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
             empty=True,
             name='T11',
             switches = Slist + [rd_randint(0, 2**4-1)],
             cut_expression=True)
    T11.name = 'T11'
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R0,
               room_arrival=RE,
               relative_position=0.5)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Sum',
                 door_window_size=375,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True,
                 intermediate_values_list=[V0])
    
    return level

# def level_random_sum():
#     # return aux_level_random_sum()
#     return Maze.get_random_level_from_file(aux_level_random_sum)