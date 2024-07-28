from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice

# Problème 3-SAT
def level_3sat():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')

    Slist = [S0, S1, S2]

    l = ['FFF', 'TFF',
         'FTF', 'TTF',
         'FFT', 'TFT',
         'FTT', 'TTT']
    assert len(set(l)) == 8
    
    bool_sol = rd_choice(l)
    
    opposite_bool = ''
    for c in bool_sol:
        if c == 'F':
            opposite_bool += 'T'
        if c == 'T':
            opposite_bool += 'F'
    l.remove(opposite_bool)

    CNF_expression = ' '.join(l)
    
    sol = ''
    for i in range(3):
        if bool_sol[i] == 'T':
            sol += Slist[i].name + ' '
    sol += 'D0'

    T0 = Tree(tree_list=Tree.tree_list_from_str(CNF_expression, CNF=True),
              name='T0',
              switches=Slist*7,
              cut_expression=True)

    R0 = Room(name='R0',
              position=[0, 0, 2, 3],
              switches_list=Slist)
    RE = Room(name='RE',
              position=[0, 4, 2, 1],
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1 / 2, 1],
              relative_arrival_coordinates=[1 / 2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, RE],
                 doors_list=[D0],
                 fastest_solution=sol,
                 level_color=Levels_colors_list.WHITE_AND_BLACK,
                 name='3 SAT',
                 door_window_size=530,
                 keep_proportions=True)

    return level