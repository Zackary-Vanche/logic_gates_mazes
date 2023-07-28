help_menus_list = {}

######################
## TREE'S NOTATIONS ##
######################

# 'NOR'

help_menus_list['basis'] = '''
D0 = S0 means : 
    D0 is open if S0 is turned on.'''

help_menus_list['NOT'] = """
¬ means 'NOT'.
¬S0 = 1 if S0 = 0
¬S0 = 0 if S0 = 1
Be carefull with the negation, because you have :
    ¬ 1 = 0
    ¬ 0 = 1"""

help_menus_list['MINUS'] = """
- means 'MINUS'.
-S0 is the opposite of S0."""

help_menus_list['AND'] = """
& means 'AND'.
D0 = & S0 S1 means :
    D0 is open if (S0, S1) = (1,1)"""

help_menus_list['NAND'] = """
NAND truth table (D0 = ¬& S0 S1):
S0  S1  D0
  0    0    1
  0    1    1
  1    0    1
  1    1    0"""

help_menus_list['NAND 3'] = """NAND can also apply to 3 parameters instead of 2:

    NAND truth table [D0 = NAND ( S0 S1 S2 ) = ¬& ( S0 S1 S2 )]:
    S0  S1  S2  D0
      0    0    0     1
      0    1    0     1
      1    0    0     1
      1    1    0     1
      0    0    1     1
      0    1    1     1
      1    0    1     1
      1    1    1     0"""

help_menus_list['OR'] = '''
| means 'OR'.
D2 = | S1 S2 means :
    D1 is open if S1 or S2 is turned on (i.e. if (S0, S1) = (0,1) or (S0, S1) = (1,0) or (S0, S1) = (1,1))'''

help_menus_list['XOR'] = """
^ means exclusive or ('XOR').
D0 = ^ S0 S1 means :
    D0 is open if S0 is different from S1.
It can be used with more than two parameters:
    D0 = ^ (S0 S1 ...) means :
        D0 is open if there is exactly one switch among all its parameters that is turned on."""

help_menus_list['XOR 3'] = """
XOR can be used with more than 3 parameters :
    D0 = XOR(S0, S1, ...) means :
        D0 is open if there is exactly one switch among its parameters that is turned on."""
        
help_menus_list['XNOR short'] = """
XOR means exclusive or. XNOR is its opposite.

Their definitions are :
    XOR S0 S1 = | & S0 ¬ S1 & ¬ S0 S1 
    XNOR S0 S1 = | & S0 S1 & ¬ S0 ¬ S1
    XNOR S0 S1 = ¬ XOR S0 S1"""

help_menus_list['XNOR'] = """
XOR means exclusive or. XNOR is its opposite.

XOR truth table (D0 = ^ S0 S1):
S0  S1  D0
  0    0    0
  0    1    1
  1    0    1
  1    1    0  
In other words, D0 is open if S0 is different from S1.

XNOR truth table (D0 = ¬^ S0 S1):
S0  S1  D0
  0    0    1
  0    1    0
  1    0    0
  1    1    1    
In other words, D0 is open if S0 = S1.

You can write :
    XOR S0 S1 = | & S0 ¬ S1 & ¬ S0 S1 
    XNOR S0 S1 = | & S0 S1 & ¬ S0 ¬ S1
    XNOR S0 S1 = ¬ XOR S0 S1"""

help_menus_list['SUM'] = """
+ S0 S1 is the sum of S0 and S1.
With parenthesis, the operator + can be used with more than 2 operands:
    + (S0 S1 S2) is the sum of S0, S1 and S2."""

help_menus_list['DIV'] = """
/ S0 S1 is equal to S0 divided by S1."""

help_menus_list['PROD'] = """
* S0 S1 is equal to the product of S0 and S1."""

help_menus_list['POW'] = """
** S0 S1 is equal to S0 raised to the power of S1."""

help_menus_list['MOD'] = """
% S0 S1 is equal to S0 modulo S1."""

help_menus_list['ABS'] = """
@ S0 is the absolute value of S0."""

