# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:01:51 2022

@author: utilisateur
"""

# from numba import njit
from numpy import array as np_array, prod as np_prod

class Logic_Gate:

    def __init__(self, name):
        self.switch = None
        self.name = name

    def aux_func_NOT(branches_values):
        # # assert len(sons_list) == 1
        return not branches_values[0]

    def aux_func_AND(branches_values):
        return not 0 in branches_values

    def aux_func_OR(branches_values):
        return 1 in branches_values

    def aux_func_XOR(branches_values):
        return sum(branches_values) == 1

    def aux_func_XNOR(branches_values):
        return not sum(branches_values) == 1

    def aux_func_EQU(branches_values):
        # # assert len(sons_list) >= 2
        return all(branches_values[i] == branches_values[i+1] for i in range(len(branches_values)-1))

    def aux_func_EQUSET(branches_values):
        # # assert len(branches_values) % 2 == 0
        n = len(branches_values) // 2
        return set(branches_values[:n]) == set(branches_values[n:])

    def aux_func_DIFF(branches_values):
        # # assert len(sons_list) >= 2
        # print(branches_values)
        branches_values_sorted = sorted(branches_values)
        return all(branches_values_sorted[i] != branches_values_sorted[i+1] for i in range(len(branches_values)-1))

    def aux_func_NAND(branches_values):
        return 0 in branches_values

    def aux_func_NOR(branches_values):
        return not 1 in branches_values

    def aux_func_SUM(branches_values):
        return sum(branches_values)

    def aux_func_PROD(branches_values):
        return np_prod(np_array(branches_values))

    def aux_func_ABS(branches_values):
        # # assert len(sons_list) == 1
        return abs(branches_values[0])

    def aux_func_MINUS(branches_values):
        # # assert len(sons_list) == 1
        return -branches_values[0]

    def aux_func_INF(branches_values):
        return all(branches_values[i] < branches_values[i+1] for i in range(len(branches_values)-1))
    
    def aux_func_INF0(branches_values):
        for i in range(len(branches_values)-1):
            A, B = branches_values[i], branches_values[i+1]
            if A != 0 and B != 0 and A >= B:
                return False
        return True

    def aux_func_INFOREQU(branches_values):
        return all(branches_values[i] <= branches_values[i+1] for i in range(len(branches_values)-1))

    def aux_func_SUP(branches_values):
        return all(branches_values[i] > branches_values[i+1] for i in range(len(branches_values)-1))

    def aux_func_SUPOREQU(branches_values):
        return all(branches_values[i] >= branches_values[i+1] for i in range(len(branches_values)-1))
    
    def aux_func_BIN(branches_values):
        return sum([branches_values[i]*2**i for i in range(len(branches_values))])

    def aux_func_POW(branches_values):
        # # assert len(sons_list) == 2
        return branches_values[0]**branches_values[1]
    
    def aux_func_DIV(branches_values):
        # # assert len(sons_list) == 2
        return branches_values[0]/branches_values[1]
    
    def aux_func_DIVINT(branches_values):
        # # assert len(sons_list) == 2
        return branches_values[0]//branches_values[1]
    
    def aux_func_MOD(branches_values):
        # # assert len(sons_list) == 2
        return branches_values[0]%branches_values[1]

    def aux_func_NONO(branches_values):
        branches_values = list(branches_values)
        n = branches_values[0]  # number of groups of 1
        groups_of_1_needed = branches_values[1:1+n]  # every possible positive integer in that list
        line = branches_values[1+n:]  # only 0 and 1 in here
        line_string = ''.join([str(i) for i in line])
        groups_of_1 = [len(x) for x in line_string.split('0') if x != '']
        return groups_of_1_needed == groups_of_1

    def aux_func_DIST(branches_values):
        # # assert len(sons_list) == 4
        [a, b, c, d] = branches_values
        return ((a-c)**2 + (b-d)**2)**(1/2)

    def aux_func_IN(branches_values):
        # # assert len(sons_list) > 1
        return branches_values[0] in branches_values[1:]

    def aux_func_BETWEEN(branches_values):
        branches_values = list(branches_values)
        n = branches_values.pop(0)
        b_list = []
        for i in range(n):
            a = branches_values.pop(0)
            b = branches_values.pop(0)
            c = branches_values.pop(0)
            b_list.append([a, b, c])
        for i in range(n):
            [a, b, c] = b_list[i]
            if b not in branches_values:
                return False
            for j in range(len(branches_values)):
                if branches_values[j] == b:
                    l0 = branches_values[:j]
                    l1 = branches_values[j+1:]
                    if not (a in l0 and c in l1 or c in l0 and a in l1):
                        return False
        return True

    def aux_func_JUMP(branches_values):
        n = len(branches_values)
        # assert n%2 == 0
        # assert n >= 6
        sublists = []
        for i in range(n//2-2):
            bl = branches_values[2*i:2*i+6]
            sublists.append(bl)
        n_True = 0
        for bl in sublists:
            if list(bl) in [[0, 1,
                             0, 1,
                             1, 0],
                            [1, 0,
                             0, 1,
                             0, 1],
                            [1, 0,
                             1, 0,
                             0, 1],
                            [0, 1,
                             1, 0,
                             1, 0]]:
                n_True += 1
        return n_True == 1

    func_dict = {'NOT': aux_func_NOT,
                 'AND': aux_func_AND,
                 'OR': aux_func_OR,
                 'XOR': aux_func_XOR,
                 'XNOR': aux_func_XNOR,
                 'EQU': aux_func_EQU,
                 'EQUSET': aux_func_EQUSET,
                 'DIFF': aux_func_DIFF,
                 'NAND': aux_func_NAND,
                 'NOR': aux_func_NOR,
                 'SUM': aux_func_SUM,
                 'PROD': aux_func_PROD,
                 'ABS': aux_func_ABS,
                 'MINUS': aux_func_MINUS,
                 'INF': aux_func_INF,
                 'INF0': aux_func_INF0,
                 'INFOREQU': aux_func_INFOREQU,
                 'SUP': aux_func_SUP,
                 'SUPOREQU': aux_func_SUPOREQU,
                 'BIN': aux_func_BIN,
                 'POW': aux_func_POW,
                 'DIV': aux_func_DIV,
                 'DIVINT' : aux_func_DIVINT,
                 'MOD': aux_func_MOD,
                 'NONO': aux_func_NONO,
                 'DIST': aux_func_DIST,
                 'IN': aux_func_IN,
                 'BETWEEN': aux_func_BETWEEN,
                 'JUMP': aux_func_JUMP,
                 }

    def func(self, sons_list):
        if None in sons_list:
            return None
        branches_values = [son.get_value() for son in sons_list]
        try:
            return int(Logic_Gate.func_dict[self.name](branches_values))
        except TypeError:
            print(self.name)
            raise

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

    for bl in [[2,
                1, 1,
                1, 0, 1, 0, 0],  # True
               [2,
                1, 1,
                0, 1, 0, 0, 1],  # True
               [2,
                1, 2,
                0, 1, 0, 0, 1],  # False
               [2,
                1, 2,
                0, 1, 0, 1, 1],  # True
               [1,
                5,
                1, 1, 1, 1, 1],  # True
               ]:
        print(bl)
        print(Logic_Gate.aux_func_NONO(bl))

    print('')

    for bl in [[1,
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
                2, 6, 4, 5, 1, 8, 3, 9]]:
        print('')
        print(bl)
        print(Logic_Gate.aux_func_BETWEEN(bl))

    for bl in [[1, 0, 0, 1, 0, 1],
               [1, 0, 0, 1, 0, 1, 1, 0],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]:
        print('')
        print(bl)
        print(Logic_Gate.aux_func_JUMP(bl))
