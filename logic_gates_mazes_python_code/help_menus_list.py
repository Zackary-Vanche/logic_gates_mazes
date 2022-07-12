# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:06:34 2022

@author: utilisateur
"""

help_menus_list = {}

help_menus_list["Hello_World"] = """You are trapped in the inside of a computer and want to reach the exit.

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
    
On the left size window of the game are equations that tell you when a door is open :
    (These equations work with any name of door or switch.)
    D0 = S0 means : 
        D0 is open if S0 is turned on.
    D2 = OR S1 S2 means :
        D1 is open if S1 or S2 is turned on (i.e. if (S0, S1) = (0,1) or (S0, S1) = (1,0) or (S0, S1) = (1,1))
        It can also be written : D2 = | S1 S2
    
To leave the help menu (or come back to it), press [H].
To start the level again from the beginning, press [B].
To go to the next level, press the right arrow key.
"""

help_menus_list["Linear"] = """Several new notations are used in this level :
    
    Negation :
    NOT S0 = 1 if S0 = 0
    NOT S0 = 0 if S0 = 1
    ¬S0 = NOT S0
    Be carefull with the negation, because you have :
        ¬ 1 = 0
        ¬ 0 = 1
    
    D0 = AND S0 S1 means :
        D0 is open if (S0, S1) = (1,1)
    It can also be written : 
        D2 = & S0 S1
    
    By combining these notations, you can write :
    D1 = & S2 ¬ S3 means :
        D1 is open if (S2, S3) = (1,0)
    D2 = AND ¬ S4 S5 means :
        D2 is open if (S4, S5) = (0,1)
    D3 = & ¬ S6 ¬ S7  S6 S7 means :
        D3 is open if (S6, S7) = (0,0)
        It can also be written :
        D3 = NOR S6 S7
        D3 = ¬| S6 S7
"""

help_menus_list["Loop"] = """To change level, you can use :

    the right arrow key to go to the next level
    the left arrow key to go to the previous level
    the down arrow key to go to the first level
    the up arrow key to go to the last level

    L and the number of the level you want to go to.
    For instance, L12 will make you go to the level number 12.
"""

help_menus_list["Backward"] = """One new notation is used in this level :

    To simplify notations, parentheses are used.

    Instead of writing :
        D0 = & S0 & S1 S2
    you can write :
        D0 = & S0 ( & S1 S2 )
    or :
        D0 = & ( S0 S1 S2 )
    You can use this notation with more than 3 switches.
    You can also use it with | instead of &.

    In this level, the notation is used with negations :
        D0 = & ¬ S0 ( & S1 S2 )
           = & ( ¬ S0 S1 S2 )
"""

help_menus_list["Bis repetita"] = """One new operand is used in this level : XOR

    XOR means exclusive or.
    D0 = XOR S0 S1 = ^ S0 S1 means :
        D0 is open if S0 is different from S1.
"""

help_menus_list["Binary"] = """At every step, you have only one action possible :
    In the beginning, you can only turn on S0.
    Then, a door opens, so you use it...
    And so on...
    
To go directly on a room, you can type its name (if it is possible for you to go there).
The exit room is called RE.
"""

help_menus_list["Crossroad"] = """[Reminder] : To start the level again from the beginning, press [B].
"""

help_menus_list["Square"] = """Instead of writing actions one by one, one can write several at a time, separated by spaces.
For instance, you can write :
    S0 S1 D0
if you want to turn on S0, S1 and then use the door D0.
"""

help_menus_list["Fluid"] = """A truth table tells you the result of a logical expression.
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
      1    1    1
"""

help_menus_list["Independent set"] = """New notations are used:
    
    Sometimes, a switch can be replaced by a numerical value.
    
    + S0 S1 is the sum of S0 and S1
    With parenthesis, the operator + can be used with more than 2 operands:
        + (S0 S1 S2) is the sum of S0, S1 and S2
    
    D0 = < S0 S1 means :
        D0 is open if S0 is inferior to S1
    D0 = > S0 S1 means :
        D0 is open if S0 is superior to S1
"""

help_menus_list["Odd"] = """
To leave the game, you can click an the cross but also press [Q] or [ESCAPE].
"""

help_menus_list["Dominating set"] = """Finding dominating set is a NP-Complete problem.
"""

help_menus_list["Chessboard"] = """If you remove the exit, the graph of this level is the graph of the possible moves of a knight in a 3*4 rectangle.
However, sometimes here doors are one-way only.
"""

help_menus_list["Point_of_no_return"] = """One new operand is used in this level : XNOR

    XOR means exclusive or.
    XNOR is its opposite.
    
    XOR truth table (D0 = XOR S0 S1 = ^ S0 S1):
    S0  S1  D0
      0    0    0
      0    1    1
      1    0    1
      1    1    0  
    In other words, D0 is open if S0 is different from S1.
      
    XNOR truth table (D0 = XNOR S0 S1 = ¬^ S0 S1):
    S0  S1  D0
      0    0    1
      0    1    0
      1    0    0
      1    1    1    
    In other words, D0 is open if S0 = S1.
    
    You can write :
        XOR S0 S1 = | & S0 ¬ S1 & ¬ S0 S1 
        XNOR S0 S1 = | & S0 S1 & ¬ S0 ¬ S1
        XNOR S0 S1 = ¬ XOR S0 S1
