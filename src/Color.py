from colorsys import hls_to_rgb
from numpy import array
from numpy import uint8

class Color:
    saturation=0.3
    lightness=0.4
    def color_hls(hu=0, li=lightness, sa=saturation):
        return array(255*array(hls_to_rgb(hu, li, sa)), dtype=uint8).tolist()
    BLACK = [0, 0, 0]
    BLACK_BLUE = [0, 20, 20]
    BLACK_GREEN = [0, 50, 0]
    BLACK_RED = [51, 0, 0]  # color_hls(hu=0, li=0.1, sa=1)
    BLACK_YELLOW = [50, 50, 0]
    BLUE = [40, 163, 163]  # color_hls(hu=0.5, sa=0.6)
    BLUE_GREEN = [152, 179, 171]  # color_hls(0.45, li=0.65, sa=0.15)
    BRIGHT_BLUE = [80, 149, 149]  # color_hls(hu=0.5, li=0.45)
    BRIGHT_BROWN = [107, 92, 71]  # color_hls(hu=0.1, sa=0.2, li=0.35)
    BRIGHT_GREEN = [104, 165, 89]  # color_hls(hu=0.3, li=0.5)
    BRIGHT_GREY = [96,  96,  96]
    BRIGHT_KHAKI = [189, 183, 107]
    BRIGHT_ORANGE = [165, 135, 89]  # color_hls(hu=0.1, li=0.5)
    BRIGHT_PINK = [216, 165, 196]  # color_hls(hu=0.9, li=0.65)
    BRIGHT_PURPLE = [120, 71, 132]  # color_hls(0.8, li=0.4)
    BRIGHT_PURPLE_BLUE = [156, 138, 192]  # color_hls(hu=0.72, li=0.65)
    BRIGHT_RED = [200, 0, 0]
    BRIGHT_YELLOW = [193, 185, 112]  # color_hls(hu=0.15, li=0.6, sa=0.4)
    CREAM = [240, 235, 210]
    DARK_BLUE = [74, 87, 154]  # color_hls(hu=0.64, li=0.45, sa=0.35)
    DARK_BLUE_GREEN = [108, 146, 135]  # color_hls(0.45, li=0.5, sa=0.15)
    DARK_BROWN = [45, 39, 30]  # color_hls(hu=0.1, sa=0.2, li=0.15)
    DARK_GREEN = [26, 49, 35]  # color_hls(0.4, li=0.15)
    DARK_GREY = [64,  64,  64]
    DARK_KHAKI = [99, 95, 44]
    DARK_PURPLE = [75, 44, 82]  # color_hls(0.8, li=0.25)
    DARK_PURPLE_BLUE = [56, 44, 82]  # color_hls(hu=0.72, li=0.25)
    DARK_RED = [82, 44, 44]  # color_hls(hu=0, li=0.25)
    DARK_WHITE = [180, 180, 180]
    DARK_YELLOW = [142, 134, 61]  # color_hls(hu=0.15, li=0.4, sa=0.4) 204,204,0
    DIRT_WHITE = [180, 180, 170]
    ELECTRIC_BLUE = [50, 153, 153]  # color_hls(hu=0.5, li=0.4, sa=0.5)
    GREEN = [71, 132, 95]  # color_hls(0.4)
    GREEN_GREY = [133, 151, 128]  # color_hls(hu=0.3, li=0.55, sa=0.1)
    GREY = [128, 128, 128]
    GREY_40 = [40, 40, 40]
    GREY_50 = [50, 50, 50]
    GREY_60 = [60, 60, 60]
    GREY_70 = [70, 70, 70]
    GREY_80 = [80, 80, 80]
    GREY_90 = [90, 90, 90]
    GREY_100 = [100, 100, 100]
    GREY_110 = [110, 110, 110]
    GREY_120 = [120, 120, 120]
    GREY_130 = [130, 130, 130]
    GREY_140 = [140, 140, 140]
    GREY_150 = [150, 150, 150]
    GREY_160 = [160, 160, 160]
    GREY_170 = [170, 170, 170]
    GREY_180 = [180, 180, 180]
    GREY_BLUE = [97, 131, 131]  # color_hls(hu=0.5, li=0.45, sa=0.15)
    IVORY = [230,230,210]
    KHAKI = [152, 146, 68]
    LEMON = [230, 240, 45]
    ORANGE = [116, 94, 62]  # color_hls(0.1, li=0.35)
    PALE_RED = [231, 133, 135]
    PALE_YELLOW = [193, 185, 112]  # color_hls(hu=0.15, li=0.6, sa=0.4)
    PINK = [183, 122, 159]  # color_hls(hu=0.9, li=0.6)
    PSEUDO_DARK_BLUE = [0, 0, 165]
    PSEUDO_DARK_GREEN = [49, 91, 65]  # Color.color_hls(0.4, li=0.275)
    PURE_BLUE = [101, 254, 255]  # color_hls(hu=0.5, li=0.7, sa=1)
    PURE_ORANGE = [220, 140, 0]
    PURPLE_BLUE = [102, 80, 149]  # color_hls(hu=0.72, li=0.45)
    REALLY_BRIGHT_BLUE = [50, 153, 153]  # color_hls(hu=0.5, li=0.4, sa=0.5)
    REALLY_BRIGHT_BLUE_2 = [94, 186, 186]  # color_hls(hu=0.5, li=0.55, sa=0.4)
    REALLY_BRIGHT_GREEN = [149, 192, 138]  # color_hls(hu=0.3, li=0.65)
    REALLY_BRIGHT_ORANGE = [255, 173, 0]
    REALLY_DARK_BLUE = [33, 38, 68]  # color_hls(hu=0.64, li=0.2, sa=0.35)
    REALLY_DARK_GREY = [45,  45,  45]
    REALLY_DARK_GREY_BLUE = [21, 29, 29]  # color_hls(hu=0.5, li=0.1, sa=0.15)
    REALLY_DARK_RED = [102, 0, 0]  # color_hls(hu=0, li=0.2, sa=1)
    RED = [132, 71, 71]  # color_hls(0)
    SALMON = [246, 112, 97]
    SILVER = [170, 180, 180]
    TOTAL_BLUE = [0, 0, 255]
    TOTAL_GREEN = [0, 255, 0]
    TOTAL_MAGENTA = [255, 0, 255]
    TOTAL_RED = [255, 0, 0]
    TOTAL_YELLOW = [255, 255, 0]
    TOTAL_CYAN = [0, 255, 255]
    WHITE = [255, 255, 255]
    WHITE_PINK = [181, 172, 199]  # color_hls(hu=0.72, li=0.73, sa=0.2)
    YELLOW = [165, 158, 89]  # color_hls(hu=0.15, li=0.5)