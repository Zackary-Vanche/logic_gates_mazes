# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:55:41 2022
@author: utilisateur
"""

from linear_function import linear_function
from numpy import array as array
from numpy.linalg import norm as np_linalg_norm
from time import time as time
from Level_color import Level_color
from help_menus_list import help_menus_list
# from numba import njit

class Maze: 

    # Fonctions de creation et de manipulation des differents niveaux

    calculates_solutions = False

    def __init__(self,
                 start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[],
                 doors_list=[],
                 level_color=Level_color(),
                 uniform_surrounding_colors=True,
                 uniform_inside_room_color=True,
                 fastest_solution=None,
                 name='L',
                 y_separation=50,
                 door_window_size=500,
                 border=50,
                 keep_proportions=False,
                 line_size=3,
                 random=False):
        self.random = random
        self.name = name
        self.start_room_index = start_room_index
        self.exit_room_index = exit_room_index
        if rooms_list != []:
            self.exit_room_index = self.exit_room_index % len(rooms_list)
        self.rooms_list = rooms_list
        for room in self.rooms_list:
            assert room is not None
        assert start_room_index < len(self.rooms_list)
        self.start_room = self.rooms_list[self.start_room_index]
        self.current_room_index = self.start_room_index
        self.doors_set = set()
        self.switches_set = set()
        for room in self.rooms_list:
            for door in room.departure_doors_list:
                self.add_door(door)
            for door in room.arrival_doors_list:
                self.add_door(door)
            for door in room.two_way_doors_list:
                self.add_door(door)
            for switch in room.switches_list:
                self.switches_set.add(switch)
        for room in self.rooms_list:
            for switch in room.switches_list:
                self.switches_set.add(switch)
        self.switches_dict = {}
        for switch in self.switches_set:
            self.switches_dict[switch.name] = switch
        self.rooms_dict = {}
        for room in self.rooms_list:
            self.rooms_dict[room.name] = room
        for door in self.doors_set:
            T = door.tree
            T.switch_leafs()
        self.initial_switches_values = []
        for switch in self.switches_list():
            self.initial_switches_values.append(switch.value)
        self.possibles_actions_list = []
        for switch in self.switches_set:
            self.possibles_actions_list.append(switch.name)
        for door in self.doors_set:
            self.possibles_actions_list.append(door.name)
        for room in self.rooms_list:
            self.possibles_actions_list.append(room.name)
        self.possibles_actions_list.sort()
        txterror = ', '.join([' '.join([door.name for door in self.doors_list()]), ' '.join([door.name for door in doors_list])])
        assert set(self.doors_list()) == set(doors_list), txterror
        # On verifie que aucun nom ne soit donne en double
        for i in range(len(rooms_list)):
            room_i = rooms_list[i]
            for j in range(i):
                room_j = rooms_list[j]
                assert room_i.name != room_j.name
        for i in range(len(doors_list)):
            door_i = doors_list[i]
            for j in range(i):
                door_j = doors_list[j]
                assert door_i.name != door_j.name
        switches_list = self.switches_list()
        for i in range(len(switches_list)):
            switch_i = switches_list[i]
            for j in range(i):
                switch_j = switches_list[j]
                assert switch_i.name != switch_j.name
        self.all_solutions = None
        if Maze.calculates_solutions:
            self.all_solutions = self.find_all_solutions()
        if fastest_solution is not None:
            self.fastest_solution = fastest_solution
            if self.all_solutions is not None:
                assert self.all_solutions[0] == fastest_solution
        else:
            print(self.name, 'fastest_solution is None -> TO CHANGE')
            self.fastest_solution = None
        self.extreme_coordinates = None
        self.border = border
        self.y_separation = y_separation
        self.door_window_size = door_window_size
        self.keep_proportions = keep_proportions
        self.level_color = level_color
        self.n_lines_door_printing = 0
        for k in range(len(self.doors_list())):
            door = self.doors_list()[k]
            tree = door.tree
            logical_expression = tree.get_easy_logical_expression_PN()
            logical_expression = logical_expression.split('\n')
            self.n_lines_door_printing += len(logical_expression)
        self.line_size = line_size
        self.uniform_surrounding_colors = uniform_surrounding_colors
        self.uniform_inside_room_color = uniform_inside_room_color
        if self.name in help_menus_list['levels'].keys():
            self.help_txt = [help_menus_list['levels'][self.name]]
        else:
            self.help_txt = ['']
        if len(self.help_txt[0]) > 0:
            if self.help_txt[0][0] == '\n':
                self.help_txt[0] = self.help_txt[0][1:]
        self.n_help_pages = len(self.help_txt)
        if ' '.join(self.help_txt).replace(' ', '') == '':
            print(self.name, 'empty help')
                
    def add_door(self, door):
        self.doors_set.add(door)
                
    def doors_list(self):
        l = []
        for door in self.doors_set:
            l.append(door)
        return sorted(l, key = lambda door : (len(door.name), door.name))
    
    def doors_dict(self):
        d = {}
        for door in self.doors_set:
            d[door.name] = door
        return d
    
    def switches_list(self):
        l = []
        for switch in self.switches_set:
            l.append(switch)
        return sorted(l, key = lambda switch : [len(switch.name), switch.name])
    
    def rooms_names_dict(self):
        rooms_names_dict = {}
        for i in range(len(self.rooms_list)):
            room = self.rooms_list[i]
            rooms_names_dict[room.name] = i
        return rooms_names_dict
            
    def __str__(self):
        len_line = 100
        txt = ''
        separateur = '\n' + "-"*len_line
        txt += "-"*len_line
        txt += '\n|'
        txt +=  '\n|   Maze {} :'.format(self.name)
        txt +=  '\n|   Start room index : {}'.format(self.start_room_index)
        txt +=  '\n|   Current room index : {}'.format(self.current_room_index)
        if self.all_solutions is not None:
            txt +=  '\n|   Solution(s) :'
            for sol in self.all_solutions:
                txt += '\n|      {}'.format(sol)
        elif self.fastest_solution is not None:
            txt +=  '\n|   Fastest solution :'
            txt += '\n|      {}'.format(self.fastest_solution)
        txt += '\n|'
        txt += separateur
        for room in self.rooms_list:
            txt += '\n|'
            txt += str(room)
            txt += '\n|'
            txt += separateur
        for door in self.doors_list():
            txt += '\n|'
            txt += str(door)
            txt += '\n|'
            txt += separateur
        for switch in self.switches_list():
            txt += '\n|'
            txt += str(switch)
            txt += '\n|'
            txt += separateur
        txt = txt.split('\n')
        for i in range(len(txt)):
            line = txt[i]
            if len(line) < len_line:
                while len(line) < len_line-1:
                    line += ' '
                line += '|'
            txt[i] = line
        return '\n'.join(txt)

    def current_room(self):
        return self.rooms_list[self.current_room_index]

    def current_room_name(self):
        return self.current_room().name

    def save_txt(self, title_header=''):
        if Maze.calculates_solutions and self.all_solutions is None:
            self.all_solutions = self.find_all_solutions()
        with open('{}_{}.txt'.format(title_header,
                                     self.name.replace(' ', '_')), 'w') as f:
            f.write(str(self))

    def save_txt_short(self, title_header = ''):
        self.reboot_solution()
        with open('{}_{}.txt'.format(title_header, self.name.replace(' ', '_')), 'w') as f:
            for switch in self.switches_list():
                f.write('{} : {}; '.format(switch.name, switch.value))
            f.write('\n')
            for room in self.rooms_list:
                if room.is_exit:
                    txt_exit = '(EXIT)'
                else:
                    txt_exit = ''
                f.write("{} {}: ".format(room.name, txt_exit))
                for switch in room.switches_list:
                    f.write(switch.name)
                    f.write(' ')
                f.write('\n')
            for door in self.doors_list():
                f.write("{} : ".format(door.name))
                tree = door.tree
                f.write("{}; ".format(tree.get_raw_logical_expression_RPN()))
                if door.two_way:
                    f.write("{} <-> {}\n".format(door.room_departure.name, door.room_arrival.name))
                else:
                    f.write("{} --> {}\n".format(door.room_departure.name, door.room_arrival.name))

    def change_switch(self, switch_name, update_doors=True):
        assert switch_name[0] == 'S'
        switch = self.switches_dict[switch_name]
        new_value = int(not switch.value)
        switch.set_value(new_value, update_doors)

    def legit_change_switch(self, switch_name):
        assert switch_name[0] == 'S'
        return self.current_room() == self.switches_dict[switch_name].room

    def change_switch_if_legit(self, switch_name, verbose = 0):
        if verbose >= 1:
            print(switch_name)
        if self.legit_change_switch(switch_name):
            self.change_switch(switch_name)

    def change_room(self, room_name):
        assert room_name[0] == 'R'
        self.current_room_index = self.rooms_names_dict()[room_name]
        
    def get_current_possible_rooms(self):
        visited_rooms = []
        rooms_to_visit = [self.current_room()]
        while rooms_to_visit != []:
            room_departure = rooms_to_visit[0]
            del rooms_to_visit[0]
            for door in room_departure.departure_doors_list:
                if door.is_open:
                    if door.room_arrival not in visited_rooms:
                        rooms_to_visit.append(door.room_arrival)
                        visited_rooms.append(door.room_arrival)
            for door in room_departure.two_way_doors_list:
                if door.is_open:
                    if room_departure == door.room_arrival:
                        if door.room_departure not in visited_rooms:
                            rooms_to_visit.append(door.room_departure)
                            visited_rooms.append(door.room_departure)
                    else:
                        if door.room_arrival not in visited_rooms:
                            rooms_to_visit.append(door.room_arrival)
                            visited_rooms.append(door.room_arrival)
        return visited_rooms

    def legit_change_room(self, room_name):
        assert room_name[0] == 'R'
        new_current_room_index = self.rooms_names_dict()[room_name]
        new_room = self.rooms_list[new_current_room_index]
        return new_room in self.get_current_possible_rooms()

    def change_room_if_legit(self, room_name):
        if self.legit_change_room(room_name):
            self.change_room(room_name)

    def use_door(self, door_name):
        door = self.doors_dict()[door_name]
        if door.two_way:
            current_room = self.current_room()
            room_departure = door.room_departure
            room_arrival = door.room_arrival
            if current_room == room_departure:
                self.change_room(room_arrival.name)
            if current_room == room_arrival:
                self.change_room(room_departure.name)
        else:
            new_room = door.room_arrival
            self.change_room(new_room.name)

    def legit_use_door(self, door_name):
        door = self.doors_dict()[door_name]
        if not door.is_open:
            return False
        else:
            if door.two_way:
                is_rd = self.current_room() == door.room_departure
                is_ra = self.current_room() == door.room_arrival
                return is_rd or is_ra
            else:
                return self.current_room() == door.room_departure

    def use_door_if_legit(self, door_name, verbose=0):
        if verbose >= 1:
            print(door_name)
        if self.legit_use_door(door_name):
            self.use_door(door_name)

    def reboot_solution(self,
                        current_room_index=None,
                        list_switches_values=None):
        if current_room_index is None:
            self.current_room_index = self.start_room_index
        else:
            self.current_room_index = current_room_index
        switches_list = self.switches_list()
        for i in range(len(switches_list)):
            switch = switches_list[i]
            if list_switches_values is None:
                switch.set_value(self.initial_switches_values[i], update_doors=False)
            else:
                switch.set_value(list_switches_values[i], update_doors=False)
        doors_list = self.doors_list()
        for i in range(len(doors_list)):
            door = doors_list[i]
            door.update_open()

    def make_actions(self, actions, separator=' ', allow_all=False):
        actions_list = actions.split(separator)
        for action in actions_list:
            if not (action in self.possibles_actions_list or (action in self.rooms_dict.keys() and allow_all)):
                return None
        for action in actions_list:
            action_type = action[0]
            if action_type == 'S' and (self.legit_change_switch(action) or allow_all):
                # print(action)
                self.change_switch(action)
            if action_type == 'D' and (self.legit_use_door(action) or allow_all):
                # print(action)
                self.use_door(action)
            if action_type == 'R' and (self.legit_change_room(action) or allow_all):
                # print(action)
                self.change_room(action)

    # Les solutions sont données sous forme de texte

    def try_solution(self,
                     solution,
                     separator=' ',
                     verbose=0,
                     allow_all_doors=False,
                     allow_all_switches=False,
                     door_trees_dico={}):
        # results : 0 unauthorised, 1 authorised but wrong, 2 you won
        self.reboot_solution()
        solution = solution.replace('\n', separator).split(separator)
        txt_verbose_3 = ''
        if verbose == 2:
            print("Switches values : {}".format([switch.value for switch in self.switches_list()]))
        for action in solution:
            if action in self.possibles_actions_list:
                action_type = action[0]
                if action_type == 'S':
                    if self.legit_change_switch(action) or allow_all_switches:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                        self.change_switch(action)# solutions = level_solitaire().find_all_solutions(verbose=1,
    #                                                  stop_at_first_solution=False,
    #     
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                        return 0
                if action_type == 'D':
                    if self.legit_use_door(action) or allow_all_doors:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                        self.use_door(action)
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                        return 0
                    if 3 > verbose > 0:
                        print("You are in room {}\n".format(self.current_room_name()))
                    switches_values_txt = ''
                    for switch in self.switches_list():
                        if switch.value:
                            switches_values_txt += str(switch.name) + ' '
                    txt_verbose_3 += action + ' : ' + switches_values_txt + '\n'
                    switches_TF = ''
                    for switch in self.switches_list():
                        if switch.value:
                            switches_TF = switches_TF + 'T'
                        else:
                            switches_TF = switches_TF + 'F'
                    if action not in door_trees_dico.keys():
                        door_trees_dico[action] = ''
                    door_trees_dico[action] = door_trees_dico[action] + switches_TF + ' '
                if action_type == 'R': # TODO : verify
                    if self.legit_change_room(action) or allow_all_doors:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                        self.change_room(action)
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                        return 0
                    if 3 > verbose > 0:
                        print("You are in room {}\n".format(self.current_room_name()))
                if verbose == 2:
                    switches_values_txt = '"Switches values :'
                    for switch in self.switches_list():
                        switches_values_txt += str(switch.value)
                    print(switches_values_txt)
        if 3 > verbose > 0:
            if self.current_room_index == self.exit_room_index:
                print('Success !')
            else:
                for switch in self.switches_list():
                    if switch.value:
                        print(switch.name)
                print(self.current_room_index, self.exit_room_index)
                print('Try again !')
        if verbose == 3:
            print('')
            print('\n'.join(sorted(txt_verbose_3.split('\n'))))
            print('')
            # for door in sorted(door_trees_dico.keys()):
            #     print("""tree_list_{0} = Tree.tree_list_from_str("{1}")""".format(door[1:], door_trees_dico[door][:-1]))
        bool_solution = self.current_room_index == self.exit_room_index
        return int(bool_solution) + 1
    
    def fast_try_solution(self,
                          solution,
                          separator=' '):
        # results : 0 unauthorised, 1 authorised but wrong, 2 you won
        self.reboot_solution()
        for action in solution:
            if action in self.possibles_actions_list:
                action_type = action[0]
                if action_type == 'S':
                    if self.legit_change_switch(action):
                        self.change_switch(action, update_doors=False)
                    else:
                        return 0
                if action_type == 'D':
                    door = self.doors_dict()[action]
                    door.update_open()
                    if self.legit_use_door(action):
                        self.use_door(action)
                    else:
                        return 0
        bool_solution = self.current_room_index == self.exit_room_index
        return int(bool_solution) + 1

    def current_situation_to_vector(self):
        vector = [switch.value for switch in self.switches_list()]
        vector.append(self.current_room_index)
        return tuple(vector)
    
    def get_current_possible_doors(self):
        room = self.current_room()
        current_possible_doors = []
        for door in room.departure_doors_list:
            if door.is_open:
                current_possible_doors.append(door.name)
        for door in room.two_way_doors_list:
            if door.is_open:
                current_possible_doors.append(door.name)
        current_possible_doors.sort(key=lambda l: [len(l), l])
        return current_possible_doors
    
    def get_current_possible_switches(self):
        room = self.current_room()
        current_possible_switches = []
        for switch in room.switches_list:
            current_possible_switches.append(switch.name)
        current_possible_switches.sort(key=lambda l: [len(l), l])
        return current_possible_switches

    def get_current_possible_actions_list(self):
        return self.get_current_possible_doors() + self.get_current_possible_switches()
    
    def find_all_solutions(self,
                           verbose=0,
                           stop_at_first_solution=False,
                           reverse_actions_order=False,
                           initial_try=(),
                           nb_iterations_print=10**3,
                           max_calculation_time=float('inf')):
        t0 = time()
        if self.all_solutions is None:
            visited_situations = set()
            solutions_to_visit = [initial_try]
            solutions_that_work = []
            nb_iterations = 0
            while solutions_to_visit != []:
                if time() - t0 > max_calculation_time:
                    return []
                nb_iterations += 1
                if nb_iterations % nb_iterations_print == 0 and verbose >= 1:
                     print('nb_iterations : {}'.format(nb_iterations))
                     print('solutions_to_visit[-1] : {}'.format(' '.join(solutions_to_visit[-1])))
                     print("solutions_to_visit[-1].count('D') : {}".format(' '.join(solutions_to_visit[-1]).count('D')))
                     print('len(solutions_to_visit) : {}'.format(len(solutions_to_visit)))
                     print('len(solutions_to_visit)/nb_iterations : {}'.format(len(solutions_to_visit)/nb_iterations))
                     print('len(solutions_that_work) : {}'.format(len(solutions_that_work)))
                     print('')
                solution = solutions_to_visit.pop(0)
                result_solution = self.fast_try_solution(solution)
                for door in self.doors_list():
                    door.update_open()
                if result_solution == 1:
                    current_situation_vector = self.current_situation_to_vector()
                    if current_situation_vector not in visited_situations:
                        # DOORS
                        actions_doors = self.get_current_possible_doors()
                        if reverse_actions_order:
                            actions_doors.reverse()
                        for action in actions_doors:
                            solutions_to_visit.append(solution+(action,))
                        # SWITCHES
                        if solution == () or solution[-1][0] != 'S':
                            for Slist in self.current_room().get_possible_switches_actions():
                                solutions_to_visit.append(solution+tuple(Slist)) 
                    visited_situations.add(current_situation_vector)
                elif result_solution == 2:
                    if verbose >= 1 and len(solutions_that_work) <= 10:
                        print(' '.join(solution))
                    solutions_that_work.append(solution)
                    if stop_at_first_solution:
                        self.reboot_solution()
                        self.all_solutions = solutions_that_work
                        return solutions_that_work
            # if verbose >= 3:
            #     print('Last solution tested :\n', solution)
            assert solutions_to_visit == []
            self.reboot_solution()
        else:
            solutions_that_work = self.all_solutions
        solutions_that_work = sorted(solutions_that_work, key=len)
        if not (reverse_actions_order or self.fastest_solution is None or ' '.join(solutions_that_work[0]) == self.fastest_solution):
            print(self.name, "wrong fastest solution")
            print("solution found")
            print(str(' '.join(solutions_that_work[0])))
            print("solution in memory")
            print(str(self.fastest_solution))
            print('')
        self.all_solutions = solutions_that_work
        if verbose >= 1:
            t1 = time()
            print(t1 - t0, 's')
        return solutions_that_work
    
    def old_find_all_solutions(self,
                               verbose=0,
                               stop_at_first_solution=False,
                               reverse_actions_order=False,
                               initial_try=(),
                               nb_iterations_print=10**3):
        if verbose > 1:
            t0 = time()
        if self.all_solutions is None:
            visited_situations = set()
            solutions_to_visit = [initial_try]
            solutions_that_work = []
            nb_iterations = 0
            while solutions_to_visit != []:
                nb_iterations += 1
                if nb_iterations % nb_iterations_print == 0 and verbose >= 3:
                     print('nb_iterations : {}'.format(nb_iterations))
                     print('solutions_to_visit[-1] : {}'.format(solutions_to_visit[-1]))
                     print('len(solutions_to_visit) : {}'.format(len(solutions_to_visit)))
                     print('len(solutions_to_visit)/nb_iterations : {}'.format(len(solutions_to_visit)/nb_iterations))
                     print('')
                solution = solutions_to_visit.pop(0)
                result_solution = self.fast_try_solution(solution)
                if result_solution == 1:
                    current_situation_vector = self.current_situation_to_vector()
                    if current_situation_vector not in visited_situations:
                        actions_list = self.get_current_possible_actions_list()
                        if reverse_actions_order:
                            actions_list.reverse()
                        for action in actions_list:
                            solutions_to_visit.append(solution+(action,))
                    visited_situations.add(current_situation_vector)
                elif result_solution == 2:
                    if verbose >= 1:
                        print(solution)
                    solutions_that_work.append(solution)
                    if stop_at_first_solution:
                        self.reboot_solution()
                        self.all_solutions = solutions_that_work
                        return solutions_that_work
            assert solutions_to_visit == []
            self.reboot_solution()
        else:
            solutions_that_work = self.all_solutions
        solutions_that_work = sorted(solutions_that_work, key=len)
        if not (reverse_actions_order or self.fastest_solution is None or ' '.join(solutions_that_work[0]) == self.fastest_solution):
            print(self.name, "wrong fastest solution")
            print("solution found")
            print(str(' '.join(solutions_that_work[0])))
            print("solution in memory")
            print(str(self.fastest_solution))
            print('')
        self.all_solutions = solutions_that_work
        if verbose >= 2:
            t1 = time()
            print(t1 - t0, 's')
        return solutions_that_work

    def get_extreme_coordinates(self):
        if self.extreme_coordinates is None:
            x_min = +float('inf')
            y_min = +float('inf')
            x_max = -float('inf')
            y_max = -float('inf')
            for room in self.rooms_list:
                [x_gap, y_gap, x, y] = room.position
                assert x_gap is not None
                assert y_gap is not None
                assert x is not None
                assert y is not None
                x_min = min(x_min, x_gap)
                y_min = min(y_min, y_gap)
                x_max = max(x_max, x_gap + x)
                y_max = max(y_max, y_gap + y)
            self.extreme_coordinates = [x_min, x_max, y_min, y_max]
        return self.extreme_coordinates

    def invert_x_y_coordinates(self):
        for room in self.rooms_list:
            [x_gap, y_gap, x, y] = room.position
            room.position = [y_gap, x_gap, y, x]
            self.extreme_coordinates = None

    def set_extreme_coordinates(self,
                                new_x_min,
                                new_x_max,
                                new_y_min,
                                new_y_max,
                                border,
                                keep_proportions):
        # On change les coordonnees extremes
        # mais on cherche à garder le rapport x/y des coordonnees
        [old_x_min, old_x_max, old_y_min, old_y_max] = self.get_extreme_coordinates()
        new_x_min = new_x_min + border
        new_x_max = new_x_max - border
        new_y_min = new_y_min + border
        new_y_max = new_y_max - border
        if keep_proportions:
            old_delta_x = old_x_max - old_x_min
            old_delta_y = old_y_max - old_y_min
            pente_x = (new_x_max - new_x_min) / old_delta_x
            pente_y = (new_y_max - new_y_min) / old_delta_y
            if 1/pente_x > 1/pente_y:
                new_y_moy = (new_y_min + new_y_max)/2
                (pente, coeff_x) = linear_function(old_x_min,
                                                   new_x_min,
                                                   old_x_max,
                                                   new_x_max)
                new_y_min = new_y_moy - pente*old_delta_y/2
                coeff_y = new_y_min - old_y_min*pente
            else:
                new_x_moy = (new_x_min + new_x_max)/2
                (pente, coeff_y) = linear_function(old_y_min,
                                                   new_y_min,
                                                   old_y_max,
                                                   new_y_max)
                new_x_min = new_x_moy - pente*old_delta_x/2
                coeff_x = new_x_min - old_x_min*pente
            for room in self.rooms_list:
                [x_gap, y_gap, x, y] = room.position
                x_gap = pente*x_gap+coeff_x
                y_gap = pente*y_gap+coeff_y
                x = pente*x
                y = pente*y
                room.position = [x_gap, y_gap, x, y]
                self.extreme_coordinates = None
        else:
            (pente_x, coeff_x) = linear_function(old_x_min,
                                                 new_x_min,
                                                 old_x_max,
                                                 new_x_max)
            (pente_y, coeff_y) = linear_function(old_y_min,
                                                 new_y_min,
                                                 old_y_max,
                                                 new_y_max)
            for room in self.rooms_list:
                [x_gap, y_gap, x, y] = room.position
                x_gap = pente_x*x_gap+coeff_x
                y_gap = pente_y*y_gap+coeff_y
                x = pente_x*x
                y = pente_y*y
                room.position = [x_gap, y_gap, x, y]
                self.extreme_coordinates = None
        self.calculate_doors_coordinates()

    def calculate_doors_coordinates(self):
        for door in self.doors_set:
            Rd = door.room_departure
            Ra = door.room_arrival
            cRd = door.relative_departure_coordinates
            cRa = door.relative_arrival_coordinates
            [Rd_x_gap, Rd_y_gap, Rd_x, Rd_y] = Rd.position
            [Ra_x_gap, Ra_y_gap, Ra_x, Ra_y] = Ra.position
            door.real_departure_coordinates = array([Rd_x_gap + Rd_x*cRd[0],
                                                     Rd_y_gap + Rd_y*cRd[1]])
            door.real_arrival_coordinates = array([Ra_x_gap + Ra_x*cRa[0],
                                                   Ra_y_gap + Ra_y*cRa[1]])
            rp = door.relative_position
            dc = door.real_departure_coordinates
            ac = door.real_arrival_coordinates
            door.real_middle_coordinates = rp*ac + (1-rp)*dc
            vect_unit = door.real_arrival_coordinates - door.real_departure_coordinates
            vect_unit = vect_unit / np_linalg_norm(vect_unit)
            [x, y] = vect_unit

            if door.two_way:
                l_diag = 55
                L_diag = 65
                door.arrow_coordinates = [door.real_middle_coordinates + L_diag*vect_unit/2,
                                          door.real_middle_coordinates + l_diag*array([y, -x])/2,
                                          door.real_middle_coordinates - L_diag*vect_unit/2,
                                          door.real_middle_coordinates - l_diag*array([y, -x])/2]
                door.real_middle_coordinates = door.real_middle_coordinates - array([11/2*len(door.name), 8])
            else:
                D = 20
                d = 20
                L = 25
                F = 30
                door.arrow_coordinates = [door.real_middle_coordinates + L*vect_unit,
                                          door.real_middle_coordinates + d*array([y, -x]),
                                          door.real_middle_coordinates - F*vect_unit + D*array([y, -x]),
                                          door.real_middle_coordinates - F*vect_unit - D*array([y, -x]),
                                          door.real_middle_coordinates - d*array([y, -x])]
                door.real_middle_coordinates = door.real_middle_coordinates - array([11/2*len(door.name), 8])-10*vect_unit