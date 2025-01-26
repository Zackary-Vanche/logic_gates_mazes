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
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')

    Slist_0 = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15]
    Slist_1 = [S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31]
    
    OR_index_list = [[] for k in range(8)]
    for vertex_i in range(4):
        for vertex_j in range(4):
            edge_index = vertex_i+4*vertex_j
            OR_index_list[vertex_i].append(edge_index)
            OR_index_list[4+vertex_j].append(edge_index)

    Vlist = [Tree(tree_list=Tree.tree_list_NOR(2),
                  name=f'V{i}',
                  switches=[Slist_0[i], Slist_1[i]]) for i in range(16)]
    
    tree_list_V = ["AND"] + [Tree.tree_list_OR(4)]*8
    
    def get_Slist_T_OR(Sl):
        assert len(Sl) == 16, str(Sl)
        SlT = []
        for l in OR_index_list:
            for i in l:
                SlT.append(Sl[i])
        assert len(SlT) == 32
        return SlT
    
    V16 = Tree(tree_list=tree_list_V,
               name='V16',
               switches=get_Slist_T_OR(Slist_0),
               cut_expression_depth_1=True)
    V17 = Tree(tree_list=tree_list_V,
               name='V17',
               switches=get_Slist_T_OR(Slist_1),
               cut_expression_depth_1=True)
    V18 = Tree(tree_list=["SUPOREQU", Tree.tree_list_SUM(16), [None]],
               name='V18',
               switches=Vlist+[2])
    Slist_T19 = []
    for i in range(16):
        Slist_T19.extend([Slist_0[i], Slist_1[i]])
    V19 = Tree(tree_list=["AND"] + [Tree.tree_list_NAND(16)]*2,
               name='V19',
               switches=Slist_T19)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[V16])
    T1 = Tree(tree_list=Tree.tree_list_AND(3),
                name='T1',
                switches=[V17, V18, V19])

    R0 = Room(name='R0',
                position=[0, 0, 8, 2],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[0, -3, 8, 2],
                switches_list=Slist_1)
    RE = Room(name='RE',
              position=[0, -5, 8, 1],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/5, 0.2],
                relative_arrival_coordinates=[4/5, 0.8])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=RE,
                relative_departure_coordinates=[1/5, 0.2],
                relative_arrival_coordinates=[4/5, 0.8])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Arboricity',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.4, sa=0.25, li=0.3)
    lcolor.contour_color = Color.color_hls(hu=0.1, sa=1, li=0.7)
    lcolor.surrounding_color = Color.color_hls(hu=0.35, sa=1, li=0.7)
    return lcolor