# Problème de la couverture exacte d'un ensemble

# Solution
# 0 2 5
# 1 4
# 3 6 7

#S1 S3 S5

# 0 1     S0
# 0 2 5   S1
# 1 2 3   S2
# 1 4     S3
# 3 4 6   S4
# 3 6 7   S5
# 4 5     S6
# 4 6     S7
# 7 5     S8

#0 S0 S1
#1 S0 S2 S3
#2 S1 S1
#3 S2 S4 S5
#4 S3 S4 S4 S7
#5 S1 S6 S8
#6 S4 S5 S7
#7 S5 S8

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Level_color import Level_color
from Color import Color

def f():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    
    tree_list_0 = ["AND",
                   Tree.tree_list_XOR(2),
                   Tree.tree_list_XOR(3),
                   Tree.tree_list_XOR(2),
                   Tree.tree_list_XOR(3),
                   Tree.tree_list_XOR(4),
                   Tree.tree_list_XOR(3),
                   Tree.tree_list_XOR(3),
                   Tree.tree_list_XOR(2)]

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches = [S0, S1,
                          S0, S2, S3,
                          S1, S2,
                          S2, S4, S5,
                          S3, S4, S6, S7,
                          S1, S6, S8,
                          S4, S5, S7,
                          S5, S8],
              cut_expression=True)

    R0 = Room(name='R0',
              position = [3, 0, 1, 9],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7, S8])
    RE = Room(name='RE',
              position=[0, 7, 1, 1],
              is_exit=True)   # E pour exit ou end

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=[1/2, 3/4])

    level = Maze(start_room_index=0, 
                 exit_room_index=-1, 
                 rooms_list=[R0, RE], 
                 doors_list = [D0], 
                 fastest_solution='S1 S3 S5 D0',
                 level_color=get_color(),
                 name='Exact cover',
                 door_window_size = 500,
                 keep_proportions=True)

    return level

def get_color():
    return Level_color(background_color=Color.color_hls(hu=0.1, sa=0.5, li=0.2),
                       room_color=Color.PURE_ORANGE,
                       contour_color=Color.PURE_ORANGE,
                       letters_color=Color.WHITE,
                       inside_room_color=Color.BLACK,
                       letter_contour_color=Color.BLACK)