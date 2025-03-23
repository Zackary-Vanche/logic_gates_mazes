from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Level_color import Level_color
from Color import Color

def f():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    tree_list = Tree.tree_list_from_str('TF')
    tree_list_4 = Tree.tree_list_from_str('FTT')

    T0 = Tree(tree_list=tree_list,  name='T0', switches=[S0, S3])
    T1 = Tree(tree_list=tree_list,  name='T1', switches=[S1, S4])
    T2 = Tree(tree_list=tree_list,  name='T2', switches=[S2, S5])
    T3 = Tree(tree_list=tree_list,  name='T3', switches=[S0, S3])
    T4 = Tree(tree_list=tree_list_4,  name='T4', switches=[S1, S4, S5])
    T5 = Tree(tree_list=tree_list,  name='T5', switches=[S2, S5])
    T6 = Tree(tree_list=Tree.tree_list_AND(6),  name='T6', switches=[S0, S1, S2, S3, S4, S5])

    position_R0 = [0, 0, 6, 1]
    position_R1 = [3, 2, 2, 1]
    position_R2 = [0, 4, 6, 1]
    position_RE = [1, 2, 1, 1]

    R0 = Room(name='R0', position=position_R0, switches_list=[S0, S3])
    R1 = Room(name='R1', position=position_R1, switches_list=[S1, S4])
    R2 = Room(name='R2', position=position_R2, switches_list=[S2, S5])
    RE = Room(name='RE', position=position_RE, is_exit=True)  # E pour exit ou end

    relative_departure_coordinates_D0 = [1 / 2, 1]
    relative_arrival_coordinates_D0 = [0, 0]
    relative_departure_coordinates_D1 = [0, 1]
    relative_arrival_coordinates_D1 = [1 / 2, 0]
    relative_departure_coordinates_D2 = [0.01, 0]
    relative_arrival_coordinates_D2 = [0.01, 1]
    relative_departure_coordinates_D3 = [1, 0]
    relative_arrival_coordinates_D3 = [5 / 6, 1]
    relative_departure_coordinates_D4 = [5 / 6, 0]
    relative_arrival_coordinates_D4 = [1, 1]
    relative_departure_coordinates_D5 = [0.99, 1]
    relative_arrival_coordinates_D5 = [0.99, 0]
    relative_departure_coordinates_D6 = [1.5 / 6, 1]
    relative_arrival_coordinates_D6 = [1 / 2, 0]

    D0 = Door(two_way=False,
              tree=T0, name='D0',
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D0,
              relative_arrival_coordinates=relative_arrival_coordinates_D0)
    D1 = Door(two_way=False,
              tree=T1, name='D1',
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D1,
              relative_arrival_coordinates=relative_arrival_coordinates_D1)
    D2 = Door(two_way=False,
              tree=T2,
              name='D2',
              room_departure=R2,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D2,
              relative_arrival_coordinates=relative_arrival_coordinates_D2)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R1,
              room_arrival=R0,
              relative_departure_coordinates=relative_departure_coordinates_D3,
              relative_arrival_coordinates=relative_arrival_coordinates_D3)
    D4 = Door(two_way=False,
              tree=T4,
              name='D4',
              room_departure=R2,
              room_arrival=R1,
              relative_departure_coordinates=relative_departure_coordinates_D4,
              relative_arrival_coordinates=relative_arrival_coordinates_D4)
    D5 = Door(two_way=False,
              tree=T5,
              name='D5',
              room_departure=R0,
              room_arrival=R2,
              relative_departure_coordinates=relative_departure_coordinates_D5,
              relative_arrival_coordinates=relative_arrival_coordinates_D5)
    D6 = Door(two_way=False,
              tree=T6,
              name='D6',
              room_departure=R0,
              room_arrival=RE,
              relative_departure_coordinates=relative_departure_coordinates_D6,
              relative_arrival_coordinates=relative_arrival_coordinates_D6)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6],
                 fastest_solution='S0 D0 S1 D1 S2 D2 D0 S1 S4 D3 D5 S5 D4 S1 D3 S3 D6',
                 level_color=get_color(),
                 name='Parallel',
                 door_window_size=450,
                 border=50)

    return level

def get_color():
    return Level_color(background_color=Color.color_hls(hu=0, li=0.2, sa=0.5),
                       room_color=Color.color_hls(hu=0, li=0.3, sa=0.5),
                       contour_color=Color.WHITE,
                       letters_color=Color.WHITE,
                       letter_contour_color=Color.WHITE)