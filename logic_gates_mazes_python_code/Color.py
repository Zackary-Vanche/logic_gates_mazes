# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:57:18 2022

@author: utilisateur
"""

from colorsys import hls_to_rgb
from numpy import array
from numpy import uint8


class Color:
    
    saturation = 0.3
    lightness = 0.4

    def color_hls(h = 0, l = lightness, s = saturation):
        return array(255*array(hls_to_rgb(h, l, s)), dtype=uint8).tolist()

    BLACK                 = (  0,   0,   0)
    BLACK_BLUE            = [0, 20, 20]
    BLACK_RED             = color_hls(h = 0, l = 0.1, s = 1)
    BLACK_YELLOW          = ( 50,  50,   0)
    BLUE                  = color_hls(h = 0.5, s = 0.6)
    BLUE_GREEN            = color_hls(0.45, l = 0.65, s = 0.15)
    BRIGHT_BLUE           = color_hls(h = 0.5, l = 0.45)
    BRIGHT_BROWN          = color_hls(h = 0.1, s = 0.2, l = 0.35)
    BRIGHT_GREEN          = color_hls(h = 0.3, l = 0.5)
    BRIGHT_GREY           = ( 96,  96,  96)
    BRIGHT_ORANGE         = color_hls(h = 0.1, l = 0.5)
    BRIGHT_PINK           = color_hls(h = 0.9, l = 0.65)
    BRIGHT_PURPLE         = color_hls(0.8, l = 0.4)
    BRIGHT_PURPLE_BLUE    = color_hls(0.72, l = 0.65)
    BRIGHT_RED            = (200, 0, 0) # color_hls(0, l = 0.5)
    BRIGHT_YELLOW         = color_hls(h = 0.15, l = 0.6, s = 0.4)
    DARK_BLUE             = color_hls(h = 0.64, l = 0.4, s = 0.35)
    DARK_BLUE_GREEN       = color_hls(0.45, l = 0.5, s = 0.15)
    DARK_BROWN            = color_hls(h = 0.1, s = 0.2, l = 0.15)
    DARK_GREEN            = color_hls(0.4, l = 0.15)
    DARK_GREY             = ( 64,  64,  64)
    DARK_PURPLE           = color_hls(0.8, l = 0.25)
    DARK_PURPLE_BLUE      = color_hls(0.72, l = 0.25)
    DARK_RED              = color_hls(h = 0, l = 0.25)
    DARK_WHITE            = (180, 180, 180)
    DARK_YELLOW           = color_hls(h = 0.15, l = 0.4, s = 0.4)
    ELECTRIC_BLUE         = color_hls(h = 0.5, l = 0.4, s = 0.5)
    GREEN                 = color_hls(0.4)
    GREEN_GREY            = color_hls(h = 0.3, l = 0.55, s = 0.1)
    GREY                  = (128, 128, 128)
    GREY_100              = (100, 100, 100)
    GREY_BLUE             = color_hls(h = 0.5, l = 0.45, s = 0.15)
    LEMON                 = (230, 240, 45)
    ORANGE                = color_hls(0.1, l = 0.35)
    PALE_YELLOW           = color_hls(h = 0.15, l = 0.6, s = 0.4)
    PINK                  = color_hls(h = 0.9, l = 0.5)
    PURE_BLUE             = color_hls(h = 0.5, l = 0.7, s = 1)
    REALLY_BRIGHT_BLUE    = color_hls(h = 0.5, l = 0.4, s = 0.5)
    REALLY_BRIGHT_BLUE_2  = color_hls(h = 0.5, l = 0.55, s = 0.4)
    REALLY_BRIGHT_GREEN   = color_hls(h = 0.3, l = 0.65)
    REALLY_DARK_BLUE      = color_hls(h = 0.64, l = 0.2, s = 0.35)
    REALLY_DARK_GREY      = ( 45,  45,  45)
    REALLY_DARK_GREY_BLUE = color_hls(h = 0.5, l = 0.1, s = 0.15)
    REALLY_DARK_RED       = color_hls(h = 0, l = 0.2, s = 1)
    RED                   = color_hls(0)
    SALMON                = color_hls(h = 0.017, l = 0.675, s = 0.9) #(250, 128, 114)
    SILVER                = (170, 180, 180)
    WHITE                 = (255, 255, 255)
    WHITE_PINK            = color_hls(0.72, l = 0.73, s=0.2)
    YELLOW                = color_hls(h = 0.15, l = 0.5)