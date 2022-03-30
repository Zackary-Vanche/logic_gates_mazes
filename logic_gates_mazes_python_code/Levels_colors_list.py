# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:50:57 2022

@author: utilisateur
"""

from Color import Color
from Level_color import Level_color

class Levels_colors_list:
    
    BEIGE = Level_color(background_color = Color.DARK_KHAKI,
                        room_color = Color.KHAKI,
                        contour_color = Color.WHITE,
                        letters_color = Color.WHITE,
                        inside_room_color = Color.BLACK,
                        letter_contour_color = Color.BLACK)
    
    BLACK_AND_WHITE = Level_color(background_color = Color.GREY_100,
                                  room_color = Color.BLACK,
                                  contour_color = Color.BRIGHT_RED,
                                  letters_color = Color.WHITE,
                                  inside_room_color = Color.WHITE,
                                  letter_contour_color = Color.BLACK,
                                  surrounding_color = Color.BRIGHT_RED)
    
    BLACK_AND_WHITE_2 = Level_color(background_color = Color.BLACK,
                                    room_color = Color.WHITE,
                                    contour_color = Color.BRIGHT_RED,
                                    letters_color = Color.WHITE,
                                    inside_room_color = Color.BLACK,
                                    letter_contour_color = Color.WHITE,
                                    surrounding_color = Color.BRIGHT_RED)
    
    BLACK_AND_YELLOW = Level_color(background_color = Color.BLACK_BLUE,
                                  room_color = Color.PALE_YELLOW,
                                  contour_color = Color.RED,
                                  letters_color = Color.WHITE,
                                  letter_contour_color = Color.BLACK,
                                  inside_room_color = Color.BLACK,
                                  surrounding_color = Color.BRIGHT_RED)
    
    BLACK_AND_BLUE = Level_color(background_color = Color.GREY_100,
                                 room_color = Color.BLACK,
                                 contour_color = Color.PURE_BLUE,
                                 letters_color = Color.WHITE,
                                 letter_contour_color = Color.BLACK,
                                 inside_room_color = Color.PURE_BLUE,
                                 surrounding_color = Color.PURE_BLUE)
    
    BLUE_GREEN = Level_color(background_color = Color.DARK_BLUE_GREEN,
                             room_color = Color.BLUE_GREEN,
                             contour_color = Color.DARK_GREY,
                             letters_color = Color.BLACK_RED,
                             letter_contour_color = Color.DARK_GREY,
                             inside_room_color = Color.BLACK_RED,
                             surrounding_color = Color.BLACK_RED)
    
    BRIGHT_BLUE = Level_color(background_color = Color.REALLY_BRIGHT_BLUE,
                              room_color = Color.REALLY_BRIGHT_BLUE_2,
                              contour_color = Color.BLACK_RED,
                              letters_color = Color.BLACK_RED,
                              letter_contour_color = Color.BLACK_RED)
    
    BRIGHT_GREEN = Level_color(background_color = Color.BRIGHT_GREEN,
                               room_color = Color.REALLY_BRIGHT_GREEN,
                               contour_color = Color.BLACK,
                               letters_color = Color.BLACK,
                               letter_contour_color = Color.BLACK)
    
    BRIGHT_RED = Level_color(background_color = Color.DARK_RED,
                             room_color = Color.RED,
                             contour_color = Color.WHITE,
                             surrounding_color = Color.WHITE,
                             letters_color = Color.WHITE,
                             letter_contour_color = Color.BLACK)
    
    BROWN = Level_color(Color.DARK_BROWN,
                        room_color = Color.ORANGE,
                        contour_color = Color.WHITE,
                        letters_color = Color.WHITE,
                        letter_contour_color = Color.BLACK)
    
    DARK_BLUE = Level_color(background_color = Color.REALLY_DARK_BLUE,
                            room_color = Color.DARK_BLUE,
                            contour_color = Color.WHITE,
                            letters_color = Color.WHITE,
                            letter_contour_color = Color.BLACK)
    
    DARK_GREEN = Level_color(background_color = Color.DARK_GREEN,
                             room_color = Color.GREEN,
                             contour_color = Color.WHITE,
                             letters_color = Color.WHITE,
                             letter_contour_color = Color.WHITE)
    
    DARK_RED = Level_color(background_color = Color.REALLY_DARK_RED,
                           room_color = Color.BLACK,
                           contour_color = Color.WHITE,
                           surrounding_color = Color.WHITE,
                           letters_color = Color.WHITE,
                           letter_contour_color = Color.BLACK)
    
    GOLD_AND_SILVER = Level_color(background_color = Color.SILVER,
                                  room_color = Color.YELLOW,
                                  contour_color = Color.BLACK,
                                  letters_color = Color.BLACK,
                                  letter_contour_color = Color.DARK_GREY,
                                  inside_room_color = Color.BLACK,
                                  surrounding_color = Color.BLACK)
    
    GREEN_GREY = Level_color(background_color = Color.GREEN_GREY,
                             room_color = Color.REALLY_BRIGHT_GREEN,
                             contour_color = Color.BLACK,
                             letters_color = Color.BLACK,
                             letter_contour_color = Color.BLACK)
    
    GREY = Level_color(background_color = Color.GREY_100,
                       room_color = Color.DARK_GREY,
                       contour_color = Color.WHITE,
                       letters_color = Color.WHITE,
                       letter_contour_color = Color.BLACK,
                       inside_room_color = Color.WHITE,
                       surrounding_color = Color.WHITE)
    
    PINK = Level_color(background_color = Color.PINK,
                       room_color = Color.BRIGHT_PINK,
                       contour_color = Color.BLACK,
                       letters_color = Color.BLACK,
                       letter_contour_color = Color.WHITE)
    
    PURPLE = Level_color(background_color = Color.DARK_PURPLE,
                         room_color = Color.BRIGHT_PURPLE,
                         contour_color = Color.WHITE,
                         letters_color = Color.WHITE,
                         letter_contour_color = Color.DARK_PURPLE)
    
    PURPLE_BLUE = Level_color(background_color = Color.PURPLE_BLUE,
                              room_color = Color.DARK_PURPLE_BLUE,
                              contour_color = Color.WHITE,
                              letters_color = Color.WHITE,
                              inside_room_color = Color.WHITE,
                              surrounding_color = Color.WHITE,
                              letter_contour_color = Color.DARK_PURPLE_BLUE)
    
    RED_AND_ORANGE = Level_color(background_color = Color.DARK_RED,
                                 room_color = Color.ORANGE,
                                 contour_color = Color.WHITE,
                                 letters_color = Color.WHITE,
                                 inside_room_color = Color.WHITE,
                                 letter_contour_color = Color.BLACK)
    
    SALMON_AND_GREY = Level_color(background_color = Color.GREY,
                                  room_color = Color.SALMON,
                                  contour_color = Color.BLACK,
                                  letters_color = Color.BLACK,
                                  letter_contour_color = Color.WHITE)
    
    YELLOW = Level_color(background_color = Color.DARK_YELLOW,
                         room_color = Color.BRIGHT_YELLOW,
                         contour_color = Color.BLACK,
                         letters_color = Color.BLACK,
                         letter_contour_color = Color.BLACK)
    
    

    