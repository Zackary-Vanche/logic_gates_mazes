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

from fonction_affine import fonction_affine
from Maze import Maze
from Levels import Levels


class Game:

    # gestion de l'affichage

    def save_levels_txt(verbose=0, calculates_solutions=True):
        t0 = time()
        Maze.calculates_solutions = calculates_solutions
        if not os_path_exists('mazes'):
            os_mkdir('mazes')
        for k in range(len(Levels.levels_list)):
            level = Levels.levels_list[k]()
            if level.fastest_solution is not None:
                level.save_txt(title_header='mazes/Level_{}'.format(k))
                level.save_txt_short(title_header='mazes/L{}'.format(k))
            else:
                print(level.name, 'TODO')
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')

    def save_solutions_txt(verbose=0):
        t0 = time()
        txt = ''
        calculations_times = []
        if not os_path_exists('mazes'):
            os_mkdir('mazes')
        for k in range(len(Levels.levels_list)):
            level = Levels.levels_list[k]()
            print('')
            name = level.name
            print(name)
            txt += name + '\n'
            t2 = time()
            solutions = level.find_all_solutions(stop_at_first_solution=False,
                                                 verbose=0)
            t3 = time()
            for sol in solutions:
                print(sol)
                txt += sol + '\n'
            if verbose >= 1:
                print(t3 - t2, 's')
                calculations_times.append(t3 - t2)
            txt += '\n'
        with open('mazes/solutions.txt', 'w') as f:
            f.write(txt)
        t1 = time()
        if verbose >= 1:
            print(t1 - t0, 's')
        return calculations_times

    # def print_level_list(WINDOW, WINDOW_WIDTH, WINDOW_HEIGHT):
    #     WINDOW.blit(img_score_left, (WINDOW_WIDTH // 2 - 30, 20))

    # The main function that controls the game
    def play(WINDOW_SIZE=(1366-20, 768-100),
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
             index_help_page=0):

        pygame_init()

        looping = True

        # Game Setup
        # FPS = 60
        # fpsClock = pygame.time.Clock()
        TOTAL_WIDTH, TOTAL_HEIGHT = WINDOW_SIZE
        # TOTAL_WIDTH, TOTAL_HEIGHT = 1366, 1024
        X_marge, Y_marge = XY_marge
        WINDOW_WIDTH = TOTAL_WIDTH - X_marge
        WINDOW_HEIGHT = TOTAL_HEIGHT - Y_marge

        WINDOW = pygame_display_set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                         pygame_RESIZABLE,
                                         pygame_SCALED)
        # WINDOW = pygame_display_set_mode((0, 0), pygame.FULLSCREEN)
        pygame_display_set_caption('Logic gates maze')

        WINDOW_SIZE_changed = True

        font = pygame_font_SysFont(None, 25)
        # font = pygame_font_SysFont('microsofthimalaya', 27)
        # Ligne à decommenter si on choisi de pouvoir changer de font
        # n_font = -1

        level_changed = True
        # Cette variable vaut True quand le joueur
        # vient de choisir de changer de niveau
        # ou au début du jeu (il faut initialiser le niveau)
        last_level_change_time = time()

        click_rect_size = 40

        if save_image:
            if not os_path_exists('images'):
                os_mkdir('images')

        current_action = ''
        last_key_pressed_time = time()
        last_key_BACKSPACE_pressed_time = time()
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

        # The main game loop
        # number_of_loops = 0
        while looping:

            # number_of_loops += 1
            # Get inputs
            for event in pygame_event_get():
                if event.type == QUIT:
                    # print(number_of_loops)
                    pygame_quit()
                    return None

            # Processing
            # La moitie du processing se fait ici
            # et la moitie plus loin dans le code
            # utiliser level_changed
            # Creation de la variable du niveau
            if level_changed:

                level_changed = False
                maze = Levels.levels_list[index_current_level]()
                maze.reboot_solution()
                
                doors_list = maze.doors_list()
                
                level_colors = maze.level_color
                background_color = level_colors.background_color
                room_color = level_colors.room_color
                contour_color = level_colors.contour_color
                letters_color = level_colors.letters_color
                # letter_contour_color = maze.letter_contour_color
                inside_room_color = level_colors.inside_room_color
                surrounding_color = level_colors.surrounding_color

                y_separation = maze.y_separation
                door_window_size = maze.door_window_size

                x_separation = WINDOW_WIDTH - door_window_size
                current_action = ''
                keep_proportions = maze.keep_proportions

                # Choix de la bordure en fonction de la hauteur de la fenêtre
                (pente, coeff) = fonction_affine(643, 35, 1080, 75)
                maze.set_extreme_coordinates(0,
                                             x_separation,
                                             0,
                                             WINDOW_HEIGHT,
                                             pente*WINDOW_HEIGHT+coeff,
                                             keep_proportions)

            if WINDOW_SIZE_changed:

                y_separation = maze.y_separation
                door_window_size = maze.door_window_size

                x_separation = WINDOW_WIDTH - door_window_size
                current_action = ''
                keep_proportions = maze.keep_proportions

                # Choix de la bordure en fonction de la hauteur de la fenêtre
                (pente, coeff) = fonction_affine(643, 35, 1080, 75)
                maze.set_extreme_coordinates(0,
                                             x_separation,
                                             0,
                                             WINDOW_HEIGHT,
                                             pente*WINDOW_HEIGHT+coeff,
                                             keep_proportions)

                WINDOW_SIZE_changed = False

            # print(WINDOW.get_size())

            if (WINDOW_WIDTH, WINDOW_HEIGHT) != WINDOW.get_size():
                WINDOW_SIZE_changed = True
                WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW.get_size()
                WINDOW_WIDTH = max(SMALLEST_WINDOW_SIZE[0], WINDOW_WIDTH)
                WINDOW_HEIGHT = max(SMALLEST_WINDOW_SIZE[1], WINDOW_HEIGHT)

            # Render elements of the game
            WINDOW.fill(background_color)

            pressed = pygame_key_get_pressed()

            if show_help:
                # Bords exterieurs
                l = 4 # Largeur des bords exterieurs
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, 0),
                                 (0, WINDOW_HEIGHT),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (WINDOW_WIDTH, 0),
                                 (WINDOW_WIDTH, WINDOW_HEIGHT),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, 0),
                                 (WINDOW_WIDTH, 0),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, WINDOW_HEIGHT),
                                 (WINDOW_WIDTH, WINDOW_HEIGHT),
                                 l+2)
                # Affichage du nom du niveau courant
                level_name_render = font.render('HELP - Level ' + str(index_current_level) + ' : ' + maze.name.replace('_', ' '), 
                                                True,
                                                letters_color)
                WINDOW.blit(level_name_render, (10, 10))
                # Gestion du clavier
                # if time() - last_key_pressed_time > time_between_actions:
                #     if (pressed[K_UP]):
                #         index_help_page += 1
                #         last_key_pressed_time = time()
                #     if (pressed[K_DOWN]):
                #         index_help_page -= 1
                #         last_key_pressed_time = time()
                index_help_page = index_help_page % maze.n_help_pages
                string_help = maze.help_txt[index_help_page]
                gap = 0
                help_list = string_help.split('\n')
                p, c = fonction_affine(768-Y_marge, 50, 1080-Y_marge, 50)
                y0 = p*WINDOW_HEIGHT + c
                p, c = fonction_affine(1366-X_marge, 50, 1920-X_marge, 50)
                x0 = p*WINDOW_WIDTH + c
                for line in help_list:
                    WINDOW.blit(font.render(line,
                                True,
                                letters_color),
                                (x0, y0 + gap))
                    if line.replace(' ', '') == '':
                        gap += 15
                    else:
                        gap += 20

                pygame_display_update()

                if save_image:
                    fname = "images/HELP_level_{}_{}_WIDTH_{}_HEIGHT_{}.png".format(index_current_level,
                                                                                    maze.name,
                                                                                    WINDOW_WIDTH,
                                                                                    WINDOW_HEIGHT)
                    if not os_path_exists(fname):
                        print(fname)
                        pygame_image_save(WINDOW, fname)

            else:
                # Affichage de la fenêtre de droite
                right_window_rectangle = pygame_Rect(x_separation,
                                                     0,
                                                     door_window_size,
                                                     WINDOW_HEIGHT)
                pygame_draw_rect(WINDOW, room_color, right_window_rectangle)

                # Bords exterieurs
                l = 5 # Largeur des bords exterieurs
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, 0),
                                 (0, WINDOW_HEIGHT),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (WINDOW_WIDTH, 0),
                                 (WINDOW_WIDTH, WINDOW_HEIGHT),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, 0),
                                 (WINDOW_WIDTH, 0),
                                 l+2)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (0, WINDOW_HEIGHT),
                                 (WINDOW_WIDTH, WINDOW_HEIGHT),
                                 l+2)

                # Séparation des différentes fenetres
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (x_separation, 0),
                                 (x_separation, WINDOW_HEIGHT),
                                 3)
                pygame_draw_line(WINDOW,
                                 contour_color,
                                 (x_separation, y_separation),
                                 (WINDOW_WIDTH, y_separation),
                                 3)

                # Affichage du nom du niveau courant
                level_name_render = font.render('Level ' + str(index_current_level) + ' : ' + maze.name.replace('_', ' '),
                                                True,
                                                letters_color)
                WINDOW.blit(level_name_render, (10, 10))

                # Gestion des actions
                if maze.current_room_index == maze.exit_room_index:
                    current_action = 'YOU WON !'

                current_action_render = font.render(current_action,
                                                    True,
                                                    inside_room_color)
                WINDOW.blit(current_action_render,
                            (x_separation + 20, y_separation/2-7))

                # Affichage des arbres des portes
                if print_tree_polygon:
                    pass
                else:
                    gap = y_separation + 10
                    WINDOW.blit(font.render('DOORS :',
                                            True,
                                            inside_room_color),
                                (x_separation + 10, gap))
                    gap = y_separation + 45
                    for k in range(len(doors_list)):
                        door = doors_list[k]
                        tree = door.tree
                        str_logical_expression = tree.get_easy_logical_expression_PN()
                        str_logical_expression = str_logical_expression.split('\n')
                        # if k == 0:
                        #     print('')
                        for i in range(len(str_logical_expression)):
                            string = str_logical_expression[i]
                            if i == 0:
                                logical_expression_render = font.render(door.name + ' = ' + string,
                                                                        True,
                                                                        inside_room_color)
                                WINDOW.blit(logical_expression_render, (x_separation + 10, gap))
                            else:
                                logical_expression_render = font.render(' '*(len(door.name)+3) + string,
                                                                        True,
                                                                        inside_room_color)
                                WINDOW.blit(logical_expression_render, (x_separation + 10, gap))
                            gap += 28
                            # print(door.name + ' = ' + string)

                # Affichage des lignes des portes
                for door in maze.doors_set:
                    real_departure_coordinates = door.real_departure_coordinates
                    real_arrival_coordinates = door.real_arrival_coordinates
                    pygame_draw_line(WINDOW,
                                     room_color,
                                     real_departure_coordinates,
                                     real_arrival_coordinates,
                                     3)

                # Affichage des pieces
                for room in maze.rooms_list:
                    [x_gap, y_gap, x, y] = array(room.position)
                    room_rectangle = pygame_Rect(x_gap, y_gap, x, y)
                    if room.is_exit:
                        pygame_draw_ellipse(WINDOW, room_color, room_rectangle)
                        room_name_render = font.render('EXIT',
                                                       True,
                                                       inside_room_color)
                        WINDOW.blit(room_name_render, room.get_name_position())
                        if maze.current_room() == room:
                            pygame_draw_ellipse(WINDOW, surrounding_color, room_rectangle, width=3)
                    else:
                        pygame_draw_rect(WINDOW, room_color, room_rectangle)
                        if maze.current_room() == room:
                            pygame_draw_rect(WINDOW, surrounding_color, room_rectangle, width=3)
                        room_name_render = font.render(room.name,
                                                       True,
                                                       inside_room_color)
                        if print_room_name:
                            WINDOW.blit(room_name_render, room.get_name_position())

                # Affichage des polygones des portes
                for door in maze.doors_set:
                    real_middle_coordinates = door.real_middle_coordinates
                    arrow_coordinates = door.arrow_coordinates
                    pygame_draw_polygon(WINDOW,
                                        room_color,
                                        arrow_coordinates)
                    # rect = pygame_Rect(real_middle_coordinates[0]-click_rect_size/2,
                    #                    real_middle_coordinates[1]-click_rect_size/2,
                    #                    click_rect_size,
                    #                    click_rect_size)
                    # if print_click_rects:
                    #     pygame_draw_rect(WINDOW,
                    #                      background_color,
                    #                      rect)
                for door in maze.doors_set:
                    arrow_coordinates = door.arrow_coordinates
                    if door.is_open:
                        pygame_draw_polygon(WINDOW,
                                            surrounding_color,
                                            arrow_coordinates,
                                            width=3)

                # Affichage des portes
                for door in maze.doors_set:
                    real_middle_coordinates = door.real_middle_coordinates
                    door_name_render = font.render(door.name,
                                                   True,
                                                   inside_room_color)
                    WINDOW.blit(door_name_render,
                                real_middle_coordinates)

                # Affichage des interrupteurs
                for room in maze.rooms_list:
                    switches_positions = room.get_switches_positions()
                    switches_list = room.switches_list
                    assert len(switches_positions) == len(switches_list)
                    for i in range(len(switches_list)):
                        switch = switches_list[i]
                        position = switches_positions[i]
                        rect = pygame_Rect(position[0]-click_rect_size/2,
                                           position[1]-click_rect_size/2,
                                           click_rect_size,
                                           click_rect_size)
                        if print_click_rects:
                            pygame_draw_rect(WINDOW,
                                             background_color,
                                             rect)
                        if switch.value:
                            rectangle_switch = pygame_Rect(position[0]-click_rect_size/2,
                                                           position[1]-click_rect_size/2,
                                                           click_rect_size,
                                                           click_rect_size)
                            pygame_draw_rect(WINDOW,
                                             surrounding_color,
                                             rectangle_switch,
                                             width = 3)
                        if print_click_rects:
                            switch_name_render = font.render(switch.name,
                                                             True,
                                                             letters_color)
                        else:
                            switch_name_render = font.render(switch.name,
                                                             True,
                                                             inside_room_color)
                        WINDOW.blit(switch_name_render,
                                    position - array([11/2*len(switch.name), 8]))

                if time() - last_key_pressed_time > time_between_actions:
                    pressed = pygame_key_get_pressed()
                    for key in keys_dict.keys():
                        if pressed[key]:
                            current_action = current_action + keys_dict[key]
                            last_key_pressed_time = time()
                    if pressed[K_RETURN]:
                        if len(current_action) > 0:
                            if current_action[0] == 'D' or current_action[0] == 'S':
                                maze.make_actions(current_action)
                            if current_action[0:2] == 'A ':
                                maze.make_actions(current_action[2:], allow_all=True)
                            if current_action[0] == 'A':
                                maze.make_actions(current_action[1:], allow_all=True)
                            elif current_action[0] == 'L':
                                level_number_list = [str(i) for i in range(Levels.number_of_levels)]
                                if current_action[1:] in level_number_list:
                                    index_current_level = int(current_action[1:])
                                    level_changed = True
                            current_action = ''
                    if pressed[K_b]:
                        maze.reboot_solution()
                        last_key_pressed_time = time()
                        current_action = ''
                    # if pressed[K_n]:
                    #     easy_notation = not easy_notation
                    #     last_key_pressed_time = time()
                if time() - last_key_BACKSPACE_pressed_time > time_between_deletings:
                    if pressed[K_BACKSPACE]:
                        current_action = current_action[:-1]
                        last_key_BACKSPACE_pressed_time = time()

                pygame_display_update()

                if save_image:
                    fname = "images/level_{}_{}_WIDTH_{}_HEIGHT_{}.png".format(index_current_level,
                                                                               maze.name,
                                                                               WINDOW_WIDTH,
                                                                               WINDOW_HEIGHT)
                    if not os_path_exists(fname):
                        print(fname)
                        pygame_image_save(WINDOW, fname)

            # Changement de niveau
            # pressed = pygame_key_get_pressed()
            if pressed[K_q] or pressed[K_ESCAPE]:
                pygame_quit()
                return None
            if time() - last_level_change_time > time_between_actions:
                if (pressed[K_RIGHT]):
                    index_current_level += 1
                    level_changed = True
                if (pressed[K_LEFT]):
                    index_current_level -= 1
                    level_changed = True
                if (pressed[K_UP]):
                    index_current_level = len(Levels.levels_list)-1
                    level_changed = True
                if (pressed[K_DOWN]):
                    index_current_level = 0
                    level_changed = True
            if level_changed:
                last_level_change_time = time()
            index_current_level = min(index_current_level,
                                      len(Levels.levels_list)-1)
            index_current_level = max(index_current_level,
                                      0)

            # Passage au menu d'aide / quitter le menu aide
            if time() - last_key_pressed_time > time_between_actions:
                if pressed[K_h]:
                    show_help = not show_help
                    last_key_pressed_time = time()

            # fpsClock.tick(FPS)
            
if __name__ == "__main__":
    
    Game.save_levels_txt(verbose = 0, calculates_solutions = False)
