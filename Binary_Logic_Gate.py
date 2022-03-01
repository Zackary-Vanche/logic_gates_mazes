# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:47:18 2022

@author: utilisateur
"""

class Binary_Logic_Gate:

    """
    Les booléens sont représentés par les chiffres 0 et 1.
    Une porte logique est une fonction
    qui prend en entrée deux booléens et qui renvoie un booléen.
    Chaque porte logique est représentée par un quadruplet de booléen
    qui sont les résultats de la porte logique pour différentes entrées.
    On note p une porte logique.
    Les booléens représentant cette dernière sont donnés dans l'ordre suivant:
        p(0,0), p(0,1), p(1,0), p(1,1)
    """

    def __init__(self,
                 results_list=[None, None, None, None]):
        if isinstance(results_list, str):
            results_list = Binary_Logic_Gate.shortcuts_gates[results_list]
        self.results_list = results_list
        self.depth = 0
        self.str_results_list = ''
        for i in self.results_list:
            self.str_results_list = self.str_results_list + str(i)
        self.switch = None
        name = Binary_Logic_Gate.reverse_shortcuts_gates[self.str_results_list]
        self.name = name

    def func(self, a, b):
        if a is None or b is None:
            return None
        else:
            return self.results_list[int(2*a+b)]

    def get_results_list(self):
        return self.results_list

    def invert_gate(self):
        for i in range(4):
            self.results_list[i] = int(not self.results_list[i])

    def __str__(self):
        l_txt = []
        k = 0
        for i in range(2):
            for j in range(2):
                depth_spaces = '|   '*(self.depth+1)
                result_k = self.results_list[k]
                line = """{}{} {} | {}""".format(depth_spaces, i, j, result_k)
                l_txt.append(line)
                k += 1
        return '\n'.join(l_txt)

    def opposite_gate_name(self):
        str_results_list_inv = ''
        for i in self.results_list:
            str_results_list_inv = str_results_list_inv + str(int(not(i)))
        return Binary_Logic_Gate.reverse_shortcuts_gates[str_results_list_inv]

    def invert_A_B_gate_name(self):
        results_list = self.results_list
        str_results_list_inv = ''
        for i in [0, 2, 1, 3]:
            str_results_list_inv += str(int(results_list[i]))
        return Binary_Logic_Gate.reverse_shortcuts_gates[str_results_list_inv]

    shortcuts_gates = {'FALSE': [0, 0, 0, 0],
                       'AND':   [0, 0, 0, 1],
                       # A AND NOT B
                       'ANB':   [0, 0, 1, 0],
                       'A':     [0, 0, 1, 1],
                       # B AND NOT A
                       'BNA':   [0, 1, 0, 0],
                       'B':     [0, 1, 0, 1],
                       'XOR':   [0, 1, 1, 0],
                       'OR':    [0, 1, 1, 1],
                       'NOR':   [1, 0, 0, 0],
                       'XNOR':  [1, 0, 0, 1],
                       'NB':    [1, 0, 1, 0],
                       # Implication B => A
                       'AONB':  [1, 0, 1, 1],
                       'NA':    [1, 1, 0, 0],
                       # Implication A => B
                       'BONA':  [1, 1, 0, 1],
                       'NAND':  [1, 1, 1, 0],
                       'TRUE':  [1, 1, 1, 1]}

    reverse_shortcuts_gates = {}
    for key in shortcuts_gates.keys():
        results_list = shortcuts_gates[key]
        str_results_list = ''
        for i in results_list:
            str_results_list = str_results_list + str(i)
        reverse_shortcuts_gates[str_results_list] = key