help_menus_list['EQU'] = '''
D0 = = S0 S1 means :
    D0 is open if S0 is equal to S1.
It is similar to XNOR with two operands.
Used with more than 2 operands, it means that all its operands are equal to each other.'''

help_menus_list['EQUSET'] = '''
D0 = ~  ( S0 ; S2 ; ...) ( S1 ; S3 ; ...) means :
    D0 is open if the two sets ( S0 ; S2 ; ...) and ( S1 ; S3 ; ...) contain the same elements, but not obligatorily in the same order.
D0 = ~  ( S0 ; S2 ) ( S1 ; S3) means :
    D0 = | & = S0 S1 = S2 S3 & = S0 S3 = S2 S1'''

help_menus_list['DIFF'] = '''
D0 = ≠ (S0 S1 ...) means :
    D0 is open if every elements of (S0 S1 ...) are two by two differents.'''

help_menus_list['INF'] = """
D0 = < S0 S1 means :
    D0 is open if S0 is inferior to S1"""
    
help_menus_list['INF0'] = """
D0 = <0 a b means :
    D0 = | < a b = a 0 = b 0
D0 = <0 a b c means :
    D0 = & <0 a b <0 b c
"""

help_menus_list['SUP'] = """
D0 = > S0 S1 means :
    D0 is open if S0 is superior to S1"""

help_menus_list['INFOREQU'] = """
D0 = <= S0 S1 means :
    D0 is open if S0 is inferior or equal to S1"""

help_menus_list['SUPOREQU'] = """
D0 = >= S0 S1 means :
    D0 is open if S0 is superior or equal to S1"""

help_menus_list['BIN'] = """
b (S0 S1 ...) is the number whose binary little endian code is S0 S1 etc.
For example:
    b (S0 S1 S2) = + (S0 * 2 S1 * 4 S2)"""

help_menus_list['IN'] = """
The operator i takes two arguments : one switch and a switch list.
It returns the value 1 if the switch is included in the list, 0 if not.
For example:
    i 0 [1 2] = 0
    i 4 [4 2] = 1"""

help_menus_list['INLIST'] = """
Let l1 and l2 be two switches list.
Then,
    i l1 l2 = 1
if and only if l1 is a substring of l2.
For example:
    i (1) [1 2] = 1
    i (1 0) [0 1 2] = 0
    i (2 0) [3 2 0] = 1
    i (3 2) [3 0 2] = 0
"""

help_menus_list['DIST'] = """
d (S0 S1 S2 S3) is the euclidian distance between the two points of the plane (S0 S1) and (S2 S3)."""

help_menus_list['NONO'] = """
The operator # takes two list in argument.
The first list tells you the number of unbroken lines of 1 that should be presents in the second list in order for the result to be 1.
For example:
    # (1 1) [1 0 0 1 0] = 1
    # (2 1) [1 1 0 0 1] = 1
    # (4) [1 1 1 1] = 1
    # (1 3) [1 0 1 1] = 0
    # (2 1) [1 0 0 1 1] = 0"""

help_menus_list['BETWEEN'] = """
The operator BETWEEN takes several arguments:
    A list of triplets of switches
    A list or switches. Let be L that ast list.
For every triplet:
    Let (a, b, c) be the triplet
    If a, b or c are not in L or b is not in between a and c, then the operator result is 0.
If, for every triplet, a, b and c are in L and b is in between a and c, the operator result is 1."""

help_menus_list['JUMP'] = """
j stands for 'jump'.
This operator takes as argument a list of switches.

    j (S0 S1 S2 S3 S4 S5) = i b(S0 S1 S2 S3 S4 S5) [22 26 37 41]
    j (S0 S1 S2 S3 S4 S5 S6 S7) = ^ j (S0 S1 S2 S3 S4 S5) j (S2 S3 S4 S5 S6 S7)
    j (S0 S1 S2 S3 S4 S5 S6 S7 S8 S9) = ^ [ j (S0 S1 S2 S3 S4 S5) j (S2 S3 S4 S5 S6 S7) j (S4 S5 S6 S7 S8 S9) ]"""

