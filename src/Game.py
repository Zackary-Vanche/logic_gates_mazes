from pygame import init as pygame_init
# from pygame import MOUSEBUTTONDOWN
import pygame.locals
from pygame.locals import K_KP0, K_KP1, K_KP2, K_KP3, K_KP4
from pygame.locals import K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
from pygame.locals import QUIT, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE, K_LALT, K_RALT, K_KP_PERIOD
from pygame.locals import K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.locals import MOUSEWHEEL
from pygame.display import set_mode as pygame_display_set_mode
from pygame.display import set_caption as pygame_display_set_caption
from pygame.display import update as pygame_display_update
from pygame.event import get as pygame_event_get
from pygame.font import SysFont as pygame_font_SysFont
from pygame import Rect as pygame_Rect
from pygame.draw import rect as pygame_draw_rect
from pygame.draw import line as pygame_draw_line
from pygame.draw import ellipse as pygame_draw_ellipse
from pygame.draw import polygon as pygame_draw_polygon
from pygame.key import get_pressed as pygame_key_get_pressed
from pygame.image import save as pygame_image_save
from pygame import quit as pygame_quit
from pygame import RESIZABLE as pygame_RESIZABLE
from pygame import SCALED as pygame_SCALED
from pygame import FULLSCREEN as pygame_FULLSCREEN

from os.path import exists as os_path_exists
from os import mkdir as os_mkdir
from os import listdir as os_listdir
from os import remove as os_remove
from numpy import array
# from numpy import sqrt
from numpy.linalg import norm
from time import time
from time import sleep

from linear_function import linear_function
from Maze import Maze
from Levels import Levels

from Levels_colors_list import Levels_colors_list

from random import choice as rd_choice

