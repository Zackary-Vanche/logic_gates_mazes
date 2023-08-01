ns = 18+11
nd = 21
nr = 11

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
print(f'''    Slist = [{', '.join([f'S{i}' for i in range(ns)])}]''')
print('')
    
for i in range(nd):
    print(f'''    T{i} = Tree(tree_list=[None],
                empty=True,
                name='T{i}',
                switches=[S{i-1}])''')
    
print('')
    
for i in range(nr):
    x = (i-1)%4
    y = (i-1)//4
    print(f'''    R{i} = Room(name='R{i}',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=[])''')
    
print('''    RE = Room(name='RE',
              position=[0, 0, ex, ey],
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
