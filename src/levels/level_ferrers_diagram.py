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
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')

    Slist_0 = [S0, S1, S2, S3, S4, S5, S6, S7]
    Slist_1 = [S8, S9, S10, S11, S12, S13, S14, S15]
    Slist_2 = [S16, S17, S18, S19, S20, S21, S22, S23]
    Slist_3 = [S24, S25, S26, S27, S28, S29, S30, S31]
    Slist_4 = [S32, S33, S34, S35, S36, S37, S38, S39]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_0)),
          name='V0',
          switches=Slist_0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_1)),
          name='V1',
          switches=Slist_1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_2)),
          name='V2',
          switches=Slist_2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_3)),
          name='V3',
          switches=Slist_3)
    V4 = Tree(tree_list=Tree.tree_list_BIN(len(Slist_4)),
          name='V4',
          switches=Slist_4)
    
    Vlist = [V0, V1, V2, V3, V4]
    
    def get_Slist_T(i):
        Sll = [Slist_0, Slist_1, Slist_2, Slist_3, Slist_4][i]
        Sl = [Sll[0], Sll[1],
              Sll[0], Sll[4],
              Sll[1], Sll[2],
              Sll[1], Sll[5],
              Sll[2], Sll[3],
              Sll[4], Sll[5],
              Sll[4], Sll[6],
              Sll[6], Sll[7],] + Sll + [4]
        if i == 0:
            return Sl
        else:
            return Sl + [Vlist[i-1], Vlist[i]]
        
    tree_list_0 = ["AND"] + [["NAND", Tree.tree_list_NOT, [None]]]*8 + [["EQU", Tree.tree_list_SUM(8), [None]]]
    tree_list_1 = tree_list_0 + [Tree.tree_list_INF(2)]
    
    def get_tree(i):
        if i == 0:
            tree_list = tree_list_0
        else:
            tree_list = tree_list_1
        return Tree(tree_list=tree_list,
                    name=f'T{i}',
                    switches=get_Slist_T(i),
                    cut_expression_depth_1=True)

    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    
    dx = 4
    dy = 2
    ex = 4
    ey = 2

    R0 = Room(name='R0',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_4)
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, ey],
              is_exit=True)

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 0])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 0])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[1, 1],
                relative_arrival_coordinates=[1, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=RE,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 1/2])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, RE],
                 doors_list=[D0, D1, D2, D3, D4],
                 fastest_solution="S0 S1 S2 S3 D0 S8 S9 S10 S12 D1 S16 S17 S20 S21 D2 S24 S25 S28 S30 D3 S32 S36 S38 S39 D4",
                 level_color=get_color(),
                 name='Ferrers diagram',
                 keep_proportions=True,
                 door_window_size=370)
    
    return level
    
def get_color():
    hu = 0.25
    sa = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.4, sa),
                         room_color=Color.color_hls(hu, 0.15, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.color_hls(hu=0.1, li=0.7, sa=1),
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.color_hls(hu=0.1, li=0.8, sa=1))
    return lcolor