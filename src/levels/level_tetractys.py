from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Graph import Graph
from random import shuffle as rd_shuffle
from Color import Color

def level_tetractys(fast_solution_finding=False): 

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
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    
    # Choice of a random spanning tree
    
    l_weights = [i+1 for i in range(127)]
    rd_shuffle(l_weights)
    l_weights = l_weights[:24]
    
    doors_dico = {('R2', 'R1') : 'D1',
                  ('R3', 'R1') : 'D2',
                  ('R3', 'R2') : 'D3',
                  ('R4', 'R2') : 'D4',
                  ('R5', 'R2') : 'D5',
                  ('R5', 'R3') : 'D6',
                  ('R6', 'R3') : 'D7',
                  ('R5', 'R4') : 'D8',
                  ('R7', 'R4') : 'D9',
                  ('R8', 'R4') : 'D10',
                  ('R6', 'R5') : 'D11',
                  ('R8', 'R5') : 'D12',
                  ('R9', 'R5') : 'D13',
                  ('R9', 'R6') : 'D14',
                  ('R10', 'R6') : 'D15',
                  ('R8', 'R7') : 'D16',
                  ('R9', 'R8') : 'D17',
                  ('R10', 'R9') : 'D18',}
    doors_dico_keys = list(doors_dico.keys())
    
    rooms_names_set = set()
    for couple in doors_dico_keys:
        ra, rd = couple
        rooms_names_set.add(ra)
        rooms_names_set.add(rd)
    rooms_names_list = list(rooms_names_set)
    rooms_names_list.sort(key = lambda x : int(x.replace('R', '')))
    
    room_door_list = []
    for room_name in rooms_names_list:
        room_door_list.append([])
        for couple in doors_dico_keys:
            if room_name in couple:
                room_door_list[-1].append(doors_dico[couple])
        room_door_list[-1] = list(set(room_door_list[-1]))
    
    edges = []
    
    for i in range(len(doors_dico_keys)):
        [ra, rd] = doors_dico_keys[i]
        edges.append((ra, rd, l_weights[i]))

    k_list = list(doors_dico.keys())
    for k in k_list:
        ra, rd = k
        doors_dico[(rd, ra)] = doors_dico[k]
    
    mst_door_names_set = set()
    g = Graph()
    g.add_edge_list(edges)
    dico = g.kruskals_mst()
    mst = dico['mst']
    for i in range(len(mst)):
        ra, rd, w = mst[i]
        door_name = doors_dico[(ra, rd)]
        mst_door_names_set.add(door_name)
        
    # Calculation of l_count
    # print(mst_door_names_set) # List of the doors you should take

    l_count = [0 for i in range(len(room_door_list))]
    for i in range(len(room_door_list)):
        for door_name in room_door_list[i]:
            l_count[i] += door_name in mst_door_names_set

    tree_list_0 = ['AND']
    for l in room_door_list:
        k = len(l)
        tree_list_0.append(['EQU', Tree.tree_list_SUM(k), [None]])
        
    if fast_solution_finding:
        possible_switches_values = [[1]]
    else:
        possible_switches_values = None

    T0 = Tree(tree_list=tree_list_0,
              name='T0',
              switches=[S0, S1, l_count[0],
                        S0, S2, S3, S4, l_count[1],
                        S1, S2, S5, S6, l_count[2],
                        S3, S7, S8, S9, l_count[3],
                        S4, S5, S7, S10, S11, S12, l_count[4],
                        S6, S10, S13, S14, l_count[5],
                        S8, S15, l_count[6],
                        S9, S11, S15, S16, l_count[7],
                        S12, S13, S16, S17, l_count[8],
                        S14, S17, l_count[9],],
              cut_expression_depth_1=True)
    T1 = Tree(tree_list=[None],
              name='T1',
              switches=[S0])
    T2 = Tree(tree_list=[None],
              name='T2',
              switches=[S1])
    T3 = Tree(tree_list=[None],
              name='T3',
              switches=[S2])
    T4 = Tree(tree_list=[None],
              name='T4',
              switches=[S3])
    T5 = Tree(tree_list=[None],
              name='T5',
              switches=[S4])
    T6 = Tree(tree_list=[None],
              name='T6',
              switches=[S5])
    T7 = Tree(tree_list=[None],
              name='T7',
              switches=[S6])
    T8 = Tree(tree_list=[None],
              name='T8',
              switches=[S7])
    T9 = Tree(tree_list=[None],
              name='T9',
              switches=[S8])
    T10 = Tree(tree_list=[None],
               name='T10',
               switches=[S9])
    T11 = Tree(tree_list=[None],
               name='T11',
               switches=[S10])
    T12 = Tree(tree_list=[None],
               name='T12',
               switches=[S11])
    T13 = Tree(tree_list=[None],
               name='T13',
               switches=[S12])
    T14 = Tree(tree_list=[None],
               name='T14',
               switches=[S13])
    T15 = Tree(tree_list=[None],
               name='T15',
               switches=[S14])
    T16 = Tree(tree_list=[None],
               name='T16',
               switches=[S15])
    T17 = Tree(tree_list=[None],
               name='T17',
               switches=[S16])
    T18 = Tree(tree_list=[None],
               name='T18',
               switches=[S17])
    T19 = Tree(tree_list=Tree.tree_list_AND(10),
               name='T19',
               switches=[S18, S19, S20, S21, S22, S23, S24, S25, S26, S27])

    dx = 0.5
    dy = (3)**0.5 / 2
    ex = 0.4
    ey = 0.4

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, 3*dx, 2*dy],
                switches_list=[S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17])
    R1 = Room(name='R1',
                position=[5*dx, 0*dy, ex, ey],
                switches_list=[S18],
                possible_switches_values=possible_switches_values)
    R2 = Room(name='R2',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[S19],
                possible_switches_values=possible_switches_values)
    R3 = Room(name='R3',
                position=[6*dx, 1*dy, ex, ey],
                switches_list=[S20],
                possible_switches_values=possible_switches_values)
    R4 = Room(name='R4',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[S21],
                possible_switches_values=possible_switches_values)
    R5 = Room(name='R5',
                position=[5*dx, 2*dy, ex, ey],
                switches_list=[S22],
                possible_switches_values=possible_switches_values)
    R6 = Room(name='R6',
                position=[7*dx, 2*dy, ex, ey],
                switches_list=[S23],
                possible_switches_values=possible_switches_values)
    R7 = Room(name='R7',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[S24],
                possible_switches_values=possible_switches_values)
    R8 = Room(name='R8',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[S25],
                possible_switches_values=possible_switches_values)
    R9 = Room(name='R9',
                position=[6*dx, 3*dy, ex, ey],
                switches_list=[S26],
                possible_switches_values=possible_switches_values)
    R10 = Room(name='R10',
                position=[8*dx, 3*dy, ex, ey],
                switches_list=[S27],
                possible_switches_values=possible_switches_values)
    RE = Room(name='RE',
              position=[0*dx, 3*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, ey/2/(2*dy)],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=True,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=True,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R3)
    D3 = Door(two_way=True,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R3)
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R2,
                room_arrival=R4)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R2,
                room_arrival=R5)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R3,
                room_arrival=R5)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R3,
                room_arrival=R6)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R4,
                room_arrival=R5)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R4,
                room_arrival=R7)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R4,
                room_arrival=R8)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R5,
                room_arrival=R6)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R5,
                room_arrival=R8)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R9)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R6,
                room_arrival=R9)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R6,
                room_arrival=R10)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R7,
                room_arrival=R8)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R8,
                room_arrival=R9)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R9,
                room_arrival=R10)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R7,
                room_arrival=RE)

    lcolor = Levels_colors_list.FROM_HUE(hu=0.16, sa=0.3, li=0.6)
    lcolor.room_color = Color.CREAM
    lcolor.surrounding_color = Color.ORANGE
    lcolor.letters_color = Color.WHITE

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19],
                 fastest_solution=None,
                 level_color=lcolor,
                 name='Tetractys',
                 keep_proportions=True,
                 door_window_size=300,
                 random=True)
    
    return level