help_menus_list['MAS'] = """
w stands for 'white'.
This operator takes as argument two lists of switches.
w l1 l2 is the number of values of l1 that are in l2 but not at the same index.

    w [0 0 0] [0 0 1] = 0
    w [1 2 3] [2 1 3] = 2
    w [1 1 2] [1 1 2] = 0
    w [5 6 2] [5 6 2] = 0
    w [1 1 5] [5 1 1] = 2
    w [1 1 5] [6 1 1] = 1
"""

help_menus_list['N3L'] = """
N3L stands for 'no three in line'.
This operator takes as argument one list of switches.
N3L (S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15) = 1
only if there are no three switches aligned in the array :
         S0  S1  S2  S3
         S4  S5  S6  S7
         S8  S9  S10 S11
         S12 S13 S14 S15
and if > SUM (S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15) 8
"""

help_menus_list['E'] = """
One notation is used only in this level :

    E (S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S20 S21 S22 S23)
    = ~ (b (S0 S1 S2);
         b (S3 S4 S5);
         b (S6 S7 S8);
         b (S9 S10 S11);
         b (S12 S13 S14);
         b (S15 S16 S17);
         b (S18 S19 S20);
         b (S21 S22 S23))
         (0 ; 0 ; 0 ; 0 ; 3 ; 5 ; 6 ; 7)
"""

help_menus_list['AND and NOT'] = """  
By combining these notations, you can write :
D1 = & S2 ¬ S3 means :
    D1 is open if (S2, S3) = (1,0)
D2 = AND ¬ S4 S5 means :
    D2 is open if (S4, S5) = (0,1)
D3 = & ¬ S6 ¬ S7  S6 S7 means :
    D3 is open if (S6, S7) = (0,0)
    It can also be written :
    D3 = NOR S6 S7
    D3 = ¬| S6 S7"""

help_menus_list['numerical value'] = """
Sometimes, a switch can be replaced by a numerical value."""

help_menus_list['parenthesis'] = """
To simplify notations, parentheses are used.

Instead of writing :
    D0 = & S0 & S1 S2
you can write :
    D0 = & S0 ( & S1 S2 )
or :
    D0 = & ( S0 S1 S2 )
You can use this notation with more than 3 switches.
You can also use it with | instead of &.

You can use this notation with negations :
    D0 = & ¬ S0 ( & S1 S2 )
       = & ( ¬ S0 S1 S2 )"""

help_menus_list['brackets'] = """
Sometime, square brackets can be used instead of parentheses."""

help_menus_list['Introduction thuth table'] = """
A truth table tells you the result of a logical expression.
Here are some examples :

    Negation truth table (D0 = ¬S0):
    S0  D0
      0     1
      1     0

    AND truth table (D0 = & S0 S1):
    S0  S1  D0
      0    0    0
      0    1    0
      1    0    0
      1    1    1

    OR truth table (D0 = | S0 S1):
    S0  S1  D0
      0    0    0
      0    1    1
      1    0    1
      1    1    1"""

help_menus_list["cheat code"] = """
A cheat code exists.
If you add the letter A before a command :
    You can turn on a switch even if you are not in its room.
    You can use a door even if it is not open.
    If a door is one-way, you can use it even if you are not in the good room.

Writing A D10 allows you to end this level by cheating.

You can also use the cheat code to go directly in a room by giving its name :
    A R2 allows you to go in the room R2.
The name of the exit room is RE."""

###################
## MISCELLANEOUS ##
###################

help_menus_list['introduction'] = """You are trapped in the inside of a computer and want to reach the exit.

There are differents elements in this game :
    Rooms (R0, R1, R2, ..., EXIT) :  
        The room inside which you are is surrounded.
    Switches (S0, S1, S2, ...) : 
        If a switch is turned on, it is surrounded, and you say it is equal to 1.
        If it is turned off, it is equal to 0.
        To turn on a switch, write its name and press enter.
    Doors (D0, D1, D2, ...) :    
        If a door is open, it is surrounded, and you say it is equal to 1.
        If it is closed, it is equal to 0.
        To use a door, write its name and press enter.
        Diamond-shape doors are two-way while triangle-shaped doors are one-way only (in this level, all doors are one-way only).      
If you made a mistake when taping the name of a door or a switch, you can always erase it by taping on the backspace key.

To leave the help menu (or come back to it), press [H].
To start the level again from the beginning, press [B].
To go to the next level, press the right arrow key.
To go to the previous level, press the right arrow key.

On the left size window of the game are equations that tell you when a door is open :
These equations work with any name of door or switch."""

