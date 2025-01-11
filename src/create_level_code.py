ns = 2
nd = 1
nr = 1
nv = 0
####
####
####

print('''
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list

def f(): 
''')

for i in range(ns):
    print(f'''    S{i} = Switch(name='S{i}')''')
    
print('')
print(f'''    Slist = [{', '.join([f'S{i}' for i in range(ns)])}]''')
print('')

for i in range(nv):
    print(f'    Slist_{i} = []')

for i in range(nv):
    print(f'    Slist_{i} = [S{2*i}, S{2*i+1}]')
    
for i in range(nv):
    print(f'    Slist_{i} = [S{3*i}, S{3*i+1}, S{3*i+2}]')
    
for i in range(nv):
    print(f'    Slist_{i} = [S{9*i}, S{9*i+1}, S{9*i+2}, S{9*i+3}, S{9*i+4}, S{9*i+5}, S{9*i+6}, S{9*i+7}, S{9*i+8}]')
    
for i in range(nv):
    print(f'    Slist_{i} = Sl[9*{i}:9*{i}+9]')
    
# for i in range(nv):
#     print(f'    Slist_{i} = [S{8*i}, S{8*i+1}, S{8*i+2}, S{8*i+3}, S{8*i+4}, S{8*i+5}, S{8*i+6}, S{8*i+7}]')

for i in range(nv):
    print(f'''    V{i} = Tree(tree_list=Tree.tree_list_BIN(len(Slist_{i})),
          name='V{i}',
          switches=Slist_{i})''')
    
for i in range(nv):
    print(f'''    V{i} = Tree(tree_list=Tree.tree_list_BIN(9),
          name='V{i}',
          switches=Sl[9*{i}:9*{i}+9])''')

for i in range(nv):
    print(f'''    V{i} = Tree(tree_list=tree_list_V,
          name='V{i}',
          switches=[V, 21, V])''')

if nv != 0:
    print('')
    print(f'''    Vlist = [{', '.join([f'V{i}' for i in range(nv)])}]''')
    print('')
    
for i in range(nd):
    print(f'''    T{i} = Tree(tree_list=tree_list_0,
                name='T{i}',
                switches=[1])''')
    
for i in range(nd):
    print(f'''    T{i} = get_tree({i})''')
    
for i in range(nd):
    print(f'''    T{i} = Tree(tree_list=[None],
                name='T{i}',
                switches=[1])''')
    
print('')

print('''    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5\n''')
    
for i in range(nr):
    y = i//4
    x = i%4
    # print(f'''    R{i} = Room(name='R{i}',
    #             position=[{x}*dx, {y}*dy, ex, ey],
    #             switches_list=[])''')
    print(f'''    R{i} = Room(name='R{i}',
                position=[{x}*dx, {y}*dy, ex, ey],
                switches_list=Slist_{i})''')
    # print(f'''    R{i} = Room(name='R{i}',
    #             position=position({i}),
    #             switches_list=[S{i}])''')
    
print('''    RE = Room(name='RE',
              position=[1*dx, 1*dy, ex, ey],
              is_exit=True)''')

print('')

room_names_list = [f'R{i}' for i in range(nr)] + ['RE']
# room_departure_arrival_list = []
# for i_room_departure in range(len(room_names_list)-1):
#     for a in [-4, -1, +1, +4]:
#         i_room_arrival = i_room_departure+a
#         if a == -1 and i_room_departure%4 == 0:
#             continue
#         if a == 1 and i_room_arrival%4 == 0:
#             continue
#         if 0 <= i_room_arrival < len(room_names_list):
#             room_departure_arrival_list.append([i_room_departure, i_room_arrival])
# for i in range(len(room_departure_arrival_list)):
#     i_room_departure = room_departure_arrival_list[i][0]
#     i_room_arrival = room_departure_arrival_list[i][1]
#     room_departure_name = room_names_list[i_room_departure]
#     room_arrival_name = room_names_list[i_room_arrival]
#     a = i_room_arrival - i_room_departure
#     if a == +1:
#         rdc = 'c'
#         rac = 'a'
#     elif a == -1:
#         rdc = 'b'
#         rac = 'd'
#     elif a == +4:
#         rdc = 'd'
#         rac = 'c'
#     elif a == -4:
#         rdc = 'b'
#         rac = 'a'
#     else:
#         rdc = '[1/2, 1/2]'
#         rac = '[1/2, 1/2]'
#     print(f'''    D{i} = Door(two_way=False,
#                 tree=T{i},
#                 name='D{i}',
#                 room_departure={room_departure_name},
#                 room_arrival={room_arrival_name},
#                 relative_departure_coordinates={rdc},
#                 relative_arrival_coordinates={rac})''')

for i in range(nd):
    print(f'''    D{i} = Door(two_way=False,
                tree=T{i},
                name='D{i}',
                room_departure=R{i},
                room_arrival=R{i+1})''')

print(f'''
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[{', '.join(room_names_list)}],
                 doors_list=[{', '.join([f'D{i}' for i in range(nd)])}],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='TODO',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level

def get_color():
    return Levels_colors_list.FROM_HUE(hu, sa, li)
''')

# k = 0
# for i in range(1, 7):
#     for j in range(1, i):
#         print(f"""D{k} = Door(two_way=True,
#               tree=T{k},
#               name='D{k}',
#               room_departure=R{i},
#               room_arrival=R{j},
#               relative_position=rp)""")
#         k += 1
