# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:01:51 2022

@author: utilisateur
"""

class Logic_Gate:


    def __init__(self,
                 results_list=[]):
        if isinstance(results_list, str):
            results_list = Logic_Gate.shortcuts_gates[results_list]
        self.results_list = results_list
        self.depth = 0
        self.str_results_list = ''
        for i in self.results_list:
            self.str_results_list = self.str_results_list + str(i)
        self.switch = None
        name = Logic_Gate.reverse_shortcuts_gates[self.str_results_list]
        self.name = name


    def func(self, branches_values_list):
        if None in branches_values_list:
            return None
        else:
            k = 0
            for i in range(len(branches_values_list)):
                b = branches_values_list[i]
                e = len(branches_values_list)-i-1
                k += b*2**e
            return self.results_list[int(k)]


    def get_results_list(self):
        return self.results_list


    def invert_gate(self):
        for i in range(4):
            self.results_list[i] = int(not self.results_list[i])


    def __str__(self):
        l_txt = []
        k = 0
        results_list = self.results_list
        n = len(results_list)
        depth_spaces = '|   '*(self.depth+1)
        n_decimals_bin = len(bin(n)) - 3
        for k in range(n):
            result_k = results_list[k]
            k_bin = bin(k)[2:]
            k_bin_str = ''
            for decimal in k_bin:
                k_bin_str = k_bin_str + decimal + ' '
            while len(k_bin_str) < 2*n_decimals_bin:
                k_bin_str = '0 ' + k_bin_str
            line = depth_spaces + k_bin_str + "| {}".format(result_k)
            l_txt.append(line)
            k += 1
        return '\n'.join(l_txt)


    def opposite_gate_name(self):
        str_results_list_inv = ''
        for i in self.results_list:
            str_results_list_inv = str_results_list_inv + str(int(not(i)))
        return Logic_Gate.reverse_shortcuts_gates[str_results_list_inv]
    

    def invert_A_B_gate_name(self):
        results_list = self.results_list
        str_results_list_inv = ''
        for i in [0, 2, 1, 3]:
            str_results_list_inv += str(int(results_list[i]))
        return Logic_Gate.reverse_shortcuts_gates[str_results_list_inv]

    def AND_list(n):
        l = [0]*2**n
        l[-1] = 1
        return l
    
    def NOR_list(n):
        l = [0]*2**n
        l[0] = 1
        return l
    
    def OR_list(n):
        l = [1]*2**n
        l[0] = 0
        return l
    
    def NAND_list(n):
        l = [1]*2**n
        l[-1] = 0
        return l

    shortcuts_gates = {'FALSE' : [0, 0],
                       'BUFFER' : [0, 1],
                       'TRUE' : [1, 1],
                       'NOT' : [1, 0],
                       'FALSE_2': [0, 0, 0, 0],
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
                       'TRUE_2':  [1, 1, 1, 1]}
    
    for n in range(3, 11):
        shortcuts_gates['AND_{}'.format(n)] = AND_list(n)
        shortcuts_gates['NOR_{}'.format(n)] = NOR_list(n)
        shortcuts_gates['OR_{}'.format(n)] = OR_list(n)
        shortcuts_gates['NAND_{}'.format(n)] = NAND_list(n)
    

    reverse_shortcuts_gates = {}
    for key in shortcuts_gates.keys():
        results_list = shortcuts_gates[key]
        str_results_list = ''
        for i in results_list:
            str_results_list = str_results_list + str(i)
        reverse_shortcuts_gates[str_results_list] = key
        
if __name__ == "__main__":
    
    # for gate_name in Logic_Gate.shortcuts_gates.keys():
    #     gate = Logic_Gate(gate_name)
    #     results_list = gate.results_list
    #     assert not '1' in bin(len(results_list))[:2]
    #     print('')
    #     print(gate_name)
    #     print(gate)
    #     print('opposite_gate_name\n', gate.opposite_gate_name())
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    