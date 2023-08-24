help_menus_list = {}

######################
## TREE'S NOTATIONS ##
######################

# 'NOR'

help_menus_list['basis'] = '''
D0 = S0 means : 
    D0 is open if S0 is turned on.'''
    
help_menus_list['V'] = '''
The elements named V0, V1, etc. are intermediate values.'''

help_menus_list['NOT'] = """
¬ means 'NOT'.
¬S0 = 1 if S0 = 0
¬S0 = 0 if S0 = 1
Be carefull with the negation, because :
    ¬ 1 = 0
    ¬ 0 = 1"""

help_menus_list['MINUS'] = """
- means 'MINUS'. -S0 is the opposite of S0."""

help_menus_list['AND'] = """
& means 'AND'.
D0 = & S0 S1 means :
    D0 is open only if (S0, S1) = (1,1)"""

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

help_menus_list['XOR XNOR'] = """
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
+ S0 S1 is the sum of S0 and S1."""

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
Used with more than 2 operands, it means that all its operands are equal to each other.'''

help_menus_list['EQUSET'] = '''
D0 = ~  ( S0 ; S2 ; ...) ( S1 ; S3 ; ...) means :
    D0 is open if the two sets ( S0 ; S2 ; ...) and ( S1 ; S3 ; ...) contain the same elements, but not obligatorily in the same order.