help_menus_list['directions keys'] = """
To change level, you can use :

    the right arrow key to go to the next level
    the left arrow key to go to the previous level

    L and the number of the level you want to go to.
    For instance, if you write L12 and then press enter you will go to the level 12.

Instead of taping the action you want to do, you can see the possibles actions by using the UP and the DOWN keys.
"""

help_menus_list['go in a room'] = """
To go directly in a room, you can type its name (if it is possible for you to go there).
The exit room is called RE."""

help_menus_list['reminder B'] = """
[Reminder] : To start the level again from the beginning, press [B]."""

help_menus_list['write several actions'] = """
Instead of writing actions one by one, one can write several at a time, separated by spaces.
For instance, you can write :
    S0 S1 D0
if you want to turn on S0, S1 and then use the door D0."""

help_menus_list['leave the game'] = """
To leave the game, you can click an the cross but also press [Q] or [ESCAPE]."""

help_menus_list['see other doors'] = """
By pressing [P] or [M], you can see the values of the other doors."""

help_menus_list['random'] = """
By pressing [N], you get a new random level.

Door's expression and solutions of the random levels have all been calculated by computer only."""

help_menus_list['random exit'] = """The configuration you have to reach to open the exit gate is chosen randomly in a file.
Press [N] to get a new exit gate."""

help_menus_list['random configuration'] = """The initial configuration is chosen randomly in a file.
Press [N] to get a new configuration."""

############
## LEVELS ##
############

help_menus_list['levels'] = {}

help_menus_list['levels']["Hello world"] = '\n'.join([help_menus_list['introduction'], help_menus_list['basis']])

help_menus_list['levels']["Playground"] = help_menus_list['NOT']

help_menus_list['levels']["Initiation"] = help_menus_list['OR']

help_menus_list['levels']["Linear"] = '\n'.join([help_menus_list['AND'], help_menus_list['NOT'], help_menus_list['AND and NOT']])

help_menus_list['levels']['Loop'] = help_menus_list['directions keys']

help_menus_list['levels']['Boolean'] = help_menus_list['XOR']

help_menus_list['levels']["Backward"] = help_menus_list['parenthesis']

help_menus_list['levels']["Bis repetita"] = """You might have to repeat twice the same actions."""

help_menus_list['levels']["Binary"] = help_menus_list['go in a room']

help_menus_list['levels']["OR"] = '''Enjoy the game while it is still easy.'''

help_menus_list['levels']["Crossroad"] = help_menus_list['reminder B']

help_menus_list['levels']["Forest"] = help_menus_list['XNOR']

help_menus_list['levels']["Square"] = help_menus_list['write several actions']

help_menus_list['levels']["Fluid"] = help_menus_list['Introduction thuth table']

help_menus_list['levels']["Numeration"] = '\n'.join([help_menus_list['EQU'], help_menus_list['BIN']])

help_menus_list['levels']["Sum"] = help_menus_list['random'] + '\n\n' + help_menus_list['IN'] + '\n\n' + \
                                   help_menus_list['SUM']

help_menus_list['levels']["Product"] = help_menus_list['PROD']

help_menus_list['levels']["Congruence"] = help_menus_list['MOD']

help_menus_list['levels']["Sorted"] = '\n'.join([help_menus_list['random'], help_menus_list['EQUSET']])

help_menus_list['levels']["Meanders"] = """You have to go inside every room."""

help_menus_list['levels']["Infinity"] = help_menus_list["cheat code"]

help_menus_list['levels'][
    "3 SAT"] = """The 3 SAT problem is NP complete.\n\nThe door expression has been randomly chosen by computer."""

help_menus_list['levels']["Point of no return"] = help_menus_list['XNOR']

help_menus_list['levels']["Bipartite"] = """Several paths lead to the exit."""

help_menus_list['levels']["Hamiltonian"] = """Don't look for something too complicated."""

