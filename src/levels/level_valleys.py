from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

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
    S23 = Switch(name='S23', value=1)
    
    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]

    V0 = Tree(tree_list=["SUM", Tree.tree_list_MINUS, [None]],
          name='V0',
          switches=[S0, S1])
    V1 = Tree(tree_list=["SUM", Tree.tree_list_MINUS, [None]],
          name='V1',
          switches=[S2, S3])
    V2 = Tree(tree_list=Tree.tree_list_BIN(5),
          name='V2',
          switches=[S4, S5, S6, S7, S8])
    V3 = Tree(tree_list=Tree.tree_list_BIN(5),
          name='V3',
          switches=[S9, S10, S11, S12, S13])
    V4 = Tree(tree_list=Tree.tree_list_BIN(5),
          name='V4',
          switches=[S14, S15, S16, S17, S18])
    V5 = Tree(tree_list=Tree.tree_list_BIN(5),
          name='V5',
          switches=[S19, S20, S21, S22, S23])
    
    # R 0
    # B 1
    # Y 2
    
    l = [0, 1, 2, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2, 0, 2, 1, 0]
    
    def get_V_Slist(V):
        tree_list = []
        for i in range(len(l)):
            tree_list.extend([V, i, l[i]])
        return tree_list
    
    tree_list_V = ["SUM"] + [["PROD", Tree.tree_list_EQU(2), [None]]]*len(l)
    
    V6 = Tree(tree_list=tree_list_V,
              name='V6',
              switches=get_V_Slist(V4))
    V7 = Tree(tree_list=tree_list_V,
              name='V7',
              switches=get_V_Slist(V5))

    T0 = Tree(tree_list=["AND"] + [Tree.tree_list_NAND(2)]*2,
                name='T0',
                switches=[S0, S1, S2, S3])
    T1 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T1',
                switches=[V2, V4])
    T2 = Tree(tree_list=Tree.tree_list_EQU(2),
                name='T2',
                switches=[V3, V5])
    T3 = Tree(tree_list=["EQU", [None], Tree.tree_list_SUM(2)],
                name='T3',
                switches=[V2, V0, V4,])
    T4 = Tree(tree_list=["AND",
                         ["EQU", [None], Tree.tree_list_SUM(2)],
                         ["INFOREQU", [None], [None], [None]],
                         ["EQU", [None], [None]]
                         ],
                name='T4',
                switches=[V3, V1, V5,
                          V4, V5, len(l)-1,
                          V6, V7,
                          ])
    T5 = Tree(tree_list=Tree.tree_list_NOR(len(Slist)),
                name='T5',
                switches=Slist)

    dx = 1.2
    dy = 1.2
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, dx+ex, dy+ey],
                switches_list=[S0, S1, S2, S3])
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ey*5, ey],
                switches_list=[S4, S5, S6, S7, S8])
    R2 = Room(name='R2',
                position=[2*dx, 1*dy, ey*5.5, ey],
                switches_list=[S9, S10, S11, S12, S13])
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ey*5.5, ey],
                switches_list=[S14, S15, S16, S17, S18])
    R4 = Room(name='R4',
                position=[2*dx, 3*dy, ey*5, ey],
                switches_list=[S19, S20, S21, S22, S23])
    
    RE = Room(name='RE',
              position=[0*dx, 3*dy, dx+ex, dy+ey],
              is_exit=True)
    
    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1, ex/2/(dx+ex)],
                relative_arrival_coordinates=[0, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R0,
                relative_departure_coordinates=[0, 1/2],
                relative_arrival_coordinates=[1, (dx+ex/2)/(dx+ex)])
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R0,
                room_arrival=RE,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="S0 S3 D0 D1 S13 D2 S14 D3 S19 S20 S21 S22 S23 D4 D0 S4 D1 S9 S10 S11 S12 S13 D2 S14 S15 D3 S19 D4 S2 S3 D0 S4 S5 D1 S9 D2 S14 D3 S19 D4 S2 S3 D0 S4 D1 S9 D2 S14 S15 S16 D3 S19 D4 D0 S4 S5 S6 D1 S9 D2 S14 D3 S19 S20 D4 S0 S1 D0 S4 D1 S9 S10 D2 S14 D3 S19 D4 D0 S4 D1 S9 D2 S14 S15 S16 D3 S19 S20 S21 D4 S2 S3 D0 S4 S5 S6 D1 S9 S10 S11 D2 S14 D3 S19 S20 S21 D4 S2 S3 D0 S4 D1 S9 S10 S11 D2 S14 S15 D3 S19 S20 S21 D4 D0 S4 S5 D1 S9 S10 S11 D2 S14 D3 S19 D4 S0 S1 D0 S4 D1 S9 D2 S14 D3 S19 S20 D4 D0 S4 D1 S9 S10 D2 S14 S15 D3 S19 D4 S2 S3 D0 S4 S5 D1 S9 D2 S14 D3 S19 D4 S2 S3 D0 S4 D1 S9 D2 S14 S15 S16 D3 S19 D4 D0 S4 S5 S6 D1 S9 D2 S14 D3 S19 S20 S21 S22 D4 D0 S4 D1 S9 S10 S11 S12 D2 S14 S15 D3 S19 D4 S0 S1 D0 S4 S5 D1 S9 D2 S14 S15 D3 S19 S20 D4 D0 S4 S5 D1 S9 S10 D2 S14 D3 S19 D4 D0 S4 D1 S9 D2 S14 S15 S16 D3 S19 S20 S21 D4 D0 S4 S5 S6 D1 S9 S10 S11 D2 S14 D3 S19 D4 D0 S4 D1 S9 D2 S14 S15 D3 S19 S20 D4 D0 S4 S5 D1 S9 S10 D2 S14 D3 S19 D4 S1 S3 D0 S4 D1 S9 D2 D3 D4 D5",
                 level_color=get_color(),
                 name='Valleys',
                 keep_proportions=True,
                 door_window_size=450)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.2, li=0.6)
    lcolor.room_color = Color.color_hls(hu=0.6, sa=0.1, li=0.6)
    lcolor.inside_room_color = Color.color_hls(hu=0.4, sa=0.1, li=0.1)
    lcolor.surrounding_color = Color.color_hls(hu=0.1, sa=0.6, li=0.4)
    return lcolor