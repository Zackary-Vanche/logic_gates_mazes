from Switch import Switch
from Tree import Tree

class Door:

    def __init__(self,
                 room_departure=None,
                 room_arrival=None,
                 two_way=False,
                 tree=None,
                 relative_departure_coordinates=[1/2, 1/2],
                 relative_arrival_coordinates=[1/2, 1/2],
                 relative_position=1/2,
                 name=None,
                 surrounding_color=[255,255,255],
                 inside_color=[0, 0, 0],
                 is_open=None):
        """
        La position d'une porte est donnee dans le repere de la piece qui le contient.
        Les axes du repere de la piece sont normalises par les dimensions de la piece.
        Si position == [0,0] l'interrupteur est dans le coin haut gauche de la piece.
        Si position == [0,1] l'interrupteur est dans le coin bas gauche de la piece.
        Si position == [1,0] l'interrupteur est dans le coin haut droite de la piece.
        Si position == [1,1] l'interrupteur est dans le coin bas droite de la piece.
        """
        assert not room_departure.is_exit
        assert not room_departure.name.replace(' ', '') == ''
        assert not room_arrival.name.replace(' ', '') == ''
        if room_arrival.is_exit:
            two_way=False
        if name is None:
            self.name = tree.name.replace('T', 'D')
        else:
            self.name = name
        assert self.name[0] == 'D'
        self.room_departure = None
        self.room_arrival = None
        self.two_way = two_way
        self.tree = tree
        assert self.tree.name.replace('T', 'D') == self.name, f'{self.tree.name} {self.name}'
        to_update_list = self.tree.switches_list[:]
        while len(to_update_list) != 0: # recursive loop to update every switch
            x = to_update_list.pop(0)
            if type(x) == Switch: # It is a switch
                x.add_door(self)
            elif type(x) == Tree: # It is a tree
                for y in x.switches_list:
                    to_update_list.append(y)
            else:
                print(type(x))
                print(x)
                assert False
                raise
        if room_departure is not None and room_arrival is not None:
            self.set_rooms(room_departure, room_arrival)
            assert self.room_departure.name != self.room_arrival.name, " ".join([self.name, room_departure.name, room_arrival.name])
        if self.room_arrival is not None and self.room_arrival.is_exit:
            self.two_way = False
        if is_open is None:
            self.is_open = bool(self.tree.get_value())
        else:
            self.is_open = is_open
        # Coordonnées de la porte dans le repère de la salle de départ
        self.relative_departure_coordinates = relative_departure_coordinates
        self.relative_arrival_coordinates = relative_arrival_coordinates
        self.relative_position = relative_position
        self.real_departure_coordinates = None
        self.real_arrival_coordinates = None
        self.real_middle_coordinates = None
        self.arrow_coordinates = None
        self.surrounding_color = surrounding_color
        self.inside_color = inside_color
        self.pages_list = []

    def set_rooms(self, room_departure, room_arrival):
        self.room_departure = room_departure
        self.room_arrival = room_arrival
        if self.two_way:
            self.room_departure.two_way_doors_list.append(self)
            self.room_arrival.two_way_doors_list.append(self)
        else:
            self.room_departure.departure_doors_list.append(self)
            self.room_arrival.arrival_doors_list.append(self)

    def set_tree(self, tree):
        self.tree = tree

    def update_open(self):
        self.is_open = bool(self.tree.get_value())

    def switches_names(self):
        return [switch.name for switch in self.tree.switches_list]

    def truth_table(self):
        return self.tree.truth_table()

    def __str__(self):
        txt = '\n|   Door {} :'.format(self.name)
        txt += "\n|   Room of departure : {}".format(self.room_departure.name)
        txt += "\n|   Room of arrival : {}".format(self.room_arrival.name)
        txt += "\n|   Two-way : {}".format(self.two_way)
        txt += "\n|   opened : {}".format(self.is_open)
        txt += str(self.tree)
        return txt