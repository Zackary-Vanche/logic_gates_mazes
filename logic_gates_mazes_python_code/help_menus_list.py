# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:06:34 2022

@author: utilisateur
"""

help_menus_list = {}

    ######################
    ## TREE'S NOTATIONS ##
    ######################

#'NOR' 

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
b (S0 S1 ...) is the number whose binary big endian code is S0 S1 etc.
For example:
    b (S0 S1 S2) = + (S0 * 2 S1 * 4 S2)"""

help_menus_list['IN'] = """
The operator i takes two arguments : une switch and a switch list.
It returns the value 1 if the switch is included in the list, 0 if not.
For example:
    i 0 [1 2] = 0
    i 4 [4 2] = 1"""

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
        Diamond-shape doors are two-way while triangle-shaped doors are one-way only.      
If you made a mistake when taping the name of a door or a switch, you can always erase it by taping on the backspace key.

To leave the help menu (or come back to it), press [H].
To start the level again from the beginning, press [B].
To go to the next level, press the right arrow key.

On the left size window of the game are equations that tell you when a door is open :
These equations work with any name of door or switch."""

help_menus_list['change level'] = """
To change level, you can use :

    the right arrow key to go to the next level
    the left arrow key to go to the previous level
    the down arrow key to go to the first level
    the up arrow key to go to the last level

    L and the number of the level you want to go to.
    For instance, L12 will make you go to the level number 12."""

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

    ############
    ## LEVELS ##
    ############
    
help_menus_list['levels'] = {}

help_menus_list['levels']["Hello_World"] = '\n'.join([help_menus_list['introduction'],
                                                      help_menus_list['basis'],
                                                      help_menus_list['OR']])

help_menus_list['levels']["Linear"] = '\n'.join([help_menus_list['AND'],
                                                 help_menus_list['NOT'],
                                                 help_menus_list['AND and NOT']])

help_menus_list['levels']['Loop'] = help_menus_list['change level']

help_menus_list['levels']["Backward"] = help_menus_list['parenthesis']

help_menus_list['levels']["Bis repetita"] = help_menus_list['XOR']

help_menus_list['levels']["Binary"] = help_menus_list['go in a room']

help_menus_list['levels']["OR"] = '''Enjoy the game while it is still easy.'''

help_menus_list['levels']["Crossroad"] = help_menus_list['reminder B']

help_menus_list['levels']["Square"] = help_menus_list['write several actions']

help_menus_list['levels']["Infinity"] = help_menus_list["cheat code"]

help_menus_list['levels']["Fluid"] = help_menus_list['Introduction thuth table']

help_menus_list['levels']["Bipartite"] = """Several paths lead to the exit."""

help_menus_list['levels']["Hamiltonian"] = """Don't look for something too complicated."""

help_menus_list['levels']["Pong"] = '\n'.join([help_menus_list['numerical value'],
                                               help_menus_list['SUM'],
                                               help_menus_list['EQU']])

help_menus_list['levels']["Longest path"] = "The longest path problem is NP-complete."
                             
help_menus_list['levels']["Hitting set"] = """The hitting set is one of the Karp's 21 NP-complete problems.
It is equivalent to the set cover problem\n""" + '\n'.join([help_menus_list['INF'],
                                                            help_menus_list['SUP'],
                                                            help_menus_list['INFOREQU'],
                                                            help_menus_list['SUPOREQU']])

help_menus_list['levels']["Independent set"] = "The independent set is one of the Karp's 21 NP-complete problems."

help_menus_list['levels']["Dominating set"] = """Finding dominating set is a NP-Complete problem."""

help_menus_list['levels']["Exact cover"] = """The exact cover is one of the Karp's 21 NP-complete problems."""

help_menus_list['levels']["Odd"] = help_menus_list['leave the game']

help_menus_list['levels']["Recurrence"] = help_menus_list['brackets']

help_menus_list['levels']["Point of no return"] = help_menus_list['XNOR']

help_menus_list['levels']["Naturals"] = '\n'.join([help_menus_list['ABS'],
                                                   help_menus_list['MINUS'],
                                                   help_menus_list['BIN']])

help_menus_list['levels']["Parallel"] = """The "Guess and check" method works well here."""

help_menus_list['levels']["Pythagorean"] = help_menus_list['POW']

help_menus_list['levels']["Taxicab number"] = """Taxicab numbers are also called Hardy–Ramanujan numbers."""

help_menus_list['levels']["Chessboard"] = """If you remove the exit, the graph of this level is the graph of the possible moves of a knight in a 3*4 rectangle.
However, sometimes here doors are one-way only."""

help_menus_list['levels']["Tetrahedron"] = """The logic expressions of the doors of this level have been calculated by computer.
The program that calculated it already knew all the rest of the level.

This level looks complicated, but you do only need to let the game lead you to the exit."""

help_menus_list['levels']["The 4 queens"] = """This level is inspired from the 8 queens problem."""

help_menus_list['levels']["Alice and Bob"] = """Alice wants to send a package to Bob."""

help_menus_list['levels']["Nonogram"] = help_menus_list['NONO']

help_menus_list['levels']["Crystal"] = """If you make a mistake, you have to start all over again."""

help_menus_list['levels']["Pancake sorting"] = """Pancake sorting is a real computational problem."""

help_menus_list['levels']["Tetris"] = """Each number can represent a position in the plane.\n""" + help_menus_list['EQUSET']

help_menus_list['levels']["4 colors theorem"] = """Each couple of switches represent a color.\n""" + help_menus_list["PROD"]

help_menus_list['levels']["Partition"] = """The partition is one of the Karp's 21 NP-complete problems.\n""" + help_menus_list['EQU']

help_menus_list['levels']["Knapsack"] = """The knapsack is one of the Karp's 21 NP-complete problems."""

help_menus_list['levels']["Magic square"] = help_menus_list['DIFF']

help_menus_list['levels']["XOR"] = help_menus_list['NAND']

help_menus_list['levels']["Matrix"] = """To solve this level you need to do a 5*5 matrix inversion."""

help_menus_list['levels']["River"] = """You want to cross the river with a wolf, a goat and a cabbage."""

help_menus_list['levels']["Tree"] = """The tree is hidden in the equations."""

help_menus_list['levels']["Fractal"] = """As you see, several doors lead to the exit.
There is only one that can be opened."""

help_menus_list['levels']["Tesseract"] = """The tesseract is hidden in the equations."""

help_menus_list['levels']["Cartesian"] = """Sorry, there is nothing to help you here."""

help_menus_list['levels']["Eulerian"] = """This level was initially inspired by the seven bridges of Königsberg problem.
The difference is that here there is a solution."""

help_menus_list['levels']["Electricity"] = help_menus_list['NAND 3']

help_menus_list['levels']["Wave"] = help_menus_list['XOR 3']

help_menus_list['levels']["Travelling salesman"] = help_menus_list['DIST']

help_menus_list['levels']["Dead_ends"] = """Even if it is the first level that actually looks like a printed circuit board, you have been in a computer all this time."""

help_menus_list['levels']["Manhattan_distance"] = """The cheat code might be very useful here."""

help_menus_list['levels']["Knight"] = """To solve this level you need to find a knight's tour."""

help_menus_list['levels']["Syracuse"] = help_menus_list['DIV']

help_menus_list['levels']["Temple"] = """This level is the retranscription of a really known puzzle game.
Once you find which game it is, the level is over."""
