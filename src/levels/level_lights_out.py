from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import choice as rd_choice
from Color import Color

def level_lights_out(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9', value=rd_choice([0, 1]))
    S10 = Switch(name='S10', value=rd_choice([0, 1]))
    S11 = Switch(name='S11', value=rd_choice([0, 1]))
    S12 = Switch(name='S12', value=rd_choice([0, 1]))
    S13 = Switch(name='S13', value=rd_choice([0, 1]))
    S14 = Switch(name='S14', value=rd_choice([0, 1]))
    S15 = Switch(name='S15', value=rd_choice([0, 1]))
    S16 = Switch(name='S16', value=rd_choice([0, 1]))
    S17 = Switch(name='S17', value=rd_choice([0, 1]))
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17]
    
    t0 = Tree.tree_list_not
    t1 = [None]

    T0 = Tree(tree_list=['EQU',
                         ['BIN',
                          t0, t0, t1,
                          t0, t1, t1,
                          t1, t1, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T0',
                switches=Slist)
    T1 = Tree(tree_list=['EQU',
                         ['BIN',
                          t0, t0, t0,
                          t1, t0, t1,
                          t1, t1, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T1',
                switches=Slist)
    T2 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t0, t0,
                          t1, t1, t0,
                          t1, t1, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T2',
                switches=Slist)
    T3 = Tree(tree_list=['EQU',
                         ['BIN',
                          t0, t1, t1,
                          t0, t0, t1,
                          t0, t1, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T3',
                switches=Slist)
    T4 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t0, t1,
                          t0, t0, t0,
                          t1, t0, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T4',
                switches=Slist)
    T5 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t1, t0,
                          t1, t0, t0,
                          t1, t1, t0],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T5',
                switches=Slist)
    T6 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t1, t1,
                          t0, t1, t1,
                          t0, t0, t1],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T6',
                switches=Slist)
    T7 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t1, t1,
                          t1, t0, t1,
                          t0, t0, t0],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T7',
                switches=Slist)
    T8 = Tree(tree_list=['EQU',
                         ['BIN',
                          t1, t1, t1,
                          t1, t1, t0,
                          t1, t0, t0],
                         Tree.tree_list_BIN(9)],
                empty=True,
                name='T8',
                switches=Slist)
    T9 = Tree(tree_list=['EQU', Tree.tree_list_BIN(9), Tree.tree_list_BIN(9)],
                empty=True,
                name='T9',
                switches=Slist)
    T10 = Tree(tree_list=['EQU', Tree.tree_list_BIN(18), [None]],
                empty=True,
                name='T10',
                switches=Slist + [0])

    R0 = Room(name='R0',
                position=[0, 2, 3, 3],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8])
    R1 = Room(name='R1',
                position=[0, 7.5, 3, 3],
                switches_list=[S9, S10, S11, S12, S13, S14, S15, S16, S17])
    RE = Room(name='RE',
              position=[1, 0.5, 1, 0.5],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0],
                relative_position=0.2)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/3, 1],
                relative_arrival_coordinates=[1/3, 0],
                relative_position=0.2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[2/3, 1],
                relative_arrival_coordinates=[2/3, 0],
                relative_position=0.2)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0],
                relative_position=0.5)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/3, 1],
                relative_arrival_coordinates=[1/3, 0],
                relative_position=0.5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[2/3, 1],
                relative_arrival_coordinates=[2/3, 0],
                relative_position=0.5)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 0],
                relative_position=0.8)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/3, 1],
                relative_arrival_coordinates=[1/3, 0],
                relative_position=0.8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[2/3, 1],
                relative_arrival_coordinates=[2/3, 0],
                relative_position=0.8)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1])
    
    lcolor = Levels_colors_list.FROM_HUE(hu=0.2, sa=0.5, li=0.9)
    lcolor.contour_color = Color.GREY_60
    lcolor.room_color = Color.BLACK
    lcolor.inside_room_color = Color.WHITE
    lcolor.surrounding_color = Color.WHITE
    # lcolor.letters_color = Color.BLACK

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Lights_out',
                 keep_proportions=True,
                 door_window_size=1000,
                 random=True)
    
    return level