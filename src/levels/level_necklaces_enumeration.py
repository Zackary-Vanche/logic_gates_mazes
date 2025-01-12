from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
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

    Slist_0 = [S0, S1, S2, S3]
    Slist_1 = [S4, S5, S6, S7]
    Slist_2 = [S8, S9, S10, S11]
    Slist_3 = [S12, S13, S14, S15]
    Slist_4 = [S16, S17, S18, S19]
    Slist_5 = [S20, S21, S22, S23]
    
    Sl_list = [Slist_0, Slist_1, Slist_2, Slist_3, Slist_4, Slist_5]
    
    # a b
    # d c
    
    Vl = {}
    
    def get_tree(i):
        SlR = Sl_list[i]
        [a, b, c, d] = SlR
        V = Tree(tree_list=Tree.tree_list_BIN(4),
                 name=f'V{i}',
                 switches=[a, b, d, c])
        Vl[f'V{i}'] = V
        # SlT = [V, b, c, d, a,
        #        V, c, d, a, b,
        #        V, d, a, b, c,
        #        V, b, a, d, c,
        #        V, a, d, c, b,
        #        V, d, c, b, a,
        #        V, c, b, a, d]
        SlT = [V, b, d, c, a,
               V, d, c, a, b,
               V, c, a, b, d,
               V, b, a, c, d,
               V, a, c, d, b,
               V, c, d, b, a,
               V, d, b, a, c]
        if i == 0:
            return Tree(tree_list=["AND"] + [["INFOREQU", [None], Tree.tree_list_BIN(4)]]*7,
                        name=f'T{i}',
                        switches=SlT,
                        cut_expression_depth_1=True)
        else:
            return Tree(tree_list=["AND"] + [["INFOREQU", [None], Tree.tree_list_BIN(4)]]*7 + [["INF", [None], [None]]],
                        name=f'T{i}',
                        switches=SlT + [Vl[f'V{i-1}'], V],
                        cut_expression_depth_1=True)
        

    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)

    dx = 1
    dy = 1
    ex = 0.7
    ey = 0.7

    R0 = Room(name='R0',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_0)
    R1 = Room(name='R1',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_1)
    R2 = Room(name='R2',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=Slist_5)
    RE = Room(name='RE',
              position=[0*dx, 1*dy, ex, ey],
              is_exit=True)

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
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5],
                 fastest_solution="D0 S4 D1 S8 S9 D2 S12 S15 D3 S16 S17 S19 D4 S20 S21 S22 S23 D5",
                 level_color=get_color(),
                 name='Necklaces enumeration',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    hu = 0.2
    sa = 0.6
    li = 0.8
    lcolor = Level_color(background_color=Color.color_hls(hu, li, sa),
                         room_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                         letters_color=Color.BLACK,
                         contour_color=Color.YELLOW,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.YELLOW)
    return lcolor