from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_superflip():
    
    f = 8
    
    temp_values = [[1, 1, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0],
                   [1, 1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [0, 0, 1, 1, 1, 1],]

    temp_initial_values_index = [1, 4, 1, 5, 1, 3, 1, 2,
                                 2, 4, 2, 1, 2, 3, 2, 6,
                                 3, 1, 3, 5, 3, 6, 3, 2,
                                 4, 1, 4, 5, 4, 6, 4, 2,
                                 5, 4, 5, 1, 5, 3, 5, 6,
                                 6, 4, 6, 5, 6, 3, 6, 2,]
    
    initial_values_list = []
    for v in temp_initial_values_index:
        initial_values_list.extend(temp_values[v-1])
    
    final_values_list = temp_values[0]*f + temp_values[1]*f + temp_values[2]*f + temp_values[3]*f + temp_values[4]*f + temp_values[5]*f

    assert set(initial_values_list) == set(final_values_list)

    Slist = [Switch(name='S{}'.format(i), value=initial_values_list[i]) for i in range(144*2)]
    
    # D0
    index2 = [[j*48+i*6 for i in range(8)] for j in range(6)] + [[]]
    index3 = [[144, 150, 156, 204, 210, 216, 108, 102, 96, 72, 66, 60],
               [180, 186, 144, 0, 42, 36, 96, 138, 132, 276, 282, 240],
               [36, 30, 24, 216, 222, 228, 264, 270, 276, 84, 78, 72],
               [0, 6, 12, 204, 198, 192, 252, 246, 240, 48, 54, 60],
               [168, 162, 156, 12, 18, 24, 108, 114, 120, 264, 258, 252],
               [180, 174, 168, 192, 234, 228, 120, 126, 132, 84, 90, 48],] + [[]]
    
    assert len(index2) == 7
    assert len(index3) == 7

    l_dico = []
    for i in range(7):
        l2 = index2[i]
        l3 = index3[i]
        dico = {2*i:2*i+1 for i in range(144)}
        for j in range(len(l2)):
            a = l2[j]
            assert a in dico.keys()
            b = l2[(j+2)%len(l2)]+1
            dico[a] = b
        for j in range(len(l3)):
            a = l3[j]
            assert a in dico.keys()
            b = l3[(j+3)%len(l3)]+1
            dico[a] = b
        assert set(dico.keys()) == set([2*i for i in range(144)])
        l_dico.append(dico)
        
    l_switches = []
    for i in range(7):
        dico = l_dico[i]
        switches = []
        for j in range(12):
            for k in range(12):
                a = 2*(j*12+k)
                switches.append(Slist[a])
            for k in range(12):
                a = 2*(j*12+k)
                b = dico[a]
                switches.append(Slist[b])
        l_switches.append(switches)
    
    tree_list = ['AND'] + [['EQU', Tree.tree_list_BIN(12), Tree.tree_list_BIN(12)]]*12

    T0 = Tree(tree_list=tree_list,
              empty=True,
              name='T0',
              switches = l_switches[0],
              cut_expression=True)
    T1 = Tree(tree_list=tree_list,
              empty=True,
              name='T1',
              switches = l_switches[1],
              cut_expression=True)
    T2 = Tree(tree_list=tree_list,
              empty=True,
              name='T2',
              switches = l_switches[2],
              cut_expression=True)
    T3 = Tree(tree_list=tree_list,
              empty=True,
              name='T3',
              switches = l_switches[3],
              cut_expression=True)
    T4 = Tree(tree_list=tree_list,
              empty=True,
              name='T4',
              switches = l_switches[4],
              cut_expression=True)
    T5 = Tree(tree_list=tree_list,
              empty=True,
              name='T5',
              switches = l_switches[5],
              cut_expression=True)
    T6 = Tree(tree_list=tree_list,
              empty=True,
              name='T6',
              switches = l_switches[6],
              cut_expression=True)
    
    switches_D7 = []
    for i in range(24):
        for j in range(12):
            a = i*12+j
            switches_D7.append(Slist[a])
        for j in range(12):
            switches_D7.append(Switch(value=final_values_list[i*12+j]))
    
    T7 = Tree(tree_list=['AND'] + [['EQU', Tree.tree_list_BIN(12), Tree.tree_list_BIN(12)]]*24,
              empty=True,
              name='T7',
              switches = switches_D7,
              cut_expression=True)
    
    x = 90
    y = 160
    dx = 15
    rx = 15
    ry = 10
    
    R0 = Room(name='R0',
              position = [0, 0, x, y],
              switches_list = [Slist[2*i] for i in range(144)])
    R1 = Room(name='R1',
              position = [x+dx, 0, x, y],
              switches_list = [Slist[2*i+1] for i in range(144)])
    RE = Room(name='RE',
              position=[x+dx/2-rx/2, -10, rx, ry],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.55
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 0.5/7],
              relative_arrival_coordinates=[0, 0.5/7])
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 1.5/7],
              relative_arrival_coordinates=[0, 1.5/7])
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 2.5/7],
              relative_arrival_coordinates=[0, 2.5/7])
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 3.5/7],
              relative_arrival_coordinates=[0, 3.5/7])
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 4.5/7],
              relative_arrival_coordinates=[0, 4.5/7])
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=[1, 5.5/7],
              relative_arrival_coordinates=[0, 5.5/7])
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp,
              relative_departure_coordinates=[0, 6.5/7],
              relative_arrival_coordinates=[1, 6.5/7])
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R0,
              room_arrival=RE,
              relative_position=0.7,
              relative_departure_coordinates=[0, 0],
              relative_arrival_coordinates=[1/2, 0.1])

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0.1, li=0.5, sa=0.6),
                 name='Superflip',
                 door_window_size=350,
                 keep_proportions=True,
                 y_separation=40,
                 border=15,
                 door_multipages=True)

    return level