"""

help_menus_list["4 colors theorem"] = """One new operand is used in this level :
    
    * S0 S1 is equal to the product of S0 and S1.

Each couple of switches represent a color.
"""

help_menus_list["Alice and Bob"] = """Alice wants to send a package to Bob.
"""

help_menus_list["Recurrence"] = """Sometime, square brackets can be used instead of parentheses.
"""

help_menus_list["Partition"] = """One new notation is used in this level:
    
    D0 = = S0 S1 means :
        D0 is open if S0 is equal to S1
    It is similar to XNOR.

The partition is one of the Karp's 21 NP-complete problems.
"""

help_menus_list["Infinity"] = """A cheat code exists.
If you add the letter A before a command :
    You can turn on a switch even if you are not in its room.
    You can use a door even if it is not open.
    If a door is one-way, you can use it even if you are not in the good room.

Writing A D10 allows you to end this level by cheating.

You can also use the cheat code to go directly in a room by giving its name :
    A R2 allows you to go in the room R2.
The name of the exit room is RE.
"""

help_menus_list["Parallel"] = """The "Guess and check" method works well here.
"""

help_menus_list["Matrix"] = """To solve this level you need to do a 5*5 matrix inversion.
"""

help_menus_list["Tetrahedron"] = """The logic expressions of the doors of this level have been calculated by computer.
The program that calculated it already knew all the rest of the level.
"""

help_menus_list["Knapsack"] = """The knapsack is one of the Karp's 21 NP-complete problems.
"""

help_menus_list["Bipartite"] = """This level has several solutions.
"""

help_menus_list["Alien"] = """Don't look for something too complicated.
"""

help_menus_list["Tesseract"] = """One new notation is used in this level :
    
    D0 = 1 means that D0 is always open.
    
The tesseract is hidden in the equations.
"""

help_menus_list["Tree"] = """The tree is hidden in the equations.
"""

help_menus_list["River"] = """XOR is used with 3 parameters instead of 2.
  
    XOR truth table [D0 = XOR ( S0 S1 S2 )]:
    S0  S1  S2  D0
      0    0    0     0
      0    1    0     1
      1    0    0     1
      1    1    0     0
      0    0    1     1
      0    1    1     0
      1    0    1     0
      1    1    1     0    
    In other words:
    D0 is open if there is exactly one switch among S0, S1 and S2 that is turned on.
    
You want to cross the river with a wolf, a goat and a cabbage.
"""

help_menus_list["Crystal"] = """If you make a mistake, you have to start all over again.
"""

help_menus_list["Cartesian"] = """Sorry, there is nothing to help you here.
"""

help_menus_list["Fractal"] = """As you see, several doors lead to the exit.
There is only one that can be opened."""

help_menus_list["XOR"] = """A new operand is used in this level :

    NAND truth table (D0 = NAND S0 S1 = ¬& S0 S1):
    S0  S1  D0
      0    0    1
      0    1    1
      1    0    1
      1    1    0
"""

help_menus_list["Graph"] = """This level was initially inspired by the seven bridges of Königsberg problem.
The difference is that here there is a solution.
"""

help_menus_list["Dead_ends"] = """Even if it is the first level that actually looks like a printed circuit board, you have been in a computer all this time.
"""

help_menus_list["Electricity"] = """NAND can also apply to 3 parameters instead of 2:

    NAND truth table [D0 = NAND ( S0 S1 S2 ) = ¬& ( S0 S1 S2 )]:
    S0  S1  S2  D0
      0    0    0     1
      0    1    0     1
      1    0    0     1
      1    1    0     1
      0    0    1     1
      0    1    1     1
      1    0    1     1
      1    1    1     0  
"""

help_menus_list["Wave"] = """One new notation is used in this level :
    
    XOR can be used with more than 3 parameters :
        D0 = XOR(S0, S1, ...) means :
            D0 is open if there is exactly one switch among its parameters that is turned on.
"""

help_menus_list["Manhattan_distance"] = """The cheat code might be very useful here.
"""

help_menus_list["Temple"] = """This level is the retranscription of a really known puzzle game.
Once you find which game it is, the level is over.
"""

