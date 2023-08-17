from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_strange(a=1, b=1, c=1, d=1):

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')

    tree_list_MOD = ['MOD', Tree.tree_list_BIN(8), [None]]
    tree_list_EQU = ['EQU', tree_list_MOD, [None]]
    tree_list_0 = ['AND'] + [tree_list_EQU]*2
    
    a, b, c, d = 5, 2, 3, 0

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches = [S0, S1, S2, S3, S4, S5, S6, S7,
                          Switch(value=a),
                          Switch(value=b),
                          S1, S3, S5, S7, S0, S2, S4, S6,
                          Switch(value=c),
                          Switch(value=d),],
              cut_expression=True)

    R0 = Room(name='R0',
              position = [0, 2, 2, 4],
              switches_list = [S0, S1, S2, S3, S4, S5, S6, S7])
    RE = Room(name='RE',
              position=[-3, 0, 8, 1],
              is_exit=True)   # E pour exit ou end

    rp = 1/2

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=RE,
              relative_position=rp,
              relative_departure_coordinates=[1 / 2, 0],
              relative_arrival_coordinates=[1 / 2, 1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0] + [RE],
                 doors_list=[D0],
                 fastest_solution="S1 S2 S5 S6 D0",
                 level_color=Levels_colors_list.FROM_HUE(hu=0.3, sa=0.4, li=0.7),
                 name='Strange',
                 door_window_size=400,
                 keep_proportions=True,
                 y_separation=40,
                 border=40)
    
    return level