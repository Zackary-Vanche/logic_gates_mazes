# Solution :
# House 	    1 	      2 	       3 	      4 	       5
# Color 	    yellow 	  blue 	       red 	      ivory 	   green
# Nationality 	Norwegian Ukrainian    Englishman Spaniard 	   Japanese
# Drink 	    Water 	  Tea 	       Milk 	  Orange juice Coffee
# Smoke 	    kools 	  chesterfield Old Gold   Lucky Strike Parliament
# Pet 	        fox 	  horse 	   Snails 	  Dog 	       Zebra

# 4 0 3 2 1
# 2 4 0 3 1
# 4 3 1 2 0
# 1 0 3 2 4
# 1 2 3 0 4
[4, 2, 4, 1, 1,
 0, 4, 3, 0, 2,
 3, 0, 1, 3, 3,
 2, 3, 2, 2, 0,
 1, 1, 0, 4, 4]

from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list


def level_zebra():
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41')
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    S45 = Switch(name='S45')
    S46 = Switch(name='S46')
    S47 = Switch(name='S47')
    S48 = Switch(name='S48')
    S49 = Switch(name='S49')
    S50 = Switch(name='S50')
    S51 = Switch(name='S51')
    S52 = Switch(name='S52')
    S53 = Switch(name='S53')
    S54 = Switch(name='S54')
    S55 = Switch(name='S55')
    S56 = Switch(name='S56')
    S57 = Switch(name='S57')
    S58 = Switch(name='S58')
    S59 = Switch(name='S59')
    S60 = Switch(name='S60')
    S61 = Switch(name='S61')
    S62 = Switch(name='S62')
    S63 = Switch(name='S63')
    S64 = Switch(name='S64')
    S65 = Switch(name='S65')
    S66 = Switch(name='S66')
    S67 = Switch(name='S67')
    S68 = Switch(name='S68')
    S69 = Switch(name='S69')
    S70 = Switch(name='S70')
    S71 = Switch(name='S71')
    S72 = Switch(name='S72')
    S73 = Switch(name='S73')
    S74 = Switch(name='S74')

    blue = [0]
    green = [1]
    ivory = [2]
    red = [3]
    yellow = [4]

    Englishman = [0]
    Japanese = [1]
    Norwegian = [2]
    Spaniard = [3]
    Ukrainian = [4]

    Coffee = [0]
    Milk = [1]
    Orange_juice = [2]
    Tea = [3]
    Water = [4]

    chesterfield = [0]
    kools = [1]
    Lucky_Strike = [2]
    Old_Gold = [3]
    Parliament = [4]

    Dog = [0]
    fox = [1]
    horse = [2]
    Snails = [3]
    Zebra = [4]

    Slist = [S0, S1, S2,
             S3, S4, S5,
             S6, S7, S8,
             S9, S10, S11,
             S12, S13, S14,

             S15, S16, S17,
             S18, S19, S20,
             S21, S22, S23,
             S24, S25, S26,
             S27, S28, S29,

             S30, S31, S32,
             S33, S34, S35,
             S36, S37, S38,
             S39, S40, S41,
             S42, S43, S44,

             S45, S46, S47,
             S48, S49, S50,
             S51, S52, S53,
             S54, S55, S56,
             S57, S58, S59,

             S60, S61, S62,
             S63, S64, S65,
             S66, S67, S68,
             S69, S70, S71,
             S72, S73, S74, ]

    tree_list_equ = ['EQU', [None], Tree.tree_list_BIN(3)]
    tree_list_XNOR_equ = ['XNOR', tree_list_equ, tree_list_equ]

    color_S = []
    nationality_S = []
    drink_S = []
    smoke_S = []
    pet_S = []
    for i_door in range(5):
        Slist_room = Slist[15 * i_door:15 * i_door + 15]
        color = Slist_room[0:3]
        nationality = Slist_room[3:6]
        drink = Slist_room[6:9]
        smoke = Slist_room[9:12]
        pet = Slist_room[12:15]
        color_S.append(color)
        nationality_S.append(nationality)
        drink_S.append(drink)
        smoke_S.append(smoke)
        pet_S.append(pet)

    def get_S(i_door):
        # Slist_room = Slist[15*i_door:15*i_door+15]
        # color = Slist_room[0:3]
        # nationality = Slist_room[3:6]
        # drink = Slist_room[6:9]
        # smoke = Slist_room[9:12]
        # pet = Slist_room[12:15]
        color = color_S[i_door]
        nationality = nationality_S[i_door]
        drink = drink_S[i_door]
        smoke = smoke_S[i_door]
        pet = pet_S[i_door]
        Slist_tree = []
        # The Englishman lives in the red house.
        Slist_tree = Slist_tree + Englishman + nationality + red + color
        # The Spaniard owns the dog.
        Slist_tree = Slist_tree + Spaniard + nationality + Dog + pet
        # Coffee is drunk in the green house.
        Slist_tree = Slist_tree + green + color + Coffee + drink
        # The Ukrainian drinks tea.
        Slist_tree = Slist_tree + Ukrainian + nationality + Tea + drink
        # The Old Gold smoker owns snails.
        Slist_tree = Slist_tree + Old_Gold + smoke + Snails + pet
        # kools are smoked in the yellow house.
        Slist_tree = Slist_tree + yellow + color + kools + smoke
        # The Lucky Strike smoker drinks orange juice.
        Slist_tree = Slist_tree + Orange_juice + drink + Lucky_Strike + smoke
        # The Japanese smokes Parliaments.
        Slist_tree = Slist_tree + Japanese + nationality + Parliament + smoke
        return Slist_tree

    def get_tree(i_door):
        return Tree(tree_list=['AND'] + [tree_list_XNOR_equ] * 8,
                    empty=True,
                    name=f'T{i_door}',
                    switches=get_S(i_door),
                    cut_expression=True)

    # The Norwegian lives in the first house.
    T0 = Tree(tree_list=['AND',
                         ['EQU', [None], Tree.tree_list_BIN(3)]] + [tree_list_XNOR_equ] * 8,
              empty=True,
              name='T0',
              switches=Norwegian + Slist[0:15][3:6] + get_S(0),
              cut_expression=True)
    T1 = get_tree(1)
    # Milk is drunk in the middle house.
    T2 = Tree(tree_list=['AND',
                         ['EQU', [None], Tree.tree_list_BIN(3)]] + [tree_list_XNOR_equ] * 8,
              empty=True,
              name='T2',
              switches=Milk + Slist[15 * 2:15 * 3][6:9] + get_S(2),
              cut_expression=True)
    T3 = get_tree(3)
    T4 = get_tree(4)
    S_type_list = [[] for i in range(5)]
    for i_door in range(5):
        Slist_room = Slist[15 * i_door:15 * i_door + 15]
        for i_type in range(5):
            S_type_list[i_type].extend(Slist_room[3 * i_type:3 * i_type + 3])
    Slist5 = []
    for i in range(5):
        Slist5.extend(S_type_list[i] + [0, 1, 2, 3, 4])
    tree_list_EQUSET = ['EQUSET'] + [Tree.tree_list_BIN(3)] * 5 + [[None]] * 5
    T5 = Tree(tree_list=['AND'] + [tree_list_EQUSET] * 5,
              empty=True,
              name='T5',
              switches=Slist5,
              cut_expression=True,
              cut_expression_separator=')')
    tree_list_AND_equ = ['AND', tree_list_equ, tree_list_equ]
    Slist6 = []
    # The green house is immediately to the right of the ivory house.
    tree_list_right_of = ['OR'] + [tree_list_AND_equ] * 4
    for i in range(4):
        Slist6 += ivory + color_S[i] + green + color_S[i + 1]
    # The man who smokes chesterfields lives in the house next to the man with the fox.
    tree_list_next_t0 = ['OR'] + [tree_list_AND_equ] * 8
    for i in range(4):
        Slist6 += chesterfield + smoke_S[i] + fox + pet_S[i + 1]
        Slist6 += chesterfield + smoke_S[i + 1] + fox + pet_S[i]
    T6 = Tree(tree_list=['AND'] + [tree_list_right_of] + [tree_list_next_t0],
              empty=True,
              name='T6',
              switches=Slist6,
              cut_expression=True,
              cut_expression_separator=')')
    Slist7 = []
    # kools are smoked in the house next to the house where the horse is kept.
    for i in range(4):
        Slist7 += kools + smoke_S[i] + horse + pet_S[i + 1]
        Slist7 += kools + smoke_S[i + 1] + horse + pet_S[i]
    # The Norwegian lives next to the blue house.
    for i in range(4):
        Slist7 += Norwegian + nationality_S[i] + blue + color_S[i + 1]
        Slist7 += Norwegian + nationality_S[i + 1] + blue + color_S[i]
    T7 = Tree(tree_list=['AND'] + [tree_list_next_t0] * 2,
              empty=True,
              name='T7',
              switches=Slist7,
              cut_expression=True,
              cut_expression_separator=')')

    ex = 0.25
    ey = 4
    dx = 1

    # There are five houses.
    R0 = Room(name='R0',
              position=[dx, 0, ex, ey],
              switches_list=Slist[0:15])
    R1 = Room(name='R1',
              position=[2 * dx, 0, ex, ey],
              switches_list=Slist[15:2 * 15])
    R2 = Room(name='R2',
              position=[3 * dx, 0, ex, ey],
              switches_list=Slist[2 * 15:3 * 15])
    R3 = Room(name='R3',
              position=[4 * dx, 0, ex, ey],
              switches_list=Slist[3 * 15:4 * 15])
    R4 = Room(name='R4',
              position=[5 * dx, 0, ex, ey],
              switches_list=Slist[4 * 15:5 * 15])
    R5 = Room(name='R5',
              position=[6 * dx, 0, ex, ex],
              switches_list=[])
    R6 = Room(name='R6',
              position=[6 * dx, (ey - ex) / 3, ex, ex],
              switches_list=[])
    R7 = Room(name='R7',
              position=[6 * dx, 2 * (ey - ex) / 3, ex, ex],
              switches_list=[])
    RE = Room(name='RE',
              position=[6 * dx, ey - ex, ex, ex],
              is_exit=True)  # E pour exit ou end

    rdc = [0.3, 0.3]
    rda = [0.7, 0.7]

    D0 = Door(two_way=False,
              tree=T0,
              room_departure=R0,
              room_arrival=R1,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rda)
    D1 = Door(two_way=False,
              tree=T1,
              room_departure=R1,
              room_arrival=R2,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rda)
    D2 = Door(two_way=False,
              tree=T2,
              room_departure=R2,
              room_arrival=R3,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rda)
    D3 = Door(two_way=False,
              tree=T3,
              room_departure=R3,
              room_arrival=R4,
              relative_departure_coordinates=rdc,
              relative_arrival_coordinates=rda)
    D4 = Door(two_way=False,
              tree=T4,
              room_departure=R4,
              room_arrival=R5)
    D5 = Door(two_way=False,
              tree=T5,
              room_departure=R5,
              room_arrival=R6)
    D6 = Door(two_way=False,
              tree=T6,
              room_departure=R6,
              room_arrival=R7)
    D7 = Door(two_way=False,
              tree=T7,
              room_departure=R7,
              room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7] + [RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7],
                 fastest_solution='''S2 S4 S8 S9 S12 D0 S20 S21 S22 S28 D1 S30 S31 S36 S39 S40 S42 S43 D2 S46 S48 S49 S52 S55 D3 S60 S63 S71 S74 D4 D5 D6 D7''',
                 level_color=Levels_colors_list.FROM_HUE(hu=0.15, sa=0, li=0.95),
                 name='Zebra',
                 door_window_size=500,
                 keep_proportions=True,
                 y_separation=35,
                 border=40,
                 door_multipages=True)

    return level