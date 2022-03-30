# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:21:09 2022

@author: utilisateur
"""

n = 12
for i in range(2, n+2):
    if i%2 == 0:
        print("""D{0}  = Door(two_way = True,  
            tree = T{0},  
            name='D{0}',  
            room_departure = R1, 
            room_arrival = R{1}, 
            relative_arrival_coordinates = [0, 0])""".format(i-1, i))
    else:
        print("""D{0}  = Door(two_way = True,  
            tree = T{0},  
            name='D{0}',  
            room_departure = R1, 
            room_arrival = R{1}, 
            relative_arrival_coordinates = [0, 0],
            relative_position=p)""".format(i-1, i))
for i in range(2, n+2):
    if i%2 == 1:
        print("""D{0}  = Door(two_way = True,  
            tree = T{0},  
            name='D{0}',  
            room_departure = R14, 
            room_arrival = R{1}, 
            relative_arrival_coordinates = [1, 1])""".format(i+n-1, i))
    else:
        print("""D{0}  = Door(two_way = True,  
            tree = T{0},  
            name='D{0}',  
            room_departure = R14, 
            room_arrival = R{1}, 
            relative_arrival_coordinates = [1, 1],
            relative_position=p)""".format(i+n-1, i))