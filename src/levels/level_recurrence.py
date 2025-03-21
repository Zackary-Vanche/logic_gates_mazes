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
    S2=Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    
    tree_list_0 = Tree.tree_list_OR(4)
    tree_list_1 = [None]
    tree_list_2 = ['AND', Tree.tree_list_not, Tree.tree_list_OR(3)]
    tree_list_3 = [None]
    tree_list_4 = ['AND', Tree.tree_list_NOR(2), Tree.tree_list_OR(2)]
    tree_list_5 = [None]
    # tree_list_6 = ['BNA', Tree.tree_list_or_3, Tree.tree_list_and_4]
    tree_list_6 = Tree.tree_list_from_str('F'*7)
    
    T0 = Tree(tree_list=tree_list_0,  name='T0', switches = [S0, S2, S4, S6])
    T1 = Tree(tree_list=tree_list_1,  name='T1', switches = [S1])
    T2 = Tree(tree_list=tree_list_2,  name='T2', switches = [S0, S2, S4, S6])
    T3 = Tree(tree_list=tree_list_3,  name='T3', switches = [S3])
    T4 = Tree(tree_list=tree_list_4,  name='T4', switches = [S0, S2, S4, S6])
    T5 = Tree(tree_list=tree_list_5,  name='T5', switches = [S5])
    T6 = Tree(tree_list=tree_list_6,  name='T6', switches = [S0, S1, S2, S3, S4, S5, S6])
    
    position_R0 = [0,4,2,2]
    position_R1 = [0,0,2,2]
    position_R2 = [4,0,2,2]
    position_R3 = [4,4,2,2]
    position_RE = [2.5,2.5,1,1]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0, S1])
    R1 = Room(name='R1', position = position_R1, switches_list = [S2, S3])
    R2 = Room(name='R2', position = position_R2, switches_list = [S4, S5])
    R3 = Room(name='R3', position = position_R3, switches_list = [S6])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    relative_departure_coordinates_D0 = [1/3,   0]
    relative_arrival_coordinates_D0   = [1/3,   1]
    relative_departure_coordinates_D1 = [2/3,   1]
    relative_arrival_coordinates_D1   = [2/3,   0]
    relative_departure_coordinates_D2 = [  1, 1/3]
    relative_arrival_coordinates_D2   = [  0, 1/3]
    relative_departure_coordinates_D3 = [  0, 2/3]
    relative_arrival_coordinates_D3   = [  1, 2/3]
    relative_departure_coordinates_D4 = [2/3,   1]
    relative_arrival_coordinates_D4   = [2/3,   0]
    relative_departure_coordinates_D5 = [1/3,   0]
    relative_arrival_coordinates_D5   = [1/3,   1]
    relative_departure_coordinates_D6 = [  0,   0]
    relative_arrival_coordinates_D6   = [0.85, 0.85]
    
    D0 = Door(two_way = False, 
          tree = T0, 
          name='D0', 
          room_departure = R0, 
          room_arrival = R1,
          relative_departure_coordinates = relative_departure_coordinates_D0,
          relative_arrival_coordinates = relative_arrival_coordinates_D0)
    D1 = Door(two_way = False, 
          tree = T1, 
          name='D1', 
          room_departure = R1, 
          room_arrival = R0,
          relative_departure_coordinates = relative_departure_coordinates_D1,
          relative_arrival_coordinates = relative_arrival_coordinates_D1)
    D2 = Door(two_way = False, 
          tree = T2, 
          name='D2', 
          room_departure = R1, 
          room_arrival = R2,
          relative_departure_coordinates = relative_departure_coordinates_D2,
          relative_arrival_coordinates = relative_arrival_coordinates_D2)
    D3 = Door(two_way = False, 
          tree = T3, 
          name='D3', 
          room_departure = R2, 
          room_arrival = R1,
          relative_departure_coordinates = relative_departure_coordinates_D3,
          relative_arrival_coordinates = relative_arrival_coordinates_D3)
    D4 = Door(two_way = False, 
          tree = T4, 
          name='D4', 
          room_departure = R2, 
          room_arrival = R3,
          relative_departure_coordinates = relative_departure_coordinates_D4,
          relative_arrival_coordinates = relative_arrival_coordinates_D4)
    D5 = Door(two_way = False, 
          tree = T5, 
          name='D5', 
          room_departure = R3, 
          room_arrival = R2,
          relative_departure_coordinates = relative_departure_coordinates_D5,
          relative_arrival_coordinates = relative_arrival_coordinates_D5)
    D6 = Door(two_way = False, 
          tree = T6, 
          name='D6', room_departure = R3, 
          room_arrival = RE,
          relative_departure_coordinates = relative_departure_coordinates_D6,
          relative_arrival_coordinates = relative_arrival_coordinates_D6)
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, RE], 
             doors_list = [D0, D1, D2, D3, D4, D5, D6], 
             fastest_solution='S0 S1 D0 S2 S3 D1 S0 S1 D0 D2 S4 S5 D3 S2 S3 D2 D4 S6 D5 S4 S5 D4 S6 D6',
             level_color=get_color(),
             name='Recurrence',
             border = 55)
    
    return level

def get_color():
    return Level_color(background_color=Color.BLACK,
                       room_color=[40]*3,
                       contour_color=Color.BRIGHT_RED,
                       letters_color=Color.WHITE,
                       inside_room_color=Color.WHITE,
                       letter_contour_color=Color.BLACK,
                       surrounding_color=Color.BRIGHT_RED)