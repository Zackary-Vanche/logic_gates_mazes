# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:01:51 2022

@author: utilisateur
"""

# from convert_base_2 import base_2


class Logic_Gate:

    def __init__(self, name):
        self.switch = None
        self.name = name

    def func(self, branches_values_list):
        if None in branches_values_list:
            return None
        if self.name == 'NOT':
            assert len(branches_values_list) == 1
            return not branches_values_list[0]
        if self.name == 'AND':
            return not 0 in branches_values_list
        if self.name == 'OR':
            return 1 in branches_values_list
        if self.name == 'XOR':
            return sum(branches_values_list) == 1
        if self.name == 'XNOR':
            return not sum(branches_values_list) == 1
        if self.name == 'EQU':
            assert len(branches_values_list) >= 2
            for i in range(len(branches_values_list)-1):
                if branches_values_list[i] != branches_values_list[i+1]:
                    return 0
            return 1
        if self.name == 'EQUSET':
            assert len(branches_values_list) % 2 == 0
            n = len(branches_values_list) // 2
            return set(branches_values_list[:n]) == set(branches_values_list[n:])
        if self.name == 'DIFF':
            assert len(branches_values_list) >= 2
            for i in range(len(branches_values_list)-1):
                if branches_values_list[i] != branches_values_list[i+1]:
                    return 1
            return 0
        if self.name == 'NAND':
            return 0 in branches_values_list
        if self.name == 'NOR':
            return not 1 in branches_values_list
        if self.name == 'SUM':
            return sum(branches_values_list)
        if self.name == 'PROD':
            p = 1
            for x in branches_values_list:
                p = p * x
            return p
        if self.name == 'ABS':
            assert len(branches_values_list) == 1
            return abs(branches_values_list[0])
        if self.name == 'MINUS':
            assert len(branches_values_list) == 1
            return -branches_values_list[0]
        if self.name == 'INF':
            assert len(branches_values_list) == 2
            return branches_values_list[0] < branches_values_list[1]
        if self.name == 'INFOREQU':
            assert len(branches_values_list) == 2
            return branches_values_list[0] <= branches_values_list[1]
        if self.name == 'SUP':
            assert len(branches_values_list) == 2
            return branches_values_list[0] > branches_values_list[1]
        if self.name == 'SUPOREQU':
            assert len(branches_values_list) == 2
            return branches_values_list[0] >= branches_values_list[1]
        if self.name == 'ANB':
            assert len(branches_values_list) == 2
            return not branches_values_list[0] and not branches_values_list[1]
        if self.name == 'BNA':
            assert len(branches_values_list) == 2
            return not branches_values_list[1] and not branches_values_list[0]
        if self.name == 'AONB':
            assert len(branches_values_list) == 2
            return not branches_values_list[0] or not branches_values_list[1]
        if self.name == 'BONA':
            assert len(branches_values_list) == 2
            return not branches_values_list[1] or not branches_values_list[0]
        if self.name == 'BIN':
            s = 0
            for i in range(len(branches_values_list)):
                s += branches_values_list[i] * 2**i
            return s
        return None

    def get_results_list(self):
        return self.results_list

    def invert_gate(self):
        for i in range(4):
            self.results_list[i] = int(not self.results_list[i])

    def __str__(self): # TODO : rewrite, no self.results_list anymore 
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
        
if __name__ == "__main__":
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    