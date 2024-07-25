from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
from Color import Color

def level_tetrahedron(): 

    S1 = Switch(name='S1')
    S0 = Switch(name='S0')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')

    Slist = [S0, S1, S2, S3]
    
    tree_list_0 = Tree.tree_list_from_str('TF')

    T0 = Tree(tree_list=tree_list_0,
                        name='T0',
                        switches=[S1, S0])
    T1 = Tree(tree_list=tree_list_0,
                        name='T1',
                        switches=[S0, S1])
    T2 = Tree(tree_list=tree_list_0,
                        name='T2',
                        switches=[S1, S2])
    T3 = Tree(tree_list=tree_list_0,
                        name='T3',
                        switches=[S2, S1])
    T4 = Tree(tree_list=tree_list_0,
                        name='T4',
                        switches=[S1, S3])
    T5 = Tree(tree_list=tree_list_0,
                        name='T5',
                        switches=[S3, S1])
    T6 = Tree(tree_list=tree_list_0,
                        name='T6',
                        switches=[S0, S2])
    T7 = Tree(tree_list=tree_list_0,
                        name='T7',
                        switches=[S2, S0])
    T8 = Tree(tree_list=tree_list_0,
                        name='T8',
                        switches=[S0, S3])
    T9 = Tree(tree_list=tree_list_0,
                        name='T9',
                        switches=[S3, S0])
    T10 = Tree(tree_list=tree_list_0,
                        name='T10',
                        switches=[S2, S3])
    T11 = Tree(tree_list=tree_list_0,
                        name='T11',
                        switches=[S3, S2])
    T12 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                name='T12',
                switches=Slist)
    
    dx = 1
    dy = 1
    ex = 1
    ey = 0.5

    R0 = Room(name='R0',
                position=[3*dx, 0*dy, 2*ex, 2*ey],
                switches_list=[S0])
    R1 = Room(name='R1',
                position=[3*dx, 3*dy, 2*ex, 2*ey],
                switches_list=[S1])
    R2 = Room(name='R2',
                position=[0*dx, 6.5*dy, 2*ex, 2*ey],
                switches_list=[S2])
    R3 = Room(name='R3',
                position=[6*dx, 6.5*dy, 2*ex, 2*ey],
                switches_list=[S3])
    RE = Room(name='RE',
              position=[3*dx, 6*dy, 2*ex, 2*ey],
              is_exit=True)
    
    a = 0.02
    b = 1-a
    rp = 0.3

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R1,
                room_arrival=R0,
                relative_departure_coordinates=[1/2, 0],
                relative_arrival_coordinates=[1/2, 1],
                relative_position=rp)
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[1/2, 1],
                relative_arrival_coordinates=[1/2, 0],
                relative_position=rp)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R1,
                room_arrival=R2,
                relative_departure_coordinates=[a, b],
                relative_arrival_coordinates=[b, a],
                relative_position=rp)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R2,
                room_arrival=R1,
                relative_departure_coordinates=[b, a],
                relative_arrival_coordinates=[a, b],
                relative_position=rp)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R1,
                room_arrival=R3,
                relative_departure_coordinates=[b, b],
                relative_arrival_coordinates=[a, a],
                relative_position=rp)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R3,
                room_arrival=R1,
                relative_departure_coordinates=[a, a],
                relative_arrival_coordinates=[b, b],
                relative_position=rp)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R0,
                room_arrival=R2,
                relative_departure_coordinates=[a, a],
                relative_arrival_coordinates=[a, a],
                relative_position=rp)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R2,
                room_arrival=R0,
                relative_departure_coordinates=[a, a],
                relative_arrival_coordinates=[a, a],
                relative_position=rp)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R0,
                room_arrival=R3,
                relative_departure_coordinates=[b, a],
                relative_arrival_coordinates=[b, a],
                relative_position=rp)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R3,
                room_arrival=R0,
                relative_departure_coordinates=[b, a],
                relative_arrival_coordinates=[b, a],
                relative_position=rp)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R2,
                room_arrival=R3,
                relative_departure_coordinates=[b, b],
                relative_arrival_coordinates=[a, b],
                relative_position=rp)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R3,
                room_arrival=R2,
                relative_departure_coordinates=[a, b],
                relative_arrival_coordinates=[b, b],
                relative_position=rp)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R1,
                room_arrival=RE)
    
    hu = 0.1
    lcolor = Levels_colors_list.FROM_HUE(hu=hu, sa=0.5, li=0.25)
    lcolor.surrounding_color = Color.color_hls(hu=hu+0.1, sa=1, li=0.7)
    lcolor.contour_color = Color.color_hls(hu=hu+0.1, sa=1, li=0.7)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution="S0 D6 S2 D10 S3 D5 S1 D12",
                 level_color=lcolor,
                 name='Tetrahedron',
                 keep_proportions=True,
                 door_window_size=300)
    
    # for door in level.doors_list:
    #     i = int(door.name.replace('D', ''))
    #     room_departure = door.room_departure
    #     room_arrival = door.room_arrival
    #     S1 = room_departure.switches_list[0]
    #     if not room_arrival.is_exit:
    #         S0 = room_arrival.switches_list[0]
    #         print(f'''    T{i} = Tree(tree_list=tree_list_0,
    #                     name='T{i}',
    #                     switches=[{S1.name}, {S0.name}])''')
    
    return level