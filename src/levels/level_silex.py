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

    Slist = [S0, S1, S2, S3, S4, S5, S6]
    
    tree_list_0 = Tree.tree_list_NOT
    tree_list_1 = [None]

    T0 = Tree(tree_list=tree_list_0,
                        name='T0',
                        switches=[S0])
    T1 = Tree(tree_list=tree_list_1,
                        name='T1',
                        switches=[S0])
    T2 = Tree(tree_list=tree_list_0,
                        name='T2',
                        switches=[S1])
    T3 = Tree(tree_list=tree_list_1,
                        name='T3',
                        switches=[S1])
    T4 = Tree(tree_list=tree_list_0,
                        name='T4',
                        switches=[S2])
    T5 = Tree(tree_list=tree_list_1,
                        name='T5',
                        switches=[S2])
    T6 = Tree(tree_list=tree_list_0,
                        name='T6',
                        switches=[S0])
    T7 = Tree(tree_list=tree_list_1,
                        name='T7',
                        switches=[S0])
    T8 = Tree(tree_list=tree_list_0,
                        name='T8',
                        switches=[S3])
    T9 = Tree(tree_list=tree_list_1,
                        name='T9',
                        switches=[S3])
    T10 = Tree(tree_list=tree_list_0,
                        name='T10',
                        switches=[S4])
    T11 = Tree(tree_list=tree_list_1,
                        name='T11',
                        switches=[S4])
    T12 = Tree(tree_list=tree_list_0,
                        name='T12',
                        switches=[S1])
    T13 = Tree(tree_list=tree_list_1,
                        name='T13',
                        switches=[S1])
    T14 = Tree(tree_list=tree_list_0,
                        name='T14',
                        switches=[S3])
    T15 = Tree(tree_list=tree_list_1,
                        name='T15',
                        switches=[S3])
    T16 = Tree(tree_list=tree_list_0,
                        name='T16',
                        switches=[S5])
    T17 = Tree(tree_list=tree_list_1,
                        name='T17',
                        switches=[S5])
    T18 = Tree(tree_list=tree_list_0,
                        name='T18',
                        switches=[S6])
    T19 = Tree(tree_list=tree_list_1,
                        name='T19',
                        switches=[S6])
    T20 = Tree(tree_list=tree_list_0,
                        name='T20',
                        switches=[S2])
    T21 = Tree(tree_list=tree_list_1,
                        name='T21',
                        switches=[S2])
    T22 = Tree(tree_list=tree_list_0,
                        name='T22',
                        switches=[S4])
    T23 = Tree(tree_list=tree_list_1,
                        name='T23',
                        switches=[S4])
    T24 = Tree(tree_list=tree_list_0,
                        name='T24',
                        switches=[S5])
    T25 = Tree(tree_list=tree_list_1,
                        name='T25',
                        switches=[S5])
    T26 = Tree(tree_list=tree_list_0,
                        name='T26',
                        switches=[S6])
    T27 = Tree(tree_list=tree_list_1,
                        name='T27',
                        switches=[S6])
    T28 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                name='T28',
                switches=Slist)

    dx = 1
    dy = 1
    ex = 0.7
    ey = 0.7
    
    a = 0.2

    R0 = Room(name='R0',
                position=[8*dx, 3*dy, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[1*dx, 6*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[6*dx, 3*dy, ex, ey],
                switches_list=[S0])
    R5 = Room(name='R5',
                position=[4*dx, 5.5*dy, ex, ey],
                switches_list=[S1])
    R6 = Room(name='R6',
                position=[4*dx, 0.5*dy, ex, ey],
                switches_list=[S2])
    R7 = Room(name='R7',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[S3])
    R8 = Room(name='R8',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[S4])
    R9 = Room(name='R9',
                position=[0.5*dx-a, 3*dy, ex, ey],
                switches_list=[S5])
    R10 = Room(name='R10',
                position=[-0.5*dx-2*a, 3*dy, ex, ey],
                switches_list=[S6])
    RE = Room(name='RE',
              position=[1.5*dx, 3*dy, ex, ey],
              is_exit=True)
    
    rp = 0.37

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R4,
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R4,
                room_arrival=R0,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R5,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R5,
                room_arrival=R0,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R6,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R6,
                room_arrival=R0,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R1,
                room_arrival=R4,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R4,
                room_arrival=R1,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R7,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R7,
                room_arrival=R1,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R8,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R8,
                room_arrival=R1,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R2,
                room_arrival=R5,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R2,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R7,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R7,
                room_arrival=R2,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R2,
                room_arrival=R9,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R9,
                room_arrival=R2,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R2,
                room_arrival=R10,
                relative_position=0.48)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R10,
                room_arrival=R2,
                relative_position=0.26)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R3,
                room_arrival=R6,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R6,
                room_arrival=R3,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R3,
                room_arrival=R8,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R8,
                room_arrival=R3,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R3,
                room_arrival=R9,
                relative_position=rp)
    D25 = Door(two_way=False,
                tree=T25,
                name='D25',
                room_departure=R9,
                room_arrival=R3,
                relative_position=rp)
    D26 = Door(two_way=False,
                tree=T26,
                name='D26',
                room_departure=R3,
                room_arrival=R10,
                relative_position=0.48)
    D27 = Door(two_way=False,
                tree=T27,
                name='D27',
                room_departure=R10,
                room_arrival=R3,
                relative_position=0.26)
    D28 = Door(two_way=False,
                tree=T28,
                name='D28',
                room_departure=R1,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11,
                             D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23,
                             D24, D25, D26, D27, D28],
                 fastest_solution="D0 S0 D1 D2 S1 D3 D4 S2 D21 D22 S4 D23 D24 S5 D17 D18 S6 D19 D14 S3 D9 D28",
                 level_color=get_color(),
                 name='Silex',
                 keep_proportions=True,
                 door_window_size=250)
    
    # for i, door in enumerate(level.doors_list):
    #     R0 = door.room_departure
    #     R1 = door.room_arrival
    #     if R1.is_exit:
    #         continue
    #     if len(R0.switches_list) == 1:
    #         print(f'''    T{i} = Tree(tree_list=tree_list_1,
    #                     name='T{i}',
    #                     switches=[{R0.switches_list[0].name}])''')
    #     else:
    #         print(f'''    T{i} = Tree(tree_list=tree_list_0,
    #                     name='T{i}',
    #                     switches=[{R1.switches_list[0].name}])''')
    
    return level

def get_color():
    hu = 0.16
    sa = 0.2
    li = 0.6
    lcolor = Level_color(background_color=Color.color_hls(hu, 0.2, sa),
                         room_color=Color.color_hls(hu, li*0.2, 0.8 * sa),
                         letters_color=Color.color_hls(hu=0.72, li=0.95, sa=0.9),
                         contour_color=Color.GREY,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.KHAKI)
    return lcolor