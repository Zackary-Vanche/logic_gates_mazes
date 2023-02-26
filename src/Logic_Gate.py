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
        return all(branches_values[i] == branches_values[i+1] for i in range(len(branches_values)-1))

    def aux_func_EQUSET(branches_values):
        n = len(branches_values) // 2
        return sorted(branches_values[:n]) == sorted(branches_values[n:])

    def aux_func_DIFF(branches_values):
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
        return abs(branches_values[0])

    def aux_func_MINUS(branches_values):
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
        return branches_values[0]**branches_values[1]
    
    def aux_func_DIV(branches_values):
        return branches_values[0]/branches_values[1]
    
    def aux_func_DIVINT(branches_values):
        return branches_values[0]//branches_values[1]
    
    def aux_func_MOD(branches_values):
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
    
    def aux_func_INLIST(branches_list):
        n = branches_list[0]
        l1 = [str(b) for b in branches_list[1:n+1]]
        l2 = [str(b) for b in branches_list[n+1:]]
        return ''.join(l1) in ''.join(l2)

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
    
    def aux_func_MAS(branches_list):
        v_list = set()
        for v in branches_list:
            v_list.add(v)
        assert len(branches_list)%2 == 0
        n = len(branches_list)//2
        l1 = branches_list[:n]
        l2 = branches_list[n:]
        S = 0
        for v in v_list:
            c1 = l1.count(v)
            c2 = l2.count(v)
            S += min(c1, c2)
        for i in range(n):
            S -= int(l1[i] == l2[i])
        return S

    def aux_func_N3L_4(branches_list):
        assert len(branches_list) == 16
        if sum(branches_list) != 8:
            return False
        [S0, S1, S2, S3,
         S4, S5, S6, S7,
         S8, S9, S10, S11,
         S12, S13, S14, S15] = branches_list
        branches_array = np_array(branches_list).reshape((4, 4))
        if (branches_array.sum(axis=0) >= 3).any():
            return False
        if (branches_array.sum(axis=1) >= 3).any():
            return False
        if S1 + S6 + S11 >= 3:
            return False
        if S0 + S5 + S10 + S15 >= 3:
            return False
        if S4 + S9 + S14 >= 3:
            return False
        if S2 + S5 + S8 >= 3:
            return False
        if S3 + S6 + S9 + S12 >= 3:
            return False
        if S7 + S10 + S13 >= 3:
            return False
        return True

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
                 'INLIST' : aux_func_INLIST,
                 'BETWEEN': aux_func_BETWEEN,
                 'JUMP': aux_func_JUMP,
                 'MAS': aux_func_MAS,
                 'N3L_4':aux_func_N3L_4
                 }

    def func(self, sons_list):
        if None in sons_list:
            return None
        branches_values = [son.get_value() for son in sons_list]
        if None in branches_values: # I use that case in level_seven when I create random levels
            return True
        try:
            return Logic_Gate.func_dict[self.name](branches_values)
        except TypeError:
            print(self.name)
            raise

    def get_results_list(self):
        return self.results_list

    def invert_gate(self):
        for i in range(4):
            self.results_list[i] = int(not self.results_list[i])

if __name__ == "__main__":

    assert Logic_Gate.aux_func_NOT([0]) == 1
    assert Logic_Gate.aux_func_NOT([1]) == 0

    assert Logic_Gate.aux_func_AND([0, 0]) == 0
    assert Logic_Gate.aux_func_AND([0, 1]) == 0
    assert Logic_Gate.aux_func_AND([1, 0]) == 0
    assert Logic_Gate.aux_func_AND([1, 1]) == 1

    assert Logic_Gate.aux_func_OR([0, 0]) == 0
    assert Logic_Gate.aux_func_OR([0, 1]) == 1
    assert Logic_Gate.aux_func_OR([1, 0]) == 1
    assert Logic_Gate.aux_func_OR([1, 1]) == 1

    for i in range(5):
        bl = [[2,
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
              ][i]
        r = [1, 1, 0, 1, 1][i]
        assert Logic_Gate.aux_func_NONO(bl) == r

    for i in range(6):
        bl = [[1,
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
                2, 6, 4, 5, 1, 8, 3, 9]][i]
        r = [1, 1, 0, 0, 0, 1][i]
        assert Logic_Gate.aux_func_BETWEEN(bl) == r

    for i in range(3):
        r = [1, 0, 0][i]
        bl = [[1, 0, 0, 1, 0, 1],
               [1, 0, 0, 1, 0, 1, 1, 0],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]][i]
        assert Logic_Gate.aux_func_JUMP(bl) == r
        
    assert Logic_Gate.aux_func_MAS([0, 1, 2, 3,
                                    0, 1, 2, 3]) == 0
    
    assert Logic_Gate.aux_func_MAS([0, 1, 2, 3,
                                    0, 1, 3, 2]) == 2
    
    assert Logic_Gate.aux_func_MAS([0, 0, 2, 3,
                                    0, 0, 3, 2]) == 2
    
    assert Logic_Gate.aux_func_MAS([0, 3, 0, 3,
                                    0, 0, 3, 2]) == 2
    
    assert Logic_Gate.aux_func_MAS([1, 1, 1, 1,
                                    1, 1, 0, 0]) == 0
    
    assert Logic_Gate.aux_func_MAS([1, 1, 0, 1,
                                    1, 1, 0, 0]) == 0
    
    assert Logic_Gate.aux_func_MAS([1, 1, 0, 1,
                                    1, 1, 1, 2]) == 1
