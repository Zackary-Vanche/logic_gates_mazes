from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_eulerian():
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    
    T0   = Tree(tree_list=['AND', [None], [None], [None], [None], Tree.tree_list_NAND(2), Tree.tree_list_XNOR(2)],  
             name='T0',  switches = [S3, S11, S13, S14, S1, S10, S6, S12])
    T5  = Tree(tree_list=[None],   name='T5', switches = [S2])
    T7   = Tree(tree_list=[None],   name='T7',  switches = [S4])
    T11  = Tree(tree_list=[None],   name='T11', switches = [S8])
    T14  = Tree(tree_list=[None],   name='T14', switches = [S9])
    T17  = Tree(tree_list=[None],   name='T17', switches = [S13])

    T4   = Tree(tree_list=Tree.tree_list_not,   name='T4',  switches = [S2])
    T6   = Tree(tree_list=['AND', Tree.tree_list_not, Tree.tree_list_XOR(2), Tree.tree_list_XOR(2), Tree.tree_list_XOR(2)],
                  name='T6',  switches = [S3, S1, S6, S7, S10, S10, S12])
    T8   = Tree(tree_list=Tree.tree_list_not,   name='T8',  switches = [S4])
    T9   = Tree(tree_list=Tree.tree_list_not,   name='T9',  switches = [S9])
    T13  = Tree(tree_list=Tree.tree_list_not,   name='T13', switches = [S8])
    T18  = Tree(tree_list=Tree.tree_list_not,   name='T18', switches = [S13])
    
    T1   = Tree(tree_list=Tree.tree_list_from_str('TF'),   name='T1',  switches = [S0, S1])
    T3   = Tree(tree_list=[None],   name='T3',  switches = [S0])
    T15  = Tree(tree_list=Tree.tree_list_XOR(2),   name='T15', switches = [S5, S9])
    T10  = Tree(tree_list=Tree.tree_list_not,   name='T10', switches = [S5])
    T16  = Tree(tree_list=Tree.tree_list_NAND(2),   name='T16', switches = [S8, S14])
    T12  = Tree(tree_list=Tree.tree_list_XNOR(2),   name='T12', switches = [S8, S14])
    
    T2   = Tree(tree_list=Tree.tree_list_from_str('T'*6),   name='T2',  
            switches = [S0, S2, S3, S4, S8, S9])
    
    c = 2
    e = 0.15
    
    position_RE =  [12,  0,  c,  c]
    position_R0  = [ 8-e,  0-e,  c+2*e,  c+2*e]
    position_R1  = [ 4,  0,  c,  c]
    position_R2  = [ 0,  0,  c,  c]
    position_R3  = [12,  4,  c,  c]
    position_R4  = [ 8,  4,  c,  c]
    position_R5  = [ 4-e,  4-e,  c+2*e,  c+2*e]
    position_R6  = [ 0-e,  4-e,  c+2*e,  c+2*e]
    position_R7  = [12-e,  8-e,  c+2*e,  c+2*e]
    position_R8  = [ 8,  8,  c,  c]
    position_R9  = [ 4,  8,  c,  c]
    position_R10 = [ 0,  8,  c,  c]
    position_R11 = [12, 12,  c,  c]
    position_R12 = [ 8-e, 12-e,  c+2*e,  c+2*e]
    position_R13 = [ 4, 12,  c,  c]
    position_R14 = [ 0-e, 12-e,  c+2*e,  c+2*e]
    
    
    R0  = Room(name='R0',  position = position_R0,  switches_list = [S0])
    R1  = Room(name='R1',  position = position_R1,  switches_list = [S1])
    R2  = Room(name='R2',  position = position_R2,  switches_list = [S2])
    R3  = Room(name='R3',  position = position_R3,  switches_list = [S3])
    R4  = Room(name='R4',  position = position_R4,  switches_list = [S4])
    R5  = Room(name='R5',  position = position_R5,  switches_list = [S5])
    R6  = Room(name='R6',  position = position_R6,  switches_list = [S6])
    R7  = Room(name='R7',  position = position_R7,  switches_list = [S7])
    R8  = Room(name='R8',  position = position_R8,  switches_list = [S8])
    R9  = Room(name='R9',  position = position_R9,  switches_list = [S9])
    R10 = Room(name='R10', position = position_R10, switches_list = [S10])
    R11 = Room(name='R11', position = position_R11, switches_list = [S11])
    R12 = Room(name='R12', position = position_R12, switches_list = [S12])
    R13 = Room(name='R13', position = position_R13, switches_list = [S13])
    R14 = Room(name='R14', position = position_R14, switches_list = [S14])
    RE  = Room(name='RE', position = position_RE, is_exit = True) # E pour exit ou end
    
    b = False
    
    D0  = Door(two_way = b, tree = T0,  room_departure = R3, room_arrival = R0)
    D1  = Door(two_way = b, tree = T1,  room_departure = R0, room_arrival = R1)
    D2  = Door(two_way = b, tree = T2,  room_departure = R0, room_arrival = RE)
    D3  = Door(two_way = b, tree = T3,  room_departure = R1, room_arrival = R5)
    D4  = Door(two_way = b, tree = T4,  room_departure = R5, room_arrival = R2)
    D5  = Door(two_way = b, tree = T5,  room_departure = R2, room_arrival = R6)
    D6  = Door(two_way = b, tree = T6,  room_departure = R7, room_arrival = R3)
    D7  = Door(two_way = b, tree = T7,  room_departure = R4, room_arrival = R5)
    D8  = Door(two_way = b, tree = T8,  room_departure = R7, room_arrival = R4)
    D9  = Door(two_way = b, tree = T9,  room_departure = R5, room_arrival = R9) 
    D10 = Door(two_way = b, tree = T10, room_departure = R6, room_arrival = R10)
    D11 = Door(two_way = b, tree = T11, room_departure = R8, room_arrival = R7)
    D12 = Door(two_way = b, tree = T12, room_departure = R11, room_arrival = R7)
    D13 = Door(two_way = b, tree = T13, room_departure = R14, room_arrival = R8, 
           relative_departure_coordinates=[1,0], relative_arrival_coordinates=[0,1])
    D14 = Door(two_way = b, tree = T14, room_departure = R9, room_arrival = R14,
           relative_arrival_coordinates=[0.3, 0.5])
    D15 = Door(two_way = b, tree = T15, room_departure = R10, room_arrival = R14)
    D16 = Door(two_way = b, tree = T16, room_departure = R12, room_arrival = R11)
    D17 = Door(two_way = b, tree = T17, room_departure = R13, room_arrival = R12)
    D18 = Door(two_way = b, tree = T18, room_departure = R14, room_arrival = R13)
    
    level = Maze(start_room_index=0, 
             exit_room_index=-1, 
             rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, RE], 
             doors_list = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18], 
             fastest_solution="S0 D1 D3 D9 S9 D14 D18 S13 D17 S12 D16 S11 D12 S7 D8 S4 D7 D4 S2 D5 S6 D10 D15 S14 D13 S8 D11 D6 S3 D0 D2",
             level_color=Levels_colors_list.BLACK_AND_BLUE,
             name='Eulerian',
             door_window_size = 325,
             # print_tree_gap=28
             )
    
    return level