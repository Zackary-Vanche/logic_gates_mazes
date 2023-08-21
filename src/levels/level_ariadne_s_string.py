from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from random import shuffle as rd_shuffle
from random import choice as rd_choice
from random import random as rd_random

def kruskal(edges):
    
    # Ajouter des poids aléatoires
    for i in range(len(edges)):
        edges[i].append(rd_random())
    
    # Trier les arêtes par poids croissant
    edges.sort(key=lambda x: x[3])

    # Dictionnaire pour suivre les composantes connexes
    components = {}

    def find(node):
        if components[node] != node:
            components[node] = find(components[node])
        return components[node]

    def union(node1, node2):
        components[find(node1)] = find(node2)

    # Initialiser les composantes connexes
    for edge in edges:
        components[edge[1]] = edge[1]
        components[edge[2]] = edge[2]

    mst_edges = []

    for edge in edges:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            mst_edges.append(edge)

    return mst_edges

# # Exemple d'utilisation
# edges = [("a", "A", "B"), ("b", "A", "C"), ("c", "B", "C"), ("d", "B", "D"),
#          ("e", "C", "D"), ("f", "D", "E")]

# mst_edges = random_minimum_spanning_tree(edges)
# for edge in mst_edges:
#     print(edge)

def level_ariadne_s_string():
    
    v = 1
    
    S0 = Switch(name='S0', value=v)
    S1 = Switch(name='S1', value=v)
    S2 = Switch(name='S2', value=v)
    S3 = Switch(name='S3', value=v)
    S4 = Switch(name='S4', value=v)
    S5 = Switch(name='S5', value=v)
    S6 = Switch(name='S6', value=v)
    S7 = Switch(name='S7', value=v)
    S8 = Switch(name='S8', value=v)
    S9 = Switch(name='S9', value=v)
    S10 = Switch(name='S10', value=v)
    S11 = Switch(name='S11', value=v)
    S12 = Switch(name='S12', value=v)
    S13 = Switch(name='S13', value=v)
    S14 = Switch(name='S14', value=v)
    S15 = Switch(name='S15', value=v)
    S16 = Switch(name='S16', value=v)
    S17 = Switch(name='S17', value=v)
    S18 = Switch(name='S18', value=v)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = Tree(tree_list=[None],
                name='T1',
                switches=[1])
    T2 = Tree(tree_list=[None],
                name='T2',
                switches=[1])
    T3 = Tree(tree_list=[None],
                name='T3',
                switches=[1])
    T4 = Tree(tree_list=[None],
                name='T4',
                switches=[S0])
    T5 = Tree(tree_list=[None],
                name='T5',
                switches=[S1])
    T6 = Tree(tree_list=[None],
                name='T6',
                switches=[S2])
    T7 = Tree(tree_list=[None],
                name='T7',
                switches=[S3])
    T8 = Tree(tree_list=[None],
                name='T8',
                switches=[S4])
    T9 = Tree(tree_list=[None],
                name='T9',
                switches=[S5])
    T10 = Tree(tree_list=[None],
                name='T10',
                switches=[S6])
    T11 = Tree(tree_list=[None],
                name='T11',
                switches=[S7])
    T12 = Tree(tree_list=[None],
                name='T12',
                switches=[S8])
    T13 = Tree(tree_list=[None],
                name='T13',
                switches=[S9])
    T14 = Tree(tree_list=[None],
                name='T14',
                switches=[S10])
    T15 = Tree(tree_list=[None],
                name='T15',
                switches=[S11])
    T16 = Tree(tree_list=[None],
                name='T16',
                switches=[S12])
    T17 = Tree(tree_list=[None],
                name='T17',
                switches=[S13])
    T18 = Tree(tree_list=[None],
                name='T18',
                switches=[S14])
    T19 = Tree(tree_list=[None],
                name='T19',
                switches=[S15])
    T20 = Tree(tree_list=[None],
                name='T20',
                switches=[S16])
    T21 = Tree(tree_list=[None],
                name='T21',
                switches=[1])

    dx = 1
    dy = 0.7
    ex = 0.5
    ey = 0.25

    R0 = Room(name='R0',
                position=[-1.75*ex, 3*dy, 3*ex, ey],
                switches_list=[S0, S1, S2, S3, S4, S5,])
    R1 = Room(name='R1',
                position=[-1.25*ex, 2*dy, 2.5*ex, ey],
                switches_list=[S6, S7, S8, S9, S10,])
    R2 = Room(name='R2',
                position=[-1.25*ex, 1*dy, 2.5*ex, ey],
                switches_list=[S11, S12, S13, S14, S15])
    R3 = Room(name='R3',
                position=[-0.25*ex, 0*dy, 1.5*ex, ey],
                switches_list=[S16, S17, S18])
    R4 = Room(name='R4',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R11 = Room(name='R11',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R12 = Room(name='R12',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[])
    R13 = Room(name='R13',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R14 = Room(name='R14',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[])
    R15 = Room(name='R15',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx, 4*dy, ex, ey],
              is_exit=True)
    
    Ra = rd_choice([R4, R8, R12])

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
                room_arrival=R3)
    D3 = Door(two_way=False,
              tree=T3,
              name='D3',
              room_departure=R3,
              room_arrival=R7,
              relative_departure_coordinates=[1, 1/2],
              relative_arrival_coordinates=[0, 1/2])
    D4 = Door(two_way=True,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=True,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=True,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=True,
                tree=T7,
                name='D7',
                room_departure=R8,
                room_arrival=R9)
    D8 = Door(two_way=True,
                tree=T8,
                name='D8',
                room_departure=R9,
                room_arrival=R10)
    D9 = Door(two_way=True,
                tree=T9,
                name='D9',
                room_departure=R10,
                room_arrival=R11)
    D10 = Door(two_way=True,
                tree=T10,
                name='D10',
                room_departure=R12,
                room_arrival=R13)
    D11 = Door(two_way=True,
                tree=T11,
                name='D11',
                room_departure=R13,
                room_arrival=R14)
    D12 = Door(two_way=True,
                tree=T12,
                name='D12',
                room_departure=R14,
                room_arrival=R15)
    D13 = Door(two_way=True,
                tree=T13,
                name='D13',
                room_departure=R4,
                room_arrival=R8)
    D14 = Door(two_way=True,
                tree=T14,
                name='D14',
                room_departure=R8,
                room_arrival=R12)
    D15 = Door(two_way=True,
                tree=T15,
                name='D15',
                room_departure=R5,
                room_arrival=R9)
    D16 = Door(two_way=True,
                tree=T16,
                name='D16',
                room_departure=R9,
                room_arrival=R13)
    D17 = Door(two_way=True,
                tree=T17,
                name='D17',
                room_departure=R6,
                room_arrival=R10)
    D18 = Door(two_way=True,
                tree=T18,
                name='D18',
                room_departure=R10,
                room_arrival=R14)
    D19 = Door(two_way=True,
                tree=T19,
                name='D19',
                room_departure=R7,
                room_arrival=R11)
    D20 = Door(two_way=True,
                tree=T20,
                name='D20',
                room_departure=R11,
                room_arrival=R15)
    D21 = Door(two_way=True,
                tree=T21,
                name='D21',
                room_departure=Ra,
                room_arrival=RE)
    # D22 = Door(two_way=True,
    #             tree=T22,
    #             name='D22',
    #             room_departure=R0,
    #             room_arrival=RE)
    # D23 = Door(two_way=True,
    #             tree=T23,
    #             name='D23',
    #             room_departure=R0,
    #             room_arrival=RE)
    
    doors_list_0 = [D0, D1, D2, D3]
    doors_list_1 = [D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14]
    doors_list_2 = [D15, D16, D17, D18, D19, D20, D21]
    
    doors_list = doors_list_0 + doors_list_1 + doors_list_2

    edges = [['D4', 'R4', 'R5'],
             ['D5', 'R5', 'R6'],
             ['D6', 'R6', 'R7'],
             ['D7', 'R8', 'R9'],
             ['D8', 'R9', 'R10'],
             ['D9', 'R10', 'R11'],
             ['D10', 'R12', 'R13'],
             ['D11', 'R13', 'R14'],
             ['D12', 'R14', 'R15'],
             ['D13', 'R4', 'R8'],
             ['D14', 'R8', 'R12']]
    edges = kruskal(edges)
    for door in doors_list_1:
        if not door.name in edges:
            door.tree = Tree(tree_list=[None],
                             name=door.name.replace('D', 'T'),
                             switches=[0])
            door.update_open()
            print(door.name)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, RE],
                 doors_list=doors_list,
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name="Ariadne's string",
                 keep_proportions=True,
                 door_window_size=300)
    
    return level