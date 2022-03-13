# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:57:18 2022

@author: utilisateur
"""

from colorsys import hls_to_rgb
from numpy import array
from numpy import uint8


class Color:
    
    saturation=0.3
    lightness=0.4

    def color_hls(hu=0, li=lightness, sa=saturation):
        return array(255*array(hls_to_rgb(hu, li, sa)), dtype=uint8).tolist()
    
    PURPLE_BLUE_HUE = 0.72 

    BLACK                 = (  0,   0,   0)
    BLACK_BLUE            = [0, 20, 20]
    BLACK_RED             = color_hls(hu=0, li=0.1, sa=1)
    BLACK_YELLOW          = ( 50,  50,   0)
    BLUE                  = color_hls(hu=0.5, sa=0.6)
    BLUE_GREEN            = color_hls(0.45, li=0.65, sa=0.15)
    BRIGHT_BLUE           = color_hls(hu=0.5, li=0.45)
    BRIGHT_BROWN          = color_hls(hu=0.1, sa=0.2, li=0.35)
    BRIGHT_GREEN          = color_hls(hu=0.3, li=0.5)
    BRIGHT_GREY           = ( 96,  96,  96)
    BRIGHT_ORANGE         = color_hls(hu=0.1, li=0.5)
    BRIGHT_PINK           = color_hls(hu=0.9, li=0.65)
    BRIGHT_PURPLE         = color_hls(0.8, li=0.4)
    BRIGHT_PURPLE_BLUE    = color_hls(hu=PURPLE_BLUE_HUE, li=0.65)
    BRIGHT_RED            = (200, 0, 0) # color_hls(0, li=0.5)
    BRIGHT_YELLOW         = color_hls(hu=0.15, li=0.6, sa=0.4)
    DARK_BLUE             = color_hls(hu=0.64, li=0.4, sa=0.35)
    DARK_BLUE_GREEN       = color_hls(0.45, li=0.5, sa=0.15)
    DARK_BROWN            = color_hls(hu=0.1, sa=0.2, li=0.15)
    DARK_GREEN            = color_hls(0.4, li=0.15)
    DARK_GREY             = ( 64,  64,  64)
    DARK_PURPLE           = color_hls(0.8, li=0.25)
    DARK_PURPLE_BLUE      = color_hls(hu=PURPLE_BLUE_HUE, li=0.25)
    DARK_RED              = color_hls(hu=0, li=0.25)
    DARK_WHITE            = (180, 180, 180)
    DARK_YELLOW           = color_hls(hu=0.15, li=0.4, sa=0.4)
    ELECTRIC_BLUE         = color_hls(hu=0.5, li=0.4, sa=0.5)
    GREEN                 = color_hls(0.4)
    GREEN_GREY            = color_hls(hu=0.3, li=0.55, sa=0.1)
    GREY                  = (128, 128, 128)
    GREY_100              = (100, 100, 100)
    GREY_BLUE             = color_hls(hu=0.5, li=0.45, sa=0.15)
    LEMON                 = (230, 240, 45)
    ORANGE                = color_hls(0.1, li=0.35)
    PALE_YELLOW           = color_hls(hu=0.15, li=0.6, sa=0.4)
    PINK                  = color_hls(hu=0.9, li=0.5)
    PURE_BLUE             = color_hls(hu=0.5, li=0.7, sa=1)
    REALLY_BRIGHT_BLUE    = color_hls(hu=0.5, li=0.4, sa=0.5)
    REALLY_BRIGHT_BLUE_2  = color_hls(hu=0.5, li=0.55, sa=0.4)
    REALLY_BRIGHT_GREEN   = color_hls(hu=0.3, li=0.65)
    REALLY_DARK_BLUE      = color_hls(hu=0.64, li=0.2, sa=0.35)
    REALLY_DARK_GREY      = ( 45,  45,  45)
    REALLY_DARK_GREY_BLUE = color_hls(hu=0.5, li=0.1, sa=0.15)
    REALLY_DARK_RED       = color_hls(hu=0, li=0.2, sa=1)
    RED                   = color_hls(0)
    SALMON                = color_hls(hu=0.017, li=0.675, sa=0.9) #(250, 128, 114)
    SILVER                = (170, 180, 180)
    WHITE                 = (255, 255, 255)
    WHITE_PINK            = color_hls(hu=PURPLE_BLUE_HUE, li=0.73, sa=0.2)
    YELLOW                = color_hls(hu=0.15, li=0.5)