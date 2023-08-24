from linear_function import linear_function
from numpy import array as array
from numpy.linalg import norm as np_linalg_norm
from time import time as time
from Level_color import Level_color
from help_menus_list import help_menus_list
from random import shuffle as rd_shuffle
from random import seed as rd_seed
from random import choice as rd_choice
from random import randint as rd_randint
from random import random as rd_random
from pickle import dump as pickle_dump
from pickle import load as pickle_load
# from numba import njit

from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from os import remove as os_remove
from os import listdir as os_listdir

from Logic_Gate import Logic_Gate
from Tree import Tree
from Door import Door
from Switch import Switch

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
                 random=False,
                 current_page=0,
                 door_multipages=False,
                 current_door_page=0,
                 do_not_write_trees_always_open=False,
                 random_long=False,
                 random_several_exit=False,
                 exit_doors_indexes=[],
                 group='',
                 unique_solution=True):

        self.group = group
        self.unique_solution = unique_solution

        self.random = random
        # A level is said random only if you need to use the function save_random_door_trees_list to creates some versions of it
        # Some levels have a random component (level_tree, level_sum, level_dichotomy, etc) but are not considered as random.
        self.random_long = random_long
        self.random_several_exit = random_several_exit
        self.exit_doors_indexes = exit_doors_indexes
        self.name = name
        self.start_room_index = start_room_index
        self.exit_room_index = exit_room_index

        # ROOMS LIST

        if rooms_list != []:
            self.exit_room_index = self.exit_room_index % len(rooms_list)
        self.rooms_list = rooms_list
        for room in self.rooms_list:
            assert room is not None
            room.maze = self
        assert start_room_index < len(self.rooms_list)

        # ROOM DICT

        self.rooms_dict = {}
        for room in self.rooms_list:
            self.rooms_dict[room.name] = room

        # ROOMS NAMES DICT

        self.rooms_names_dict = {}
        for i in range(len(self.rooms_list)):
            self.rooms_names_dict[self.rooms_list[i].name] = i

        # START AND CURRENT ROOM

        self.start_room = self.rooms_list[self.start_room_index]
        self.current_room_index = self.start_room_index

        # DOORS SET

        self.doors_set = set()
        for room in self.rooms_list:
            for door in room.departure_doors_list:
                self.doors_set.add(door)
            for door in room.arrival_doors_list:
                self.doors_set.add(door)
            for door in room.two_way_doors_list:
                self.doors_set.add(door)

        # DOORS DICT

        self.doors_dict = {}
        for door in self.doors_set:
            self.doors_dict[door.name] = door

        # DOOR LIST

        self.doors_list = []
        for door in self.doors_set:
            self.doors_list.append(door)
        self.doors_list = sorted(self.doors_list, key=lambda door: (len(door.name), door.name))

        # DOOR NAMES LIST

        self.door_names_list = self.doors_dict.keys()

        # SWITCHES SET

        self.switches_set = set()
        for room in self.rooms_list:
            for switch in room.switches_list:
                self.switches_set.add(switch)

        # SWITCHES DICT

        self.switches_dict = {}
        for switch in self.switches_set:
            self.switches_dict[switch.name] = switch

        # SWITCHES LIST

        self.switches_list = []
        for switch in self.switches_set:
            self.switches_list.append(switch)
        self.switches_list = sorted(self.switches_list, key=lambda switch: [len(switch.name), switch.name])

        ####################

        for door in self.doors_set:
            T = door.tree
            T.switch_leafs()
        self.initial_switches_values = []
        for switch in self.switches_list:
            self.initial_switches_values.append(switch.get_value())
        self.possibles_actions_list = []
        for switch in self.switches_set:
            self.possibles_actions_list.append(switch.name)
        for door in self.doors_set:
            self.possibles_actions_list.append(door.name)
        for room in self.rooms_list:
            self.possibles_actions_list.append(room.name)
        self.possibles_actions_list.sort()
        txterror = ', '.join([' '.join([door.name for door in self.doors_list]),
                              ' '.join([door.name for door in doors_list])])
        assert set(self.doors_list) == set(doors_list), txterror
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
        switches_list = self.switches_list
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
            # print(self.name, 'fastest_solution is None -> TO CHANGE')
            self.fastest_solution = None
        self.extreme_coordinates = None
        self.border = border
        self.y_separation = y_separation
        self.door_window_size = door_window_size
        self.keep_proportions = keep_proportions
        self.level_color = level_color
        self.n_lines_door_printing = 0
        self.do_not_write_trees_always_open = do_not_write_trees_always_open
        for k in range(len(self.doors_list)):
            door = self.doors_list[k]
            tree = door.tree
            logical_expression = tree.get_easy_logical_expression_PN()
            logical_expression = logical_expression.split('\n')
            if not (self.do_not_write_trees_always_open and logical_expression == ['1']):
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
        self.current_page = current_page
        self.number_of_pages = 0
        for room in self.rooms_list:
            self.number_of_pages = max(self.number_of_pages, max(room.pages_list) + 1)
        for door in self.doors_set:
            door.maze = self
            Rd = door.room_departure
            Ra = door.room_arrival
            for ipage in range(self.number_of_pages):
                if ipage in Rd.pages_list and ipage in Ra.pages_list:
                    door.pages_list.append(ipage)
        self.door_multipages = door_multipages
        self.current_door_page = current_door_page
        
        self.intermediate_values_list = []
        
        list_to_visit = self.doors_list[:]
        while len(list_to_visit) != 0:
            # print(list_to_visit)
            x = list_to_visit.pop(0)
            if type(x) == Door:
                list_to_visit.extend(x.tree.all_switches_list)
            if type(x) == Tree:
                self.intermediate_values_list.append(x)
                list_to_visit.extend(x.all_switches_list)
        self.intermediate_values_list = list(set(self.intermediate_values_list))
        
        self.intermediate_values_list.sort(key = lambda x : int(x.name[1:]))
        
        intermediate_values_names = [t.name for t in self.intermediate_values_list]
        assert len(intermediate_values_names) == len(set(intermediate_values_names)), str(intermediate_values_names)
        
        # ROOTS SET
        self.roots_names_set = set()
        for door in self.doors_list:
            tree_list = [door.tree]
            while len(tree_list) != 0:
                tree = tree_list.pop(0)
                if type(tree.root) == Logic_Gate:
                    root_name = tree.root.name
                    self.roots_names_set.add(root_name)
                    tree_list.extend(tree.sons_list)
        
        help_menu = []
        if self.help_txt[0].replace(' ', '').replace('\n', '') != '':
            help_menu.append(self.help_txt[0])
        if len(self.intermediate_values_list) != 0:
            help_menu.append(help_menus_list['V'])
        for root in Logic_Gate.func_dict.keys():
            help_menus_list[root]
            if root in self.roots_names_set:
                help_menu.append(help_menus_list[root])
        if self.random:
            help_menu.append(help_menus_list['random'])
        self.help_txt[0] = '\n'.join(help_menu)

    def __str__(self):
        len_line = 100
        txt = ''
        separateur = '\n' + "-" * len_line
        txt += "-" * len_line
        txt += '\n|'
        txt += '\n|   Maze {} :'.format(self.name)
        txt += '\n|   Start room index : {}'.format(self.start_room_index)
        txt += '\n|   Current room index : {}'.format(self.current_room_index)
        if self.all_solutions is not None:
            txt += '\n|   Solution(s) :'
            for sol in self.all_solutions:
                txt += '\n|      {}'.format(sol)
        elif self.fastest_solution is not None:
            txt += '\n|   Fastest solution :'
            txt += '\n|      {}'.format(self.fastest_solution)
        txt += '\n|'
        txt += separateur
        for room in self.rooms_list:
            txt += '\n|'
            txt += str(room)
            txt += '\n|'
            txt += separateur
        for door in self.doors_list:
            txt += '\n|'
            txt += str(door)
            txt += '\n|'
            txt += separateur
        for switch in self.switches_list:
            txt += '\n|'
            txt += str(switch)
            txt += '\n|'
            txt += separateur
        txt = txt.split('\n')
        for i in range(len(txt)):
            line = txt[i]
            if len(line) < len_line:
                while len(line) < len_line - 1:
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

    def save_txt_short(self, title_header=''):
        self.reboot_solution()
        with open('{}_{}.txt'.format(title_header,
                                     self.name.replace(' ', '_')), 'w') as f:
            for switch in self.switches_list:
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
            for door in self.doors_list:
                f.write("{} : ".format(door.name))
                tree = door.tree
                f.write("{}; ".format(tree.get_raw_logical_expression_RPN()))
                if door.two_way:
                    f.write("{} <-> {}\n".format(door.room_departure.name,
                                                 door.room_arrival.name))
                else:
                    f.write("{} --> {}\n".format(door.room_departure.name,
                                                 door.room_arrival.name))

    def change_switch(self, switch_name, update_doors=True):
        assert switch_name[0] == 'S'
        switch = self.switches_dict[switch_name]
        new_value = int(not switch.value)
        switch.set_value(new_value, update_doors)

    def legit_change_switch(self, switch_name):
        assert switch_name[0] == 'S'
        return self.current_room() == self.switches_dict[switch_name].room

    def change_switch_if_legit(self,
                               switch_name,
                               verbose=0):
        if verbose >= 1:
            print(switch_name)
            pass
        if self.legit_change_switch(switch_name):
            self.change_switch(switch_name)

    def change_room(self, room_name):
        assert room_name[0] == 'R'
        self.current_room_index = self.rooms_names_dict[room_name]

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
        new_current_room_index = self.rooms_names_dict[room_name]
        new_room = self.rooms_list[new_current_room_index]
        return new_room in self.get_current_possible_rooms()

    def change_room_if_legit(self, room_name):
        if self.legit_change_room(room_name):
            self.change_room(room_name)

    def use_door(self, door_name):
        door = self.doors_dict[door_name]
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
        door = self.doors_dict[door_name]
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
            pass
        if self.legit_use_door(door_name):
            self.use_door(door_name)

    def reboot_solution(self, fast=False):
        self.current_room_index = self.start_room_index
        switches_list = self.switches_list
        for i in range(len(switches_list)):
            switches_list[i].set_value(self.initial_switches_values[i], update_doors=False)
        if not fast:
            doors_list = self.doors_list
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
        if isinstance(solution, str):
            solution = solution.replace('\n', separator).split(separator)
        txt_verbose_3 = ''
        if verbose == 2:
            print("Switches values : {}".format([switch.value for switch in self.switches_list]))
            pass
        for door_name in self.door_names_list:
            door_trees_dico[door_name] = set()
        for action in solution:
            if action in self.possibles_actions_list:
                action_type = action[0]
                if action_type == 'S':
                    if self.legit_change_switch(action) or allow_all_switches:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                            pass
                        self.change_switch(action)
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                            pass
                        return 0
                if action_type == 'D':
                    if self.legit_use_door(action) or allow_all_doors:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                            pass
                        self.use_door(action)
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                            pass
                        return 0
                    if 3 > verbose > 0:
                        print("You are in room {}\n".format(self.current_room_name()))
                        pass
                    sv = 0
                    door = self.doors_dict[door_name]
                    if door.tree.random_switches_bin_list != []:
                        switches_list = door.tree.random_switches_bin_list
                    else:
                        switches_list = self.switches_list
                    for i in range(len(switches_list)):
                        sv += self.switches_list[i].value * 2 ** i
                    txt_verbose_3 += action + ' : ' + str(sv) + '\n'
                    door_trees_dico[action].add(sv)
                if action_type == 'R':
                    if self.legit_change_room(action) or allow_all_doors:
                        if 3 > verbose > 0:
                            print('{} is authorised'.format(action))
                            pass
                        self.change_room(action)
                    else:
                        if 3 > verbose > 0:
                            print('{} is not authorised'.format(action))
                            pass
                        return 0
                    if 3 > verbose > 0:
                        print("You are in room {}\n".format(self.current_room_name()))
                        pass
                if verbose == 2:
                    switches_values_txt = '"Switches values :'
                    for switch in self.switches_list:
                        switches_values_txt += str(switch.value)
                    print(switches_values_txt)
        if 3 > verbose > 0:
            if self.current_room_index == self.exit_room_index:
                print('Success !')
                pass
            else:
                for switch in self.switches_list:
                    if switch.value:
                        print(switch.name)
                        pass
                print(self.current_room_index, self.exit_room_index)
                print('Try again !')
        if verbose == 3:
            door_trees_list = []
            for door_name in sorted(door_trees_dico.keys(), key=lambda door_name: int(door_name[1:])):
                door_trees_list.append(sorted(list(door_trees_dico[door_name])))
            return door_trees_list
        bool_solution = self.current_room_index == self.exit_room_index
        return int(bool_solution) + 1

    def save_random_door_trees_list(aux_level_function, n_files=64, i0=0):  # use it with aux level fonctions

        aux_level = aux_level_function()
        n_bin = 2 ** len(aux_level.switches_list)
        folder = f'levels/{aux_level.name}'
        if not os_path_exists(folder):
            os_mkdir(folder)

        for seed in range(i0, i0 + n_files):

            file_name = folder + f'/door_trees_list_{seed}'
            if not os_path_exists(file_name):

                # Choix de la graine de génération de nombre aléatoires
                rd_seed(seed)
                print('seed', seed)
                exit_number = rd_randint(0, n_bin - 1)
                if aux_level.random_several_exit:
                    exit_door = rd_choice(aux_level.exit_doors_indexes)
                    print('exit_door =', exit_door)
                    aux_level = aux_level_function(exit_number=exit_number,
                                                   exit_door=exit_door)
                else:
                    print('Only one exit')
                    aux_level = aux_level_function(exit_number=exit_number)
                print('exit_number =', exit_number)

                # Calcul de la solution du niveau et de la première door_trees_list correspondante
                aux_level.all_solutions = None
                solutions = aux_level.find_all_solutions(verbose=0,
                                                         DFS=False,
                                                         random_search=True,
                                                         save_solutions_txt=False)
                assert solutions[0] != []
                solutions[0].sort(key=lambda sol: sol.count('D'))
                door_trees_list = aux_level.try_solution(' '.join(solutions[0][-1]), verbose=3)
                # print(' '.join(solutions[0][-1]))

                # Ajout de nombres à door_trees_list tant que la solution reste identique (pour rendre la résolution plus compliquée)
                door_trees_list_copy = [l[:] for l in door_trees_list]
                if aux_level.random_several_exit:
                    sol = aux_level_function(door_trees_list_copy,
                                             exit_number=exit_number,
                                             exit_door=exit_door).find_all_solutions()
                else:
                    sol = aux_level_function(door_trees_list_copy,
                                             exit_number=exit_number).find_all_solutions()
                assert sol[0] != []
                i_door_list = [i for i in range(len(door_trees_list))]
                rd_shuffle(i_door_list)
                for i_door in i_door_list:
                    for i_bin in range(n_bin):
                        if i_bin not in door_trees_list[i_door]:
                            door_trees_list[i_door].append(i_bin)
                            new_sol = aux_level_function(door_trees_list).find_all_solutions()
                            if new_sol == sol or len(new_sol) == 0:
                                door_trees_list_copy = [l[:] for l in door_trees_list]
                            else:
                                door_trees_list = [l[:] for l in door_trees_list_copy]
                door_trees_list = door_trees_list_copy

                # On vérifie que la nouvelle solution est identique à la solution initiale
                new_sol = aux_level_function(door_trees_list).find_all_solutions()
                print(new_sol)
                # print(door_trees_list)
                sol = aux_level_function(door_trees_list).find_all_solutions()
                assert sol[0] != []

                # Enregistrement de door_trees_list dans un fichier
                for i_door in range(len(door_trees_list)):
                    door_trees_list[i_door].sort()
                if not os_path_exists(file_name):
                    with open(file_name, 'wb') as fp:
                        pickle_dump(door_trees_list, fp)

                assert Maze.get_random_level_from_file(aux_level_function, file_name=None).find_all_solutions()[0] != []

    def get_random_level_from_file(aux_level_function, file_name=None):
        folder = f'levels/{aux_level_function().name}'
        if not os_path_exists(folder) or os_listdir(folder) == []:
            return aux_level_function()
        if file_name is None:
            file_name = rd_choice(os_listdir(folder))
        with open('/'.join([folder, file_name]), 'rb') as fp:
            door_trees_list = pickle_load(fp)
        level = aux_level_function(door_trees_list)
        level.name = level.name.replace('Random - ', '')
        level.random = True
        # level.name = ' '.join([level.name, f"v{file_name.split('_')[-1]}"])
        return level

    def fast_try_solution(self,
                          solution,
                          separator=' ',
                          really_fast=False):
        # results : 0 unauthorised, 1 authorised but wrong, 2 you won
        self.reboot_solution(fast=True)
        for action in solution[:-1]:
            action_type = action[0]
            if action_type == 'S':
                self.change_switch(action, update_doors=False)
            if action_type == 'D':
                self.use_door(action)
        if len(solution) > 0:
            action = solution[-1]
            action_type = action[0]
            if action_type == 'S':
                if self.legit_change_switch(action):
                    self.change_switch(action, update_doors=False)
                else:
                    return 0
            if action_type == 'D':
                door = self.doors_dict[action]
                door.update_open()
                if self.legit_use_door(action):
                    self.use_door(action)
                else:
                    return 0
        bool_solution = self.current_room_index == self.exit_room_index
        return int(bool_solution) + 1

    def current_situation_to_vector(self):
        vector = [switch.value for switch in self.switches_list]
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

    def visited_sitution_by_solution(self, solution):
        self.reboot_solution(fast=True)
        visited_situations = set()
        for action in solution[:-1]:
            action_type = action[0]
            if action_type == 'S':
                self.change_switch(action, update_doors=False)
            if action_type == 'D':
                self.use_door(action)
            visited_situations.add(self.current_situation_to_vector())
        return visited_situations

    def find_all_solutions(self,
                           verbose=0,
                           stop_at_first_solution=False,
                           reverse_actions_order=False,
                           initial_try=(),
                           nb_iterations_print=10**3,
                           max_calculation_time=float('inf'),
                           save_solutions_txt=True,
                           DFS=False,  # DFS : deep-first search
                           random_search=False,
                           level_number=None,
                           only_if_not_yet_calculated=False):  # Only used for printing

        from tqdm import tqdm
        # The main function doesn't use this function
        # The import is here because you need to be able to run the game without tqdm

        t0 = time()
        nb_iterations = 0
        nb_operations = 0

        name = self.name
        if self.fastest_solution is None:
            solutions_file = f'solutions/levels/random/level_{name}_solutions.txt'
            nb_iterations_file = f'solutions/levels/random/level_{name}_nb_iterations.txt'
            nb_operations_file = f'solutions/levels/random/level_{name}_nb_operations.txt'
        else:
            solutions_file = f'solutions/levels/{name}_solutions.txt'
            nb_iterations_file = f'solutions/levels/{name}_nb_iterations.txt'
            nb_operations_file = f'solutions/levels/{name}_nb_operations.txt'
        nb_iterations_tot = None
        nb_operations_tot = None
        solutions_from_file = None
        if os_path_exists(nb_iterations_file):
            try:
                with open(nb_iterations_file, 'r') as fr:
                    nb_iterations_tot = int(fr.readline())
            except ValueError:
                print('something wrong with {nb_iterations_file}')
        if os_path_exists(nb_operations_file):
            try:
                with open(nb_operations_file, 'r') as fr:
                    nb_operations_tot = int(fr.readline())
            except ValueError:
                print('something wrong with {nb_iterations_file}')
        if os_path_exists(solutions_file):
            try:
                with open(solutions_file, 'r') as fr:
                    solutions_from_file = fr.readlines()
            except ValueError:
                print('something wrong with {solutions_file}')
        if not (nb_iterations_tot is None or nb_operations_tot is None or solutions_from_file is None) and only_if_not_yet_calculated:
            return [solutions_from_file, nb_iterations_tot, nb_operations_tot]

        if self.all_solutions is None:
            visited_situations = set()
            solutions_to_visit = [initial_try]
            solutions_that_work = []
            if verbose == 1:
                if level_number is None:
                    pbar_nb_iterations = tqdm(desc=f'{self.name}',
                                              position=0)
                else:
                    if nb_iterations_tot is None:
                        pbar_nb_iterations = tqdm(desc=f'Level {level_number}: {self.name}',
                                                  position=0)
                    else:
                        pbar_nb_iterations = tqdm(desc=f'Level {level_number}: {self.name}',
                                                  total=nb_iterations_tot,
                                                  position=0)
            while solutions_to_visit != []:
                if time() - t0 > max_calculation_time:
                    return [], nb_iterations, nb_operations
                nb_iterations += 1
                if verbose == 1:
                    pbar_nb_iterations.update(1)
                if nb_iterations % nb_iterations_print == 0 and verbose == 2:
                    print('nb_iterations : {}'.format(nb_iterations))
                    if len(solutions_to_visit[-1]) < 100:
                        print('solutions_to_visit[-1] : {}'.format(' '.join(solutions_to_visit[-1])))
                    print("solutions_to_visit[-1].count('D') : {}".format(' '.join(solutions_to_visit[-1]).count('D')))
                    print('len(solutions_to_visit) : {}'.format(len(solutions_to_visit)))
                    print('len(solutions_to_visit)/nb_iterations : {}'.format(len(solutions_to_visit) / nb_iterations))
                    print(
                        f'estimated remaining time : {int(round((time() - t0) * len(solutions_to_visit) / nb_iterations, 0))} s')
                    print('len(solutions_that_work) : {}'.format(len(solutions_that_work)))
                    print('')
                solution = solutions_to_visit.pop(0)
                nb_operations += len(solution)
                result_solution = self.fast_try_solution(solution)
                for door in self.doors_list:
                    door.update_open()
                if result_solution == 1:
                    current_situation_vector = self.current_situation_to_vector()
                    if current_situation_vector not in visited_situations:  # or (random_search and current_situation_vector not in self.visited_sitution_by_solution(solution[:-1])):
                        if random_search:
                            actions_doors = self.get_current_possible_doors()
                            actions_switches = self.current_room().get_possible_switches_actions()
                            last_solutions_to_visit = []
                            for Slist in actions_switches:
                                for door in actions_doors:
                                    last_solutions_to_visit.append(solution + tuple(Slist) + (door,))
                            rd_shuffle(last_solutions_to_visit)
                            # with open('temp.txt', 'a') as f:
                            #     for string in [' '.join(l) for l in last_solutions_to_visit]:
                            #         f.write(string)
                            #         f.write('\n')
                            #     f.write('\n')
                            solutions_to_visit.extend(last_solutions_to_visit)
                            solutions_to_visit.reverse()
                            print(solutions_to_visit)
                        # not random search
                        else:
                            # DOORS
                            actions_doors = self.get_current_possible_doors()
                            if reverse_actions_order:
                                actions_doors.reverse()
                            doors_to_visit = []
                            for action in actions_doors:
                                doors_to_visit.append(solution + (action,))
                            # SWITCHES
                            switches_to_visit = []
                            if solution == () or solution[-1][0] != 'S':
                                for Slist in self.current_room().get_possible_switches_actions():
                                    switches_to_visit.append(solution + tuple(Slist))
                            # solutions_to_visit extend
                            if DFS:
                                doors_to_visit.reverse()
                                switches_to_visit.reverse()
                                solutions_to_visit.extend(switches_to_visit)
                                solutions_to_visit.extend(doors_to_visit)
                                solutions_to_visit.reverse()
                            else:
                                solutions_to_visit.extend(switches_to_visit)
                                solutions_to_visit.extend(doors_to_visit)
                    visited_situations.add(current_situation_vector)
                elif result_solution == 2:
                    if save_solutions_txt:
                        if os_path_exists('solutions'):
                            with open(solutions_file, 'w') as file:
                                file.write(' '.join(solution) + '\n')
                            with open(nb_iterations_file, 'w') as file:
                                file.write(str(nb_iterations))
                            with open(nb_operations_file, 'w') as file:
                                file.write(str(nb_operations))
                    solutions_that_work.append(solution)
                    if stop_at_first_solution:
                        self.reboot_solution()
                        self.all_solutions = solutions_that_work
                        return solutions_that_work, nb_iterations, nb_operations
            assert solutions_to_visit == []
            self.reboot_solution(fast=True)
        else:
            solutions_that_work = self.all_solutions
        solutions_that_work = sorted(solutions_that_work, key=len)
        try:
            if not (reverse_actions_order or self.fastest_solution is None or ' '.join(solutions_that_work[0]) == self.fastest_solution) and self.unique_solution:
                print(self.name, "wrong fastest solution")
                print("solution found")
                print(str(' '.join(solutions_that_work[0])))
                print("solution in memory")
                print(str(self.fastest_solution))
                print('')
                pass
        except IndexError:
            print('IndexError')
        self.all_solutions = solutions_that_work
        return solutions_that_work, nb_iterations, nb_operations

    def get_extreme_coordinates(self, ipagein):
        if self.extreme_coordinates is None:
            self.extreme_coordinates = []
            for ipage in range(self.number_of_pages):
                x_min = +float('inf')
                y_min = +float('inf')
                x_max = -float('inf')
                y_max = -float('inf')
                for room in self.rooms_list:
                    if ipage in room.pages_list:
                        assert ipage in room.position.keys(), room.name
                        [x_gap, y_gap, x, y] = room.position[ipage]
                        assert x_gap is not None
                        assert y_gap is not None
                        assert x is not None
                        assert y is not None
                        x_min = min(x_min, x_gap)
                        y_min = min(y_min, y_gap)
                        x_max = max(x_max, x_gap + x)
                        y_max = max(y_max, y_gap + y)
                self.extreme_coordinates.append([x_min, x_max, y_min, y_max])
        return self.extreme_coordinates[ipagein]

    def set_ipage_extreme_coordinates(self,
                                      new_x_min,
                                      new_x_max,
                                      new_y_min,
                                      new_y_max,
                                      border,
                                      keep_proportions,
                                      ipage):
        new_x_min = new_x_min + border
        new_x_max = new_x_max - border
        new_y_min = new_y_min + border
        new_y_max = new_y_max - border
        [old_x_min, old_x_max, old_y_min, old_y_max] = self.get_extreme_coordinates(ipage)
        if keep_proportions:
            old_delta_x = old_x_max - old_x_min
            old_delta_y = old_y_max - old_y_min
            pente_x = (new_x_max - new_x_min) / old_delta_x
            pente_y = (new_y_max - new_y_min) / old_delta_y
            if 1 / pente_x > 1 / pente_y:
                new_y_moy = (new_y_min + new_y_max) / 2
                (pente, coeff_x) = linear_function(old_x_min,
                                                   new_x_min,
                                                   old_x_max,
                                                   new_x_max)
                new_y_min = new_y_moy - pente * old_delta_y / 2
                coeff_y = new_y_min - old_y_min * pente
            else:
                new_x_moy = (new_x_min + new_x_max) / 2
                (pente, coeff_y) = linear_function(old_y_min,
                                                   new_y_min,
                                                   old_y_max,
                                                   new_y_max)
                new_x_min = new_x_moy - pente * old_delta_x / 2
                coeff_x = new_x_min - old_x_min * pente
            for room in self.rooms_list:
                if ipage in room.position.keys():
                    [x_gap, y_gap, x, y] = room.position[ipage]
                    x_gap = pente * x_gap + coeff_x
                    y_gap = pente * y_gap + coeff_y
                    x = pente * x
                    y = pente * y
                    room.position[ipage] = [x_gap, y_gap, x, y]
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
                if ipage in room.position.keys():
                    [x_gap, y_gap, x, y] = room.position[ipage]
                    x_gap = pente_x * x_gap + coeff_x
                    y_gap = pente_y * y_gap + coeff_y
                    x = pente_x * x
                    y = pente_y * y
                    room.position[ipage] = [x_gap, y_gap, x, y]
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
        for ipage in range(self.number_of_pages):
            self.set_ipage_extreme_coordinates(new_x_min,
                                               new_x_max,
                                               new_y_min,
                                               new_y_max,
                                               border,
                                               keep_proportions,
                                               ipage)
        self.calculate_doors_coordinates()

    def calculate_doors_coordinates(self): # DEPRECATED
        for door in self.doors_set:
            # for ipage in range(self.number_of_pages): # TODO
            Rd = door.room_departure
            Ra = door.room_arrival
            cRd = door.relative_departure_coordinates
            cRa = door.relative_arrival_coordinates
            [Rd_x_gap, Rd_y_gap, Rd_x, Rd_y] = Rd.position[self.current_page]
            [Ra_x_gap, Ra_y_gap, Ra_x, Ra_y] = Ra.position[self.current_page]
            door.real_departure_coordinates = array([Rd_x_gap + Rd_x * cRd[0],
                                                     Rd_y_gap + Rd_y * cRd[1]])
            door.real_arrival_coordinates = array([Ra_x_gap + Ra_x * cRa[0],
                                                   Ra_y_gap + Ra_y * cRa[1]])
            rp = door.relative_position
            dc = door.real_departure_coordinates
            ac = door.real_arrival_coordinates
            door.real_middle_coordinates = rp * ac + (1 - rp) * dc
            vect_unit = door.real_arrival_coordinates - door.real_departure_coordinates
            vect_unit = vect_unit / np_linalg_norm(vect_unit)
            [x, y] = vect_unit

            if door.two_way:
                l_diag = 55
                L_diag = 65
                door.arrow_coordinates = [door.real_middle_coordinates + L_diag * vect_unit / 2,
                                          door.real_middle_coordinates + l_diag * array([y, -x]) / 2,
                                          door.real_middle_coordinates - L_diag * vect_unit / 2,
                                          door.real_middle_coordinates - l_diag * array([y, -x]) / 2]
                door.real_middle_coordinates = door.real_middle_coordinates - array([11 / 2 * len(door.name), 8])
            else:
                D = 20
                d = 20
                L = 25
                F = 30
                door.arrow_coordinates = [door.real_middle_coordinates + L * vect_unit,
                                          door.real_middle_coordinates + d * array([y, -x]),
                                          door.real_middle_coordinates - F * vect_unit + D * array([y, -x]),
                                          door.real_middle_coordinates - F * vect_unit - D * array([y, -x]),
                                          door.real_middle_coordinates - d * array([y, -x])]
                door.real_middle_coordinates = door.real_middle_coordinates - array(
                    [11 / 2 * len(door.name), 8]) - 10 * vect_unit
