ns = 0
nd = 4*8+1
nr = 0

print('''
from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_(): 
''')

for i in range(ns):
    print(f'''    S{i} = Switch(name='S{i}')''')
    
print('')
    
for i in range(nd):
    print(f'''    T{i} = Tree(tree_list=[None],
                empty=True,
                name='T{i}',
                switches=[1])''')
    
print('')
    
for i in range(nr):
    print(f'''    R{i} = Room(name='R{i}',
                position=[,,,],
                switches_list=[])''')
    
print('''    RE = Room(name='RE',
              position=[,,,],
              is_exit=True)''')

print('')

for i in range(nd):
    print(f'''    D{i} = Door(two_way=False,
                tree=T{i},
                name='D{i}',
                room_departure=R0,
                room_arrival=RE)''')

print(f'''
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[{', '.join([f'R{i}' for i in range(nr)] + ['RE'])}],
                 doors_list=[{', '.join([f'D{i}' for i in range(nd)])}],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='TODO',
                 keep_proportions=True,
                 door_window_size=500)
    
    return level''')

print(f'''[{', '.join([f'S{i}' for i in range(ns)])}]''')