# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:01:20 2022

@author: utilisateur
"""

for i in range(30):
    print("""S{0} = Switch(name='S{0}')""".format(i))

for i in range(30):
    print("""T{0} = Tree(tree_list=[None],
            empty=True,
            name='T{0}',
            switches = [S0])""".format(i))
    
for i in range(30):
    print("""R{0} = Room(name='R{0}',
            position = [0, 0, 1, 1],
            switches_list = [])""".format(i))
    
for i in range(23):
    print("""D{0} = Door(two_way=False,
            tree=T{0},
            room_departure=R?,
            room_arrival=R?)""".format(i))