help_menus_list['levels']["Pong"] = '\n'.join([help_menus_list['numerical value'], help_menus_list['SUM'], help_menus_list['EQU']])

help_menus_list['levels']["Longest path"] = "The longest path problem is NP-complete."

help_menus_list['levels']["Hitting set"] = """The hitting set is one of the Karp's 21 NP-complete problems.\nIt is equivalent to the set cover problem\n""" + '\n'.join([help_menus_list['INF'],
                                                                                                                                                                         help_menus_list['SUP'],
                                                                                                                                                                         help_menus_list['INFOREQU'],
                                                                                                                                                                         help_menus_list['SUPOREQU']])

help_menus_list['levels']["Independent set"] = "The independent set is one of the Karp's 21 NP-complete problems."

help_menus_list['levels']["Dominating set"] = """Finding dominating set is a NP-Complete problem."""

help_menus_list['levels']["Exact cover"] = """The exact cover is one of the Karp's 21 NP-complete problems.\n""" + help_menus_list['XOR 3']

help_menus_list['levels']["Odd"] = help_menus_list['leave the game']

help_menus_list['levels']["Triangulate"] = help_menus_list['DIST']

help_menus_list['levels']["Recurrence"] = help_menus_list['brackets']

help_menus_list['levels']["Naturals"] = '\n'.join([help_menus_list['ABS'], help_menus_list['MINUS'], help_menus_list['BIN']])

help_menus_list['levels']["Wasted"] = """It looks easy, and it is easy."""

help_menus_list['levels']["Wind compass"] = """It is not more complicated than the level named "meanders"."""

help_menus_list['levels']["Compact"] = """It looks easy, but it is maybe just an impression."""

help_menus_list['levels']["Parallel"] = """The "Guess and check" method works well here."""

help_menus_list['levels']["Pythagorean"] = help_menus_list['POW']

help_menus_list['levels']["Elementary"] = """An elementary permutation is a swap of two adjacent elements.\n""" + help_menus_list['EQUSET']
                                          
help_menus_list['levels']["Rotation"] = help_menus_list['random exit']                                          

help_menus_list['levels']["Superpermutation"] = help_menus_list['INLIST']

help_menus_list['levels']["Singleton"] = """A singleton is a set with exactly one element."""

help_menus_list['levels']["Taxicab number"] = """Taxicab numbers are also called Hardy–Ramanujan numbers."""

help_menus_list['levels']["Chessboard"] = """If you remove the exit, the graph of this level is the graph of the possible moves of a knight in a 3*4 rectangle.\nHowever, sometimes here doors are one-way only."""

help_menus_list['levels']["Water lily"] = """A water lily is a floating aquatic plant with round, flat leaves and beautiful flowers that bloom on or above the water's surface."""

help_menus_list['levels']["Entropy"] = """You have a limited number of moves."""

help_menus_list['levels']["Dichotomy"] = """? is a random integer.\n\nOnce you found the value of ?, the level is over.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Partition"] = """The partition is one of the Karp's 21 NP-complete problems.\n""" + help_menus_list["PROD"]

help_menus_list['levels']["Second"] = """You need to solve a second order polynomial equation."""

help_menus_list['levels']["Knapsack"] = """The knapsack is one of the Karp's 21 NP-complete problems."""

help_menus_list['levels']["Egyptian fractions"] = help_menus_list['DIV']

help_menus_list['levels']["Code"] = "You may want to learn what the Gray code is."

help_menus_list['levels']["Spider"] = "Walk on the spider web."

help_menus_list['levels']["Tetrahedron"] = """The logic expressions of the doors of this level have been calculated by computer.\nThe program that calculated it already knew all the rest of the level.\n\nThis level looks complicated, but you do only need to let the game lead you to the exit."""

help_menus_list['levels']["Small"] = """The solution and the door's expressions of this level have been chosen randomly and calculated by the computer only."""

help_menus_list['levels']["The 4 queens"] = """This level is inspired from the 8 queens problem."""

help_menus_list['levels']["Mansion"] = """You might get lost in this mansion."""

help_menus_list['levels']["K"] = """You have to locate as many knights in a chessboard as possible."""