class Game:
    keys_dict = {K_KP0: '0',
                 K_KP1: '1',
                 K_KP2: '2',
                 K_KP3: '3',
                 K_KP4: '4',
                 K_KP5: '5',
                 K_KP6: '6',
                 K_KP7: '7',
                 K_KP8: '8',
                 K_KP9: '9',
                 K_KP_PERIOD: '.',
                 K_SPACE: ' '}
    
    # Add all alphabet letters to the dictionary
    for letter_key in range(pygame.locals.K_a, pygame.locals.K_z + 1):
        letter_char = chr(letter_key).upper()
        keys_dict[letter_key] = letter_char
    
    # Add numbers to the dictionary
    for number_key in range(pygame.locals.K_0, pygame.locals.K_9 + 1):
        number_char = chr(number_key)
        keys_dict[number_key] = number_char
    
    def __init__(self,
                 WINDOW_SIZE=(1366, 768),
                 SMALLEST_WINDOW_SIZE=(1366, 768),
                 XY_marge=(0, 0),  # (25, 120)
                 is_fullscreen=True,
                 save_image=False,
                 index_current_level=0,  # Cette variable détermine le niveau joué.
                 time_between_actions=0.15,
                 time_between_deletings=0.05,
                 time_between_level_changing=0.25,
                 print_click_rects=True,
                 print_room_name=True,
                 print_tree_polygon=False,
                 show_help=True,
                 index_help_page=0,
                 show_loop_time=False,
                 update_display_at_every_loop=False,
                 sleep_time=1e-2,
                 game_color=None,
                 dev_mode=False): # if game_color is not None, it overwrites the levels colors
        if WINDOW_SIZE is None or SMALLEST_WINDOW_SIZE is None:
            from pyautogui import size as pyautogui_size
            TOTAL_SIZE = pyautogui_size()
            WINDOW_SIZE = (0.95 * TOTAL_SIZE.width, 0.90 * TOTAL_SIZE.height)
            self.WINDOW_SIZE = WINDOW_SIZE
            self.SMALLEST_WINDOW_SIZE = WINDOW_SIZE
        else:
            self.WINDOW_SIZE = WINDOW_SIZE
            self.SMALLEST_WINDOW_SIZE = SMALLEST_WINDOW_SIZE
        self.XY_marge = XY_marge
        self.save_image = save_image
        self.index_current_level = index_current_level
        self.time_between_actions = time_between_actions
        self.time_between_deletings = time_between_deletings
        self.time_between_level_changing = time_between_level_changing
        self.print_click_rects = print_click_rects
        self.print_room_name = print_room_name
        self.print_tree_polygon = print_tree_polygon
        self.show_help = show_help
        self.index_help_page = index_help_page
        self.show_loop_time = show_loop_time
        self.update_display_at_every_loop = update_display_at_every_loop
        self.sleep_time = sleep_time
        self.change_in_display = False
        self.font_size = 22
        self.help_font_size = 30
        self.is_fullscreen = is_fullscreen
        self.get_new_level = False
        if self.save_image:
            self.show_help = False
        self.game_color = game_color
        self.possible_current_actions = None
        self.current_action_index = 0
        self.current_action_index_changed = False
        self.show_wires = False
        self.element_dict = {}
        self.upper_right_window_rectangle = None
        self.lower_right_window_rectangle = None
        self.do_you_quit_game = False
        self.dev_mode = dev_mode

    def game_setup(self):
        # Game Setup
        pygame_init()
        self.looping = True
        self.TOTAL_WIDTH, self.TOTAL_HEIGHT = self.WINDOW_SIZE
        self.X_marge, self.Y_marge = self.XY_marge
        self.WINDOW_WIDTH = self.TOTAL_WIDTH - self.X_marge
        self.WINDOW_HEIGHT = self.TOTAL_HEIGHT - self.Y_marge
        if self.is_fullscreen:
            self.WINDOW = pygame_display_set_mode((0, 0),
                                                  pygame_FULLSCREEN)
        else:
            self.WINDOW = pygame_display_set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                                                  pygame_RESIZABLE,
                                                  pygame_SCALED)
        pygame_display_set_caption('Logic Gates Mazes')
        self.WINDOW_SIZE_changed = False

        self.font = pygame_font_SysFont(None, self.font_size)
        self.level_changed = True
        # Cette variable vaut True quand le joueur
        # vient de choisir de changer de niveau
        # ou au début du jeu (il faut initialiser le niveau)
        self.last_level_change_time = time()
        self.click_rect_size_x = 40
        self.click_rect_size_y = 30
        if self.save_image:
            if not os_path_exists('images'):
                os_mkdir('images')
        self.current_action = ''
        self.last_key_pressed_time = time()
        self.last_space_pressed_time = time()
        self.last_key_BACKSPACE_pressed_time = time()

    def get_level(self, fast_solution_finding=False):

        if self.level_changed or self.get_new_level:
            try:
                self.change_in_display = True
    
                self.level_changed = False
    
                # self.maze = Levels.levels_functions_list[self.index_current_level]()
                self.maze = Levels.get_level(self.index_current_level,
                                             get_new_level=self.get_new_level,
                                             fast_solution_finding=False)
                self.get_new_level = False
                # if self.maze.random:
                #     self.maze = level_random()
                # else:
                self.maze.reboot_solution()
    
                self.doors_list = self.maze.doors_list
                self.name_tree_list = []
                for tree in self.maze.intermediate_values_list:
                    assert tree.name[0] == 'V'
                    self.name_tree_list.append([tree.name, tree])
                for k in range(len(self.doors_list)): # loop on the doors
                    door = self.doors_list[k]
                    tree = door.tree
                    self.name_tree_list.append([door.name, tree])
    
                if self.game_color is not None:
                    self.maze.level_color = self.game_color
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
                border = self.maze.border
                self.maze.set_extreme_coordinates(0,
                                                  self.x_separation,
                                                  0,
                                                  self.WINDOW_HEIGHT,
                                                  border,
                                                  self.keep_proportions)
                
                self.update_possible_actions()
            except ZeroDivisionError:
                maze_name = Levels.get_level(self.index_current_level, get_new_level=self.get_new_level).name
                print(f'The level {maze_name} cannot be loaded.')
                print('Your screen is too small.')

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
            # keep_proportions = self.maze.keep_proportions

            # Choix de la bordure en fonction de la hauteur de la fenêtre
            (pente, coeff) = linear_function(643, 35, 1080, 75)
            border = self.maze.border
            self.maze.set_extreme_coordinates(0,
                                              self.x_separation,
                                              0,
                                              self.WINDOW_HEIGHT,
                                              border,
                                              self.keep_proportions)
            self.WINDOW_SIZE_changed = False
            self.change_in_display = True

    def draw_right_window(self):
        # Affichage de la fenêtre de droite
        upper_right_window_rectangle = pygame_Rect(self.x_separation,
                                                   0,
                                                   self.door_window_size,
                                                   self.y_separation)
        lower_right_window_rectangle = pygame_Rect(self.x_separation,
                                                   self.y_separation,
                                                   self.door_window_size,
                                                   self.WINDOW_HEIGHT)
        self.upper_right_window_rectangle = upper_right_window_rectangle
        self.lower_right_window_rectangle = lower_right_window_rectangle
        pygame_draw_rect(self.WINDOW, self.room_color, upper_right_window_rectangle)
        pygame_draw_rect(self.WINDOW, self.room_color, lower_right_window_rectangle)

    def draw_door_lines(self):
        # Affichage des lignes des portes
        self.line_size = self.maze.line_size
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                real_departure_coordinates = door.real_departure_coordinates
                real_arrival_coordinates = door.real_arrival_coordinates
                if not door.is_open:
                    if self.uniform_surrounding_colors:
                        pygame_draw_line(self.WINDOW,
                                         self.room_color,
                                         real_departure_coordinates,
                                         real_arrival_coordinates,
                                         self.line_size)
                    else:
                        pygame_draw_line(self.WINDOW,
                                         door.inside_color,
                                         real_departure_coordinates,
                                         real_arrival_coordinates,
                                         self.line_size)
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
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

    def draw_exterior_lines(self):
        # Bords exterieurs
        l = 5  # Largeur des bords exterieurs
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, 0),
                         (0, self.WINDOW_HEIGHT),
                         l + 2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (self.WINDOW_WIDTH, 0),
                         (self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                         l + 2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, 0),
                         (self.WINDOW_WIDTH, 0),
                         l + 2)
        pygame_draw_line(self.WINDOW,
                         self.contour_color,
                         (0, self.WINDOW_HEIGHT),
                         (self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                         l + 2)

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
        maze_name = self.maze.name
        if self.maze.random:
            maze_name = maze_name + " (random)"
        level_name_render = self.font.render(
            f'Level {str(self.index_current_level+1)} / {Levels.number_of_levels} : {maze_name.replace('_', ' ')}',
            True,
            self.letters_color)
        self.WINDOW.blit(level_name_render, (10, 10))
        
    def print_you_won(self):
        if self.maze.current_room_index == self.maze.exit_room_index and self.current_action != 'YOU WON !':
            word_surface = self.font.render('YOU WON !',
                                            True,
                                            self.letters_color)
            word_width, word_height = word_surface.get_size()
            self.WINDOW.blit(word_surface, (self.x_separation - word_width - 10, 10))
        
    def blit_text(self,
                  text,
                  pos,
                  max_width,
                  color=None):
        if text == '':
            return
        if color is None:
            color = self.inside_room_color
        lines_list = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        # max_width, max_height = self.WINDOW.get_size()
        x0, y = pos
        x = x0
        xmax = 0
        for line in lines_list:
            for word in line:
                word_surface = self.font.render(word, 1, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= x0 + max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height * 1.1  # Start on new row.
                self.WINDOW.blit(word_surface, (x, y))
                xmax = max(x+word_width, xmax)
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        return xmax, y + word_height/2

    def print_trees(self):
        # Affichage des arbres des portes
        self.n_lines_door_printing = self.maze.n_lines_door_printing
        if self.n_lines_door_printing == 0:
            return None
        if self.print_tree_polygon:
            pass  # deprecated
        else:
            self.gap_between_lines = min(
                (self.WINDOW_HEIGHT - self.maze.y_separation - 50) / (self.n_lines_door_printing), 25)
            gap = self.y_separation + 10
            for c in self.name_tree_list:
                [name, tree] = c
                str_logical_expression = tree.get_easy_logical_expression_PN()
                str_logical_expression = str_logical_expression.split('\n')
                all_trees_expressions = []
                for i in range(len(str_logical_expression)):
                    string = str_logical_expression[i]
                    if i == 0:
                        string = name + ' = ' + string
                    else:
                        string = ' ' * (len(name) + 3) + string
                    all_trees_expressions.append(string)
                all_trees_expressions = ' \n '.join(all_trees_expressions)
                xmax, gap = self.blit_text(all_trees_expressions,
                                           pos=((self.x_separation + 10, gap)),
                                           max_width=self.door_window_size - 20)

    def draw_rooms(self):
        # Affichage des pieces
        self.line_size = self.maze.line_size
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.position[self.maze.current_page])
                room_rectangle = pygame_Rect(x_gap, y_gap, x + 2, y + 2)
                self.element_dict[room.name] = room_rectangle
                if room.is_exit:
                    if self.uniform_inside_room_color:
                        pygame_draw_ellipse(self.WINDOW, self.room_color, room_rectangle)
                    else:
                        pygame_draw_ellipse(self.WINDOW, room.inside_color, room_rectangle)
                    if self.maze.current_room() == room:
                        if self.uniform_surrounding_colors:
                            pygame_draw_ellipse(self.WINDOW, self.surrounding_color, room_rectangle,
                                                width=self.line_size)
                        else:
                            pygame_draw_ellipse(self.WINDOW, room.surrounding_color, room_rectangle,
                                                width=self.line_size)
                else:
                    if self.uniform_inside_room_color:
                        pygame_draw_rect(self.WINDOW, self.room_color, room_rectangle)
                    else:
                        pygame_draw_rect(self.WINDOW, room.inside_color, room_rectangle)
                    if self.maze.current_room() == room:
                        if self.uniform_surrounding_colors:
                            pygame_draw_rect(self.WINDOW, self.surrounding_color, room_rectangle, width=self.line_size)
                        else:
                            pygame_draw_rect(self.WINDOW, room.surrounding_color, room_rectangle, width=self.line_size)

    def draw_rooms_names(self):
        # Affichage des pieces
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.position[self.maze.current_page])
                if room.is_exit:
                    room_name_render = self.font.render('EXIT',
                                                        True,
                                                        self.inside_room_color)
                    self.WINDOW.blit(room_name_render, room.get_name_position())
                else:
                    room_name_render = self.font.render(room.name,
                                                        True,
                                                        self.inside_room_color)
                    if self.print_room_name:
                        self.WINDOW.blit(room_name_render, room.get_name_position())
                        
    def draw_cross(self):
        [pente_x, coeff_x, pente_y, coeff_y] = self.maze.coordinates_conversion
        if self.maze.rooms_list == []:
            return
        xmin = float('inf')
        ymin = float('inf')
        xmax = -float('inf')
        ymax = -float('inf')
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.user_position[self.maze.current_page])
                xmin = min(xmin, x_gap)
                ymin = min(ymin, y_gap)
                xmax = max(xmax, x_gap+x)
                ymax = max(ymax, y_gap+y)
        xmin = int(xmin)
        xmax = int(xmax)
        ymin = int(ymin)
        ymax = int(ymax)
        cross_size = 5
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                x_screen = pente_x*x + coeff_x
                y_screen = pente_y*y + coeff_y
                horizontal_start = (x_screen - cross_size, y_screen)
                horizontal_end = (x_screen + cross_size, y_screen)
                vertical_start = (x_screen, y_screen - cross_size)
                vertical_end = (x_screen, y_screen + cross_size)
                pygame_draw_line(self.WINDOW,
                                  self.contour_color,
                                  horizontal_start,
                                  horizontal_end,
                                  3)
                pygame_draw_line(self.WINDOW,
                                  self.contour_color,
                                  vertical_start,
                                  vertical_end,
                                  3)
                self.blit_text(text=f'{x} {y}',
                               pos=(x_screen+4, y_screen+4),
                               max_width=50,
                               color=self.contour_color)

    def draw_doors_polygons(self):
        # Affichage des polygones des portes
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                # real_middle_coordinates = door.real_middle_coordinates
                arrow_coordinates = door.arrow_coordinates
                self.element_dict[door.name] = arrow_coordinates
                if self.uniform_inside_room_color:
                    pygame_draw_polygon(self.WINDOW,
                                        self.room_color,
                                        arrow_coordinates)
                else:
                    pygame_draw_polygon(self.WINDOW,
                                        door.inside_color,
                                        arrow_coordinates)
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
            if self.maze.current_page in door.pages_list:
                real_middle_coordinates = door.real_middle_coordinates
                door_name_render = self.font.render(door.name,
                                                    True,
                                                    self.inside_room_color)
                self.WINDOW.blit(door_name_render,
                                 real_middle_coordinates)

    def draw_switches(self):
        # Affichage des interrupteurs
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                switches_positions = room.get_switches_positions()
                switches_list = room.switches_list
                assert len(switches_positions) == len(switches_list)
                for i in range(len(switches_list)):
                    switch = switches_list[i]
                    position = switches_positions[i]
                    rect = pygame_Rect(position[0] - self.click_rect_size_x / 2,
                                       position[1] - self.click_rect_size_y / 2,
                                       self.click_rect_size_x,
                                       self.click_rect_size_y)
                    self.element_dict[switch.name] = rect
                    if switch.value:
                        if self.print_click_rects:
                            pygame_draw_rect(self.WINDOW,
                                             self.background_color,
                                             rect)
                        else:
                            rectangle_switch = pygame_Rect(position[0] - self.click_rect_size_x / 2,
                                                           position[1] - self.click_rect_size_y / 2,
                                                           self.click_rect_size_x,
                                                           self.click_rect_size_y)
                            if self.uniform_surrounding_colors:
                                pygame_draw_rect(self.WINDOW,
                                                 self.inside_room_surrounding_color,
                                                 rectangle_switch,
                                                 width=3)
                            else:
                                pygame_draw_rect(self.WINDOW,
                                                 room.surrounding_color,
                                                 rectangle_switch,
                                                 width=3)
                    if self.print_click_rects:
                        if switch.value:
                            switch_name_render = self.font.render(switch.name,
                                                                  True,
                                                                  self.letters_color)
                        else:
                            switch_name_render = self.font.render(switch.name,
                                                                  True,
                                                                  self.inside_room_color)
                    else:
                        switch_name_render = self.font.render(switch.name,
                                                              True,
                                                              self.inside_room_color)
                    self.WINDOW.blit(switch_name_render,
                                     position - array([10 / 2 * len(switch.name), 7]))

    def display_help(self):

        try:
            self.WINDOW.fill(self.background_color)
            self.font = pygame_font_SysFont(None, self.help_font_size)
    
            self.draw_exterior_lines()
            # Affichage du nom du niveau courant
            maze_name = self.maze.name
            if self.maze.random:
                maze_name = maze_name + " (random)"
            level_name_render = self.font.render(
                f'Level {str(self.index_current_level+1)} / {Levels.number_of_levels} : {maze_name.replace('_', ' ')}',
                True,
                self.letters_color)
            self.WINDOW.blit(level_name_render, (10, 10))
            self.index_help_page = self.index_help_page % self.maze.n_help_pages
            help_txt = self.maze.help_txt[self.index_help_page]
            gap = 0
            p, c = linear_function(768-self.Y_marge, 50, 1080-self.Y_marge, 50)
            y0 = p * self.WINDOW_HEIGHT + c
            p, c = linear_function(1366-self.X_marge, 15, 1920-self.X_marge, 20)
            x0 = p * self.WINDOW_WIDTH + c
            """
            help_list = string_help.split('\n')
            help_txt = '\n'.join(help_list)
            help_txt = help_txt.split('\n')
            if help_txt[0].replace(' ', '') == '':
                help_txt = help_txt[1:]
            help_txt = '\n'.join(help_txt)
            """
            self.blit_text(text=help_txt,
                           pos=(x0, y0 + gap),
                           max_width=self.WINDOW_WIDTH-20-x0,
                           color=self.letters_color)
            pygame_display_update()
    
            if self.save_image:
                fname = f"images/HELP_level_{self.index_current_level}_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}.jpg"
                if not os_path_exists(fname):
                    pygame_image_save(self.WINDOW, fname)
        except ZeroDivisionError:
            maze_name = Levels.get_level(self.index_current_level, get_new_level=self.get_new_level).name
            print(f'The level {maze_name} cannot be loaded.')
            print('Your screen is too small.')

    def print_current_action(self):
        try:
            current_action_render = self.font.render(self.current_action,
                                                     True,
                                                     self.inside_room_color)
            self.WINDOW.blit(current_action_render,
                             (self.x_separation + self.y_separation / 3, self.y_separation / 2 - 7))
        except TypeError:
            print(self.current_action)
            raise

    def display_game_window(self):
        try:
            self.font = pygame_font_SysFont(None, self.font_size)
            self.WINDOW.fill(self.background_color)
            self.uniform_surrounding_colors = self.maze.uniform_surrounding_colors
            self.uniform_inside_room_color = self.maze.uniform_inside_room_color
            self.draw_right_window()
            self.draw_windows_separation()
            self.print_level_name()
            self.print_trees()
            self.print_you_won()
            self.draw_door_lines()
            self.draw_rooms()
            self.draw_switches()
            self.draw_doors_polygons()
            self.print_doors_names()
            self.print_current_action()
            self.draw_rooms_names()
            self.draw_exterior_lines()
            if self.dev_mode:
                self.draw_cross()
            pygame_display_update()
        except ZeroDivisionError:
            maze_name = Levels.get_level(self.index_current_level, get_new_level=self.get_new_level).name
            print(f'The level {maze_name} cannot be loaded.')
            print('Your screen is too small.')
        
    def update_possible_actions(self, reset_current_action_index=True):
        maze = self.maze
        current_room = maze.current_room()
        # SWITCHES LIST
        switches_list = []
        for switch in current_room.switches_list:
             switches_list.append(switch.name)
        # DOOR LIST
        doors_list = []
        for door in current_room.departure_doors_list:
            if door.is_open:
                doors_list.append(door.name)
        for door in current_room.two_way_doors_list:
            if door.is_open:
                doors_list.append(door.name)
        # SORT LIST
        sort_func = lambda x : int(x.replace('S', '').replace('D', ''))
        switches_list.sort(key=sort_func)
        doors_list.sort(key=sort_func)
        self.possible_current_actions = switches_list + doors_list
        if reset_current_action_index:
            self.current_action_index = -1
        
    def handle_keys_ALT(self):
        if time() - self.last_key_pressed_time > self.time_between_actions:
            if self.possible_current_actions in [None, []]:
                self.update_possible_actions(reset_current_action_index=False)
            if self.possible_current_actions == []:
                return
            n_switches = ' '.join(self.possible_current_actions).count('S')
            if (self.pressed[K_RALT]):
                self.current_action_index = max(n_switches, (self.current_action_index + 1)% len(self.possible_current_actions))
                self.current_action_index_changed = True
            if (self.pressed[K_LALT]):
                self.current_action_index = (self.current_action_index + 1)%n_switches
                self.current_action_index_changed = True
            if self.current_action_index_changed:
                self.current_action_index = self.current_action_index % len(self.possible_current_actions)
                self.current_action = self.possible_current_actions[self.current_action_index]
                self.change_in_display = True
                self.last_key_pressed_time = time()
                self.current_action_index_changed = False
    
    def show_solution(self,
                      save_videos=False,
                      dt=0.15):
        dt = min(dt, 1)
        dt = 0
        video_name = f"videos/level_{self.index_current_level}_{self.maze.name}.avi"
        if save_videos and os_path_exists(video_name):
            return
        maze = self.maze
        maze.reboot_solution()
        solution = maze.fastest_solution
        if solution is None:
            sleep(2)
            return
        solution_actions_list = solution.replace('\n', ' ').split(' ')
        assert type(solution_actions_list) == list
        if save_videos:
            name = self.maze.name.replace(' ', '_')
            folder = f"videos/frames/{name}/"
            if not os_path_exists(folder):
                os_mkdir(folder)
            def fname(i):
                fname = folder + f"level_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}_frame_{i}.jpg"
                return fname
            self.save_image_as_file(fname(0))
            self.save_image_as_file()
        for i in range(len(solution_actions_list)):
            action = solution_actions_list[i]
            self.current_action = action
            self.display_game_window()
            if save_videos:
                self.save_image_as_file(fname(1+2*i))
            sleep(dt)
            self.maze.make_actions(action)
            self.current_action = ''
            self.display_game_window()
            if save_videos:
                self.save_image_as_file(fname(2+2*i))
            sleep(dt)
            self.handle_events()
            if self.do_you_quit_game:
                return None
        if save_videos:
            import numpy as np
            from cv2 import VideoWriter, VideoWriter_fourcc, resize, cvtColor, COLOR_BGR2RGB #, imread#
            from PIL import Image
            size = (int(self.WINDOW_WIDTH), int(self.WINDOW_HEIGHT))
            out = VideoWriter(video_name,
                              VideoWriter_fourcc(*'DIVX'),
                              24,
                              size)
            name = self.maze.name.replace(' ', '_')
            i = 0
            while os_path_exists(fname(i)):
                img = Image.open(fname(i))
                img = np.array(img, dtype=np.uint8)
                img = resize(img, size)
                img = np.array(img, dtype=np.uint8)
                img = cvtColor(img, COLOR_BGR2RGB)
                for k in range(6):
                    out.write(img)
                i = i+1
            for k in range(6): # You add the last image 12 more times.
                out.write(img)
            out.release()
            
    def show_all_solutions(self, save_videos=False, dt=0.2):
        for i_level in range(self.index_current_level, Levels.number_of_levels):
            t0 = time()
            self.index_current_level = i_level
            self.level_changed = True
            self.get_level()
            self.display_game_window()
            sleep(dt)
            self.show_solution(save_videos=save_videos,
                               dt=dt)
            sleep(dt)
            assert dt >= 0
            sleep(max(0, 2*dt-time()+t0))
            
    def save_videos(self):
        # from PIL.Image import fromarray
        if not os_path_exists('videos'):
            os_mkdir('videos')
        if not os_path_exists('videos/frames'):
            os_mkdir('videos/frames')
        self.show_all_solutions(save_videos=True,
                                dt = 0)

    def handle_interractions(self):
        """
        for event in pygame_event_get():
            print('event.type', event.type)
            if event.type == MOUSEWHEEL:
               print(event)
               print(event.x, event.y)
               print(event.flipped)
               print(event.which)
        """
        self.pressed = pygame_key_get_pressed()
        if time() - self.last_key_pressed_time > self.time_between_actions:
            self.pressed = pygame_key_get_pressed()
            for key in Game.keys_dict.keys():
                if self.pressed[key]:
                    self.change_in_display = True
                    self.current_action = self.current_action + Game.keys_dict[key]
                    self.last_key_pressed_time = time()
            if self.pressed[K_RETURN] and self.current_action != '':# and self.maze.current_room_index != self.maze.exit_room_index:
                self.change_in_display = True
                if len(self.current_action) > 0:
                    # with open('temp.txt', 'a') as fa:
                    #     fa.write(self.current_action + ' ')
                    if self.current_action == 'B':
                        self.change_in_display = True
                        self.maze.reboot_solution()
                        self.last_key_pressed_time = time()
                        self.current_action = ''
                        self.maze.current_door_page = 0
                        self.update_possible_actions()
                    elif self.current_action == 'N':
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                        self.update_possible_actions()
                    elif self.current_action.split(' ')[0] in ['SOL', 'SOLUTION']:
                        if len(self.current_action.split(' ')) == 1:
                            self.show_solution()
                        else:
                            try:
                                dt = float(self.current_action.split(' ')[1])
                                print(dt)
                                self.show_solution(dt=dt)
                            except ValueError:
                                self.show_solution()
                        self.update_possible_actions()
                    elif self.current_action in ['SOLS', 'SOLUTIONS']:
                        self.show_all_solutions()
                        self.update_possible_actions()
                    elif self.current_action.split(' ')[0] in ['FIND',
                                                               'FINDSOL',
                                                               'FINDSOLUTION',
                                                               'FIND SOL',
                                                               'FIND SOLUTION']:
                        if self.maze.random:
                            maze = self.maze
                        else:
                            maze = Levels.get_level(self.index_current_level,
                                                    get_new_level=True,
                                                    fast_solution_finding=True)
                        sol_list = maze.find_all_solutions(stop_at_first_solution=True,
                                                           verbose=1,)[0]
                        self.maze.fastest_solution=' '.join(sol_list[0])
                        if len(self.current_action.split(' ')) == 1:
                            self.show_solution()
                        else:
                            try:
                                dt = float(self.current_action.split(' ')[1])
                                self.show_solution(dt=dt)
                            except ValueError:
                                self.show_solution()
                        self.update_possible_actions()
                        print(self.maze.fastest_solution)
                    elif self.current_action in ['LR', 'LRANDOM']:
                        level_number_list = [i for i in range(Levels.number_of_levels)]
                        self.index_current_level = rd_choice(level_number_list)
                        self.level_changed = True
                        self.update_possible_actions()
                    elif self.current_action in ['VIDEO', 'VIDEOS']:
                        self.save_videos()
                    elif self.current_action == 'COLOR':
                        self.game_color = None
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                    elif self.current_action[:3] == 'HSL':
                        hu = 0.1
                        sa = 0
                        li = 0.35
                        l = self.current_action.split(' ')[1:]
                        if len(l) >= 1:
                            try:
                                hu = float(l.pop(0))
                            except ValueError:
                                pass
                        if len(l) >= 1:
                            try:
                                sa = float(l.pop(0))
                            except ValueError:
                                pass
                        if len(l) >= 1:
                            try:
                                li = float(l.pop(0))
                            except ValueError:
                                pass
                        self.game_color = Levels_colors_list.FROM_HUE(hu=hu, sa=sa, li=li)
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                    else:
                        self.current_action = self.current_action.replace('EXIT', 'RE')
                        if self.current_action[0] in ['D', 'S', 'R']:
                            self.maze.make_actions(self.current_action)
                            if 'R' in self.current_action or 'D' in self.current_action:
                                self.update_possible_actions()
                            else:
                                self.update_possible_actions(reset_current_action_index=False)
                        if self.current_action[0:2] == 'A ':
                            self.maze.make_actions(self.current_action[2:], allow_all=True)
                        if self.current_action[0] == 'A':
                            self.maze.make_actions(self.current_action[1:], allow_all=True)
                        elif self.current_action[0] == 'L':
                            level_number_list = [str(i) for i in range(Levels.number_of_levels)]
                            if self.current_action[1:] in level_number_list:
                                self.index_current_level = int(self.current_action[1:])-1
                                self.level_changed = True
                            self.update_possible_actions()
                        self.current_action = ''
        if time() - self.last_key_BACKSPACE_pressed_time > self.time_between_deletings:
            if self.pressed[K_BACKSPACE]:
                self.change_in_display = True
                self.current_action = self.current_action[:-1]
                self.last_key_BACKSPACE_pressed_time = time()

    def change_level(self):
        self.pressed = pygame_key_get_pressed()
        # Changement de niveau
        if time() - self.last_level_change_time > self.time_between_level_changing:
            if (self.pressed[K_RIGHT]):
                if self.show_help:
                    self.show_help = False
                else:
                    self.index_current_level += 1
                    self.show_help = True
                self.level_changed = True
                new_level = Levels.get_level(self.index_current_level, get_new_level=False)
                if self.show_help and ''.join(new_level.help_txt) == '':
                    self.show_help = False
            if (self.pressed[K_LEFT]):
                if not self.show_help:
                    self.show_help = True
                else:
                    self.index_current_level -= 1
                    self.show_help = False
                self.level_changed = True
                if self.show_help and ''.join(self.maze.help_txt) == '':
                    self.show_help = False
                    self.index_current_level -= 1
        if self.level_changed:
            self.last_level_change_time = time()
        self.index_current_level = self.index_current_level % Levels.number_of_levels

    def save_image_as_file(self,
                           fname=None):
        for folder in ["images",
                       "videos",
                       "videos/frames"]:
            if not os_path_exists(folder):
                os_mkdir(folder)
        if type(fname) is not str:
            fname = f"images/level_{self.index_current_level}_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}.jpg"
        # if not os_path_exists(fname):
        pygame_image_save(self.WINDOW, fname)

    def quit_game(self):
        self.t1 = time()
        if self.show_loop_time:
            self.t_tot = self.t1 - self.t0
            print("number of loops :\n", self.n_loops)
            print("time of execution :\n", round(self.t_tot, 0), 's')
            print("mean time of execution of one loop :\n", self.t_tot / self.n_loops, 's')
        pygame_quit()

    def handle_events(self):
        def point_in_polygon(point, polygon_points):
            """ Vérifie si un point est à l'intérieur d'un polygone en utilisant l'algorithme du rayon """
            x, y = point
            n = len(polygon_points)
            inside = False
            p1x, p1y = polygon_points[0]
            for i in range(n + 1):
                p2x, p2y = polygon_points[i % n]
                if y > min(p1y, p2y):
                    if y <= max(p1y, p2y):
                        if x <= max(p1x, p2x):
                            if p1y != p2y:
                                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
                p1x, p1y = p2x, p2y
            return inside
        def point_in_ellipse(point, ellipse_rect):
            """ Vérifie si un point est à l'intérieur d'une ellipse définie par un Rect """
            cx = ellipse_rect.x + ellipse_rect.width / 2  # Centre x de l'ellipse
            cy = ellipse_rect.y + ellipse_rect.height / 2  # Centre y de l'ellipse
            rx = ellipse_rect.width / 2  # Rayon x de l'ellipse
            ry = ellipse_rect.height / 2  # Rayon y de l'ellipse
            px, py = point  # Point de clic
            # Formule de l'ellipse : ((x - cx)^2 / rx^2) + ((y - cy)^2 / ry^2) <= 1
            return ((px - cx) ** 2) / (rx ** 2) + ((py - cy) ** 2) / (ry ** 2) <= 1
        self.pressed = pygame_key_get_pressed()
        for event in pygame_event_get():
            if event.type == QUIT:
                # print(number_of_loops)
                self.quit_game()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_help:
                    self.show_help = False
                    self.level_changed = True
                else:
                    mouse_x, mouse_y = event.pos
                    if self.lower_right_window_rectangle.collidepoint(mouse_x, mouse_y):
                        self.name_tree_list = self.name_tree_list[1:] + self.name_tree_list[:1]
                        self.last_key_pressed_time = time()
                        self.change_in_display = True
                    # if self.upper_right_window_rectangle.collidepoint(mouse_x, mouse_y):
                    #     self.index_current_level += 1
                    #     self.show_help = True
                    #     self.change_in_display = True
                    for room in self.maze.rooms_list:
                        rect = self.element_dict[room.name]
                        if room.name == 'RE':
                            if point_in_ellipse(event.pos, rect):
                                if self.maze.current_room().is_exit:
                                    self.index_current_level += 1
                                    self.show_help = True
                                    self.level_changed = True
                                else:
                                    self.maze.make_actions('RE')
                                self.change_in_display = True
                        else:
                            if rect.collidepoint(mouse_x, mouse_y):
                                self.maze.make_actions(room.name)
                                self.change_in_display = True
                    for door in self.maze.doors_set:
                        polygon = self.element_dict[door.name]
                        if point_in_polygon(event.pos, polygon):
                            self.maze.make_actions(door.name)
                            self.change_in_display = True
                    for switch in self.maze.switches_set:
                        rect = self.element_dict[switch.name]
                        if rect.collidepoint(mouse_x, mouse_y):
                            self.maze.make_actions(switch.name)
                            self.change_in_display = True
        if self.pressed[K_ESCAPE]:
            self.quit_game()
            self.do_you_quit_game = True

    def update_to_save_images(self):
        if self.save_image:
            if self.index_current_level != Levels.number_of_levels - 1:
                self.index_current_level += 1
            else:
                if not self.show_help:
                    self.show_help = 1
                    self.change_in_display = True
                    self.index_current_level = 0
                else:
                    self.quit_game()
                    return True
            self.level_changed = True
        return False
    
    def handle_K_UP_DOWN(self):
        # print(time() - self.last_key_pressed_time)
        self.pressed = pygame_key_get_pressed()
        if time() - self.last_key_pressed_time > self.time_between_actions:
            if self.pressed[K_DOWN]:
                self.name_tree_list = self.name_tree_list[1:] + self.name_tree_list[:1]
                self.last_key_pressed_time = time()
                self.change_in_display = True
            if self.pressed[K_UP]:
                self.name_tree_list = self.name_tree_list[-1:] + self.name_tree_list[:-1]
                self.last_key_pressed_time = time()
                self.change_in_display = True

    def play(self): # The main function that controls the game
        self.game_setup()
        self.t0 = time()
        self.n_loops = 0
        while self.looping:
            sleep(self.sleep_time)  # I did that not to use too much CPU
            self.n_loops += 1
            self.handle_events()
            if self.do_you_quit_game:
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
                self.handle_keys_ALT()
                self.handle_interractions()
                if self.save_image:
                    self.save_image_as_file()
            self.change_level()
            self.handle_K_UP_DOWN()
            if self.update_to_save_images():  # It means you quit the game
                return None

    def save_levels_txt(verbose=0, calculates_solutions=True, short_only=True):
        t0 = time()
        Maze.calculates_solutions = calculates_solutions
        if not os_path_exists('mazes'):
            os_mkdir('mazes')
        for k in range(Levels.number_of_levels):
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