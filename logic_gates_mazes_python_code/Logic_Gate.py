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

    def aux_func_NOT(branches_values_list):
        assert len(branches_values_list) == 1
        return not branches_values_list[0]

    def aux_func_AND(branches_values_list):
        return not 0 in branches_values_list

    def aux_func_OR(branches_values_list):
        return 1 in branches_values_list

    def aux_func_XOR(branches_values_list):
        return sum(branches_values_list) == 1

    def aux_func_XNOR(branches_values_list):
        return not Logic_Gate.aux_func_XOR(branches_values_list)

    def aux_func_EQU(branches_values_list):
        assert len(branches_values_list) >= 2
        for i in range(len(branches_values_list)-1):
            if branches_values_list[i] != branches_values_list[i+1]:
                return 0
        return 1

    def aux_func_EQUSET(branches_values_list):
        assert len(branches_values_list) % 2 == 0
        n = len(branches_values_list) // 2
        return set(branches_values_list[:n]) == set(branches_values_list[n:])

    def aux_func_DIFF(branches_values_list):
        assert len(branches_values_list) >= 2
        branches_values_list_sorted = sorted(branches_values_list)
        for i in range(len(branches_values_list_sorted)-1):
            if branches_values_list_sorted[i] == branches_values_list_sorted[i+1]:
                return 0
        return 1

    def aux_func_NAND(branches_values_list):
        return not Logic_Gate.aux_func_AND(branches_values_list)

    def aux_func_NOR(branches_values_list):
        return not Logic_Gate.aux_func_OR(branches_values_list)

    def aux_func_SUM(branches_values_list):
        return sum(branches_values_list)

    def aux_func_PROD(branches_values_list):
        p = 1
        for x in branches_values_list:
            p = p * x
        return p

    def aux_func_ABS(branches_values_list):
        assert len(branches_values_list) == 1
        return abs(branches_values_list[0])

    def aux_func_MINUS(branches_values_list):
        assert len(branches_values_list) == 1
        return -branches_values_list[0]

    def aux_func_INF(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0] < branches_values_list[1]

    def aux_func_INFOREQU(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0] <= branches_values_list[1]

    def aux_func_SUP(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0] > branches_values_list[1]

    def aux_func_SUPOREQU(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0] >= branches_values_list[1]

    def aux_func_ANB(branches_values_list):
        assert len(branches_values_list) == 2
        return not branches_values_list[0] and not branches_values_list[1]

    def aux_func_BNA(branches_values_list):
        assert len(branches_values_list) == 2
        return not branches_values_list[1] and not branches_values_list[0]

    def aux_func_AONB(branches_values_list):
        assert len(branches_values_list) == 2
        return not branches_values_list[0] or not branches_values_list[1]

    def aux_func_BONA(branches_values_list):
        assert len(branches_values_list) == 2
        return not branches_values_list[1] or not branches_values_list[0]

    def aux_func_BIN(branches_values_list):
        s = 0
        for i in range(len(branches_values_list)):
            s += branches_values_list[i] * 2**i
        return s

    def aux_func_POW(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0]**branches_values_list[1]

    def aux_func_DIV(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0]/branches_values_list[1]

    def aux_func_MOD(branches_values_list):
        assert len(branches_values_list) == 2
        return branches_values_list[0] % branches_values_list[1]
    
    def aux_func_NONO(branches_values_list):
        n = branches_values_list[0] # number of groups of 1
        groups_of_1_needed = branches_values_list[1:1+n] # every possible positive integer in that list
        line = branches_values_list[1+n:] # only 0 and 1 in here
        line_string = ''.join([str(i) for i in line])
        groups_of_1 = [len(x) for x in line_string.split('0') if x != '']
        return groups_of_1_needed == groups_of_1
    
    def aux_func_DIST(branches_values_list):
        assert len(branches_values_list) == 4
        [a, b, c, d] = branches_values_list
        return ( (a-c)**2 + (b-d)**2 )**(1/2)
    
    def aux_func_IN(branches_values_list):
        assert len(branches_values_list) > 1
        return branches_values_list[0] in branches_values_list[1:]
    
    def aux_func_BETWEEN(branches_values_list):
        n = branches_values_list.pop(0)
        b_list = []
        for i in range(n):
            a = branches_values_list.pop(0)
            b = branches_values_list.pop(0)
            c = branches_values_list.pop(0)
            b_list.append([a, b, c])
        for i in range(n):
            [a, b, c] = b_list[i]
            if not b in branches_values_list:
                return False
            for j in range(len(branches_values_list)):
                if branches_values_list[j] == b:
                    l0 = branches_values_list[:j]
                    l1 = branches_values_list[j+1:]
                    if not (a in l0 and c in l1 or c in l0 and a in l1):
                        return False
        return True
        

    func_dict = {'NOT' : aux_func_NOT,
                 'AND' : aux_func_AND,
                 'OR' : aux_func_OR,
                 'XOR' : aux_func_XOR,
                 'XNOR' : aux_func_XNOR,
                 'EQU' : aux_func_EQU,
                 'EQUSET' : aux_func_EQUSET,
                 'DIFF' : aux_func_DIFF,
                 'NAND' : aux_func_NAND,
                 'NOR' : aux_func_NOR,
                 'SUM' : aux_func_SUM,
                 'PROD' : aux_func_PROD,
                 'ABS' : aux_func_ABS,
                 'MINUS' : aux_func_MINUS,
                 'INF' : aux_func_INF,
                 'INFOREQU' : aux_func_INFOREQU,
                 'SUP' : aux_func_SUP,
                 'SUPOREQU' : aux_func_SUPOREQU,
                 'ANB' : aux_func_ANB,
                 'BNA' : aux_func_BNA,
                 'AONB' : aux_func_AONB,
                 'BONA' : aux_func_BONA,
                 'BIN' : aux_func_BIN,
                 'POW': aux_func_POW,
                 'DIV' : aux_func_DIV,
                 'MOD': aux_func_MOD,
                 'NONO' : aux_func_NONO,
                 'DIST' : aux_func_DIST,
                 'IN' : aux_func_IN,
                 'BETWEEN' : aux_func_BETWEEN,
                 }

    def func(self, branches_values_list):
        if None in branches_values_list:
            return None
        return Logic_Gate.func_dict[self.name](branches_values_list)
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
    
    for l in [[2,
               1, 1,
               1, 0, 1, 0, 0], # True
              [2,
               1, 1,
               0, 1, 0, 0, 1], # True
              [2,
               1, 2,
               0, 1, 0, 0, 1], # False
              [2,
               1, 2,
               0, 1, 0, 1, 1], # True
              [1,
               5,
               1, 1, 1, 1, 1], # True
              ]:
        print(l)
        print(Logic_Gate.aux_func_NONO(l))
        
    print('')
    
    for l in [[1,
               0, 1, 2,
               0, 4, 5, 1, 2, 6],
              [1,
               5, 6, 4,
               5, 2, 2, 4, 6, 6, 4],
              [1,
               7, 6, 2],
              [1,
               7, 5, 1,
               7, 1, 1, 1, 5, 2],
              [1,
               4, 6, 2,
               8, 5, 2, 4],
              [1,
               8, 5, 2,
               2, 6, 4, 5, 1, 8, 3, 9],]:
        print('')
        print(l)
        print(Logic_Gate.aux_func_BETWEEN(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    