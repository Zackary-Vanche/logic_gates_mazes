from pygame import init as pygame_init
# from pygame import MOUSEBUTTONDOWN
import pygame.locals
from pygame.locals import K_KP0, K_KP1, K_KP2, K_KP3, K_KP4
from pygame.locals import K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
from pygame.locals import QUIT, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE, K_LALT, K_RALT, K_KP_PERIOD
from pygame.locals import K_q, K_s, K_d, K_z
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

from pygame.mixer import init as pygame_mixer_init
from pygame.mixer import Sound as pygame_sound
from pygame.mixer import music as pygame_music

from os.path import exists as os_path_exists, join as os_path_join, isfile as os_path_isfile, abspath as os_abspath
from os import mkdir as os_mkdir
from os import listdir as os_listdir
from os import remove as os_remove
from numpy import array
# from numpy import sqrt
from numpy.linalg import norm
from numpy import sin
from time import time
from time import sleep

from linear_function import linear_function
from Maze import Maze
from Levels import Levels

from geometry import point_in_polygon, point_in_ellipse

from Color import Color
from tree_geometry import Map, make_nodes_dict, make_edges_list, make_children_dict
from tree_geometry import compute_positions as compute_levels_positions

from Levels_colors_list import Levels_colors_list

from random import choice as rd_choice

current_folder = '/'.join(__file__.split('\\')[:-1])

