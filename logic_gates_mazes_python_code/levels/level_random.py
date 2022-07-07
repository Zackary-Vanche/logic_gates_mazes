# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:41:06 2022

@author: utilisateur
"""

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color
from random import sample
from random import choice

def random_treelist(depth=1):
    assert depth >= 1
    gates_name = ['AND', 'ANB', 'BNA', 'NOR', 'XOR', 'XNOR']#, 'OR', 'AONB', 'BONA', 'NAND']
    if depth == 1:
        return [choice(gates_name),
                [None],
                [None]]
    else:
        return [choice(gates_name),
                random_treelist(depth-1),
                random_treelist(depth-1)]

def aux_level_random():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    SN = Switch(name='1', value=1)
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7]
    
    depth = 2
    n_leafs = 2**depth
    
    T0 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T0',
              switches = sample(Slist, n_leafs))
    T1 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T1',
              switches = sample(Slist, n_leafs))
    T2 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T2',
              switches = sample(Slist, n_leafs))
    T3 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T3',
              switches = sample(Slist, n_leafs))
    T4 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T4',
              switches = sample(Slist, n_leafs))
    T5 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T5',
              switches = sample(Slist, n_leafs))
    T6 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T6',
              switches = sample(Slist, n_leafs))
    T7 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T7',
              switches = sample(Slist, n_leafs))
    T8 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T8',
              switches = sample(Slist, n_leafs))
    T9 = Tree(tree_list=random_treelist(1),
              empty=True,
              name='T9',
              switches = [S6, S7])
    T10 = Tree(tree_list=random_treelist(1),
              empty=True,
              name='T10',
              switches = [S6, S7])
    T11 = Tree(tree_list=random_treelist(1),
              empty=True,
              name='T11',
              switches = [S6, S7])
    T12 = Tree(tree_list=random_treelist(1),
              empty=True,
              name='T12',
              switches = [S6, S7])
    T13 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T13',
              switches = sample(Slist, n_leafs))
    T14 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T14',
              switches = sample(Slist, n_leafs))
    T15 = Tree(tree_list=random_treelist(depth),
              empty=True,
              name='T15',
              switches = sample(Slist, n_leafs))
    T16 = Tree(tree_list=[None],
              empty=True,
              name='T16',
              switches=[SN])
    # T17 = Tree(tree_list=random_treelist(depth),
    #           empty=True,
    #           name='T17',
    #           switches = sample(Slist, n_leafs))
    
    position_R0 = [7.25, 0, 2, 2]
    position_R1 = [3.75, 0, 2, 2]
    position_R2 = [-0.5, 4, 2, 2]
    position_R3 = [3.75, 8, 2, 2]
    position_R4 = [0.25, 0, 2, 2]
    position_R5 = [4.5, 4, 2, 2]
    position_R6 = [0.25, 8, 2, 2]
    position_R7 = [7.25, 8, 2, 2]
    position_RE = [8.75, 4.5, 1, 1]
    
    R0 = Room(name='R0',
              position=position_R0,
              switches_list=[S6])
    R1 = Room(name='R1',
              position=position_R1,
              switches_list=[S0])
    R2 = Room(name='R2',
              position=position_R2,
              switches_list=[S1])
    R3 = Room(name='R3',
              position=position_R3,
              switches_list=[S2])
    R4 = Room(name='R4',
              position=position_R4,
              switches_list=[S3])
    R5 = Room(name='R5',
              position=position_R5,
              switches_list=[S4])
    R6 = Room(name='R6',
              position=position_R6,
              switches_list=[S5])
    
    R7 = Room(name='R7',
              position=position_R7,
              switches_list=[S7])
    RE = Room(name='RE',
              position=position_RE,
              is_exit=True)   # E pour exit ou end
    
    D0 = Door(two_way=True,
              tree=T0,
              room_departure=R1,
              room_arrival=R4)
    D1 = Door(two_way=True,
              tree=T1,
              room_departure=R1,
              room_arrival=R5)
    D2 = Door(two_way=True,
              tree=T2,
              room_departure=R1,
              room_arrival=R6,
              relative_position=2/3)
    D3 = Door(two_way=True,
              tree=T3,
              room_departure=R2,
              room_arrival=R4)
    D4 = Door(two_way=True,
              tree=T4,
              room_departure=R2,
              room_arrival=R5,
              relative_position=2/3)
    D5 = Door(two_way=True,
              tree=T5,
              room_departure=R2,
              room_arrival=R6)
    D6 = Door(two_way=True,
              tree=T6,
              room_departure=R3,
              room_arrival=R4,
              relative_position=2/3)
    D7 = Door(two_way=True,
              tree=T7,
              room_departure=R3,
              room_arrival=R5)
    D8 = Door(two_way=True,
              tree=T8,
              room_departure=R3,
              room_arrival=R6)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R0,
              room_arrival=R1)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R0,
               room_arrival=R5,
               relative_departure_coordinates = [0, 1],
               relative_position = 0.4)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R5,
               room_arrival=R7,
               relative_arrival_coordinates = [0, 0],
               relative_position = 0.6)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R3,
               room_arrival=R7)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.1, 0],
               relative_arrival_coordinates = [0.1, 1],
               relative_position = 0.3)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.4, 0],
               relative_arrival_coordinates = [0.4, 1])
    D15 = Door(two_way=False,
               tree=T15,
               room_departure=R7,
               room_arrival=R0,
               relative_departure_coordinates = [0.7, 0],
               relative_arrival_coordinates = [0.7, 1],
               relative_position = 0.7)
    D16 = Door(two_way=False,
               tree=T16,
               room_departure=R0,
               room_arrival=RE,
               relative_departure_coordinates = [1, 1])
    # D17 = Door(two_way=False,
    #             tree=T17,
    #             room_departure=R7,
    #             room_arrival=RE,
    #             relative_departure_coordinates = [1, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16],
                 fastest_solution=None,#"S0 D0 S1 D1 S4 D4 S8 D4 D7 S3 D8 S11 D2 D3 S12 D3 S1 S7 D1 S4 S10 D7 S3 S9 D10 D11",
                 level_color=Levels_colors_list.RANDOM(),
                 uniform_surrounding_colors=False,
                 name='Random',
                 door_window_size=500,
                 border=100,
                 keep_proportions=False,
                 random=True)

    return level, D16, Slist

def level_random(verbose=0):
    # return aux_level_random()[0]
    print('level_random')
    level, D16, Slist = aux_level_random()
    sol = ""
    while len(sol.split(' ')) < 10:
        level, D16, Slist = aux_level_random()
        l = level.find_all_solutions(verbose=verbose,
                                     max_iter_without_many_solutions=500,
                                     min_solutions_to_find=5,
                                     max_iter=50000,
                                     min_sol_len=float('inf'))
        l.sort(key=lambda x : len(x.split(' ')))
        sol = l[-1]
        print(sol, len(sol.split(' ')) < 20)
    level, D16, Slist = aux_level_random()
    level.try_solution(sol, verbose=verbose)
    print('sol :', sol)
    print(len(sol.split(' ')))
    print('try_solution')
    door_trees_dico = {}
    level.try_solution(sol,
                       verbose=3,
                       allow_all_doors=True,
                       allow_all_switches=True,
                       door_trees_dico = door_trees_dico)
    print('try_solution')
    print(door_trees_dico)
    print(level.try_solution(sol, verbose=2))
    D16.tree = Tree(tree_list=Tree.tree_list_from_str(door_trees_dico['D16'][:-1]),
                    empty=True,
                    name='T16',
                    switches=Slist)
    print(level.try_solution(sol, verbose=2))
    print(sol)
    return level

if __name__ == '__main__':
    level_random()