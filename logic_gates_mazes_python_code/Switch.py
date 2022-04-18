# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:49:37 2022

@author: utilisateur
"""

class Switch:

    def __init__(self, 
                 room = None, 
                 tree = None, 
                 value = 0, 
                 name = 'S'):
        self.value = value
        self.room  = room
        self.name  = name
        try:
            assert self.name[0] == 'S' or self.name in ['0', '1']
        except:
            print(self.name[0])
            raise
        self.doors_set = set()
        self.tree = tree

    def add_door(self, door):
        assert door is not None
        self.doors_set.add(door)

    def set_value(self, new_value):
        self.value = new_value
        for door in self.doors_set:
            door.update_open()

    def __str__(self):
        txt = ''
        txt += '\n|   Switch {} :'.format(self.name)
        txt += '\n|   Room : {}'.format(self.room.name)
        door_name_list = [door.name for door in self.doors_set]
        txt += '\n|   Doors : {}'.format(door_name_list)
        txt += '\n|   Tree : {}'.format(self.tree.name)
        return txt