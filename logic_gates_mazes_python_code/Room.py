# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:53:44 2022

@author: utilisateur
"""

from numpy import ceil, sqrt
from linear_function import linear_function

class Room:
    
    def __init__(self, 
                 is_exit = False, 
                 switches_list = [], 
                 # position de la piece pour pygame
                 position = [None, None, None, None], 
                 # Dans l'ordre :
                 # ecart en y du bord
                 # ecart en x du bord
                 # longueur en y
                 # longueur en x
                 name = 'R',
                 surrounding_color=[255,255,255]):
        self.name = name
        try:
            assert self.name[0] == 'R'
        except:
            print(self.name)
            raise
        self.is_exit = is_exit
        if self.is_exit:
            assert self.name == 'RE'
        self.departure_doors_list = []
        self.arrival_doors_list = []
        self.two_way_doors_list = []
        self.switches_list = switches_list
        for switch in self.switches_list:
            switch.room = self
        self.position = position
        self.name_position = None
        self.switches_positions = None
        self.surrounding_color = surrounding_color
        
    def get_name_position(self):
        [x_gap, y_gap, x, y] = self.position
        if self.is_exit:
            self.name_position = [x_gap + x/2 - 18, y_gap + y/2 - 9]
        else:
            self.name_position = [x_gap + 5, y_gap + 5]
        return self.name_position
            
    def get_switches_positions(self): 
        [x_gap, y_gap, x, y] = self.position
        n_switches = len(self.switches_list)
        if n_switches == 0:
            return []
        positions = []
        nb_lines = int(ceil(sqrt(n_switches*x/y)))
        for k in range(n_switches):
            line = k//nb_lines
            column = k%nb_lines
            positions.append([column, line])
        # On centre les interrupteurs dans le carré
        # et on les écarte les une des autres
        x_list = [p[0] for p in positions]
        y_list = [p[1] for p in positions]
        xmax = max(x_list)
        ymax = max(y_list)
        xmin = min(x_list)
        ymin = min(y_list)

        new_xmin = max(x_gap + 0.24*x, x_gap + 35)
        new_ymin = max(y_gap + 0.24*y, y_gap + 35)
        new_xmax = min(x_gap + 0.76*x, x_gap + x - 35)
        new_ymax = min(y_gap + 0.76*y, y_gap + y - 35)
        if xmin == xmax:
            fx = lambda k : k + x_gap + x/2
        else:
            (px, cx) = linear_function(xmin, new_xmin, xmax, new_xmax)
            fx = lambda x : px*x+cx
        if ymin == ymax:
            fy = lambda k : k + y_gap + y/2
        else:
            (py, cy) = linear_function(ymin, new_ymin, ymax, new_ymax)
            fy = lambda y : py*y+cy
        for k in range(n_switches):
            [x_switch, y_switch] = positions[k]
            positions[k] = [fx(x_switch), fy(y_switch)]
        self.switches_positions = positions
        return self.switches_positions
            
    def __str__(self):
        txt =  '\n|   Room {} :'.format(self.name)
        txt += '\n|   Departure door(s) list :\n|      {}'.format([door.name for door in self.departure_doors_list])
        txt += '\n|   Arrival door(s) list :\n|      {}'.format([door.name for door in self.arrival_doors_list])
        txt += '\n|   Two-way door(s) list :\n|      {}'.format([door.name for door in self.two_way_doors_list])
        txt += '\n|   Switches list :\n|      {}'.format([switch.name for switch in self.switches_list])
        return txt