help_menus_list['levels']["Strange"] = "You can always try exhaustive testing..."

help_menus_list['levels']["Alice and Bob"] = """Alice wants to send a package to Bob."""

help_menus_list['levels']["Rotation_bis"] = help_menus_list['random exit'] 

help_menus_list['levels']["Nonogram"] = help_menus_list['NONO']

help_menus_list['levels']["Crystal"] = """If you make a mistake, you have to start all over again."""

help_menus_list['levels']["XOR"] = help_menus_list['NAND']

help_menus_list['levels']["Lights_out"] = help_menus_list['random configuration']

help_menus_list['levels']["Weights"] = '''You must find the good weights in order to reach the exit.'''

help_menus_list['levels']["Tetris"] = """Each number can represent a position in the plane.\n"""

help_menus_list['levels']["Central symmetry"] = """The name of the level is a hint."""

help_menus_list['levels']["Mastermind"] = help_menus_list['MAS'] + """\n\n?0 ?1 ?2 ?3 ?4 ?5 ?6 ?7 are switches.\n\nYou have to guess their values."""

help_menus_list['levels']["Baguenaudier"] = '''The baguenaudier is an old puzzle game.'''

help_menus_list['levels']["Spare"] = '''Use the spare room.'''

help_menus_list['levels']["4 colors theorem"] = """Each couple of switches represent a color.\n"""

help_menus_list['levels']["Grid"] = help_menus_list['random exit']

help_menus_list['levels']["Flash-back"] = """Be careful not to come back in a state you already visited."""

help_menus_list['levels']["Spaceship"] = 'You have to find the order in the chaos.'

help_menus_list['levels']["Magic square"] = help_menus_list['DIFF']

help_menus_list['levels']["Matrix"] = """To solve this level you need to do a 5*5 matrix inversion."""

help_menus_list['levels']["River"] = """You want to cross the river with a wolf, a goat and a cabbage."""

help_menus_list['levels']["Vortex"] = """You might feel dizzy."""

help_menus_list['levels']["Tree"] = """The tree is hidden in the equations.\n\n""" + help_menus_list['random']

help_menus_list['levels'][
    "Dead_ends"] = """Even if it is the first level that actually looks like a printed circuit board, you have been in a computer all this time."""

help_menus_list['levels']["Betweenness"] = help_menus_list['BETWEEN']

help_menus_list['levels'][
    "Fractal"] = """As you see, several doors lead to the exit.\nThere is only one that can be opened."""

help_menus_list['levels']["Tesseract"] = """The tesseract is hidden in the equations."""

help_menus_list['levels']["Oval_track_puzzle"] = help_menus_list["cheat code"]

help_menus_list['levels']["Cartesian"] = """Sorry, there is nothing to help you here."""

help_menus_list['levels'][
    "Eulerian"] = """This level was initially inspired by the seven bridges of Königsberg problem.\nThe difference is that here there is a solution."""

help_menus_list['levels']["Sujiko"] = """Sujiko is a logic-based, combinatorial number-placement puzzle."""

help_menus_list['levels']["Electricity"] = help_menus_list['NAND 3']

help_menus_list['levels']["Permutations"] = """Every permutation can be writen as a product of 2-cycles.\n\nYou can try to find not only one solution, but the fastest one."""

help_menus_list['levels']["Inversions"] = """This level looks a lot like the level "Permutations"."""

help_menus_list['levels']["Pancake sorting"] = """Pancake sorting is a real computational problem."""

help_menus_list['levels']["Wave"] = """The path to the exit is not so long."""

help_menus_list['levels']["Cube"] = help_menus_list['random exit']

help_menus_list['levels']["Error"] = help_menus_list['E']

help_menus_list['levels']["House"] = """Does your house have forty doors?"""

help_menus_list['levels']["The_4th_dimension"] = """More rotations..."""

help_menus_list['levels']["Draw"] = """You have to draw a house."""

help_menus_list['levels']["Takuzu"] = """Takuzu is a logic puzzle involving placement of two symbols, often 1s and 0s, on a rectangular grid."""

