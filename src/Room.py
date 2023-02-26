from numpy import ceil, sqrt
from linear_function import linear_function
from powerset import powerset

class Room:
    
    def __init__(self, 
                 is_exit = False, 
                 switches_list = [], 
                 # position de la piece pour pygame
                 position = [None, None, None, None], 
                 # Dans l'ordre :
                 # ecart en y du bord
                 # ecart en x du bord
                 # longueur en y
                 # longueur en x
                 name = 'R',
                 surrounding_color=[255,255,255],
                 possible_switches_values=None):
        self.name = name
        self.is_exit = is_exit
        if self.is_exit:
            assert self.name == 'RE'
        self.departure_doors_list = []
        self.arrival_doors_list = []
        self.two_way_doors_list = []
        self.switches_list = switches_list
        self.switches_list.sort(key = lambda x : [len(x.name), x.name])
        for switch in self.switches_list:
            switch.room = self
        if isinstance(position, list):
            self.position = {0 : position}
        else:
            self.position = position
        self.pages_list=[]
        for ipage in self.position.keys():
            self.pages_list.append(ipage)
        self.name_position = None
        self.switches_positions = None
        self.surrounding_color = surrounding_color
        self.possible_switches_values = possible_switches_values
        if type(possible_switches_values) == type([]):
            self.possible_switches_actions = []
            for switches_values in self.possible_switches_values:
                Slist = []
                for i in range(len(self.switches_list)):
                    if switches_values[i]:
                        Slist.append(self.switches_list[i].name)
                self.possible_switches_actions.append(Slist)
        else:
            self.possible_switches_actions = None
        
    def get_name_position(self):
        [x_gap, y_gap, x, y] = self.position[self.maze.current_page]
        if self.is_exit:
            self.name_position = [x_gap + x/2 - 18, y_gap + y/2 - 6]
        else:
            self.name_position = [x_gap + 4, y_gap + 4]
        return self.name_position
            
    def get_switches_positions(self):
        [x_gap, y_gap, x, y] = self.position[self.maze.current_page]
        n_switches = len(self.switches_list)
        if n_switches == 0:
            return []
        positions = []
        nb_lines = int(ceil(sqrt(n_switches*x/y)))
        for k in range(n_switches):
            line = k//nb_lines
            column = k%nb_lines
            positions.append([column, line])
        # On centre les interrupteurs dans le carré
        # et on les écarte les une des autres
        x_list = [p[0] for p in positions]
        y_list = [p[1] for p in positions]
        xmax = max(x_list)
        ymax = max(y_list)
        xmin = min(x_list)
        ymin = min(y_list)
        
        ex = 1/(xmax+3)
        ey = 1/(ymax+2)

        new_xmin = x_gap + max(ex*x, 0)
        new_ymin = y_gap + max(ey*y, 0)
        new_xmax = x_gap + min((1-ex)*x, x)
        new_ymax = y_gap + min((1-ey)*y, y)
        
        new_xmin = new_xmin + 7
        if xmin == xmax:
            fx = lambda k : k + x_gap + x/2
        else:
            (px, cx) = linear_function(xmin, new_xmin, xmax, new_xmax)
            fx = lambda x : px*x+cx
        if ymin == ymax:
            fy = lambda k : k + y_gap + y/2
        else:
            (py, cy) = linear_function(ymin, new_ymin, ymax, new_ymax)
            fy = lambda y : py*y+cy
        for k in range(n_switches):
            [x_switch, y_switch] = positions[k]
            positions[k] = [fx(x_switch), fy(y_switch)]
        self.switches_positions = positions
        return self.switches_positions
    
    def get_possible_switches_actions(self):
        if self.possible_switches_actions is None:
            self.possible_switches_actions = powerset([s.name for s in self.switches_list])
        return self.possible_switches_actions
            
    def __str__(self):
        txt =  '\n|   Room {} :'.format(self.name)
        txt += '\n|   Departure door(s) list :\n|      {}'.format([door.name for door in self.departure_doors_list])
        txt += '\n|   Arrival door(s) list :\n|      {}'.format([door.name for door in self.arrival_doors_list])
        txt += '\n|   Two-way door(s) list :\n|      {}'.format([door.name for door in self.two_way_doors_list])
        txt += '\n|   Switches list :\n|      {}'.format([switch.name for switch in self.switches_list])
        return txt
    
class Virtual_Room(Room):
    
    def __init__(self, 
                 is_exit = False, 
                 switches_list = [],
                 position = [None, None, None, None], 
                 name = 'R',
                 surrounding_color=[255,255,255],
                 possible_switches_values=None):
    
        super().__init__(is_exit, 
                         switches_list,
                         position, 
                         name,
                         surrounding_color,
                         possible_switches_values)

if __name__ == "__main__":
    
    V1 = Virtual_Room()
        