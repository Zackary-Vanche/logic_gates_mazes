from Maze import Maze
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Levels_colors_list import Levels_colors_list

def aux_level_random_tetractys(door_trees_list=[[i for i in range(2 ** 10)] for j in range(5)],
                                   exit_number=None):  # exit_number isn't usde but should remain as an argument

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

    Slist0 = [S0, S1, S2, S3]
    Slist1 = [S4, S5, S6]
    Slist2 = [S7, S8]
    Slist3 = [S9]
    Slist = Slist0 + Slist1 + Slist2 + Slist3

    def get_tree(i):
        tree_list = []
        li = [[0, 1, 2, 3],
              [0, 3, 4, 5, 6],
              [4, 5, 6, 7, 8],
              [4, 6, 7, 8, 9]][i]
        Slist_i = []
        for j in li:
            Slist_i.append(Slist[j])
        for j in door_trees_list[i]:
            str_j = format(j, f'0{21}b')[::-1]
            bin_j = 0
            for k in range(len(li)):
                lik = li[k]
                bin_j += int(str_j[lik]) * 2 ** k
            tree_list.append(bin_j)
        tree_list = list(set(tree_list))
        return Tree(['IN', Tree.tree_list_BIN(len(Slist_i))] + [[None]] * len(tree_list),
                    empty=True,
                    name=f'T{i}',
                    switches=Slist_i + tree_list,
                    cut_expression=True,
                    cut_expression_separator=')',
                    random_switches_bin_list=Slist_i)

    def pos(i):
        return [i/2, 6-i, (6-i+1)*0.75, 0.4]

    R0 = Room(name='R0',
              position=pos(0),
              switches_list=Slist0)
    R1 = Room(name='R1',
              position=pos(1),
              switches_list=Slist1)
    R2 = Room(name='R2',
              position=pos(2),
              switches_list=Slist2)
    R3 = Room(name='R3',
              position=pos(3),
              switches_list=Slist3)
    RE = Room(name='RE',
              position=pos(4),
              is_exit=True)  # E pour exit ou end

    D0 = Door(two_way=0,
              tree=get_tree(0),
              room_departure=R0,
              room_arrival=R1)
    D1 = Door(two_way=0,
              tree=get_tree(1),
              room_departure=R1,
              room_arrival=R2)
    D2 = Door(two_way=0,
              tree=get_tree(2),
              room_departure=R2,
              room_arrival=R3)
    D3 = Door(two_way=0,
              tree=get_tree(3),
              room_departure=R3,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3] + [RE],  # , R11, R12, R13, R14, R15, R16, R17, R18, R19
                 doors_list=[D0, D1, D2, D3],  # , D11, D12, D13, D14, D15, D16, D17, D18, D19
                 fastest_solution=None,
                 level_color=Levels_colors_list.RANDOM(),
                 name='Random - Tetractys',
                 door_window_size=800,
                 keep_proportions=True,
                 y_separation=40,
                 border=40,
                 random=True,
                 random_long=False)

    return level

def level_random_tetractys():
    # return aux_level_random_tetractys()
    return Maze.get_random_level_from_file(aux_level_random_tetractys)
    
