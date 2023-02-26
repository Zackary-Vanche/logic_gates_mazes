# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:12:30 2023

@author: utilisateur
"""

from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list
from numpy import sqrt

n_switches = 4
n_doors = 100

def aux_level_random_cuboctahedron(door_trees_list = [[i for i in range(2**n_switches)] for j in range(n_doors)],
                                   exit_number=None):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    Slist = [S0, S1, S2, S3]
    
    assert len(Slist) == n_switches
    
    def get_tree(i):
        return Tree(['IN', Tree.tree_list_BIN(len(Slist))] + [[None]]*len(door_trees_list[i]),
                     empty=True,
                     name=f'T{i}',
                     switches = Slist + door_trees_list[i],
                     cut_expression=True)
    
    ex = 1
    ey = 1
    
    R0 = Room(name='R0',
              position = [1, 1, ex, ey],
              switches_list = [])
    R1 = Room(name='R1',
              position = [0, 3, ex, ey],
              switches_list = [])
    R2 = Room(name='R2',
              position = [3, 0, ex, ey],
              switches_list = [])
    R3 = Room(name='R3',
              position = [2, 2, ex, ey],
              switches_list = [S0])
    R4 = Room(name='R4',
              position = [1, 5, ex, ey],
              switches_list = [])
    R5 = Room(name='R5',
              position = [2, 4, ex, ey],
              switches_list = [S2])
    R6 = Room(name='R6',
              position = [4, 2, ex, ey],
              switches_list = [S1])
    R7 = Room(name='R7',
              position = [5, 1, ex, ey],
              switches_list = [])
    R8 = Room(name='R8',
              position = [4, 4, ex, ey],
              switches_list = [S3])
    R9 = Room(name='R9',
              position = [3, 6, ex, ey],
              switches_list = [])
    R10 = Room(name='R10',
              position = [6, 3, ex, ey],
              switches_list = [])
    R11 = Room(name='R11',
              position = [5, 5, ex, ey],
              switches_list = [])
    RE = Room(name='RE',
              position=[3+1/2-sqrt(2)/2, 3+1/2-sqrt(2)/2, sqrt(2), sqrt(2)],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.5
    
    D0 = Door(two_way=False,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=get_tree(1),
              room_departure=R2,
              room_arrival=R7,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=get_tree(2),
              room_departure=R7,
              room_arrival=R10,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=get_tree(3),
              room_departure=R10,
              room_arrival=R11,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=get_tree(4),
              room_departure=R11,
              room_arrival=R9,
              relative_position=rp)
    D5 = Door(two_way=False,
              tree=get_tree(5),
              room_departure=R9,
              room_arrival=R4,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=get_tree(6),
              room_departure=R4,
              room_arrival=R1,
              relative_position=rp)
    D7 = Door(two_way=False,
              tree=get_tree(7),
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=get_tree(8),
              room_departure=R0,
              room_arrival=R7,
              relative_position=rp)
    D9 = Door(two_way=False,
              tree=get_tree(9),
              room_departure=R7,
              room_arrival=R11,
              relative_position=rp)
    D10 = Door(two_way=False,
                tree=get_tree(10),
                room_departure=R11,
                room_arrival=R4,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=get_tree(11),
                room_departure=R4,
                room_arrival=R0,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=get_tree(12),
                room_departure=R1,
                room_arrival=R3,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=get_tree(13),
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=get_tree(14),
                room_departure=R2,
                room_arrival=R6,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=get_tree(15),
                room_departure=R6,
                room_arrival=R10,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=get_tree(16),
                room_departure=R10,
                room_arrival=R8)
    D17 = Door(two_way=False,
                tree=get_tree(17),
                room_departure=R8,
                room_arrival=R9)
    D18 = Door(two_way=False,
                tree=get_tree(18),
                room_departure=R9,
                room_arrival=R5)
    D19 = Door(two_way=False,
                tree=get_tree(19),
                room_departure=R5,
                room_arrival=R1)
    D20 = Door(two_way=False,
                tree=get_tree(20),
                room_departure=R3,
                room_arrival=R6)
    D21 = Door(two_way=False,
                tree=get_tree(21),
                room_departure=R6,
                room_arrival=R8)
    D22 = Door(two_way=False,
                tree=get_tree(22),
                room_departure=R8,
                room_arrival=R5)
    D23 = Door(two_way=False,
                tree=get_tree(23),
                room_departure=R5,
                room_arrival=R3)
    if exit_number is None:
        D24 = Door(two_way=False,
                    tree=get_tree(24),
                    room_departure=R1,
                    room_arrival=RE,
                    relative_position=0.5)
    else:
        D24 = Door(two_way=False,
                    tree=Tree(['IN', Tree.tree_list_BIN(len(Slist)), [None]],
                              empty=True,
                              name=f'T{24}',
                              switches = Slist + [exit_number],
                              cut_expression=True),
                    room_departure=R1,
                    room_arrival=RE,
                    relative_position=0.5)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24],
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Cuboctahedron',
                 door_window_size=700,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level

def level_random_cuboctahedron():
    # return aux_level_random_cuboctahedron()
    return Maze.get_random_level_from_file(aux_level_random_cuboctahedron)