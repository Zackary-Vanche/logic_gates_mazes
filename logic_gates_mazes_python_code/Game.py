# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:59:09 2022

@author: utilisateur
"""

from pygame import init as pygame_init
from pygame.locals import QUIT, K_UP, K_DOWN, K_RIGHT, K_LEFT
from pygame.locals import K_a, K_b, K_d, K_e, K_h, K_r, K_s, K_l, K_q
from pygame.locals import K_KP0, K_KP1, K_KP2, K_KP3, K_KP4
from pygame.locals import K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
from pygame.locals import K_0, K_1, K_2, K_3, K_4
from pygame.locals import K_5, K_6, K_7, K_8, K_9
from pygame.locals import K_RETURN, K_BACKSPACE, K_SPACE, K_ESCAPE
from pygame.display import set_mode as pygame_display_set_mode
from pygame.display import set_caption as pygame_display_set_caption
from pygame.display import update as pygame_display_update
from pygame.font import SysFont as pygame_font_SysFont
from pygame import Rect as pygame_Rect
from pygame.draw import rect as pygame_draw_rect
from pygame.draw import line as pygame_draw_line
from pygame.draw import ellipse as pygame_draw_ellipse
from pygame.draw import polygon as pygame_draw_polygon
from pygame.event import get as pygame_event_get
from pygame.key import get_pressed as pygame_key_get_pressed
from pygame.image import save as pygame_image_save
from pygame import quit as pygame_quit
from pygame import RESIZABLE as pygame_RESIZABLE
from pygame import SCALED as pygame_SCALED

from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from numpy import array
from time import time
from time import sleep

from linear_function import linear_function
from Maze import Maze
from Levels import Levels

from levels.level_random import level_random

class Game:
    
    keys_dict = {K_a: 'A',
                 K_d: 'D',
                 K_e: 'E',
                 K_l: 'L',
                 K_r: 'R',
                 K_s: 'S',
                 K_0: '0',
                 K_1: '1',
                 K_2: '2',
                 K_3: '3',
                 K_4: '4',
                 K_5: '5',
                 K_6: '6',
                 K_7: '7',
                 K_8: '8',
                 K_9: '9',
                 K_KP0: '0',
                 K_KP1: '1',
                 K_KP2: '2',
                 K_KP3: '3',
                 K_KP4: '4',
                 K_KP5: '5',
                 K_KP6: '6',
                 K_KP7: '7',
                 K_KP8: '8',
                 K_KP9: '9',
                 K_SPACE: ' '}
    
    def __init__(self,
                 WINDOW_SIZE=(1366-20, 768-100),
                 SMALLEST_WINDOW_SIZE=(1366-20, 768-100),
                 XY_marge=(0, 0),  # (25, 120)
                 save_image=False,
                 index_current_level=0,  # Cette variable détermine le niveau joué.
                 time_between_actions=0.15,
                 time_between_deletings=0.05,
                 print_click_rects=False,
                 print_room_name=True,
                 print_tree_polygon=False,
                 show_help=True,
                 index_help_page=0,
                 show_loop_time=False,
                 update_display_at_every_loop=False,
                 sleep_time=10**(-2)):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.SMALLEST_WINDOW_SIZE = SMALLEST_WINDOW_SIZE
        self.XY_marge = XY_marge
        self.save_image = save_image
        self.index_current_level = index_current_level
        self.time_between_actions = time_between_actions
        self.time_between_deletings = time_between_deletings
        self.print_click_rects = print_click_rects
        self.print_room_name = print_room_name
        self.print_tree_polygon = print_tree_polygon
        self.show_help = show_help
        self.index_help_page = index_help_page
        self.show_loop_time = show_loop_time
        self.update_display_at_every_loop = update_display_at_every_loop
        self.sleep_time = sleep_time
        self.change_in_display = False
        
    def game_setup(self, font_size=22):
        # Game Setup
        pygame_init()
        self.looping = True
        self.TOTAL_WIDTH, self.TOTAL_HEIGHT = self.WINDOW_SIZE
        self.X_marge, self.Y_marge = self.XY_marge
        self.WINDOW_WIDTH = self.TOTAL_WIDTH - self.X_marge
        self.WINDOW_HEIGHT = self.TOTAL_HEIGHT - self.Y_marge
        self.WINDOW = pygame_display_set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                                               pygame_RESIZABLE,
                                               pygame_SCALED)
        pygame_display_set_caption('Logic gates maze')
        self.WINDOW_SIZE_changed = True

        self.font = pygame_font_SysFont(None, font_size)
        self.level_changed = True
        # Cette variable vaut True quand le joueur
        # vient de choisir de changer de niveau
        # ou au début du jeu (il faut initialiser le niveau)
        self.last_level_change_time = time()
        self.click_rect_size = 39
        if self.save_image:
            if not os_path_exists('images'):
                os_mkdir('images')
        self.current_action = ''
        self.last_key_pressed_time = time()
        self.last_key_BACKSPACE_pressed_time = time()
        
    def get_level(self):
        
        if self.level_changed:
            
            self.change_in_display = True

            self.level_changed = False
            
            # self.maze = Levels.levels_functions_list[self.index_current_level]()
            self.maze = Levels.get_level(self.index_current_level)
            if self.maze.random:
                self.maze = level_random()
            else:
                self.maze.reboot_solution()
            
            self.doors_list = self.maze.doors_list()
            
            level_colors = self.maze.level_color
            self.background_color = level_colors.background_color
            self.room_color = level_colors.room_color
            self.contour_color = level_colors.contour_color
            self.letters_color = level_colors.letters_color
            # letter_contour_color = maze.letter_contour_color
            self.inside_room_color = level_colors.inside_room_color
            self.surrounding_color = level_colors.surrounding_color
            self.inside_room_surrounding_color = level_colors.inside_room_surrounding_color

            self.y_separation = self.maze.y_separation
            self.door_window_size = self.maze.door_window_size

            self.x_separation = self.WINDOW_WIDTH - self.door_window_size
            self.current_action = ''
            self.keep_proportions = self.maze.keep_proportions

            # Choix de la bordure en fonction de la hauteur de la fenêtre
            (pente, coeff) = linear_function(643, 35, 1080, 75)
            self.maze.set_extreme_coordinates(0,
                                              self.x_separation,
                                              0,
                                              self.WINDOW_HEIGHT,
                                              pente*self.WINDOW_HEIGHT+coeff,
                                              self.keep_proportions)
    
    def update_window_size(self):
        
        if (self.WINDOW_WIDTH, self.WINDOW_HEIGHT) != self.WINDOW.get_size():
            self.WINDOW_SIZE_changed = True
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.WINDOW.get_size()
            self.WINDOW_WIDTH = max(self.SMALLEST_WINDOW_SIZE[0], self.WINDOW_WIDTH)
            self.WINDOW_HEIGHT = max(self.SMALLEST_WINDOW_SIZE[1], self.WINDOW_HEIGHT)
            
        if self.WINDOW_SIZE_changed:

            self.y_separation = self.maze.y_separation
            door_window_size = self.maze.door_window_size

            self.x_separation = self.WINDOW_WIDTH - door_window_size
            keep_proportions = self.maze.keep_proportions

            # Choix de la bordure en fonction de la hauteur de la fenêtre
            (pente, coeff) = linear_function(643, 35, 1080, 75)
            self.maze.set_extreme_coordinates(0,
                                              self.x_separation,
                                              0,
                                              self.WINDOW_HEIGHT,
                                              pente*self.WINDOW_HEIGHT+coeff,
                                              keep_proportions)

            self.WINDOW_SIZE_changed = False
            self.change_in_display = True
            
    def draw_right_window(self):
        # Affichage de la fenêtre de droite
        right_window_rectangle = pygame_Rect(self.x_separation,
                                             0,
                                             self.door_window_size,
                                             self.WINDOW_HEIGHT)
        pygame_draw_rect(self.WINDOW, self.room_color, right_window_rectangle)
    
    def draw_door_lines(self):
        # Affichage des lignes des portes
        self.line_size = self.maze.line_size
        for door in self.maze.doors_set:
            real_departure_coordinates = door.real_departure_coordinates
            real_arrival_coordinates = door.real_arrival_coordinates
            if door.is_open:
                if self.uniform_surrounding_colors:
                    pygame_draw_line(self.WINDOW,
                                     self.surrounding_color,
                                     real_departure_coordinates,
                                     real_arrival_coordinates,
                                     self.line_size)
                else:
                    pygame_draw_line(self.WINDOW,
                                     door.surrounding_color,
                                     real_departure_coordinates,
                                     real_arrival_coordinates,
                                     self.line_size)
            else:
                pygame_draw_line(self.WINDOW,
                                 self.room_color,
                                 real_departure_coordinates,
                                 real_arrival_coordinates,
                                 self.line_size)
    
    def draw_exterior_lines(self):
        # Bords exterieurs
        l = 5 # Largeur des bords exterieurs
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, 0),
                         (0, self.WINDOW_HEIGHT),
                         l+2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (self.WINDOW_WIDTH, 0),
                         (self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                         l+2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, 0),
                         (self.WINDOW_WIDTH, 0),
                         l+2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, self.WINDOW_HEIGHT),
                         (self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                         l+2)
        
    def draw_windows_separation(self):
        # Séparation des différentes fenetres
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (self.x_separation, 0),
                         (self.x_separation, self.WINDOW_HEIGHT),
                         3)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (self.x_separation, self.y_separation),
                         (self.WINDOW_WIDTH, self.y_separation),
                         3)
        
    def print_level_name(self):
        # Affichage du nom du niveau courant
        level_name_render = self.font.render('Level ' + str(self.index_current_level) + ' : ' + self.maze.name.replace('_', ' '),
                                             True,
                                             self.letters_color)
        self.WINDOW.blit(level_name_render, (10, 10))
        
    def print_trees(self):
        # Affichage des arbres des portes
        self.n_lines_door_printing = self.maze.n_lines_door_printing
        if self.n_lines_door_printing == 0:
            return None
        self.gap_between_lines = min((self.WINDOW_HEIGHT - self.maze.y_separation - 50) / (self.n_lines_door_printing), 25)
        if self.print_tree_polygon:
            pass # TODO
        else:
            gap = self.y_separation + 10
            self.WINDOW.blit(self.font.render('DOORS :',
                             True,
                             self.inside_room_color),
                             (self.x_separation + 10, gap))
            gap = self.y_separation + 35
            for k in range(len(self.doors_list)):
                door = self.doors_list[k]
                tree = door.tree
                str_logical_expression = tree.get_easy_logical_expression_PN()
                str_logical_expression = str_logical_expression.split('\n')
                # if k == 0:
                #     print('')
                for i in range(len(str_logical_expression)):
                    string = str_logical_expression[i]
                    if i == 0:
                        logical_expression_render = self.font.render(door.name + ' = ' + string,
                                                                True,
                                                                self.inside_room_color)
                        self.WINDOW.blit(logical_expression_render, (self.x_separation + 10, gap))
                    else:
                        logical_expression_render = self.font.render(' '*(len(door.name)+3) + string,
                                                                True,
                                                                self.inside_room_color)
                        self.WINDOW.blit(logical_expression_render, (self.x_separation + 10, gap))
                    gap += self.gap_between_lines

    def draw_rooms(self):
        # Affichage des pieces
        self.line_size = self.maze.line_size
        for room in self.maze.rooms_list:
            [x_gap, y_gap, x, y] = array(room.position)
            room_rectangle = pygame_Rect(x_gap, y_gap, x+2, y+2)
            if room.is_exit:
                pygame_draw_ellipse(self.WINDOW, self.room_color, room_rectangle)
                room_name_render = self.font.render('EXIT',
                                                    True,
                                                    self.inside_room_color)
                self.WINDOW.blit(room_name_render, room.get_name_position())
                if self.maze.current_room() == room:
                    if self.uniform_surrounding_colors:
                        pygame_draw_ellipse(self.WINDOW, self.surrounding_color, room_rectangle, width=self.line_size)
                    else:
                        pygame_draw_ellipse(self.WINDOW, room.surrounding_color, room_rectangle, width=self.line_size)
            else:
                pygame_draw_rect(self.WINDOW, self.room_color, room_rectangle)
                if self.maze.current_room() == room:
                    if self.uniform_surrounding_colors:
                        pygame_draw_rect(self.WINDOW, self.surrounding_color, room_rectangle, width=self.line_size)
                    else:
                        pygame_draw_rect(self.WINDOW, room.surrounding_color, room_rectangle, width=self.line_size)
                room_name_render = self.font.render(room.name,
                                                    True,
                                                    self.inside_room_color)
                if self.print_room_name:
                    self.WINDOW.blit(room_name_render, room.get_name_position())
           
    def draw_doors_polygons(self):
        # Affichage des polygones des portes
        for door in self.maze.doors_set:
            # real_middle_coordinates = door.real_middle_coordinates
            arrow_coordinates = door.arrow_coordinates
            pygame_draw_polygon(self.WINDOW,
                                self.room_color,
                                arrow_coordinates)
        for door in self.maze.doors_set:
            arrow_coordinates = door.arrow_coordinates
            if door.is_open:
                if self.uniform_surrounding_colors:
                    pygame_draw_polygon(self.WINDOW,
                                        self.surrounding_color,
                                        arrow_coordinates,
                                        width=3)
                else:
                    pygame_draw_polygon(self.WINDOW,
                                        door.surrounding_color,
                                        arrow_coordinates,
                                        width=3)
                
    def print_doors_names(self):
        # Affichage des portes
        for door in self.maze.doors_set:
            real_middle_coordinates = door.real_middle_coordinates
            door_name_render = self.font.render(door.name,
                                                True,
                                                self.inside_room_color)
            self.WINDOW.blit(door_name_render,
                             real_middle_coordinates)      
            
    def draw_switches(self):
        # Affichage des interrupteurs
        for room in self.maze.rooms_list:
            switches_positions = room.get_switches_positions()
            switches_list = room.switches_list
            assert len(switches_positions) == len(switches_list)
            for i in range(len(switches_list)):
                switch = switches_list[i]
                position = switches_positions[i]
                rect = pygame_Rect(position[0]-self.click_rect_size/2,
                                   position[1]-self.click_rect_size/2,
                                   self.click_rect_size,
                                   self.click_rect_size)
                if self.print_click_rects:
                    pygame_draw_rect(self.WINDOW,
                                     self.background_color,
                                     rect)
                if switch.value:
                    rectangle_switch = pygame_Rect(position[0]-self.click_rect_size/2 - 2,
                                                   position[1]-self.click_rect_size/2,
                                                   self.click_rect_size,
                                                   self.click_rect_size)
                    if self.uniform_surrounding_colors:
                        pygame_draw_rect(self.WINDOW,
                                         self.inside_room_surrounding_color,
                                         rectangle_switch,
                                         width = 3)
                    else:
                        pygame_draw_rect(self.WINDOW,
                                         room.surrounding_color,
                                         rectangle_switch,
                                         width = 3)
                if self.print_click_rects:
                    switch_name_render = self.font.render(switch.name,
                                                     True,
                                                     self.letters_color)
                else:
                    switch_name_render = self.font.render(switch.name,
                                                     True,
                                                     self.inside_room_color)
                self.WINDOW.blit(switch_name_render,
                            position - array([11/2*len(switch.name), 8]))
        
    def display_help(self):
        
        self.WINDOW.fill(self.background_color)
        
        self.draw_exterior_lines()
        # Affichage du nom du niveau courant
        level_name_render = self.font.render('HELP - Level ' + str(self.index_current_level) + ' : ' + self.maze.name.replace('_', ' '), 
                                        True,
                                        self.letters_color)
        self.WINDOW.blit(level_name_render, (10, 10))
        self.index_help_page = self.index_help_page % self.maze.n_help_pages
        string_help = self.maze.help_txt[self.index_help_page]
        gap = 0
        help_list = string_help.split('\n')
        p, c = linear_function(768-self.Y_marge, 50, 1080-self.Y_marge, 50)
        y0 = p*self.WINDOW_HEIGHT + c
        p, c = linear_function(1366-self.X_marge, 50, 1920-self.X_marge, 50)
        x0 = p*self.WINDOW_WIDTH + c
        for line in help_list:
            self.WINDOW.blit(self.font.render(line,
                                         True,
                                         self.letters_color),
                             (x0, y0 + gap))
            if line.replace(' ', '') == '':
                gap += 15
            else:
                gap += 20

        pygame_display_update()

        if self.save_image:
            fname = "images/HELP_level_{}_{}_WIDTH_{}_HEIGHT_{}.png".format(self.index_current_level,
                                                                            self.maze.name,
                                                                            self.WINDOW_WIDTH,
                                                                            self.WINDOW_HEIGHT)
            if not os_path_exists(fname):
                print(fname)
                pygame_image_save(self.WINDOW, fname)
                
    def print_current_action(self):
        current_action_render = self.font.render(self.current_action,
                                                 True,
                                                 self.inside_room_color)
        self.WINDOW.blit(current_action_render,
                         (self.x_separation + self.y_separation/3, self.y_separation/2-7))
                
    def display_game_window(self):
        self.WINDOW.fill(self.background_color)
        self.uniform_surrounding_colors = self.maze.uniform_surrounding_colors
        self.draw_right_window()
        self.draw_exterior_lines()
        self.draw_windows_separation()
        self.print_level_name()
        self.print_trees()
        self.draw_door_lines()
        self.draw_rooms()
        self.draw_doors_polygons()
        self.print_doors_names()
        self.draw_switches()
        self.print_current_action()
        pygame_display_update()
        
    def handle_interractions(self):
        self.pressed = pygame_key_get_pressed()
        # Gestion des actions
        if self.maze.current_room_index == self.maze.exit_room_index and self.current_action != 'YOU WON !':
            self.current_action = 'YOU WON !'
            self.change_in_display = True
        if time() - self.last_key_pressed_time > self.time_between_actions:
            self.pressed = pygame_key_get_pressed()
            for key in Game.keys_dict.keys():
                if self.pressed[key]:
                    self.change_in_display = True
                    self.current_action = self.current_action + Game.keys_dict[key]
                    self.last_key_pressed_time = time()
            if self.pressed[K_RETURN] and self.current_action != '' and self.maze.current_room_index != self.maze.exit_room_index:
                self.change_in_display = True
                if len(self.current_action) > 0:
                    if self.current_action[0] in ['D', 'S', 'R']:
                        self.maze.make_actions(self.current_action)
                    if self.current_action[0:2] == 'A ':
                        self.maze.make_actions(self.current_action[2:], allow_all=True)
                    if self.current_action[0] == 'A':
                        self.maze.make_actions(self.current_action[1:], allow_all=True)
                    elif self.current_action[0] == 'L':
                        level_number_list = [str(i) for i in range(Levels.number_of_levels)]
                        if self.current_action[1:] in level_number_list:
                            self.index_current_level = int(self.current_action[1:])
                            self.level_changed = True
                    self.current_action = ''
            if self.pressed[K_b]:
                self.change_in_display = True
                if self.maze.random:
                    self.level_changed = False
                    self.maze = level_random()
                    self.doors_list = self.maze.doors_list()
                    level_colors = self.maze.level_color
                    self.background_color = level_colors.background_color
                    self.room_color = level_colors.room_color
                    self.contour_color = level_colors.contour_color
                    self.letters_color = level_colors.letters_color
                    # letter_contour_color = maze.letter_contour_color
                    self.inside_room_color = level_colors.inside_room_color
                    self.surrounding_color = level_colors.surrounding_color
                    self.inside_room_surrounding_color = level_colors.inside_room_surrounding_color
                    self.y_separation = self.maze.y_separation
                    self.door_window_size = self.maze.door_window_size
                    self.x_separation = self.WINDOW_WIDTH - self.door_window_size
                    self.current_action = ''
                    self.keep_proportions = self.maze.keep_proportions
                    # Choix de la bordure en fonction de la hauteur de la fenêtre
                    (pente, coeff) = linear_function(643, 35, 1080, 75)
                    self.maze.set_extreme_coordinates(0,
                                                      self.x_separation,
                                                      0,
                                                      self.WINDOW_HEIGHT,
                                                      pente*self.WINDOW_HEIGHT+coeff,
                                                      self.keep_proportions)
                else:
                    self.maze.reboot_solution()
                self.last_key_pressed_time = time()
                self.current_action = ''
        if time() - self.last_key_BACKSPACE_pressed_time > self.time_between_deletings:
            if self.pressed[K_BACKSPACE]:
                self.change_in_display = True
                self.current_action = self.current_action[:-1]
                self.last_key_BACKSPACE_pressed_time = time()
                
    def change_level(self):
        self.pressed = pygame_key_get_pressed()
        # Changement de niveau
        if time() - self.last_level_change_time > self.time_between_actions:
            if (self.pressed[K_RIGHT]):
                self.index_current_level += 1
                self.level_changed = True
            if (self.pressed[K_LEFT]):
                self.index_current_level -= 1
                self.level_changed = True
            if (self.pressed[K_UP]):
                self.index_current_level = Levels.number_of_levels-1
                self.level_changed = True
            if (self.pressed[K_DOWN]):
                self.index_current_level = 0
                self.level_changed = True
        if self.level_changed:
            self.last_level_change_time = time()
        self.index_current_level = min(self.index_current_level,
                                       Levels.number_of_levels-1)
        self.index_current_level = max(self.index_current_level,
                                  0)
        
    def goto_or_leave_help(self):
        self.pressed = pygame_key_get_pressed()
        # Passage au menu d'aide / quitter le menu aide
        if time() - self.last_key_pressed_time > self.time_between_actions:
            if self.pressed[K_h]:
                self.show_help = not self.show_help
                self.last_key_pressed_time = time()
                self.change_in_display = True

    def save_image_as_png(self):
        if self.save_image:
            fname = "images/level_{}_{}_WIDTH_{}_HEIGHT_{}.png".format(self.index_current_level,
                                                                       self.maze.name,
                                                                       self.WINDOW_WIDTH,
                                                                       self.WINDOW_HEIGHT)
            if not os_path_exists(fname):
                print(fname)
                pygame_image_save(self.WINDOW, fname)
                
    def quit_game(self):
        self.t1 = time()
        if self.show_loop_time:
            self.t_tot = self.t1 - self.t0
            print("number of loops :\n", self.n_loops)
            print("time of execution :\n", round(self.t_tot, 0), 's')
            print("mean time of execution of one loop :\n", self.t_tot/self.n_loops, 's')
        pygame_quit()
        return None
    
    def do_you_quit_game(self):
        self.pressed = pygame_key_get_pressed()
        for event in pygame_event_get():
            if event.type == QUIT:
                # print(number_of_loops)
                self.quit_game()
                return True
        if self.pressed[K_q] or self.pressed[K_ESCAPE]:
            self.quit_game()
            return True
        return False

    # The main function that controls the game
    def play(self):
        self.game_setup()
        self.t0 = time()
        self.n_loops = 0
        while self.looping:
            sleep(self.sleep_time) # I did that not to use too much CPU
            self.n_loops += 1
            if self.do_you_quit_game():
                return None
            self.get_level()
            self.update_window_size()
            if self.show_help:
                if self.change_in_display or self.update_display_at_every_loop:
                    self.display_help()
                    self.change_in_display = False
            else:
                if self.change_in_display or self.update_display_at_every_loop:
                    self.display_game_window()
                    self.change_in_display = False
                self.handle_interractions()
                self.save_image_as_png()
            self.change_level()
            self.goto_or_leave_help()
            
    def save_levels_txt(verbose=0, calculates_solutions=True, short_only=True):
        t0 = time()
        Maze.calculates_solutions = calculates_solutions
        if not os_path_exists('mazes'):
            os_mkdir('mazes')
        for k in range(Levels.number_of_levels):
            # level = Levels.levels_functions_list[k]()
            level = Levels.get_level(k)
            if level.fastest_solution is not None:
                if not short_only:
                    level.save_txt(title_header='mazes/Level_{}'.format(k))
                level.save_txt_short(title_header='mazes/L{}'.format(k))
            else:
                print(level.name, 'TODO')
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')