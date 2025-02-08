from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def f(fast_solution_finding=False):

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

    Slist = [S0, S1,
             S2, S3, S4, S5,
             S6, S7, S8, S9, S10, S11,
             S12, S13, S14, S15, S16, S17,
             S18, S19, S20, S21,
             S22, S23]

    Slisttree = [0, 0, S1, S0,
                 S1, 0, S2, S3,
                 0, S0, S4, S5,
                 0, S5, S7, S6,
                 S4, S3, S9, S8,
                 S2, 0, S11, S10,
                 S11, 0, 0, S12,
                 S9, S10, S13, S14,
                 S7, S8, S15, S16,
                 0, S6, S17, 0,
                 S17, S16, S18, 0,
                 S15, S14, S20, S19,
                 S13, S12, 0, S21,
                 S20, S21, 0, S22,
                 S18, S19, S23, 0,
                 S23, S22, 0, 0]

    def tree_list(n):
        return ['NOT', ['IN'] + [Tree.tree_list_BIN(4)]*(n+1)]

    def Slist_tree_n(n):
        return Slisttree[4*n:4*n+4] + Slisttree[:4*n]

    if fast_solution_finding:
        T0 = Tree(tree_list=[None],
                  name='T0',
                  switches=[1],
                   cut_expression=True)
        T1 = Tree(tree_list=tree_list(1),
                  name='T1',
                  switches=Slist_tree_n(1),
                   cut_expression=True)
        T2 = Tree(tree_list=tree_list(2),
                  name='T2',
                  switches=Slist_tree_n(2),
                   cut_expression=True)
        T3 = Tree(tree_list=tree_list(3),
                  name='T3',
                  switches=Slist_tree_n(3),
                   cut_expression=True)
        T4 = Tree(tree_list=tree_list(4),
                  name='T4',
                  switches=Slist_tree_n(4),
                   cut_expression=True)
        T5 = Tree(tree_list=tree_list(5),
                  name='T5',
                  switches=Slist_tree_n(5),
                   cut_expression=True)
        T6 = Tree(tree_list=tree_list(6),
                  name='T6',
                  switches=Slist_tree_n(6),
                   cut_expression=True)
        T7 = Tree(tree_list=tree_list(7),
                  name='T7',
                  switches=Slist_tree_n(7),
                   cut_expression=True)
        T8 = Tree(tree_list=tree_list(8),
                  name='T8',
                  switches=Slist_tree_n(8),
                   cut_expression=True)
        T9 = Tree(tree_list=tree_list(9),
                  name='T9',
                  switches=Slist_tree_n(9),
                   cut_expression=True)
        T10 = Tree(tree_list=tree_list(10),
                   name='T10',
                   switches=Slist_tree_n(10),
                   cut_expression=True)
        T11 = Tree(tree_list=tree_list(11),
                   name='T11',
                   switches=Slist_tree_n(11),
                   cut_expression=True)
        T12 = Tree(tree_list=tree_list(12),
                   name='T12',
                   switches=Slist_tree_n(12),
                   cut_expression=True)
        T13 = Tree(tree_list=tree_list(13),
                   name='T13',
                   switches=Slist_tree_n(13),
                   cut_expression=True)
    else:
        T0 = Tree(tree_list=[None],
                  name='T0',
                  switches=[1])
        T1 = Tree(tree_list=[None],
                  name='T1',
                  switches=[1])
        T2 = Tree(tree_list=[None],
                  name='T2',
                  switches=[1])
        T3 = Tree(tree_list=[None],
                  name='T3',
                  switches=[1])
        T4 = Tree(tree_list=[None],
                  name='T4',
                  switches=[1])
        T5 = Tree(tree_list=[None],
                  name='T5',
                  switches=[1])
        T6 = Tree(tree_list=[None],
                  name='T6',
                  switches=[1])
        T7 = Tree(tree_list=[None],
                  name='T7',
                  switches=[1])
        T8 = Tree(tree_list=[None],
                  name='T8',
                  switches=[1])
        T9 = Tree(tree_list=[None],
                  name='T9',
                  switches=[1])
        T10 = Tree(tree_list=[None],
                   name='T10',
                   switches=[1])
        T11 = Tree(tree_list=[None],
                   name='T11',
                   switches=[1])
        T12 = Tree(tree_list=[None],
                   name='T12',
                   switches=[1])
        T13 = Tree(tree_list=[None],
                   name='T13',
                   switches=[1])
    T14 = Tree(tree_list=['AND',
                          ['DIFF'] + [Tree.tree_list_BIN(4)]*16,
                          ['EQU', ['MOD', Tree.tree_list_BIN(24), [None]], [None]]],
               name='T14',
               switches=Slisttree + Slist + [89, 24],
               cut_expression=True)
    def pos(i):
        pos = [(i%2)*7, i, 5, 1]
        if i%4 == 3:
            pos[0] += pos[2]*1.1
        if i%4 == 0:
            pos[0] -= pos[2]*1.1
        return pos

    R0 = Room(name='R0',
              position=pos(0),
              switches_list=[S0, S1])
    R1 = Room(name='R1',
              position=pos(1),
              switches_list=[S2, S3])
    R2 = Room(name='R2',
              position=pos(2),
              switches_list=[S4, S5])
    R3 = Room(name='R3',
              position=pos(3),
              switches_list=[S6, S7])
    R4 = Room(name='R4',
              position=pos(4),
              switches_list=[S8, S9])
    R5 = Room(name='R5',
              position=pos(5),
              switches_list=[S10, S11])
    R6 = Room(name='R6',
              position=pos(6),
              switches_list=[S12])
    R7 = Room(name='R7',
              position=pos(7),
              switches_list=[S13, S14])
    R8 = Room(name='R8',
              position=pos(8),
              switches_list=[S15, S16])
    R9 = Room(name='R9',
              position=pos(9),
              switches_list=[S17])
    R10 = Room(name='R10',
               position=pos(10),
               switches_list=[S18])
    R11 = Room(name='R11',
               position=pos(11),
               switches_list=[S19, S20])
    R12 = Room(name='R12',
               position=pos(12),
               switches_list=[S21])
    R13 = Room(name='R13',
               position=pos(13),
               switches_list=[S22])
    R14 = Room(name='R14',
               position=pos(14),
               switches_list=[S23])
    RE = Room(name='RE',
              position=pos(15),
    is_exit = True)  # E pour exit ou end

    rp = 0.5
    rdc = [1/2, 1/2]
    rac = [1/2, 1/2]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=R8,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R8,
              room_arrival=R9,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R9,
              room_arrival=R10,
              relative_position=rp,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rac)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R10,
               room_arrival=R11,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R11,
               room_arrival=R12,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R12,
               room_arrival=R13,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D13 = Door(two_way=False,
               tree=T13,
               room_departure=R13,
               room_arrival=R14,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)
    D14 = Door(two_way=False,
               tree=T14,
               room_departure=R14,
               room_arrival=RE,
               relative_position=rp,
               relative_departure_coordinates=rdc,
               relative_arrival_coordinates=rac)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14],
                 fastest_solution='D0 S2 S3 D1 S5 D2 S7 D3 S8 S9 D4 S10 S11 D5 D6 S13 S14 D7 S16 D8 S17 D9 S18 D10 D11 S21 D12 S22 D13 S23 D14',
                 level_color=get_color(),
                 name='Sign',
                 door_window_size=300,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 door_multipages=fast_solution_finding)

    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu=0.5, sa=0.4, li=0.3)