help_menus_list['levels']["Travelling salesman"] = "The travelling salesman is a NP-complete problem."

help_menus_list['levels']["No three in line"] = """The no three in line problem is a discrete geometry problem."""

help_menus_list['levels']["Manhattan_distance"] = """The cheat code might be very useful here."""

help_menus_list['levels']["Diagonal"] = """To solve this level you need to solve a 4*4 sudoku grid."""

help_menus_list['levels']["Sudoku"] = """It looks a lot like the level diagonal."""

help_menus_list['levels']["Knight"] = """To solve this level you need to find a knight's tour."""

help_menus_list['levels']["Hungarian_rings"] = help_menus_list['random configuration']

help_menus_list['levels']["Water pouring"] = """You have 3 jugs of liquid, and you need to pour water from one to another."""

help_menus_list['levels']["Syracuse"] = """The solution is pretty long."""

help_menus_list['levels']["Five"] = help_menus_list['random'] + """\n\nThere might be several solutions."""

help_menus_list['levels']["Shuffled"] = help_menus_list['random'] + """\n\nThere might be several solutions."""

help_menus_list['levels']["Sign"] = 'You might need the help of a computer to solve this one.'

help_menus_list['levels']["Combinatorics"] = help_menus_list['N3L']

help_menus_list['levels']["Temple"] = """This level is the retranscription of a really known puzzle game.\nOnce you find which game it is, the level is over."""

help_menus_list['levels']["Puzzle"] = """This level is inspired from the 15-puzzle."""

help_menus_list['levels']["Solitaire"] = help_menus_list['JUMP']

help_menus_list['levels']["MOLS"] = 'MOLS stands for "Mutually Orthogonal Latin Squares".'

help_menus_list['levels']["Separation"] = """Good luck !"""

help_menus_list['levels']["Small panex"] = help_menus_list['INF0']

help_menus_list['levels']["Zebra"] = """There are five houses.\n\n""" + help_menus_list['see other doors']

help_menus_list['levels']["Bridges"] = """There are seven bridges in Königsberg."""

help_menus_list['levels']["Chinese postman problem"] = """In graph theory the Chinese postman problem is to find a shortest closed path that visits every edge of a connected undirected graph at least once."""

help_menus_list['levels']["Postman"] = """You need to visit every house.\nThis level looks a lot like the level named "bridges"."""

help_menus_list['levels']["Parking"] = """If a door equation is not visible, it means it is always open."""

help_menus_list['levels']["Panex"] = """You are on your own."""

help_menus_list['levels']["Superflip"] = help_menus_list['see other doors']

help_menus_list['levels']["Doppelganger"] = help_menus_list['random']

help_menus_list['levels']["Random - Binary Tree"] = help_menus_list['random']

help_menus_list['levels']["Random - Blind alley"] = """The doors form a bull graph.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Random - Boustrophedon"] = """The doors form a Butterfly graph.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Random - Bull"] = """The doors form a bull graph.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Random - Butterfly"] = """The doors form a Butterfly graph.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Random - Come back"] = help_menus_list['random']

help_menus_list['levels']["Random - Cuboctahedron"] = help_menus_list['random']

help_menus_list['levels']["Random - Gemini"] = help_menus_list['random']

help_menus_list['levels']["Random - K2"] = help_menus_list['random']

help_menus_list['levels']["Random - K5"] = """Welcome to hell.\n\n""" + help_menus_list['random']

help_menus_list['levels']["Random - K3,3"] = help_menus_list['random']

help_menus_list['levels']["Random - Ladder"] = help_menus_list['random']

help_menus_list['levels']["Random - Line"] = help_menus_list['random']

help_menus_list['levels']["Random - Turning"] = help_menus_list['random']

help_menus_list['levels']["Random - Petersen"] = help_menus_list['random']

help_menus_list['levels']["Random - Simple"] = help_menus_list['random']

help_menus_list['levels']["Random - Star"] = help_menus_list['random']

help_menus_list['levels']["Random - Starting point"] = help_menus_list['random']

help_menus_list['levels']["Random - Tetractys"] = help_menus_list['random']

help_menus_list['levels']["Random - Wheel"] = help_menus_list['random']