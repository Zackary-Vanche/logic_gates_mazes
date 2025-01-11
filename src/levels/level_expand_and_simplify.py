from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color
from random import shuffle as rd_shuffle

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')

    Slist = [S0, S1]
    
    sol_val_list = ['FF', 'FT', 'TF', 'TT']
    rd_shuffle(sol_val_list)
    
    sol_val = sol_val_list[0]
    sol = {'FF':'',
           'TF':'S0 ',
           'FT':'S1 ',
           'TT':'S0 S1 '}[sol_val] + 'D0 D1 D2'
        
    sol_val_list = sol_val_list[1:]
    assert len(sol_val_list) == 3
    
    T0 = Tree(tree_list=['NOT', Tree.tree_list_from_str(sol_val_list[0])],
                name='T0',
                switches=Slist)
    T1 = Tree(tree_list=['NOT', Tree.tree_list_from_str(sol_val_list[1])],
                name='T1',
                switches=Slist)
    T2 = Tree(tree_list=['NOT', Tree.tree_list_from_str(sol_val_list[2])],
                name='T2',
                switches=Slist)

    R0 = Room(name='R0',
                position=[0, 4, 3, 1],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[2, 2, 1, 1],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0, 2, 1, 1],
                switches_list=[])
    RE = Room(name='RE',
              position=[1, 0, 1, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2],
                 fastest_solution=sol,
                 level_color=get_color(),
                 name='Expand and simplify',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.1
    lcolor = Level_color(background_color=Color.color_hls(hu, li=0.5, sa=0.6),
                         room_color=Color.BLACK,
                         letters_color=Color.BLACK,
                         contour_color=Color.SILVER,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.IVORY)
    return lcolor