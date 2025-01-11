from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def f(): 

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')

    Slist = [S0, S1, S2, S3, S4, S5]
    
    tree_list_0 = Tree.tree_list_from_str('TF')

    T0 = Tree(tree_list=tree_list_0,
                        name='T0',
                        switches=[S0, S1])
    T1 = Tree(tree_list=tree_list_0,
                        name='T1',
                        switches=[S1, S0])
    T2 = Tree(tree_list=tree_list_0,
                        name='T2',
                        switches=[S0, S3])
    T3 = Tree(tree_list=tree_list_0,
                        name='T3',
                        switches=[S3, S0])
    T4 = Tree(tree_list=tree_list_0,
                        name='T4',
                        switches=[S0, S4])
    T5 = Tree(tree_list=tree_list_0,
                        name='T5',
                        switches=[S4, S0])
    T6 = Tree(tree_list=tree_list_0,
                        name='T6',
                        switches=[S0, S5])
    T7 = Tree(tree_list=tree_list_0,
                        name='T7',
                        switches=[S5, S0])
    T8 = Tree(tree_list=tree_list_0,
                        name='T8',
                        switches=[S1, S2])
    T9 = Tree(tree_list=tree_list_0,
                        name='T9',
                        switches=[S2, S1])
    T10 = Tree(tree_list=tree_list_0,
                        name='T10',
                        switches=[S1, S4])
    T11 = Tree(tree_list=tree_list_0,
                        name='T11',
                        switches=[S4, S1])
    T12 = Tree(tree_list=tree_list_0,
                        name='T12',
                        switches=[S1, S5])
    T13 = Tree(tree_list=tree_list_0,
                        name='T13',
                        switches=[S5, S1])
    T14 = Tree(tree_list=tree_list_0,
                        name='T14',
                        switches=[S2, S3])
    T15 = Tree(tree_list=tree_list_0,
                        name='T15',
                        switches=[S3, S2])
    T16 = Tree(tree_list=tree_list_0,
                        name='T16',
                        switches=[S2, S4])
    T17 = Tree(tree_list=tree_list_0,
                        name='T17',
                        switches=[S4, S2])
    T18 = Tree(tree_list=tree_list_0,
                        name='T18',
                        switches=[S2, S5])
    T19 = Tree(tree_list=tree_list_0,
                        name='T19',
                        switches=[S5, S2])
    T20 = Tree(tree_list=tree_list_0,
                        name='T20',
                        switches=[S3, S4])
    T21 = Tree(tree_list=tree_list_0,
                        name='T21',
                        switches=[S4, S3])
    T22 = Tree(tree_list=tree_list_0,
                        name='T22',
                        switches=[S3, S5])
    T23 = Tree(tree_list=tree_list_0,
                        name='T23',
                        switches=[S5, S3])
    T24 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                name='T24',
                switches=Slist)

    dx = 1
    dy = 1
    ex = 0.75
    ey = 0.75

    epsilony = 0.2

    R0 = Room(name='R0',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[4*dx, 4*dy, ex, ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[S3])
    R4 = Room(name='R4',
                position=[2*dx, 1.5*dy-epsilony, ex, ey],
                switches_list=[S4])
    R5 = Room(name='R5',
                position=[2*dx, 2.5*dy+epsilony, ex, ey],
                switches_list=[S5])
    RE = Room(name='RE',
              position=[-1*dx, 2*dy, ex, ey],
              is_exit=True)
    
    rp = 0.4

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R0,
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R0,
                room_arrival=R3,
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R0,
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R0,
                room_arrival=R4,
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R4,
                room_arrival=R0,
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R5,
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R5,
                room_arrival=R0,
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R1,
                room_arrival=R2,
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R2,
                room_arrival=R1,
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R1,
                room_arrival=R4,
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R4,
                room_arrival=R1,
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R1,
                room_arrival=R5,
                relative_position=rp)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R5,
                room_arrival=R1,
                relative_position=rp)
    D14 = Door(two_way=False,
                tree=T14,
                name='D14',
                room_departure=R2,
                room_arrival=R3,
                relative_position=rp)
    D15 = Door(two_way=False,
                tree=T15,
                name='D15',
                room_departure=R3,
                room_arrival=R2,
                relative_position=rp)
    D16 = Door(two_way=False,
                tree=T16,
                name='D16',
                room_departure=R2,
                room_arrival=R4,
                relative_position=rp)
    D17 = Door(two_way=False,
                tree=T17,
                name='D17',
                room_departure=R4,
                room_arrival=R2,
                relative_position=rp)
    D18 = Door(two_way=False,
                tree=T18,
                name='D18',
                room_departure=R2,
                room_arrival=R5,
                relative_position=rp)
    D19 = Door(two_way=False,
                tree=T19,
                name='D19',
                room_departure=R5,
                room_arrival=R2,
                relative_position=rp)
    D20 = Door(two_way=False,
                tree=T20,
                name='D20',
                room_departure=R3,
                room_arrival=R4,
                relative_position=rp)
    D21 = Door(two_way=False,
                tree=T21,
                name='D21',
                room_departure=R4,
                room_arrival=R3,
                relative_position=rp)
    D22 = Door(two_way=False,
                tree=T22,
                name='D22',
                room_departure=R3,
                room_arrival=R5,
                relative_position=rp)
    D23 = Door(two_way=False,
                tree=T23,
                name='D23',
                room_departure=R5,
                room_arrival=R3,
                relative_position=rp)
    D24 = Door(two_way=False,
                tree=T24,
                name='D24',
                room_departure=R3,
                room_arrival=RE,
                relative_position=0.5)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24],
                 fastest_solution="S0 D0 S1 D10 S4 D17 S2 D18 S5 D23 S3 D24",
                 level_color=get_color(),
                 name='Octahedron',
                 keep_proportions=True,
                 door_window_size=300)
    
    # for door in level.doors_list:
    #     i = int(door.name.replace('D', ''))
    #     room_departure = door.room_departure
    #     room_arrival = door.room_arrival
    #     S0 = room_departure.switches_list[0]
    #     if not room_arrival.is_exit:
    #         S1 = room_arrival.switches_list[0]
    #         print(f'''    T{i} = Tree(tree_list=tree_list_0,
    #                     name='T{i}',
    #                     switches=[{S0.name}, {S1.name}])''')
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0, sa=0.5, li=0.25)
    lcolor.surrounding_color = Color.color_hls(hu=0.9, sa=1, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=0.9, sa=1, li=0.7)
    return lcolor