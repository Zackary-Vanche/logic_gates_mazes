from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list
import numpy as np
from random import shuffle as rd_shuffle
from random import randint as rd_randint
from Color import Color

def f():
    
    Snames = [f'S{i}' for i in range(11)]

    S0 = Switch(name=Snames[0])
    S1 = Switch(name=Snames[1])
    S2 = Switch(name=Snames[2])
    S3 = Switch(name=Snames[3])
    S4 = Switch(name=Snames[4])
    S5 = Switch(name=Snames[5])
    S6 = Switch(name=Snames[6])
    S7 = Switch(name=Snames[7])
    S8 = Switch(name=Snames[8])
    S9 = Switch(name=Snames[9])
    S10 = Switch(name=Snames[10])

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
    Slist_ordered = Slist[:]
    #rd_shuffle(Slist)
    
    Slist_list = []
    for i in range(len(Slist)):
        Slist_list.append([])
        if i+1<len(Slist):
            Slist_list[-1].append(Slist[i+1])
        l = Slist[i+2:]
        rd_shuffle(l)
        if l != []:
            a = max(1, len(l)//2)
            b = len(l)
            k = rd_randint(a, b)
            Slist_list[-1].extend(l[:k])
        #Slist_list[-1].extend(l)
    for i in range(len(Slist)):
        assert len(Slist_list[i]) == len(list(set(Slist_list[i])))
        Slist_list[i] = list(set(Slist_list[i]))
        Slist_list[i] = sorted(Slist_list[i], key = lambda S: int(S.name.replace('S', '')))
        
    Tnames = [f'T{i}' for i in range(23)]
    #rd_shuffle(Tnames)
    
    #Sint_list = [int(S.name.replace('S', '')) for S in Slist]
    Sint_list = [Slist_ordered.index(S) for S in Slist]
    def get_Tree(i):
        if i%2 == 0:
            return Tree(tree_list=Tree.tree_list_NOT,
                        name=Tnames[i],
                        switches=[Slist_ordered[i//2]])
        else:
            Slisti = Slist_list[Sint_list[i//2]]
            if len(Slisti) == 0:
                return Tree(tree_list=[None],
                            name=Tnames[i],
                            switches=[1])
            elif len(Slisti) == 1:
                return Tree(tree_list=Tree.tree_list_NOT,
                            name=Tnames[i],
                            switches=Slisti)
            else:
                return Tree(tree_list=Tree.tree_list_NOR(len(Slisti)),
                            name=Tnames[i],
                            switches=Slisti)
    
    T0 = get_Tree(0)
    T1 = get_Tree(1)
    T2 = get_Tree(2)
    T3 = get_Tree(3)
    T4 = get_Tree(4)
    T5 = get_Tree(5)
    T6 = get_Tree(6)
    T7 = get_Tree(7)
    T8 = get_Tree(8)
    T9 = get_Tree(9)
    T10 = get_Tree(10)
    T11 = get_Tree(11)
    T12 = get_Tree(12)
    T13 = get_Tree(13)
    T14 = get_Tree(14)
    T15 = get_Tree(15)
    T16 = get_Tree(16)
    T17 = get_Tree(17)
    T18 = get_Tree(18)
    T19 = get_Tree(19)
    T20 = get_Tree(20)
    T21 = Tree(tree_list=[None],
                name=Tnames[21],
                switches=[1])
    T22 = Tree(tree_list=Tree.tree_list_AND(len(Slist)),
                name=Tnames[22],
                switches=Slist)

    dx = 1
    ex = dx
    ex0 = 0.5
    exe = ex*np.sqrt(2)-0.05
    
    dy = 1
    ey = 1
    ey0 = ex0
    eye = exe
    
    exs = ex*2/3
    eys = ey*2/3
    
    R0 = Room(name='R0',
                position=[3*dx+(dx-ex0)/2, 3*dy+(dy-ey0)/2, ex0, ey0],
                switches_list=[])
    R1 = Room(name='R1',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[S0])
    R2 = Room(name='R2',
                position=[5*dx, 2*dy, ex, ey],
                switches_list=[S1])
    R3 = Room(name='R3',
                position=[6*dx, 3*dy, exs, ey],
                switches_list=[S2])
    R4 = Room(name='R4',
                position=[5*dx, 4*dy, ex, ey],
                switches_list=[S3])
    R5 = Room(name='R5',
                position=[4*dx, 5*dy, ex, ey],
                switches_list=[S4])
    R6 = Room(name='R6',
                position=[3*dx, 6*dy, ex, eys],
                switches_list=[S5])
    R7 = Room(name='R7',
                position=[2*dx, 5*dy, ex, ey],
                switches_list=[S6])
    R8 = Room(name='R8',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[S7])
    R9 = Room(name='R9',
                position=[0*dx+ex-exs, 3*dy, exs, ey],
                switches_list=[S8])
    R10 = Room(name='R10',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[S9])
    R11 = Room(name='R11',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[S10])
    RE = Room(name='RE',
              position=[3*dx+(dx-exe)/2, 0*dy+(dy-eye)/2, exe, eye],
              is_exit=True)
    
    rp1 = 0.62
    rp2 = 0.66
    
    Dnames = [name.replace('T', 'D') for name in Tnames]
    
    D0 = Door(two_way=False,
                tree=T0,
                name=Dnames[0],
                room_departure=R0,
                room_arrival=R1,
                relative_position=rp1)
    D1 = Door(two_way=False,
                tree=T1,
                name=Dnames[1],
                room_departure=R1,
                room_arrival=R0,
                relative_position=rp2)
    D2 = Door(two_way=False,
                tree=T2,
                name=Dnames[2],
                room_departure=R0,
                room_arrival=R2,
                relative_position=rp1)
    D3 = Door(two_way=False,
                tree=T3,
                name=Dnames[3],
                room_departure=R2,
                room_arrival=R0,
                relative_position=rp2)
    D4 = Door(two_way=False,
                tree=T4,
                name=Dnames[4],
                room_departure=R0,
                room_arrival=R3,
                relative_position=rp1)
    D5 = Door(two_way=False,
                tree=T5,
                name=Dnames[5],
                room_departure=R3,
                room_arrival=R0,
                relative_position=rp2)
    D6 = Door(two_way=False,
                tree=T6,
                name=Dnames[6],
                room_departure=R0,
                room_arrival=R4,
                relative_position=rp1)
    D7 = Door(two_way=False,
                tree=T7,
                name=Dnames[7],
                room_departure=R4,
                room_arrival=R0,
                relative_position=rp2)
    D8 = Door(two_way=False,
                tree=T8,
                name=Dnames[8],
                room_departure=R0,
                room_arrival=R5,
                relative_position=rp1)
    D9 = Door(two_way=False,
                tree=T9,
                name=Dnames[9],
                room_departure=R5,
                room_arrival=R0,
                relative_position=rp2)
    D10 = Door(two_way=False,
                tree=T10,
                name=Dnames[10],
                room_departure=R0,
                room_arrival=R6,
                relative_position=rp1)
    D11 = Door(two_way=False,
                tree=T11,
                name=Dnames[11],
                room_departure=R6,
                room_arrival=R0,
                relative_position=rp2)
    D12 = Door(two_way=False,
                tree=T12,
                name=Dnames[12],
                room_departure=R0,
                room_arrival=R7,
                relative_position=rp1)
    D13 = Door(two_way=False,
                tree=T13,
                name=Dnames[13],
                room_departure=R7,
                room_arrival=R0,
                relative_position=rp2)
    D14 = Door(two_way=False,
                tree=T14,
                name=Dnames[14],
                room_departure=R0,
                room_arrival=R8,
                relative_position=rp1)
    D15 = Door(two_way=False,
                tree=T15,
                name=Dnames[15],
                room_departure=R8,
                room_arrival=R0,
                relative_position=rp2)
    D16 = Door(two_way=False,
                tree=T16,
                name=Dnames[16],
                room_departure=R0,
                room_arrival=R9,
                relative_position=rp1)
    D17 = Door(two_way=False,
                tree=T17,
                name=Dnames[17],
                room_departure=R9,
                room_arrival=R0,
                relative_position=rp2)
    D18 = Door(two_way=False,
                tree=T18,
                name=Dnames[18],
                room_departure=R0,
                room_arrival=R10,
                relative_position=rp1)
    D19 = Door(two_way=False,
                tree=T19,
                name=Dnames[19],
                room_departure=R10,
                room_arrival=R0,
                relative_position=rp2)
    D20 = Door(two_way=False,
                tree=T20,
                name=Dnames[20],
                room_departure=R0,
                room_arrival=R11,
                relative_position=rp1)
    D21 = Door(two_way=False,
                tree=T21,
                name=Dnames[21],
                room_departure=R11,
                room_arrival=R0,
                relative_position=rp2)
    D22 = Door(two_way=False,
                tree=T22,
                name=Dnames[22],
                room_departure=R0,
                room_arrival=RE)
    
    rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, RE]
    doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21]

    randomize = True
    
    if randomize:
        
        rooms_with_switches = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11]
        room_positions_list = []
        for i, room in enumerate(rooms_with_switches):
            room_positions_list.append(room.position)
        rd_shuffle(room_positions_list)
        for i, room in enumerate(rooms_with_switches):
            room.position = room_positions_list[i]
        
        Snames = []
        for i, S in enumerate(Slist):
            Snames.append(Slist[i].name)
        rd_shuffle(Slist)
        for i, S in enumerate(Slist):
            S.name = Snames[i]

        door_names_list = []
        for i, door in enumerate(doors_list):
            door_names_list.append(door.name)
        rd_shuffle(door_names_list)
        for i, door in enumerate(doors_list):
            door.name = door_names_list[i]

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=rooms_list,
                 doors_list=doors_list+[D22],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Blind alleys',
                 keep_proportions=False,
                 door_window_size=350,
                 random=True)
    
    return level

def get_color():
    lcolor = Levels_colors_list.FROM_HUE(hu=0.8, sa=0.1, li=0.3)
    lcolor.contour_color = Color.GREY_100
    lcolor.surrounding_color = Color.PALE_RED
    return lcolor