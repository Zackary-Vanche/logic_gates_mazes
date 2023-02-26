class Level_color:
    
    def __init__(self,
                 background_color = (90, 90, 90),
                 room_color = (50, 50, 50),
                 contour_color = (255,255,255),
                 letters_color = (255,255,255),
                 inside_room_color = None,
                 letter_contour_color = (255,255,255),
                 surrounding_color = None,
                 inside_room_surrounding_color = None):
        self.background_color = background_color
        self.room_color = room_color
        self.contour_color = contour_color
        self.letters_color = letters_color
        self.inside_room_color = None
        if inside_room_color == None:
            self.inside_room_color = self.letters_color
        else:
            self.inside_room_color = inside_room_color
        self.surrounding_color = None
        if surrounding_color == None:
            self.surrounding_color = self.contour_color
        else:
            self.surrounding_color = surrounding_color
        self.letter_contour_color = letter_contour_color
        if inside_room_surrounding_color is None:
            self.inside_room_surrounding_color = self.surrounding_color
        else:
            self.inside_room_surrounding_color = inside_room_surrounding_color
        
    