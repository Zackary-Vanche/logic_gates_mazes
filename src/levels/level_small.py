from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_small():

    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    
    Slist = [S0, S1, S2, S3]
    
    V0 = Tree(tree_list=Tree.tree_list_BIN(len(Slist)),
              empty=True,
              name='V0',
              switches = Slist)
    
    def tree_list_IN(n):
        return ['IN'] + [[None]]*(n+1)
    
    door_trees_list = [[i for i in range(15)]]*20
    door_trees_list = [[1, 10, 11, 12], [3, 6, 8, 14], [0, 3, 7, 8], [10, 11], [14], [1, 12], [5], [0, 7], [0, 9, 10], [6, 8], [1, 3, 6, 12], [2, 9, 11, 14], [13]]
    
    def get_tree(i):
        try:
            return Tree(tree_list_IN(len(door_trees_list[i])),
                        empty=True,
                        name=f'T{i}',
                        switches = [V0] + door_trees_list[i],
                        cut_expression=True)
        except IndexError:
            print(i, len(door_trees_list))
            raise
    
    T0 = get_tree(0)
    T1 = get_tree(1)
    T2 = get_tree(2)
    T3 = get_tree(3)
    T4 = get_tree(4)
    T5 = get_tree(5)
    T6 = get_tree(6)
    T7 = get_tree(7)
    T8 = get_tree(8)
    T9 = get_tree(9)
    T10 = get_tree(10)
    T11 = get_tree(11)
    T12 = get_tree(12)
    
    R0 = Room(name='R0',
              position = [0, 0, 1, 1],
              switches_list = [S0])
    R1 = Room(name='R1',
              position = [2, 0, 1, 1],
              switches_list = [S1])
    R2 = Room(name='R2',
              position = [0, 2, 1, 1],
              switches_list = [S2])
    R3 = Room(name='R3',
              position = [2, 2, 1, 1],
              switches_list = [S3])
    RE = Room(name='RE',
              position=[-1, 2, 0.5, 1],
              is_exit=True)   # E pour exit ou end
    
    rp = 0.4
    
    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_position=rp)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R0,
              relative_position=rp)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R0,
              room_arrival=R2,
              relative_position=rp)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R2,
              room_arrival=R0,
              relative_position=rp)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R0,
              room_arrival=R3,
              relative_position=rp)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R3,
              room_arrival=R0,
              relative_position=rp)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R1,
              room_arrival=R2,
              relative_position=rp)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R2,
              room_arrival=R1,
              relative_position=rp)
    D8 = Door(two_way=False,
              tree=T8,
              room_departure=R1,
              room_arrival=R3,
              relative_position=rp)
    D9 = Door(two_way=False,
              tree=T9,
              room_departure=R3,
              room_arrival=R1,
              relative_position=rp)
    D10 = Door(two_way=False,
               tree=T10,
               room_departure=R2,
               room_arrival=R3,
               relative_position=rp)
    D11 = Door(two_way=False,
               tree=T11,
               room_departure=R3,
               room_arrival=R2,
               relative_position=rp)
    D12 = Door(two_way=False,
               tree=T12,
               room_departure=R2,
               room_arrival=RE,
               relative_departure_coordinates=[0, 1/2],
               relative_arrival_coordinates=[1, 1/2],
               relative_position=0.45)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3] + [RE],
                 intermediate_values_list=[V0],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12],
                 fastest_solution='S0 D0 S1 D1 D2 S2 D7 S1 D6 S2 D10 S3 D11 S2 D12',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=0.2, li=0.8),
                 name='Small',
                 door_window_size=300,
                 keep_proportions=False,
                 y_separation=40,
                 border=40)
    
    return level