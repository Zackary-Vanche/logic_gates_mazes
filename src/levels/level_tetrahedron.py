from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tetrahedron(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    
    tree_list_0 = Tree.tree_list_from_str("TFTTFFFF FTTFFTTT")
    tree_list_1 = Tree.tree_list_from_str("FFFFTFFF FFTFFFFT")
    tree_list_2 = Tree.tree_list_from_str("FFTTTFFF TFTFFFFT TTTFTTTT")
    tree_list_3 = Tree.tree_list_from_str("FFTFFFTT TTTFTTFT")
    tree_list_4 = Tree.tree_list_from_str("TFTTFFFF TFTFTTFT")
    tree_list_5 = Tree.tree_list_from_str("FFTFTFFF TTTFTTTT")
    tree_list_6 = Tree.tree_list_from_str("TFTFTTFF")
    
    ls = [S0, S1, S2, S3, S4, S5, S6, S7]
    
    T0 = Tree(tree_list=tree_list_0,  name='T0', switches = ls[:]*2, cut_expression = True)
    T1 = Tree(tree_list=tree_list_1,  name='T1', switches = ls[:]*2, cut_expression = True)
    T2 = Tree(tree_list=tree_list_2,  name='T2', switches = ls[:]*3, cut_expression = True)
    T3 = Tree(tree_list=tree_list_3,  name='T3', switches = ls[:]*2, cut_expression = True)
    T4 = Tree(tree_list=tree_list_4,  name='T4', switches = ls[:]*2, cut_expression = True)
    T5 = Tree(tree_list=tree_list_5,  name='T5', switches = ls[:]*2, cut_expression = True)
    T6 = Tree(tree_list=tree_list_6,  name='T6', switches = ls[:])
    
    d = 3
    r = 1.25
    
    position_R0 = [   2,  5,  2,  2]
    position_R1 = [   0,  2,  2,  2]
    position_R2 = [   3,  0,  2,  2]
    position_R3 = [   5,  3,  2,  2]
    position_RE = [   d,  d,  r,  r]
    
    R0 = Room(name='R0', position = position_R0, switches_list = [S0, S4])
    R1 = Room(name='R1', position = position_R1, switches_list = [S1, S5])
    R2 = Room(name='R2', position = position_R2, switches_list = [S2, S6])
    R3 = Room(name='R3', position = position_R3, switches_list = [S3, S7])
    RE = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    d0 = 0.02
    d1 = 1-d0
    
    D0 = Door(two_way = True,
              tree = T0,
              room_departure = R0,
              room_arrival = R1, 
              relative_departure_coordinates = [d0, d1], 
              relative_arrival_coordinates = [d0, d1])
    D1 = Door(two_way = True, tree = T1, room_departure = R0, room_arrival = R2, 
          relative_departure_coordinates = [d0, d0], 
          relative_arrival_coordinates = [d0, d1])
    D2 = Door(two_way = True, tree = T2, room_departure = R0, room_arrival = R3, 
          relative_departure_coordinates = [d1, d1], 
          relative_arrival_coordinates = [d1, d1])
    D3 = Door(two_way = True, tree = T3, room_departure = R1, room_arrival = R2, 
          relative_departure_coordinates = [d0, d0], 
          relative_arrival_coordinates = [d0, d0])
    D4 = Door(two_way = True, tree = T4, room_departure = R1, room_arrival = R3, 
          relative_departure_coordinates = [d1, d0], 
          relative_arrival_coordinates = [d0, d0])
    D5 = Door(two_way = True, tree = T5, room_departure = R2, room_arrival = R3, 
          relative_departure_coordinates = [d1, d0], 
          relative_arrival_coordinates = [d1, d0])
    D6 = Door(two_way = True, tree = T6, room_departure = R3, room_arrival = RE,
          relative_departure_coordinates = [d0, d1], 
          relative_arrival_coordinates = [0.7, 0.7])
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, RE], 
             doors_list = [D0, D1, D2, D3, D4, D5, D6], 
             fastest_solution="S4 D1 S2 D5 S3 D2 S0 S4 D0 D4 S3 S7 D2 S0 D1 S6 D3 S1 S5 D0 S0 S4 D2 D5 S6 D3 S1 D4 S7 D6",
             level_color=Levels_colors_list.REALLY_BRIGHT_RED,
             name='Tetrahedron',
             border = 30,
             door_window_size = 400,
             keep_proportions = True,
             group='pure maze')
    
    return level
    
if __name__ == '__main__':
    # These 2 lines
    # calculates the values that doors
    # should have 
    # in order to the solution to be sol
    sol = "S4 D1 S2 D5 S3 D2 S0 S4 D0 D4 S3 S7 D2 S0 D1 S6 D3 S1 S5 D0 S0 S4 D2 D5 S6 D3 S1 D4 S7 D6"
    level_tetrahedron().try_solution(sol, verbose = 3, allow_all_doors=True, allow_all_switches=True)