D0 = ~  ( S0 ; S2 ) ( S1 ; S3) means :
    D0 = | & = S0 S1 = S2 S3 & = S0 S3 = S2 S1'''

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
You can use this notation with more than 3 switches, and with very operand.
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
        If a switch is turned on, it is surrounded, and you say it is equal to 1. If it is turned off, it is equal to 0.
    Doors (D0, D1, D2, ...) :    
        If a door is open, it is surrounded, and you say it is equal to 1. If it is closed, it is equal to 0.
        Diamond-shape doors are two-way while triangle-shaped doors are one-way only.

To go in a room, use a switch or travel by a door, write its name and press [Enter].
You can only use switches of your current room, and travel by open doors.
You can always erase what you wrote with the backspace key.

To start the level again from the beginning, press [B] and then [Enter].
To go to the next (previous) page, press the right (left) arrow key."""

help_menus_list['directions keys'] = """
To change level, you can use :

    the right arrow key to go to the next page
    the left arrow key to go to the previous page

    L and the number of the level you want to go to.
    For instance, if you write L12 and then press [Enter] you will go to the level 12.

Instead of taping the action you want to do, you can see the possibles actions by using the ALT keys.
"""

help_menus_list['go in a room'] = """
To go directly in a room, you can type its name (if it is possible for you to go there). The exit room is called "EXIT" or "RE"."""

help_menus_list['reminder B'] = """
[Reminder] : To start the level again from the beginning, press [B] and then [Enter]."""

help_menus_list['write several actions'] = """
Instead of writing actions one by one, one can write several at a time, separated by spaces.
For instance, you can write :
    S0 S1 D0
if you want to turn on S0, S1 and then use the door D0."""

help_menus_list['leave the game'] = """
To leave the game, you can click an the cross but also press [ESCAPE]."""

help_menus_list['random'] = """
Press [N] and then [Enter] to get new random level."""

help_menus_list['UP DOWN'] = 'If you use the [UP] and [DOWN] keys, you can switch which equation appears first.'

############
## LEVELS ##
############

help_menus_list['levels'] = {}

help_menus_list['levels']["Hello world"] = '\n'.join([help_menus_list['introduction'], help_menus_list['basis']])

help_menus_list['levels']["Playground"] = '\n'.join([help_menus_list['NOT'],
                                                     help_menus_list['write several actions']])

help_menus_list['levels']["Initiation"] = '\n'.join([help_menus_list['OR']])

help_menus_list['levels']["Linear"] = '\n'.join([help_menus_list['AND'],
                                                  help_menus_list['AND and NOT'],
                                                  help_menus_list['directions keys'],])

help_menus_list['levels']['Loop'] = '\n'.join([help_menus_list['go in a room'],
                                               help_menus_list['Introduction thuth table']])

help_menus_list['levels']["Forest"] = '\n'.join([help_menus_list['XOR XNOR'],
                                                 help_menus_list['leave the game']])

help_menus_list['levels']["Backward"] = '\n'.join([help_menus_list['parenthesis'],
                                                   help_menus_list['brackets'],
                                                   ])

help_menus_list['levels']["Numeration"] = '\n'.join([help_menus_list['EQU'],
                                                     help_menus_list['BIN'],
                                                     help_menus_list['numerical value']])

help_menus_list['levels']["Sorted"] = '\n'.join([help_menus_list['V'],
                                                 help_menus_list['INF'],
                                                 help_menus_list['SUP'],
                                                 help_menus_list['INFOREQU'],
                                                 help_menus_list['SUPOREQU'],
                                                 help_menus_list['EQUSET']])

help_menus_list['levels']["Arithmetic"] ='\n'.join([help_menus_list['SUM'],
                                                    help_menus_list['MINUS'],
                                                    help_menus_list['PROD'],
                                                    help_menus_list['DIV'],
                                                    help_menus_list['MOD'],
                                                    help_menus_list['ABS'],
                                                    help_menus_list['POW'],
                                                    help_menus_list['DIST'],
                                                    help_menus_list['UP DOWN'],
                                                    ])

help_menus_list['levels']["Inside out"] = '\n'.join([help_menus_list['IN'], help_menus_list["cheat code"]])

help_menus_list['levels']["Superpermutation"] = help_menus_list['INLIST']

help_menus_list['levels']["3 SAT"] = """The 3 SAT problem is NP complete."""

help_menus_list['levels']["Longest path"] = "The longest path problem is NP-complete."

help_menus_list['levels']["Hitting set"] = """The hitting set is one of the Karp's 21 NP-complete problems.\nIt is equivalent to the set cover problem\n"""

help_menus_list['levels']["Sheffer stroke"] = """This level has several solutions..."""

help_menus_list['levels']["Peirce's arrow"] = """This level has several solutions..."""

help_menus_list['levels']["Independent set"] = "The independent set is one of the Karp's 21 NP-complete problems."

help_menus_list['levels']["Dominating set"] = """Finding dominating set is a NP-Complete problem."""

help_menus_list['levels']["Exact cover"] = """The exact cover is one of the Karp's 21 NP-complete problems.\n"""

help_menus_list['levels']["Min-cut"] = """A cut is a partition of the vertices of a graph into two disjoint subsets.\nYou must cut as few edges as possible."""

help_menus_list['levels']["Max-cut"] = """You must cut as many edges as possible."""

help_menus_list['levels']["Elementary"] = """An elementary permutation is a swap of two adjacent elements.\n"""

help_menus_list['levels']["Singleton"] = """A singleton is a set with exactly one element."""

help_menus_list['levels']["Taxicab number"] = """Taxicab numbers are also called Hardy–Ramanujan numbers."""

help_menus_list['levels']["Walk"] = """In graph theory, a walk is a finite or infinite sequence of edges which joins a sequence of vertices.\nHere, you cannot revisit vertices and edges."""

help_menus_list['levels']["Trail"] = """A trail is a walk in which all edges are distinct."""

help_menus_list['levels']["Path"] = """A path is a trail in which all vertices (and therefore also all edges) are distinct."""

help_menus_list['levels']["Dichotomy"] = """? is a random integer.\n\nOnce you found the value of ?, the level is over.\n\n"""

help_menus_list['levels']["Partition"] = """The partition is one of the Karp's 21 NP-complete problems.\n"""

help_menus_list['levels']["Knapsack"] = """The knapsack is one of the Karp's 21 NP-complete problems."""

help_menus_list['levels']["Code"] = "You may want to learn what the Gray code is."

help_menus_list['levels']["The 4 queens"] = """This level is inspired from the 8 queens problem."""

help_menus_list['levels']["Harmony"] = """This level has several solutions."""

help_menus_list['levels']["K"] = """You have to locate as many knights in a chessboard as possible."""

help_menus_list['levels']["Alice and Bob"] = """Alice wants to send a package to Bob."""

help_menus_list['levels']["Nonogram"] = help_menus_list['NONO']

help_menus_list['levels']["Tetris"] = """Each number can represent a position in the plane.\n"""

help_menus_list['levels']["Mastermind"] = help_menus_list['MAS'] + """\n\n?0 ?1 ?2 ?3 ?4 ?5 ?6 ?7 are switches.\n\nYou have to guess their values."""

help_menus_list['levels']["Baguenaudier"] = '''The baguenaudier is an old puzzle game.'''

help_menus_list['levels']["4 colors theorem"] = """Each couple of switches represent a color.\n"""

help_menus_list['levels']["Matrix"] = """To solve this level you need to do a 5*5 matrix inversion."""

help_menus_list['levels']["River"] = """You want to cross the river with a wolf, a goat and a cabbage."""

help_menus_list['levels']["Conjunctive normal form"] = "This level is the same than the level named '3 SAT', but it is random."

help_menus_list['levels']["Betweenness"] = help_menus_list['BETWEEN']

help_menus_list['levels']["Eulerian"] = """This level was initially inspired by the seven bridges of Königsberg problem.\nThe difference is that here there is a solution."""

help_menus_list['levels']["Sujiko"] = """Sujiko is a logic-based, combinatorial number-placement puzzle."""

help_menus_list['levels']["Permutations"] = """Every permutation can be writen as a product of 2-cycles.\n\nYou can try to find not only one solution, but the fastest one."""

help_menus_list['levels']["Pancake sorting"] = """Pancake sorting is a real computational problem."""

help_menus_list['levels']["Error"] = help_menus_list['E']

help_menus_list['levels']["Takuzu"] = """Takuzu is a logic puzzle involving placement of two symbols, often 1s and 0s, on a rectangular grid."""

help_menus_list['levels']["Travelling salesman"] = "The travelling salesman is a NP-complete problem."

help_menus_list['levels']["No three in line"] = """The no three in line problem is a discrete geometry problem."""

help_menus_list['levels']["Minimum spanning tree"] = """A Minimum spanning tree is the subset of edges in a graph that connects all the vertices together\nwith the minimum total edge weight possible, without forming any cycles."""

help_menus_list['levels']["Small honeycomb"] = """Honeycombs are supposed to be hexagonal...\nThe method of resolution you should use for this level is the same as for the level "minimum spanning tree".\n"""

help_menus_list['levels']["Diagonal"] = """To solve this level you need to solve a 4*4 sudoku grid."""

help_menus_list['levels']["Sudoku"] = """It looks a lot like the level diagonal."""

help_menus_list['levels']["Knight"] = """To solve this level you need to find a knight's tour."""

help_menus_list['levels']["Water pouring"] = """You have 3 jugs of liquid, and you need to pour water from one to another."""

help_menus_list['levels']["Syracuse"] = """The solution is pretty long."""

help_menus_list['levels']["Five"] = """There might be several solutions."""

help_menus_list['levels']["Shuffled"] = """There might be several solutions."""

help_menus_list['levels']["Combinatorics"] = help_menus_list['N3L']

help_menus_list['levels']["Temple"] = """This level is the retranscription of a really known puzzle game.\nOnce you find which game it is, the level is over."""

help_menus_list['levels']["Puzzle"] = """This level is inspired from the 15-puzzle."""

help_menus_list['levels']["Solitaire"] = help_menus_list['JUMP']

help_menus_list['levels']["MOLS"] = 'MOLS stands for "Mutually Orthogonal Latin Squares".'

help_menus_list['levels']["Small panex"] = help_menus_list['INF0']

help_menus_list['levels']["Zebra"] = """There are five houses.\n\n"""

help_menus_list['levels']["Bridges"] = """There are seven bridges in Königsberg."""

help_menus_list['levels']["Chinese postman problem"] = """In graph theory the Chinese postman problem is to find a shortest closed path that visits every edge of a connected undirected graph at least once."""

help_menus_list['levels']["Panex"] = ""

help_menus_list['levels']["Superflip"] = ""