from Color import Color
from Level_color import Level_color


class Levels_colors_list:
    
    def FROM_HUE(hu, sa=0.5, li=0.3):
        
        if li < 0.5:
            inside_room_color = Color.WHITE
        else:
            inside_room_color = Color.BLACK
            
        if li < 0.6:
            contour_color = Color.color_hls(hu, li=0.9, sa=1)
            surrounding_color = Color.color_hls(hu, li=0.9, sa=1)
        else:
            contour_color = Color.color_hls(hu, li=0.1, sa=1)
            surrounding_color = Color.color_hls(hu, li=0.1, sa=1)
            
        return Level_color(background_color=Color.color_hls(hu, li / 4, 0.8 * sa),
                           room_color=Color.color_hls(hu, li, sa),
                           letters_color=Color.WHITE,
                           contour_color=contour_color,
                           inside_room_color=inside_room_color,
                           surrounding_color=surrounding_color)
    
    def FROM_HUE_light_background(hu, sa=0.5, li=0.3):
        
        if li < 0.5:
            inside_room_color = Color.WHITE
        else:
            inside_room_color = Color.BLACK
            
        if li < 0.6:
            contour_color = Color.color_hls(hu, li=0.9, sa=1)
            surrounding_color = Color.color_hls(hu, li=0.9, sa=1)
        else:
            contour_color = Color.color_hls(hu, li=0.1, sa=1)
            surrounding_color = Color.color_hls(hu, li=0.1, sa=1)
            
        background_li = li*3
        if background_li < 0.5:
            letters_color=Color.WHITE
        else:
            letters_color=Color.BLACK
            
        return Level_color(background_color=Color.color_hls(hu, background_li, 0.8 * sa),
                           room_color=Color.color_hls(hu, li, sa),
                           letters_color=letters_color,
                           contour_color=contour_color,
                           inside_room_color=inside_room_color,
                           surrounding_color=surrounding_color)

    def RANDOM():
        from random import random
        return Levels_colors_list.FROM_HUE(random())
    
    
    GREY = FROM_HUE_light_background(hu=0, sa=0, li=0.1)
    
    BEIGE = Level_color(background_color=Color.KHAKI,
                        room_color=Color.DARK_KHAKI,
                        contour_color=Color.WHITE,
                        letters_color=Color.BLACK,
                        inside_room_color=Color.WHITE,
                        letter_contour_color=Color.WHITE)

    BLACK = Level_color(background_color=Color.GREY_60,
                        room_color=Color.BLACK,
                        contour_color=Color.WHITE,
                        letters_color=Color.WHITE,
                        inside_room_color=Color.WHITE,
                        letter_contour_color=Color.BLACK,
                        surrounding_color=Color.WHITE)

    BLACK_AND_ORANGE = Level_color(background_color=Color.BLACK,
                                   room_color=Color.BRIGHT_ORANGE,
                                   contour_color=Color.WHITE,
                                   letters_color=Color.REALLY_BRIGHT_ORANGE,
                                   inside_room_color=Color.BLACK,
                                   surrounding_color=Color.WHITE)

    BLACK_AND_RED = Level_color(background_color=Color.BLACK,
                                room_color=Color.RED,
                                contour_color=Color.BLACK,
                                letters_color=Color.WHITE,
                                inside_room_color=Color.BLACK,
                                surrounding_color=Color.WHITE,
                                inside_room_surrounding_color=Color.BLACK)

    BLACK_AND_WHITE_RED_CONTOUR = Level_color(background_color=Color.BLACK,
                                              room_color=Color.WHITE,
                                              contour_color=Color.BRIGHT_RED,
                                              letters_color=Color.WHITE,
                                              inside_room_color=Color.BLACK,
                                              letter_contour_color=Color.WHITE,
                                              surrounding_color=Color.BRIGHT_RED)

    BLUE_GREEN = Level_color(background_color=Color.DARK_BLUE_GREEN,
                             room_color=Color.BLUE_GREEN,
                             contour_color=Color.DARK_GREY,
                             letters_color=Color.BLACK_RED,
                             letter_contour_color=Color.DARK_GREY,
                             inside_room_color=Color.BLACK_RED,
                             surrounding_color=Color.BLACK_RED)

    BRIGHT_BLUE = Level_color(background_color=Color.REALLY_BRIGHT_BLUE,
                              room_color=Color.REALLY_BRIGHT_BLUE_2,
                              contour_color=Color.BLACK_RED,
                              letters_color=Color.BLACK_RED,
                              letter_contour_color=Color.BLACK_RED)

    BRIGHT_AND_DARK_BLUE = Level_color(background_color=Color.REALLY_DARK_BLUE,
                                       room_color=Color.REALLY_BRIGHT_BLUE,
                                       contour_color=Color.WHITE,
                                       letters_color=Color.WHITE,
                                       inside_room_color=Color.BLACK)

    BRIGHT_GREEN = Level_color(background_color=Color.BRIGHT_GREEN,
                               room_color=Color.REALLY_BRIGHT_GREEN,
                               contour_color=Color.BLACK,
                               letters_color=Color.BLACK,
                               letter_contour_color=Color.BLACK)

    BRIGHT_RED = Level_color(background_color=Color.DARK_RED,
                             room_color=Color.RED,
                             contour_color=Color.WHITE,
                             surrounding_color=Color.WHITE,
                             letters_color=Color.WHITE,
                             letter_contour_color=Color.BLACK)

    DARK_RED = Level_color(background_color=Color.REALLY_DARK_RED,
                           room_color=Color.BLACK,
                           contour_color=Color.WHITE,
                           surrounding_color=Color.WHITE,
                           letters_color=Color.WHITE,
                           letter_contour_color=Color.BLACK)

    FOUR_COLORS = Level_color(background_color=Color.BLUE,
                              room_color=Color.GREEN,
                              contour_color=Color.RED,
                              letters_color=Color.BLACK,
                              inside_room_color=Color.BLACK)

    GOLD_AND_SILVER = Level_color(background_color=Color.SILVER,
                                  room_color=Color.color_hls(hu=0.15, li=0.3, sa=0.6),
                                  contour_color=Color.BLACK,
                                  letters_color=Color.BLACK,
                                  letter_contour_color=Color.DARK_GREY,
                                  inside_room_color=Color.BLACK,
                                  surrounding_color=Color.BLACK)

    GREEN_GREY = Level_color(background_color=Color.GREEN_GREY,
                             room_color=Color.REALLY_BRIGHT_GREEN,
                             contour_color=Color.BLACK,
                             letters_color=Color.BLACK,
                             letter_contour_color=Color.BLACK)

    PINK = Level_color(background_color=Color.PINK,
                       room_color=Color.BRIGHT_PINK,
                       contour_color=Color.BLACK,
                       letters_color=Color.BLACK,
                       letter_contour_color=Color.WHITE)

    PURPLE_AND_GREY = Level_color(background_color=Color.DARK_BLUE,
                                  room_color=Color.BLUE_GREEN,
                                  contour_color=Color.WHITE,
                                  letters_color=Color.WHITE,
                                  letter_contour_color=Color.DARK_GREY,
                                  inside_room_color=Color.BLACK_RED,
                                  surrounding_color=Color.BLACK_RED)

    REALLY_BRIGHT_RED = Level_color(background_color=Color.PALE_RED,
                                    room_color=Color.RED,
                                    contour_color=Color.BLACK,
                                    surrounding_color=Color.BLACK,
                                    letters_color=Color.BLACK,
                                    letter_contour_color=Color.BLACK,
                                    inside_room_color=Color.WHITE)

    SALMON_AND_GREY = Level_color(background_color=Color.GREY,
                                  room_color=Color.SALMON,
                                  contour_color=Color.BLACK,
                                  letters_color=Color.BLACK,
                                  letter_contour_color=Color.WHITE)

    WHITE = Level_color(background_color=Color.DIRT_WHITE,
                        room_color=Color.IVORY,
                        contour_color=Color.BLACK,
                        letters_color=Color.BLACK,
                        letter_contour_color=Color.BLACK)

    WHITE_AND_BLACK = Level_color(background_color=Color.DIRT_WHITE,
                                  room_color=Color.BLACK,
                                  contour_color=Color.IVORY,
                                  surrounding_color=Color.BRIGHT_RED,
                                  letters_color=Color.BLACK,
                                  inside_room_color=Color.WHITE)

    YELLOW_AND_BLACK = Level_color(background_color=Color.PALE_YELLOW,
                                   room_color=Color.BLACK_BLUE,
                                   contour_color=Color.BRIGHT_RED,
                                   letters_color=Color.BLACK,
                                   inside_room_color=Color.WHITE,
                                   surrounding_color=Color.BRIGHT_RED)