def get_files_list(folder):
    return ['/'.join([current_folder, folder, file]) for file in os_listdir('/'.join([current_folder, folder])) if os_path_isfile('/'.join([current_folder, folder, file]))]

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
                 # Cette variable détermine le niveau joué.
                 index_current_level=0,
                 time_between_actions=0.1,
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
                 dev_mode=False):  # if game_color is not None, it overwrites the levels colors
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
        self.player_name = None
        self.player_name_selection = ''
        self.dev_mode = dev_mode

    def map_color_setup(self):
        self.level_color_dict = {}
        for node in self.levels_dict.keys():
            level_module = self.levels_dict[node]
            assert hasattr(level_module, "f"), str(level_module)
            if hasattr(level_module, "get_color"):
                self.level_color_dict[node] = level_module.get_color()
            else:
                self.level_color_dict[node] = Levels_colors_list.FROM_HUE(
                    0, sa=0, li=0)
                print(self.levels_dict[node]().name, 'no get_color')

    def map_pos_x_min(self):
        return self.x_positions_map_min - self.x_positions_map_max + self.TOTAL_WIDTH/self.dx - self.marge/self.dx

    def map_pos_y_min(self):
        return self.y_positions_map_min - self.y_positions_map_max + self.TOTAL_HEIGHT/self.dy - self.marge/self.dy

    def map_pos_x_max(self):
        return self.marge/self.dx

    def map_pos_y_max(self):
        return self.marge/self.dy
    
    def make_level_number_dict(self):
        self.level_number_dict = {}
        for i, k in enumerate(sorted(self.levels_dict.keys())):
            self.level_number_dict[k] = i

    def game_map_setup(self):
        self.show_map = True
        level_tree = Levels.level_tree
        level_positions = compute_levels_positions(level_tree)
        self.level_positions_dict = make_nodes_dict(level_positions)
        self.positions_list = self.level_positions_dict.values()
        self.levels_true_positions_dict = {}
        self.levels_dict = make_nodes_dict(level_tree)
        self.make_level_number_dict()
        self.next_node_dict = make_children_dict(level_tree)
        self.map_color_setup()
        x_positions = [p[0] for p in self.positions_list]
        y_positions = [p[1] for p in self.positions_list]
        self.edges_list = make_edges_list(level_positions)
        self.dx = 50
        self.dy = 60
        self.marge = max(self.dx, self.dy)+5
        self.map_pos_x = self.map_pos_x_max()
        self.map_pos_y = self.map_pos_y_max()
        # self.delta_x = 50
        # self.delta_y = 50
        self.x_positions_map_min = min(x_positions)
        self.x_positions_map_max = max(x_positions)
        self.y_positions_map_min = min(y_positions)
        self.y_positions_map_max = max(y_positions)
        self.dot_radius_x = self.dx-15
        self.dot_radius_y = self.dy-15
        self.node = ''

    def sound_setup(self):
        self.d_volume = 1/8
        self.volume = self.d_volume
        self.music_volume = self.d_volume
        pygame_mixer_init()
        click_sounds_folder = r'sounds/click'
        self.click_sounds_list = [pygame.mixer.Sound(
            file) for file in get_files_list(click_sounds_folder)]
        footstep_sounds_folder = r'sounds/footstep'
        self.footstep_sounds_list = [pygame.mixer.Sound(
            file) for file in get_files_list(footstep_sounds_folder)]
        bell_sounds_folder = r'sounds/bell'
        self.bell_sounds_list = [pygame.mixer.Sound(
            file) for file in get_files_list(bell_sounds_folder)]
        pygame_music.load(current_folder+'/sounds/ambiance/forest.wav')
        pygame_music.play(-1)
        pygame_music.set_volume(self.music_volume)

    def play_click(self):
        sound = rd_choice(self.click_sounds_list)
        sound.set_volume(self.volume*0.3)
        pygame_sound.play(sound)

    def play_footstep(self):
        sound = rd_choice(self.footstep_sounds_list)
        sound.set_volume(self.volume*0.5)
        pygame_sound.play(sound)

    def play_bell(self):
        sound = rd_choice(self.bell_sounds_list)
        sound.set_volume(self.volume*0.5)
        pygame_sound.play(sound)

    def game_setup(self):
        # Game Setup
        pygame_init()
        self.sound_setup()
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

        self.game_map_setup()
        if not os_path_exists(current_folder+'/saved_games'):
            os_mkdir(current_folder+'/saved_games')
        self.levels_success_list = [0]*len(Levels.levels_modules_list)
        self.pressed = pygame_key_get_pressed()
        
    def get_level(self, fast_solution_finding=False):

        if self.level_changed or self.get_new_level:
            try:
                self.change_in_display = True
                self.level_changed = False
                self.get_new_level = False
                self.maze.reboot_solution()

                self.doors_list = self.maze.doors_list
                self.name_tree_list = []
                for tree in self.maze.intermediate_values_list:
                    assert tree.name[0] == 'V'
                    self.name_tree_list.append([tree.name, tree])
                for k in range(len(self.doors_list)):  # loop on the doors
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
                print('The level cannot be loaded.')
                print('Your screen is too small.')

    def update_map_window_size(self):

        if (self.WINDOW_WIDTH, self.WINDOW_HEIGHT) != self.WINDOW.get_size():
            self.WINDOW_SIZE_changed = True
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.WINDOW.get_size()
            self.WINDOW_WIDTH = max(
                self.SMALLEST_WINDOW_SIZE[0], self.WINDOW_WIDTH)
            self.WINDOW_HEIGHT = max(
                self.SMALLEST_WINDOW_SIZE[1], self.WINDOW_HEIGHT)

    def update_window_size(self):

        if (self.WINDOW_WIDTH, self.WINDOW_HEIGHT) != self.WINDOW.get_size():
            self.WINDOW_SIZE_changed = True
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.WINDOW.get_size()
            self.WINDOW_WIDTH = max(
                self.SMALLEST_WINDOW_SIZE[0], self.WINDOW_WIDTH)
            self.WINDOW_HEIGHT = max(
                self.SMALLEST_WINDOW_SIZE[1], self.WINDOW_HEIGHT)

        if self.WINDOW_SIZE_changed and not self.show_map:
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
        pygame_draw_rect(self.WINDOW, self.room_color,
                         upper_right_window_rectangle)
        pygame_draw_rect(self.WINDOW, self.room_color,
                         lower_right_window_rectangle)

    def draw_door_lines(self):
        # Affichage des lignes des portes
        self.line_size = self.maze.line_size
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                real_departure_coordinates = door.real_departure_coordinates
                real_arrival_coordinates = door.real_arrival_coordinates
                if not door.is_open:
                    if self.uniform_surrounding_colors:
                        c = self.room_color
                    else:
                        c = door.inside_color
                    pygame_draw_line(self.WINDOW,
                                     c,
                                     real_departure_coordinates,
                                     real_arrival_coordinates,
                                     self.line_size)
        for door in self.maze.doors_set:
            if self.maze.current_page in door.pages_list:
                real_departure_coordinates = door.real_departure_coordinates
                real_arrival_coordinates = door.real_arrival_coordinates
                if self.uniform_surrounding_colors:
                    c = self.surrounding_color
                else:
                    c = door.surrounding_color
                if door.is_open:
                    line_size = self.line_size
                    pygame_draw_line(self.WINDOW,
                                c,
                                real_departure_coordinates,
                                real_arrival_coordinates,
                                line_size)
                #else:
                #    line_size = 1     

    def draw_exterior_lines(self):
        if self.show_map:
            self.contour_color = [200]*3
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
        if self.maze.random and not 'random' in self.maze.name.lower():
            maze_name = maze_name + " (random)"
        level_name_render = self.font.render(
            maze_name.replace('_', ' '),
            True,
            self.letters_color)
        self.WINDOW.blit(level_name_render, (10, 10))

    def print_map_button(self):
        word_surface = self.font.render('MAP',
                                        True,
                                        self.letters_color)
        word_width, word_height = word_surface.get_size()
        self.map_rect = pygame_Rect(self.WINDOW_WIDTH - word_width - 30,
                                     0,
                                     word_width+30,
                                     self.y_separation+2)
        pygame_draw_rect(self.WINDOW, self.background_color, self.map_rect)
        pygame_draw_rect(self.WINDOW, self.contour_color, self.map_rect, 3)
        self.WINDOW.blit(
            word_surface, (self.WINDOW_WIDTH - word_width - 15, 14))

    def print_restart_button(self):
        word_surface = self.font.render('RESTART',
                                        True,
                                        self.letters_color)
        word_width, word_height = word_surface.get_size()
        xmax = self.map_rect.x
        self.button_restart_rect = pygame_Rect(xmax - word_width - 27,
                                               0,
                                               word_width+30,
                                               self.y_separation+2)
        pygame_draw_rect(self.WINDOW, self.background_color,
                         self.button_restart_rect)
        pygame_draw_rect(self.WINDOW, self.contour_color,
                         self.button_restart_rect, 3)
        self.WINDOW.blit(word_surface, (xmax - word_width - 12, 14))

    def print_new_button(self):
        word_surface = self.font.render('NEW',
                                        True,
                                        self.letters_color)
        word_width, word_height = word_surface.get_size()
        xmax = self.button_restart_rect.x
        self.button_new_rect = pygame_Rect(xmax - word_width - 27,
                                           0,
                                           word_width+30,
                                           self.y_separation+2)
        pygame_draw_rect(self.WINDOW, self.background_color,
                         self.button_new_rect)
        pygame_draw_rect(self.WINDOW, self.contour_color,
                         self.button_new_rect, 3)
        self.WINDOW.blit(word_surface, (xmax - word_width - 12, 14))

    def print_buttons(self):
        self.print_map_button()
        self.print_restart_button()
        if self.maze.random:
            self.print_new_button()

    def export_level_success_list(self):
        with open(current_folder+'/saved_games/'+self.player_name+'.txt', 'w') as fw:
            fw.write(''.join([str(i) for i in self.levels_success_list]))

    def print_you_won(self):
        if self.maze.current_room_index == self.maze.exit_room_index and self.current_action != 'YOU WON !':
            word_surface = self.font.render('YOU WON !',
                                            True,
                                            self.letters_color)
            word_width, word_height = word_surface.get_size()
            self.WINDOW.blit(
                word_surface, (self.x_separation - word_width - 105, 10))
            if not self.dev_mode:
                self.levels_success_list[self.level_number_dict[self.node]] = 1
                self.export_level_success_list()

    def blit_text(self,
                  text,
                  pos,
                  max_width,
                  color=None):
        if text == '':
            return
        if color is None:
            color = self.inside_room_color
        # 2D array where each row is a list of words.
        lines_list = [word.split(' ') for word in text.splitlines()]
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
            
            if self.uniform_inside_room_color:
                room_color = self.room_color
            else:
                room_color = room.inside_color
                
            if self.uniform_surrounding_colors:
                surrounding_color = self.surrounding_color
            else:
                surrounding_color = room.surrounding_color
            
            if self.maze.current_room() == room:
                line_size = self.line_size
            else:
                line_size = 1
                a = 1/3
                surrounding_color = a*array(surrounding_color)+(1-a)*array(room_color)
                
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.position[self.maze.current_page])
                room_rectangle = pygame_Rect(x_gap, y_gap, x + 2, y + 2)
                self.element_dict[room.name] = room_rectangle
                if room.is_exit:
                    pygame_draw_ellipse(self.WINDOW, room_color, room_rectangle)
                    pygame_draw_ellipse(self.WINDOW, surrounding_color, room_rectangle, width=line_size)
                else:
                    pygame_draw_rect(self.WINDOW, room_color, room_rectangle)
                    pygame_draw_rect(self.WINDOW, surrounding_color, room_rectangle, width=line_size)
                    
                    

    def draw_rooms_names(self):
        # Affichage des pieces
        for room in self.maze.rooms_list:
            if self.maze.current_page in room.pages_list:
                [x_gap, y_gap, x, y] = array(room.position[self.maze.current_page])
                if room.is_exit and room.name != '':
                    room_name_render = self.font.render('EXIT',
                                                        True,
                                                        self.inside_room_color)
                    self.WINDOW.blit(room_name_render,
                                     room.get_name_position())
                else:
                    room_name_render = self.font.render(room.name,
                                                        True,
                                                        self.inside_room_color)
                    if self.print_room_name:
                        self.WINDOW.blit(room_name_render,
                                         room.get_name_position())

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
                    inside_color = self.room_color
                else:
                    inside_color = door.inside_color
                pygame_draw_polygon(self.WINDOW,
                                    inside_color,
                                    arrow_coordinates)
                if self.uniform_surrounding_colors:
                    surrounding_color = self.surrounding_color
                else:
                    surrounding_color = door.surrounding_color
                if door.is_open:
                    width = 3
                else:
                    width = 1
                    a = 1/3
                    surrounding_color = a*array(surrounding_color)+(1-a)*array(inside_color)
                pygame_draw_polygon(self.WINDOW,
                                    surrounding_color,
                                    arrow_coordinates,
                                    width=width)

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
                                       position[1] - \
                                           self.click_rect_size_y / 2,
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
                                                           position[1] - \
                                                               self.click_rect_size_y / 2,
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
            if self.maze.random and not 'random' in self.maze.name.lower():
                maze_name = maze_name + " (random)"
            level_name_render = self.font.render(
                maze_name.replace('_', ' '),
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

            self.draw_arrows_buttons()

            pygame_display_update()

            if self.save_image:
                fname = f"images/HELP_level_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}.jpg"
                if not os_path_exists(fname):
                    pygame_image_save(self.WINDOW, fname)
        except ZeroDivisionError:
            print('The level cannot be loaded.')
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

    def draw_arrows_buttons(self):
        if self.show_help:
            w = self.WINDOW_WIDTH
            e = 10
            x = 60
            y = 30
        else:
            w = self.x_separation
            e = 5
            x = 40
            y = 20
        self.left_arrow_polygon = [[x, 0],
                                   [x/2, 0],
                                   [0, y/2],
                                   [x/2, y],
                                   [x, y]]
        self.right_arrow_polygon = [[w-x, y] for [x, y] in self.left_arrow_polygon]
        for i in range(len(self.left_arrow_polygon)):
            self.left_arrow_polygon[i][0] += w-2*x-2*e
            self.left_arrow_polygon[i][1] += e
        for i in range(len(self.right_arrow_polygon)):
            self.right_arrow_polygon[i][0] += -e
            self.right_arrow_polygon[i][1] += e
        pygame_draw_polygon(self.WINDOW,
                            self.room_color,
                            self.left_arrow_polygon)
        pygame_draw_polygon(self.WINDOW,
                            self.contour_color,
                            self.left_arrow_polygon,
                            width=2)
        pygame_draw_polygon(self.WINDOW,
                            self.room_color,
                            self.right_arrow_polygon)
        pygame_draw_polygon(self.WINDOW,
                            self.contour_color,
                            self.right_arrow_polygon,
                            width=2)

    def display_game_window(self):
        try:
            self.element_dict = {}
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
            self.print_buttons()
            self.draw_arrows_buttons()
            # if self.dev_mode:
            #     self.draw_cross()
            pygame_display_update()
        except ZeroDivisionError:
            print('The level cannot be loaded.')
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
        sort_func= lambda x: int(x.replace('S', '').replace('D', ''))
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
                self.current_action_index= max(n_switches, (self.current_action_index + 1) % len(self.possible_current_actions))
                self.current_action_index_changed = True
            if (self.pressed[K_LALT]):
                self.current_action_index = (self.current_action_index + 1) % n_switches
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
        video_name = f"videos/level_{self.maze.name}.avi"
        if save_videos and os_path_exists(video_name):
            return
        maze = self.maze
        maze.reboot_solution()
        solution = maze.fastest_solution
        if solution is None:
            sleep(10*dt)
            return
        solution_actions_list = solution.replace('\n', ' ').split(' ')
        assert type(solution_actions_list) == list
        name = self.maze.name.replace(' ', '_')
        folder_video = f"videos/frames/{name}/"
        if save_videos:
            if not os_path_exists(folder_video):
                os_mkdir(folder_video)
            def fname(i):
                fname = folder_video + f"level_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}_frame_{i}.jpg"
                return fname
            self.save_image_as_file(fname(0))
            self.save_image_as_file()
        assert self.maze.try_solution(solution) == 2
        self.maze.reboot_solution()
        for i in range(len(solution_actions_list)):
            action = solution_actions_list[i]
            if len(action) > 1:
                if i+1 == len(solution_actions_list):
                    self.play_bell()
                if action[0] in ['D', 'R']:
                    self.play_footstep()
                if action[0] == 'S':
                    self.play_click()
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
            from cv2 import VideoWriter, VideoWriter_fourcc, resize, cvtColor, COLOR_BGR2RGB  # , imread#
            from PIL import Image
            from shutil import rmtree
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
            for k in range(6):  # You add the last image 12 more times.
                out.write(img)
            out.release()
            rmtree(folder_video)

    def aux_handle_interractions(self):
        if len(self.current_action) == 0:
            return
        # if self.current_action == 'B':
        #     self.change_in_display = True
        #     self.maze.reboot_solution()
        #     self.last_key_pressed_time = time()
        #     self.current_action = ''
        #     self.maze.current_door_page = 0
        #     self.update_possible_actions()
        # elif self.current_action == 'N':
        #     self.get_new_level = True
        #     self.maze = self.level_module.f()
        #     assert isinstance(self.maze, Maze)
        #     self.change_in_display = True
        #     self.update_possible_actions()
        # elif self.current_action in ['LR', 'LRANDOM']:
        #     level_number_list = [i for i in range(Levels.number_of_levels)]
        #     self.level_changed = True
        #     self.update_possible_actions()
        else:
            self.current_action = self.current_action.replace('EXIT', 'RE')
            if self.current_action[0] in ['D', 'S', 'R']:
                self.maze.make_actions(self.current_action)
                if 'R' in self.current_action or 'D' in self.current_action:
                    self.update_possible_actions()
                else:
                    self.update_possible_actions(
                        reset_current_action_index=False)
            if self.current_action[0:2] == 'A ':
                self.maze.make_actions(self.current_action[2:], allow_all=True)
            if self.current_action[0] == 'A':
                self.maze.make_actions(self.current_action[1:], allow_all=True)
            # elif self.current_action[0] == 'L':
            #     level_number_list = [str(i) for i in range(Levels.number_of_levels)]
            #     if self.current_action[1:] in level_number_list:
            #         self.index_current_level = int(self.current_action[1:])-1
            #         self.level_changed = True
            #     self.update_possible_actions()
            self.current_action = ''

    def aux_handle_dev_mode_interractions(self):
        if not self.dev_mode:
            return
        if len(self.current_action) == 0:
            return
        if self.current_action.split(' ')[0] in ['SOL',
                                                 'SOLUTION',
                                                 'SOL0',
                                                 'SOL 0',
                                                 'SOLUTION0',
                                                 'SOLUTION 0']:
            if "0" in self.current_action.split(' ')[0]:
                self.show_solution(dt=0)
            else:
                self.show_solution()
            self.update_possible_actions()
        elif self.current_action.split(' ')[0] in ['FIND',
                                                   'FIND0',
                                                   'FINDSOL',
                                                   'FINDSOL0',
                                                   'FINDSOLUTION',
                                                   'FINDSOLUTION0',
                                                   'FIND SOL',
                                                   'FIND SOL 0',
                                                   'FIND SOLUTION',
                                                   'FIND SOLUTION 0']:
            sol_list = self.maze.find_all_solutions(stop_at_first_solution=True,
                                               verbose=1,)[0]
            self.maze.fastest_solution= ' '.join(sol_list[0])
            if len(self.current_action.split(' ')) == 1:
                if "0" in self.current_action.split(' ')[0]:
                    self.show_solution(dt=0)
                else:
                    self.show_solution()
            else:
                try:
                    if "0" in self.current_action.split(' ')[0]:
                        self.show_solution(dt=0)
                    else:
                        self.show_solution()
                except ValueError:
                    self.show_solution()
            self.update_possible_actions()
            print(self.maze.fastest_solution)
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

    def handle_interractions(self):
        self.pressed = pygame_key_get_pressed()
        if time() - self.last_key_pressed_time > self.time_between_actions:
            self.pressed = pygame_key_get_pressed()
            for key in Game.keys_dict.keys():
                if self.pressed[key]:
                    self.change_in_display = True
                    self.current_action = self.current_action + Game.keys_dict[key]
                    self.last_key_pressed_time = time()
            # and self.maze.current_room_index != self.maze.exit_room_index:
            if self.pressed[K_RETURN] and self.current_action != '':
                self.change_in_display = True
                self.aux_handle_dev_mode_interractions()
                self.aux_handle_interractions()
        if time() - self.last_key_BACKSPACE_pressed_time > self.time_between_deletings:
            if self.pressed[K_BACKSPACE]:
                self.change_in_display = True
                self.current_action = self.current_action[:-1]
                self.last_key_BACKSPACE_pressed_time = time()

    def get_previous_maze(self):
        if self.node == "":
            return None
        previous_node = '_'.join(self.node.split('_')[:-1])
        self.node = previous_node
        return self.levels_dict[self.node]

    def get_next_maze(self):
        new_nodes_list = self.next_node_dict[self.node]
        self.show_help = True
        self.change_in_display = True
        self.level_changed = True
        self.last_key_pressed_time = time() + 0.1
        if len(new_nodes_list) == 1:
            self.node = new_nodes_list[0]
            new_maze = self.levels_dict[self.node]
            self.maze = new_maze.f()
            self.level_module = new_maze
            assert isinstance(self.maze, Maze)
        else:
            self.show_map = True
            self.map_color_setup()

    def change_to_next_page(self):
        if self.show_help:
            self.play_footstep()
            self.show_help = False
        elif (not self.levels_success_list[self.level_number_dict[self.node]]) and not self.dev_mode:
            return
        else:
            self.play_footstep()
            self.get_next_maze()
        self.change_in_display = True
        self.level_changed = True
        self.last_key_pressed_time = time() + 0.1

    def change_to_previous_page(self):
        self.play_footstep()
        if self.show_help:
            new_maze = self.get_previous_maze()
            self.show_help = False
            if new_maze is None:
                self.show_map = True
                self.map_color_setup()
                self.change_in_display = True
            else:
                self.level_changed = True
                self.change_in_display = True
                self.maze = new_maze.f()
                self.level_module = new_maze
                assert isinstance(self.maze, Maze)
        else:
            self.show_help = True
            self.change_in_display = True
        self.level_changed = True
        self.last_key_pressed_time = time()

    def change_level(self):
        self.pressed = pygame_key_get_pressed()
        # Changement de niveau
        if time() - self.last_level_change_time > self.time_between_level_changing:
            if (self.pressed[K_RIGHT]):
                self.change_to_next_page()
            if (self.pressed[K_LEFT]):
                self.change_to_previous_page()
        if self.level_changed:
            self.last_level_change_time = time()

    def save_image_as_file(self,
                           fname=None):
        for folder in ["images",
                       "videos",
                       "videos/frames"]:
            if not os_path_exists(folder):
                os_mkdir(folder)
        if type(fname) is not str:
            fname = f"images/level_{self.maze.name}_WIDTH_{int(self.WINDOW_WIDTH)}_HEIGHT_{int(self.WINDOW_HEIGHT)}.jpg"
        # if not os_path_exists(fname):
        pygame_image_save(self.WINDOW, fname)

    def quit_game(self):
        self.t1 = time()
        if self.show_loop_time:
            self.t_tot = self.t1 - self.t0
            print("number of loops :\n", self.n_loops)
            print("time of execution :\n", round(self.t_tot, 0), 's')
            print("mean time of execution of one loop :\n",
                  self.t_tot / self.n_loops, 's')
        pygame_quit()

    def handle_events(self):
        self.pressed = pygame_key_get_pressed()
        for event in pygame_event_get():
            if time() - self.last_key_pressed_time > self.time_between_actions:
                if event.type == QUIT:
                    self.do_you_quit_game = True
                    self.quit_game()
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.last_key_pressed_time = time()
                    if not self.show_help:
                        mouse_x, mouse_y = event.pos
                        if self.map_rect.collidepoint(mouse_x, mouse_y):
                            self.show_help = True
                            self.show_map = True
                            self.change_in_display = True
                        if self.maze.random:
                            if self.button_new_rect.collidepoint(mouse_x, mouse_y):
                                self.get_new_level = True
                                self.maze = self.level_module.f()
                                assert isinstance(self.maze, Maze)
                                self.change_in_display = True
                                self.update_possible_actions()
                        if self.button_restart_rect.collidepoint(mouse_x, mouse_y):
                            self.change_in_display = True
                            self.maze.reboot_solution()
                            self.last_key_pressed_time = time()
                            self.current_action = ''
                            self.maze.current_door_page = 0
                            self.update_possible_actions()
                        if self.lower_right_window_rectangle.collidepoint(mouse_x, mouse_y):
                            self.play_click()
                            self.name_tree_list = self.name_tree_list[1:] + self.name_tree_list[:1]
                            self.last_key_pressed_time = time()
                            self.change_in_display = True
                        for iR, room in enumerate(self.maze.rooms_list):
                            rect = self.element_dict[room.name]
                            if room.name == 'RE':
                                if point_in_ellipse(event.pos, rect):
                                    if self.maze.current_room().is_exit:
                                        self.get_next_maze()
                                    else:
                                        self.maze.make_actions('RE')
                                    if self.maze.current_room_index == self.maze.exit_room_index:
                                        self.play_bell()
                                    else:
                                        self.play_footstep()
                                    self.change_in_display = True
                            elif iR == self.maze.current_room_index:
                                continue
                            else:
                                if rect.collidepoint(mouse_x, mouse_y):
                                    if not any([self.element_dict[switch.name].collidepoint(mouse_x, mouse_y) for switch in room.switches_list]):
                                        self.play_footstep()
                                    self.maze.make_actions(room.name)
                                    self.change_in_display = True
                        if not self.level_changed:
                            for door in self.maze.doors_set:
                                polygon = self.element_dict[door.name]
                                if point_in_polygon(event.pos, polygon):
                                    self.maze.make_actions(door.name)
                                    self.change_in_display = True
                                    if self.maze.current_room_index == self.maze.exit_room_index:
                                        self.play_bell()
                                    else:
                                        self.play_footstep()
                            for switch in self.maze.switches_set:
                                rect = self.element_dict[switch.name]
                                if rect.collidepoint(mouse_x, mouse_y):
                                    self.play_click()
                                    self.maze.make_actions(switch.name)
                                    self.change_in_display = True
                    if point_in_polygon(event.pos, self.right_arrow_polygon):
                        self.change_to_next_page()
                    if point_in_polygon(event.pos, self.left_arrow_polygon):
                        self.change_to_previous_page()
        if self.pressed[K_ESCAPE]:
            self.quit_game()
            self.do_you_quit_game = True

    # def update_to_save_images(self):
    #     if self.save_image:
    #         if self.index_current_level != Levels.number_of_levels - 1:
    #             self.index_current_level += 1
    #         else:
    #             if not self.show_help:
    #                 self.show_help = 1
    #                 self.change_in_display = True
    #                 self.index_current_level = 0
    #             else:
    #                 self.quit_game()
    #                 return True
    #         self.level_changed = True
    #     return False

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

    def realign_map_pos(self):
        self.map_pos_x = max(min(self.map_pos_x, self.map_pos_x_max()), self.map_pos_x_min())
        self.map_pos_y = max(min(self.map_pos_y, self.map_pos_y_max()), self.map_pos_y_min())

    def draw_map_edges(self):
        # Affichage des lignes des portes
        color_list = [Color.GREY_100, Color.GREY_120, Color.GREY_140, Color.GREY_160, Color.GREY_180]
        line_size_list = [10, 8, 6, 4, 2]
        for i in range(len(line_size_list)):
            color = color_list[i]
            line_size = line_size_list[i]
            for edge in self.edges_list:
                a = self.dx*(edge[0][0]+self.map_pos_x)
                b = self.dy*(edge[0][1]+self.map_pos_y)
                c = self.dx*(edge[1][0]+self.map_pos_x)
                d = self.dy*(edge[1][1]+self.map_pos_y)
                pygame_draw_line(self.WINDOW, color, [c, d], [a, b], line_size)

    def draw_map_dots(self):
        self.levels_true_positions_dict = {}
        for node in self.level_positions_dict.keys():
            [x, y] = self.level_positions_dict[node]
            # old_x, old_y = x, y
            x = self.dx*(x+self.map_pos_x)-self.dot_radius_x/2
            y = self.dy*(y+self.map_pos_y)-self.dot_radius_y/2
            rect = [x, y, self.dot_radius_x, self.dot_radius_y]
            self.levels_true_positions_dict[node] = rect
            previous_node = '_'.join(node.split('_')[:-1])
            success_previous_node = self.levels_success_list[self.level_number_dict[previous_node]]
            success_node = self.levels_success_list[self.level_number_dict[node]]
            if success_node or self.dev_mode:
                lcolor = self.level_color_dict[node]
            elif node == '' or success_previous_node:
                lcolor = self.level_color_dict[node]
            else:
                lcolor = Levels_colors_list.GREY
            # self.blit_text(f"{round(old_x, 2)} {round(old_y, 2)}", [x, y], max_width=50, color=lcolor.background_color)
            rect_in = [x+self.dot_radius_x/4, y+0.45*self.dot_radius_y, self.dot_radius_x/2, self.dot_radius_y/2]
            pygame_draw_ellipse(self.WINDOW, lcolor.background_color, rect)
            pygame_draw_ellipse(self.WINDOW, lcolor.room_color, rect_in)
            if (success_previous_node or node=='') and not success_node and not self.dev_mode:
                w = 8
                a = (sin(time()*4)+1)/2 # between 0 and 1
                a_min = 0.4
                a_max = 1
                a = a * (a_max-a_min) + a_min
                k = 8
                pygame_draw_ellipse(self.WINDOW, [int(a*255-3*k)]*3, [x-w, y-w, self.dot_radius_x+2*w, self.dot_radius_y+2*w], width=5)
                pygame_draw_ellipse(self.WINDOW, [int(a*255-2*k)]*3, [x-w, y-w, self.dot_radius_x+2*w, self.dot_radius_y+2*w], width=4)
                pygame_draw_ellipse(self.WINDOW, [int(a*255-k)]*3, [x-w, y-w, self.dot_radius_x+2*w, self.dot_radius_y+2*w], width=3)
                pygame_draw_ellipse(self.WINDOW, [int(a*255)]*3, [x-w, y-w, self.dot_radius_x+2*w, self.dot_radius_y+2*w], width=2)
            pygame_draw_ellipse(self.WINDOW, lcolor.surrounding_color, rect_in, width=1)
            pygame_draw_ellipse(self.WINDOW, lcolor.contour_color, [x-1, y-1, self.dot_radius_x+2, self.dot_radius_y+2], width=1)

    def handle_map_events(self):

        for event in pygame_event_get():
            if event.type == QUIT:
                self.do_you_quit_game = True
                self.quit_game()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                assert self.levels_true_positions_dict.keys() == self.levels_dict.keys(
                ), f"{self.levels_true_positions_dict.keys} {self.levels_dict.keys}"
                px, py = event.pos
                d = 6
                if point_in_polygon(event.pos, self.right_arrow_map_button):
                    self.play_footstep()
                    self.map_pos_x += -d
                    break
                if point_in_polygon(event.pos, self.left_arrow_map_button):
                    self.play_footstep()
                    self.map_pos_x += +d
                    break
                if point_in_polygon(event.pos, self.up_arrow_map_button):
                    self.play_footstep()
                    self.map_pos_y += +d
                    break
                if point_in_polygon(event.pos, self.down_arrow_map_button):
                    self.play_footstep()
                    self.map_pos_y += -d
                    break
                if self.menu_rect.collidepoint(px, py):
                    self.player_name_selection = ''
                    self.player_name = None
                if self.volume_rect.collidepoint(px, py):
                    if self.left_volume_button.collidepoint(px, py):
                        self.volume -= self.d_volume
                        self.play_click()
                    if self.right_volume_button.collidepoint(px, py):
                        self.volume += self.d_volume
                        self.play_click()
                    self.volume = min(1, max(0, self.volume))
                    break
                if self.music_volume_rect.collidepoint(px, py):
                    if self.left_music_volume_button.collidepoint(px, py):
                        self.music_volume -= self.d_volume
                        self.play_click()
                    if self.right_music_volume_button.collidepoint(px, py):
                        self.music_volume += self.d_volume
                        self.play_click()
                    self.music_volume = min(1, max(0, self.music_volume))
                    pygame_music.set_volume(self.music_volume*0.3)
                    break
                for node in self.levels_true_positions_dict.keys():
                    previous_node = '_'.join(node.split('_')[:-1])
                    success_previous_node = self.levels_success_list[self.level_number_dict[previous_node]]
                    if success_previous_node or node == '' or self.dev_mode:
                        rect = self.levels_true_positions_dict[node]
                        cx, cy, rx, ry = rect
                        if ((px - cx) ** 2) / (rx ** 2) + ((py - cy) ** 2) / (ry ** 2) <= 1:
                            pygame_draw_ellipse(self.WINDOW, [255, 0, 0], rect)
                            self.level_module = self.levels_dict[node]
                            try:
                                self.maze = self.level_module.f()
                            except:
                                print(self.level_module)
                                raise
                            assert isinstance(self.maze, Maze)
                            self.node = node
                            self.show_map = False
                            self.change_in_display = True
                            self.level_changed = True
                            self.play_click()
                            break
        self.pressed = pygame_key_get_pressed()
        v = 25
        nt = 0.05
        if time() - self.last_key_pressed_time > nt:
            # has_moved = False
            if self.pressed[K_RIGHT] or self.pressed[K_d]:
                # has_moved = True
                self.map_pos_x += -v*nt
            if self.pressed[K_LEFT] or self.pressed[K_q]:
                # has_moved = True
                self.map_pos_x += +v*nt
            if self.pressed[K_UP] or self.pressed[K_z]:
                # has_moved = True
                self.map_pos_y += +v*nt
            if self.pressed[K_DOWN] or self.pressed[K_s]:
                # has_moved = True
                self.map_pos_y += -v*nt
            self.last_key_pressed_time = time()
        if self.pressed[K_ESCAPE]:
            self.quit_game()
            self.do_you_quit_game = True
            
    def draw_menu_button(self):
        xmin = 10
        ymin = 10
        delta_x = 183
        delta_y = 40
        rect = pygame_Rect(xmin,
                           ymin,
                           delta_x,
                           delta_y)
        pygame_draw_rect(self.WINDOW, Color.color_hls(hu=0.15, li=0.1, sa=0.1), rect)
        pygame_draw_rect(self.WINDOW, [255]*3, rect, width=2)
        self.menu_rect = pygame_Rect(xmin,
                                       ymin,
                                       delta_x,
                                       delta_y)
        menu_font_render = self.font.render("Player selection",
                                            True,
                                            [255]*3)
        self.WINDOW.blit(menu_font_render, (xmin+11, ymin+11))

    def draw_volume_button(self):
        ymin = 10
        ymax = 50
        delta_y = ymax-ymin
        delta_x = 3*delta_y
        xmin = self.TOTAL_WIDTH-delta_x-ymin
        rect_0 = pygame_Rect(xmin,
                             ymin,
                             delta_x*self.volume,
                             delta_y)
        rect_1 = pygame_Rect(xmin+delta_x*self.volume,
                             ymin,
                             delta_x*(1-self.volume),
                             delta_y)
        rect_tot = pygame_Rect(xmin,
                               ymin,
                               delta_x,
                               delta_y)
        pygame_draw_rect(self.WINDOW, Color.color_hls(
            hu=0.15, li=0.6, sa=0.1), rect_0)
        pygame_draw_rect(self.WINDOW, Color.color_hls(
            hu=0.15, li=0.1, sa=0.1), rect_1)
        pygame_draw_rect(self.WINDOW, [255]*3, rect_tot, width=2)
        self.left_volume_button = pygame_Rect(xmin,
                                              ymin,
                                              delta_x*0.3,
                                              delta_y)
        self.right_volume_button = pygame_Rect(xmin+delta_x*0.7,
                                               ymin,
                                               delta_x*0.3,
                                               delta_y)
        self.volume_rect = pygame_Rect(xmin,
                                       ymin,
                                       delta_x,
                                       delta_y)
        V_minus = self.font.render("V-",
                                   True,
                                   [16*(16-12)]*3)
        V_plus = self.font.render("V+",
                                  True,
                                  [16*12]*3)
        self.WINDOW.blit(V_minus, (xmin+11, ymin+delta_y/2-9))
        self.WINDOW.blit(V_plus, (self.TOTAL_WIDTH-44, ymin+delta_y/2-9))

    def draw_music_volume_button(self):
        ymin = 55
        ymax = 95
        delta_y = ymax-ymin
        delta_x = 3*delta_y
        xmin = self.TOTAL_WIDTH-delta_x-10
        rect_0 = pygame_Rect(xmin,
                             ymin,
                             delta_x*self.music_volume,
                             delta_y)
        rect_1 = pygame_Rect(xmin+delta_x*self.music_volume,
                             ymin,
                             delta_x*(1-self.music_volume),
                             delta_y)
        rect_tot = pygame_Rect(xmin,
                               ymin,
                               delta_x,
                               delta_y)
        pygame_draw_rect(self.WINDOW, Color.color_hls(
            hu=0.15, li=0.6, sa=0.1), rect_0)
        pygame_draw_rect(self.WINDOW, Color.color_hls(
            hu=0.15, li=0.1, sa=0.1), rect_1)
        pygame_draw_rect(self.WINDOW, [255]*3, rect_tot, width=2)
        self.left_music_volume_button = pygame_Rect(xmin,
                                                    ymin,
                                                    delta_x*0.3,
                                                    delta_y)
        self.right_music_volume_button = pygame_Rect(xmin+delta_x*0.7,
                                                     ymin,
                                                     delta_x*0.3,
                                                     delta_y)
        self.music_volume_rect = pygame_Rect(xmin,
                                             ymin,
                                             delta_x,
                                             delta_y)
        V_minus = self.font.render("M-",
                                   True,
                                   [16*(16-12)]*3)
        V_plus = self.font.render("M+",
                                  True,
                                  [16*12]*3)
        self.WINDOW.blit(V_minus, (xmin+11, ymin+delta_y/2-9))
        self.WINDOW.blit(V_plus, (self.TOTAL_WIDTH-44, ymin+delta_y/2-9))

    def draw_map_arrows_buttons(self):
        x0 = 20
        x1 = 15
        y0 = 20
        y1 = 15
        x = 80
        y = 80
        e = 8
        h = self.TOTAL_HEIGHT
        w = self.TOTAL_WIDTH
        self.left_arrow_map_button = [[e+x0, h/2-y/2],
                                      [e+x1, h/2-y/2],
                                      [e,    h/2],
                                      [e+x1, h/2+y/2],
                                      [e+x0, h/2+y/2]]
        self.right_arrow_map_button = [[w-x, y] for [x, y] in self.left_arrow_map_button]
        self.up_arrow_map_button = [[w/2-x/2, e+y0],
                                    [w/2-x/2, e+y1],
                                    [w/2,     e],
                                    [w/2+x/2, e+y1],
                                    [w/2+x/2, e+y0]]
        self.down_arrow_map_button = [[x, h-y] for [x, y] in self.up_arrow_map_button]
        for poly in [self.left_arrow_map_button,
                     self.right_arrow_map_button,
                     self.up_arrow_map_button,
                     self.down_arrow_map_button
                     ]:
            pygame_draw_polygon(self.WINDOW,
                                Color.color_hls(hu=0.15, li=0.4, sa=0.6),
                                poly)
            pygame_draw_polygon(self.WINDOW,
                                [255]*3,
                                poly,
                                width=2)

    def display_map(self):
        self.WINDOW.fill(Color.color_hls(hu=0.125, li=0.3, sa=0.1))
        self.TOTAL_WIDTH, self.TOTAL_HEIGHT = pygame.display.get_surface().get_size()
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.WINDOW.get_size()
        self.WINDOW_WIDTH = max(self.SMALLEST_WINDOW_SIZE[0], self.WINDOW_WIDTH)
        self.WINDOW_HEIGHT = max(self.SMALLEST_WINDOW_SIZE[1], self.WINDOW_HEIGHT)
        self.font = pygame_font_SysFont(None, self.help_font_size)
        self.realign_map_pos()
        self.draw_map_edges()
        self.draw_map_dots()
        # self.print_map_help()
        self.draw_menu_button()
        self.draw_volume_button()
        self.draw_music_volume_button()
        self.draw_exterior_lines()
        self.draw_map_arrows_buttons()
        self.handle_map_events()
        pygame_display_update()
        
    def create_new_game(self):
        if '/' in self.player_name_selection:
            return
        if '.' in self.player_name_selection:
            return
        if self.player_name_selection == '':
            return
        if os_path_exists(current_folder+'/saved_games/'+self.player_name_selection+'.txt'):
            return
        else:
            self.game_map_setup()
            self.player_name = self.player_name_selection
            with open(current_folder+'/saved_games/'+self.player_name_selection+'.txt', 'w') as fw:
                fw.write('0'*len(Levels.levels_modules_list))
                self.levels_success_list = [0]*len(Levels.levels_modules_list)
                
    def read_level_success(self):
        with open(current_folder+'/saved_games/'+self.player_name+'.txt', 'r') as fr:
            self.levels_success_list = [int(i) for i in fr.readline()]
        
    def handle_event_player_selection(self):
        for event in pygame_event_get():
            if event.type == QUIT:
                self.do_you_quit_game = True
                self.quit_game()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if self.new_game_rect.collidepoint(mouse_x, mouse_y):
                    self.create_new_game()
                if self.selection_rect.collidepoint(mouse_x, mouse_y):
                    self.create_new_game()
                for saved_game_name in self.saved_games_rect_dict.keys():
                    rect = self.saved_games_rect_dict[saved_game_name]
                    if rect.collidepoint(mouse_x, mouse_y):
                        self.game_map_setup()
                        self.player_name = saved_game_name
                        self.read_level_success()
            if time() - self.last_key_pressed_time > self.time_between_actions:
                self.pressed = pygame_key_get_pressed()
                for key in Game.keys_dict.keys():
                    if self.pressed[key] and not Game.keys_dict[key] in [' ', '/', '.']:
                        self.player_name_selection += Game.keys_dict[key]
                if self.pressed[K_BACKSPACE]:
                    self.player_name_selection = self.player_name_selection[:-1]
                if self.pressed[K_RETURN]:
                    self.create_new_game()
                self.last_key_pressed_time = time()
            if self.pressed[K_ESCAPE]:
                self.quit_game()
                self.do_you_quit_game = True
                
    def draw_player_selection_rectangles(self):
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT
        self.draw_exterior_lines()
        c = Color.color_hls(hu=0.15, li=0.5, sa=1)
        # NEW GAME
        new_game_surface = self.font.render("NEW GAME",
                                            True,
                                            [0]*3)
        new_game_word_width, new_game_word_height = new_game_surface.get_size()
        # SAVED
        self.saved_games_surfaces_dict = {}
        for file_name in os_listdir(current_folder+'/saved_games'):
            file_name = 'saved_games/'+file_name
            if file_name.split('.')[-1] == 'txt':
                surface = self.font.render(file_name,
                                           True,
                                           [0]*3)
                self.saved_games_surfaces_dict[file_name] = surface
        n = len(self.saved_games_surfaces_dict.keys())+0.1
        total_word_height = (new_game_word_height+15)*n
        y0 = self.WINDOW_HEIGHT/2-total_word_height/2
        # NEW GAME
        self.new_game_rect = pygame_Rect(self.WINDOW_WIDTH/4,
                                         y0,
                                         new_game_word_width+10,
                                         new_game_word_height+7)
        pygame_draw_rect(self.WINDOW, [255]*3, self.new_game_rect)
        pygame_draw_rect(self.WINDOW, c, self.new_game_rect, width=2)
        self.WINDOW.blit(new_game_surface, (self.WINDOW_WIDTH/4+4, y0+4))
        # SAVED
        max_txt_width = new_game_word_width
        self.saved_games_rect_dict = {}
        for i, saved_game_name in enumerate(sorted(self.saved_games_surfaces_dict.keys())):
            i = i+1.1
            saved_game_name = saved_game_name.replace('saved_games/', '').split('.')[0]
            saved_game_surface = self.font.render(saved_game_name,
                                                  True,
                                                  [0]*3)
            word_width, word_height = saved_game_surface.get_size()
            max_txt_width = max(max_txt_width, word_width)
            saved_game_rect = pygame_Rect(self.WINDOW_WIDTH/4,
                                          y0+i*(new_game_word_height+15),
                                          word_width+10,
                                          word_height+7)
            self.saved_games_rect_dict[saved_game_name] = saved_game_rect
            pygame_draw_rect(self.WINDOW, [200]*3, saved_game_rect)
            pygame_draw_rect(self.WINDOW, c, saved_game_rect, width=2)
            self.WINDOW.blit(saved_game_surface, (self.WINDOW_WIDTH/4+4, y0+i*(new_game_word_height+15)+4))
        # SELECTION
        dt_blink = 1
        selection_surface = self.font.render(self.player_name_selection+'_',
                                             True,
                                             [0]*3)
        selection_word_width, selection_word_height = selection_surface.get_size()
        if time()%dt_blink > dt_blink/2:
            selection_surface = self.font.render(self.player_name_selection,
                                                 True,
                                                 [0]*3)        
        
        self.selection_rect = pygame_Rect(self.WINDOW_WIDTH/4+max_txt_width+20,
                                          y0,
                                          selection_word_width+10,
                                          new_game_word_height+7)
        pygame_draw_rect(self.WINDOW, [255]*3, self.selection_rect)
        pygame_draw_rect(self.WINDOW, c, self.selection_rect, width=2)
        self.WINDOW.blit(selection_surface, (self.WINDOW_WIDTH/4+max_txt_width+20+4, y0+4))
        # ENTER YOUR NAME
        enter_your_name_surface = self.font.render('ENTER YOUR NAME',
                                                   True,
                                                   [0]*3)
        word_width, word_height = enter_your_name_surface.get_size()
        enter_your_name_rect = pygame_Rect(self.WINDOW_WIDTH/4+max_txt_width+20,
                                           y0-new_game_word_height-20,
                                           word_width+10,
                                           new_game_word_height+7)
        pygame_draw_rect(self.WINDOW, [255]*3, enter_your_name_rect)
        pygame_draw_rect(self.WINDOW, c, enter_your_name_rect, width=2)
        self.WINDOW.blit(enter_your_name_surface, (self.WINDOW_WIDTH/4+max_txt_width+23,
                                                   y0-new_game_word_height-15,
                                                   selection_word_width+10,
                                                   new_game_word_height+7))
        
    def display_player_selection(self):
        self.WINDOW.fill(Color.color_hls(hu=0.12, li=0.3, sa=0.25))
        self.TOTAL_WIDTH, self.TOTAL_HEIGHT = pygame.display.get_surface().get_size()
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.WINDOW.get_size()
        self.WINDOW_WIDTH = max(self.SMALLEST_WINDOW_SIZE[0], self.WINDOW_WIDTH)
        self.WINDOW_HEIGHT = max(self.SMALLEST_WINDOW_SIZE[1], self.WINDOW_HEIGHT)
        self.font = pygame_font_SysFont(None, 40)
        self.handle_event_player_selection()
        self.draw_player_selection_rectangles()
        pygame_display_update()

    def play(self):  # The main function that controls the game
        self.t0 = time()
        self.game_setup()
        while self.looping:
            sleep(self.sleep_time)  # I did that not to use too much CPU
            if self.show_map:
                if self.player_name is None:
                    self.display_player_selection()
                else:
                    self.display_map()
                    self.update_map_window_size()
            else:
                self.handle_events()
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
                # if self.update_to_save_images():  # It means you quit the game
                #     return None
                if self.player_name is None:
                    self.show_map = True
            if self.do_you_quit_game:
                return None

    def play_level(self):
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
        self.handle_events()
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
