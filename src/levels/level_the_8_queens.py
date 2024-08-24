from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import choice as rd_choice

def level_the_8_queens(): 

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

    Slist0 = [S0, S1, S2]
    Slist1 = [S3, S4, S5]
    Slist2 = [S6, S7, S8]
    Slist3 = [S9, S10, S11]

    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist0)),
          name='V0',
          switches=Slist0)
    V1 = Tree(tree_list=Tree.tree_list_BIN(len(Slist1)),
          name='V1',
          switches=Slist1)
    V2 = Tree(tree_list=Tree.tree_list_BIN(len(Slist2)),
          name='V2',
          switches=Slist2)
    V3 = Tree(tree_list=Tree.tree_list_BIN(len(Slist3)),
          name='V3',
          switches=Slist3)
    V4 = Tree(tree_list=['SUM', [None], ["MINUS", [None]]],
          name='V4',
          switches=[7, V3])
    V5 = Tree(tree_list=['SUM', [None], ["MINUS", [None]]],
          name='V5',
          switches=[7, V2])
    V6 = Tree(tree_list=['SUM', [None], ["MINUS", [None]]],
          name='V6',
          switches=[7, V1])
    V7 = Tree(tree_list=['SUM', [None], ["MINUS", [None]]],
          name='V7',
          switches=[7, V0])
    
    V8 = Tree(tree_list=['SUM'] + [[None]]*4,
          name='V8',
          switches=[V0, V1, V2, V3])

    Vlist = [V0, V1, V2, V3, V4, V5, V6, V7]
    
    tree_list_DIFF = ["DIFF", [None], [None]]
    
    def get_tree(n):
        if n < 8:
            Slist = []
            for i in range(n):
                Slist.extend([Vlist[i], Vlist[n]])
            for i in range(n):
                Slist.extend([Vlist[i], Vlist[n], n-i])
            tree_list = ["AND"] + [tree_list_DIFF,]*n + [["DIFF",
                                                     ["ABS",
                                                      ["SUM",
                                                       [None],
                                                       ["MINUS", [None]]]],
                                                     [None]],]*n
            return Tree(tree_list=tree_list,
                        name=f'T{n}',
                        switches=Slist,
                        cut_expression_depth_1=True)
        else:
            return Tree(tree_list=["EQU", [None], [None]],
                        name=f'T{n}',
                        switches=[Vlist[n-9], Vlist[n]],
                        cut_expression_depth_1=True)

    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = get_tree(7)
    
    isol = rd_choice([0, 1, 2, 3])
    if isol == 0:
        T8 = Tree(tree_list=['EQU', [None], [None]],
                  name='T8',
                  switches=[V8, 12])
    if isol == 1:
        T8 = Tree(tree_list=['AND',
                             ['EQU', [None], [None]],
                             ['SUP', [None], [None]]],
                  name='T8',
                  switches=[V8, 14,
                            V0, V1])
    if isol == 2:
        T8 = Tree(tree_list=['AND',
                             ['EQU', [None], [None]],
                             ['INF', [None], [None]]],
                  name='T8',
                  switches=[V8, 14,
                            V0, V1])
    if isol == 3:
        T8 = Tree(tree_list=['EQU', [None], [None]],
                  name='T8',
                  switches=[V8, 16])

    dx = 1.4
    ex = 0.7
    ey0 = 3*ex
    ey4 = ex*0.75
    
    dy0 = ey4+0.1
    dy7 = 0
    
    p0 = 1
    p1 = 0.75

    R0 = Room(name='R0',
                position=[4*dx, dy0, ex, ey0],
                switches_list=Slist0)
    R1 = Room(name='R1',
                position=[5*dx, dy0+p0, ex, ey0],
                switches_list=Slist1)
    R2 = Room(name='R2',
                position=[6*dx, dy0+2*p0, ex, ey0],
                switches_list=Slist2)
    R3 = Room(name='R3',
                position=[7*dx, dy0+3*p0, ex, ey0],
                switches_list=Slist3)
    R4 = Room(name='R4',
                position=[7*dx, dy7+3*p1, ex, ey4],
                switches_list=[])
    R5 = Room(name='R5',
                position=[6*dx, dy7+2*p1, ex, ey4],
                switches_list=[])
    R6 = Room(name='R6',
                position=[5*dx, dy7+p1, ex, ey4],
                switches_list=[])
    R7 = Room(name='R7',
                position=[4*dx, dy7, ex, ey4],
                switches_list=[])
    R8 = Room(name='R8',
                position=[3*dx-ex/2, dy7+p1, ex, ey4],
                switches_list=[])
    RE = Room(name='RE',
              position=[2*dx-ex/2, dy7+2*p1, ex, ey4],
              is_exit=True)
    
    rp = 0.65

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[0, 1],
                relative_arrival_coordinates=[0, 1])
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 1])
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0],
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0],
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7,
                relative_departure_coordinates=[1, 0],
                relative_arrival_coordinates=[1, 0],
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[0, 0])
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=RE,
                relative_departure_coordinates=[0, 0],
                relative_arrival_coordinates=[1/2, 0])
    
    c0 = Color.color_hls(hu=0.15, li=0.5, sa=0.4)
    c1 = Color.color_hls(hu=0.15, li=0.2, sa=0.8)
    contour_color = Color.color_hls(hu=0.16, li=0.9, sa=1)
    surrounding_color = Color.color_hls(hu=0.5, li=0.5, sa=0.9)
    
    if isol%2 == 0:
        lcolor = Level_color(background_color=c0,
                             room_color=c1,
                             letters_color=Color.BLACK,
                             contour_color=contour_color,
                             inside_room_color=Color.WHITE,
                             surrounding_color=surrounding_color)
    else:
        lcolor = Level_color(background_color=c1,
                             room_color=c0,
                             letters_color=Color.WHITE,
                             contour_color=contour_color,
                             inside_room_color=Color.BLACK,
                             surrounding_color=surrounding_color)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8],
                 fastest_solution=["S2 D0 S4 D1 D2 S10 S11 D3 D4 D5 D6 D7 D8",
                                   "S0 S2 D0 S3 S4 D1 S7 S8 D2 D3 D4 D5 D6 D7 D8",
                                   "S1 D0 S5 D1 S6 D2 S9 S10 S11 D3 D4 D5 D6 D7 D8",
                                   "S0 S1 D0 S3 S5 D1 S6 S7 S8 D2 S9 D3 D4 D5 D6 D7 D8"][isol],
                 level_color=lcolor,
                 name='The eight queens',
                 keep_proportions=True,
                 door_window_size=350)
    
    return level