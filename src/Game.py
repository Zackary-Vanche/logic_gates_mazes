from pygame import init as pygame_init
# from pygame import MOUSEBUTTONDOWN
import pygame.locals
from pygame.locals import K_KP0, K_KP1, K_KP2, K_KP3, K_KP4
from pygame.locals import K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
from pygame.locals import QUIT, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE, K_LALT, K_RALT
from pygame.locals import K_RETURN, K_BACKSPACE, K_ESCAPE
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
# from pygame.event import get as pygame_event_get
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
                 sleep_time=1e-3,
                 game_color=None): # if game_color is not None, it overwrites the levels colors
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
        pygame_display_set_caption('Logic gates maze')
        self.WINDOW_SIZE_changed = False

        self.font = pygame_font_SysFont(None, self.font_size)
        self.level_changed = True
        # Cette variable vaut True quand le joueur
        # vient de choisir de changer de niveau
        # ou au début du jeu (il faut initialiser le niveau)
        self.last_level_change_time = time()
        if self.print_click_rects:
            self.click_rect_size_x = 40
            self.click_rect_size_y = 30
        else:
            self.click_rect_size_x = 40
            self.click_rect_size_y = 30
        if self.save_image:
            if not os_path_exists('images'):
                os_mkdir('images')
        self.current_action = ''
        self.last_key_pressed_time = time()
        self.last_space_pressed_time = time()
        self.last_key_BACKSPACE_pressed_time = time()

    def get_level(self):

        if self.level_changed or self.get_new_level:
            try:
                self.change_in_display = True
    
                self.level_changed = False
    
                # self.maze = Levels.levels_functions_list[self.index_current_level]()
                self.maze = Levels.get_level(self.index_current_level, get_new_level=self.get_new_level)
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
        right_window_rectangle = pygame_Rect(self.x_separation,
                                             0,
                                             self.door_window_size,
                                             self.WINDOW_HEIGHT)
        pygame_draw_rect(self.WINDOW, self.room_color, right_window_rectangle)

    def draw_door_lines(self):
        # Affichage des lignes des portes
        self.line_size = self.maze.line_size
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                real_departure_coordinates = door.real_departure_coordinates
                real_arrival_coordinates = door.real_arrival_coordinates
                if not door.is_open:
                    pygame_draw_line(self.WINDOW,
                                     self.room_color,
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
        level_name_render = self.font.render(
            'Level ' + str(self.index_current_level) + ' : ' + self.maze.name.replace('_', ' '),
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
        # elif self.maze.door_multipages:
        #     door = self.doors_list[self.maze.current_door_page]
        #     tree = door.tree
        #     logical_expression = tree.get_easy_logical_expression_PN()
        #     logical_expression = logical_expression.split('\n')
        #     self.n_lines_door_printing = len(logical_expression)
        #     self.gap_between_lines = min(
        #         (self.WINDOW_HEIGHT - self.maze.y_separation - 50) / (self.n_lines_door_printing), 30)
        #     tree = door.tree
        #     str_logical_expression = tree.get_easy_logical_expression_PN()
        #     str_logical_expression = str_logical_expression.split('\n')
        #     gap = self.y_separation + 10
        #     self.WINDOW.blit(self.font.render('DOORS :',
        #                                       True,
        #                                       self.inside_room_color),
        #                       (self.x_separation + 10, gap))
        #     gap = self.y_separation + 35
        #     for i in range(len(str_logical_expression)):
        #         string = str_logical_expression[i]
        #         if i == 0:
        #             logical_expression_render = self.font.render(door.name + ' = ' + string,
        #                                                           True,
        #                                                           self.inside_room_color)
        #             self.WINDOW.blit(logical_expression_render, (self.x_separation + 10, gap))
        #         else:
        #             logical_expression_render = self.font.render(' ' * (len(door.name) + 3) + string,
        #                                                           True,
        #                                                           self.inside_room_color)
        #             self.WINDOW.blit(logical_expression_render, (self.x_separation + 10, gap))
        #         gap += self.gap_between_lines
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
                                           max_width=self.door_window_size - 40)

    def draw_rooms(self):
        # Affichage des pieces
        self.line_size = self.maze.line_size
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.position[self.maze.current_page])
                room_rectangle = pygame_Rect(x_gap, y_gap, x + 2, y + 2)
                if room.is_exit:
                    pygame_draw_ellipse(self.WINDOW, self.room_color, room_rectangle)
                    if self.maze.current_room() == room:
                        if self.uniform_surrounding_colors:
                            pygame_draw_ellipse(self.WINDOW, self.surrounding_color, room_rectangle,
                                                width=self.line_size)
                        else:
                            pygame_draw_ellipse(self.WINDOW, room.surrounding_color, room_rectangle,
                                                width=self.line_size)
                else:
                    pygame_draw_rect(self.WINDOW, self.room_color, room_rectangle)
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

    def draw_doors_polygons(self):
        # Affichage des polygones des portes
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                # real_middle_coordinates = door.real_middle_coordinates
                arrow_coordinates = door.arrow_coordinates
                pygame_draw_polygon(self.WINDOW,
                                    self.room_color,
                                    arrow_coordinates)
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
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
        # TODO
        # for door in self.maze.doors_set:
        #     word_surface = self.font.render(door.name, 1, self.inside_room_color)
        #     word_width, word_height = word_surface.get_size()
        #     real_middle_coordinates = array(door.real_middle_coordinates)
        #     center_point = array(real_middle_coordinates) + array([word_width, word_height])/2
        #     # arrow_coordinates = door.arrow_coordinates
        #     p1 = door.real_departure_coordinates
        #     p2 = door.real_arrival_coordinates
        #     epsilon = 2
    
        #     # Bounding box of the text in the native coordinates
        #     a = real_middle_coordinates + array([-epsilon, -epsilon])
        #     b = real_middle_coordinates + array([word_width+epsilon, -epsilon])
        #     c = real_middle_coordinates + array([word_width+epsilon, word_height+epsilon])
        #     d = real_middle_coordinates + array([-epsilon, word_height+epsilon])

        #     # Calculate the direction vector of the line
        #     line_direction = array([p2[0] - p1[0], p2[1] - p1[1]])
        #     line_direction /= norm(line_direction)
            
        #     # Create an orthogonal vector to the line direction
        #     orthogonal_vector = array([-line_direction[1], line_direction[0]])
        #     orthogonal_vector /= norm(orthogonal_vector)  # Normalize the orthogonal vector
            
        #     # Calculate the coordinates of a, b, c, d in the new coordinate system
        #     a_new = array([a[0] - center_point[0], a[1] - center_point[1]])
        #     b_new = array([b[0] - center_point[0], b[1] - center_point[1]])
        #     c_new = array([c[0] - center_point[0], c[1] - center_point[1]])
        #     d_new = array([d[0] - center_point[0], d[1] - center_point[1]])
            
        #     # Calculate the coordinates of the bounding box corners in the new coordinate system
        #     x_min = min(a_new.dot(orthogonal_vector),
        #                 b_new.dot(orthogonal_vector),
        #                 c_new.dot(orthogonal_vector),
        #                 d_new.dot(orthogonal_vector))
        #     x_max = max(a_new.dot(orthogonal_vector),
        #                 b_new.dot(orthogonal_vector),
        #                 c_new.dot(orthogonal_vector),
        #                 d_new.dot(orthogonal_vector))
        #     y_min = min(a_new.dot(line_direction),
        #                 b_new.dot(line_direction),
        #                 c_new.dot(line_direction),
        #                 d_new.dot(line_direction))
        #     y_max = max(a_new.dot(line_direction),
        #                 b_new.dot(line_direction),
        #                 c_new.dot(line_direction),
        #                 d_new.dot(line_direction))
            
        #     # Calculate new arrow coordinates
        #     a_final = center_point + x_min * orthogonal_vector + y_min * line_direction
        #     b_final = center_point + x_max * orthogonal_vector + y_min * line_direction
        #     c_final = center_point + x_max * orthogonal_vector + y_max * line_direction
        #     d_final = center_point + x_min * orthogonal_vector + y_max * line_direction
        #     if door.two_way:
        #         arrow_coordinates = [a_final,
        #                              center_point + (y_min-15) * line_direction,
        #                              b_final,
        #                              c_final,
        #                              center_point + (y_max+15) * line_direction,
        #                              d_final]
        #     else:
        #         arrow_coordinates = [a_final,
        #                              b_final,
        #                              c_final,
        #                              center_point + (y_max+15) * line_direction,
        #                              d_final]
        #     for i in range(len(arrow_coordinates)):
        #         line_size = self.maze.line_size
        #         arrow_coordinates[i] = arrow_coordinates[i] + line_size/2*orthogonal_vector
        #     print(arrow_coordinates)
        #     pygame_draw_polygon(self.WINDOW,
        #                         self.room_color,
        #                         arrow_coordinates)

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
            level_name_render = self.font.render(
                'HELP - Level ' + str(self.index_current_level) + ' : ' + self.maze.name.replace('_', ' '),
                True,
                self.letters_color)
            self.WINDOW.blit(level_name_render, (10, 10))
            self.index_help_page = self.index_help_page % self.maze.n_help_pages
            string_help = self.maze.help_txt[self.index_help_page]
            gap = 0
            help_list = string_help.split('\n')
            p, c = linear_function(768 - self.Y_marge, 50, 1080 - self.Y_marge, 50)
            y0 = p * self.WINDOW_HEIGHT + c
            p, c = linear_function(1366 - self.X_marge, 50, 1920 - self.X_marge, 50)
            x0 = p * self.WINDOW_WIDTH + c
            self.blit_text(text=' \n '.join(help_list),
                           pos=(x0, y0 + gap),
                           max_width=self.WINDOW_WIDTH-20-x0,
                           color=self.letters_color)
            # for line in help_list:
            #     self.WINDOW.blit(self.font.render(line,
            #                                       True,
            #                                       self.letters_color),
            #                      (x0, y0 + gap))
            #     if line.replace(' ', '') == '':
            #         gap += 12
            #     else:
            #         gap += 25
    
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
        current_action_render = self.font.render(self.current_action,
                                                 True,
                                                 self.inside_room_color)
        self.WINDOW.blit(current_action_render,
                         (self.x_separation + self.y_separation / 3, self.y_separation / 2 - 7))

    def display_game_window(self):
        try:
            self.font = pygame_font_SysFont(None, self.font_size)
            self.WINDOW.fill(self.background_color)
            self.uniform_surrounding_colors = self.maze.uniform_surrounding_colors
            self.uniform_inside_room_color = self.maze.uniform_inside_room_color
            self.draw_right_window()
            self.draw_exterior_lines()
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
            self.current_action_index = 0
        
    def handle_keys_UP_DOWN(self):
        if time() - self.last_key_pressed_time > self.time_between_actions:
            if self.possible_current_actions in [None, []]:
                self.update_possible_actions(reset_current_action_index=False)
            if self.possible_current_actions == []:
                return
            if (self.pressed[K_RALT]):
                self.current_action_index = self.current_action_index - 1
                self.current_action_index_changed = True
            if (self.pressed[K_LALT]):
                self.current_action_index = self.current_action_index + 1
                self.current_action_index_changed = True
            if self.current_action_index_changed:
                self.current_action = self.possible_current_actions[self.current_action_index % len(self.possible_current_actions)]
                self.change_in_display = True
                self.last_key_pressed_time = time()
                self.current_action_index_changed = False
    
    def show_solution(self,
                      save_videos=False,
                      dt=0.1):
        maze = self.maze
        maze.reboot_solution()
        solution = maze.fastest_solution
        if solution is None:
            return
        solution_actions_list = solution.split(' ')
        if save_videos:
            name = self.maze.name.replace(' ', '_')
            folder = f"videos/frames/{name}/"
            if not os_path_exists(folder):
                os_mkdir(folder)
            def fname(i):
                fname = folder + f"level_{self.index_current_level}_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}_frame_{i}.jpg"
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
            if self.do_you_quit_game():
                return None
        if save_videos:
            import numpy as np
            from cv2 import VideoWriter, VideoWriter_fourcc, resize, cvtColor, COLOR_BGR2RGB #, imread#
            from PIL import Image
            size = (int(self.WINDOW_WIDTH), int(self.WINDOW_HEIGHT))
            video_name = f"videos/level_{self.index_current_level}_{self.maze.name}.avi"
            out = VideoWriter(video_name,
                              VideoWriter_fourcc(*'DIVX'),
                              24,
                              size)
            name = self.maze.name.replace(' ', '_')
            def fname(i):
                fname = folder + f"level_{self.index_current_level}_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}_frame_{i}.jpg"
                return fname
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
        for i_level in range(Levels.number_of_levels):
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
        self.pressed = pygame_key_get_pressed()
        # Gestion des actions
        # if self.maze.current_room_index == self.maze.exit_room_index and self.current_action != 'YOU WON !':
        #     self.current_action = 'YOU WON !'
        #     self.change_in_display = True
        #     self.update_possible_actions()
        if time() - self.last_key_pressed_time > self.time_between_actions:
            self.pressed = pygame_key_get_pressed()
            for key in Game.keys_dict.keys():
                if self.pressed[key]:
                    self.change_in_display = True
                    self.update_possible_actions()
                    self.current_action = self.current_action + Game.keys_dict[key]
                    self.last_key_pressed_time = time()
            if self.pressed[K_RETURN] and self.current_action != '':# and self.maze.current_room_index != self.maze.exit_room_index:
                self.change_in_display = True
                self.update_possible_actions()
                if len(self.current_action) > 0:
                    # with open('temp.txt', 'a') as fa:
                    #     fa.write(self.current_action + ' ')
                    if self.current_action == 'B':
                        self.change_in_display = True
                        self.update_possible_actions()
                        self.maze.reboot_solution()
                        self.last_key_pressed_time = time()
                        self.current_action = ''
                        self.maze.current_door_page = 0
                    elif self.current_action == 'N':
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                    elif self.current_action == 'HHH':
                        self.show_solution()
                    elif self.current_action == 'HHHHH':
                        self.show_all_solutions()
                    elif self.current_action == 'VVV':
                        self.save_videos()
                    elif self.current_action == 'GREY':
                        self.game_color = Levels_colors_list.FROM_HUE(hu=0.1, sa=0, li=0.35)
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                    elif self.current_action == 'COLOR':
                        self.game_color = None
                        self.get_new_level = True
                        self.get_level()
                        self.change_in_display = True
                    else:
                        self.current_action = self.current_action.replace('EXIT', 'RE')
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
                        self.update_possible_actions()
        if time() - self.last_key_BACKSPACE_pressed_time > self.time_between_deletings:
            if self.pressed[K_BACKSPACE]:
                self.change_in_display = True
                self.update_possible_actions()
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
            if (self.pressed[K_LEFT]):
                if not self.show_help:
                    self.show_help = True
                else:
                    self.index_current_level -= 1
                    self.show_help = False
                self.level_changed = True
        if self.level_changed:
            self.last_level_change_time = time()
        if self.index_current_level == -1:
            self.index_current_level = Levels.number_of_levels - 1
        if self.index_current_level == Levels.number_of_levels:
            self.index_current_level = 0
        self.index_current_level = min(self.index_current_level,
                                       Levels.number_of_levels - 1)
        self.index_current_level = max(self.index_current_level,
                                       0)

    # def goto_or_leave_help(self):
    #     self.pressed = pygame_key_get_pressed()
    #     # Passage au menu d'aide / quitter le menu aide
    #     if time() - self.last_key_pressed_time > self.time_between_actions:
    #         if self.pressed[K_h]:
    #             self.show_help = not self.show_help
    #             self.last_key_pressed_time = time()
    #             self.change_in_display = True
    #             self.update_possible_actions()

    # def change_door_page(self):
    #     self.pressed = pygame_key_get_pressed()
    #     # Changement de page du jeu
    #     if time() - self.last_key_pressed_time > self.time_between_actions:
    #         if self.pressed[K_m]:
    #             self.last_key_pressed_time = time()
    #             self.maze.current_door_page += -1
    #             self.maze.current_door_page = self.maze.current_door_page % len(self.maze.doors_set)
    #             self.change_in_display = True
    #         # if self.pressed[K_n]:
    #         #     self.last_key_pressed_time = time()
    #         #     self.get_new_level = True
    #         #     self.get_level()
    #         #     self.change_in_display = True
    #         if self.pressed[K_p]:
    #             self.last_key_pressed_time = time()
    #             self.maze.current_door_page += 1
    #             self.maze.current_door_page = self.maze.current_door_page % len(self.maze.doors_set)
    #             self.change_in_display = True

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
        return None

    def do_you_quit_game(self):
        self.pressed = pygame_key_get_pressed()
        for event in pygame_event_get():
            if event.type == QUIT:
                # print(number_of_loops)
                self.quit_game()
                return True
        if self.pressed[K_ESCAPE]:
            self.quit_game()
            return True
        return False

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
    
    # def change_draw_wires(self):
    #     print('change_draw_wires', time())
    #     self.pressed = pygame_key_get_pressed()
    #     if time() - self.last_space_pressed_time > self.time_between_actions:
    #         if self.pressed[K_w]:
    #             self.show_wires = not self.show_wires
    #             self.last_space_pressed_time = time()
    #             self.change_in_display = True
    #             self.update_possible_actions()
    #             print('self.show_wires', self.show_wires)
        
    def draw_wires(self):
        pass
    
    def handle_ALT(self):
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

    # The main function that controls the game
    def play(self):
        self.game_setup()
        self.t0 = time()
        self.n_loops = 0
        while self.looping:
            sleep(self.sleep_time)  # I did that not to use too much CPU
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
                # if self.show_wires:
                #     if self.change_in_display or self.update_display_at_every_loop:
                #         self.draw_wires()
                # else:
                if self.change_in_display or self.update_display_at_every_loop:
                    self.display_game_window()
                    self.change_in_display = False
                self.handle_keys_UP_DOWN()
                self.handle_interractions()
                if self.save_image:
                    self.save_image_as_file()
            self.change_level()
            # self.goto_or_leave_help()
            self.handle_ALT()
            # self.change_door_page()
            if self.update_to_save_images():  # It means you quit the game
                return None
            # self.change_page()

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