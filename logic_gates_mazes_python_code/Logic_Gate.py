# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:01:51 2022

@author: utilisateur
"""


class Logic_Gate:

    def __init__(self, name):
        self.switch = None
        self.name = name

    def sons_list_values(tree):
        slv = []
        for son in tree.sons_list:
            slv.append(son.get_value())
        return slv

    def aux_func_NOT(sons_list):
        # # assert len(sons_list) == 1
        return not sons_list[0].get_value()

    def aux_func_AND(sons_list):
        for sons in sons_list:
            if not sons.get_value():
                return 0
        return 1

    def aux_func_OR(sons_list):
        for sons in sons_list:
            if sons.get_value():
                return 1
        return 0

    def aux_func_XOR(sons_list):
        S = 0
        for sons in sons_list:
            S += sons.get_value()
            if S > 1:
                return 0
        return S == 1

    def aux_func_XNOR(sons_list):
        return not Logic_Gate.aux_func_XOR(sons_list)

    def aux_func_EQU(sons_list):
        # # assert len(sons_list) >= 2
        for i in range(len(sons_list)-1):
            if sons_list[i].get_value() != sons_list[i+1].get_value():
                return 0
        return 1

    def aux_func_EQUSET(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        # # assert len(branches_values_list) % 2 == 0
        n = len(branches_values_list) // 2
        return set(branches_values_list[:n]) == set(branches_values_list[n:])

    def aux_func_DIFF(sons_list):
        # # assert len(sons_list) >= 2
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        branches_values_list_sorted = sorted(branches_values_list)
        for i in range(len(branches_values_list_sorted)-1):
            if branches_values_list_sorted[i] == branches_values_list_sorted[i+1]:
                return 0
        return 1

    def aux_func_NAND(sons_list):
        return not Logic_Gate.aux_func_AND(sons_list)

    def aux_func_NOR(sons_list):
        return not Logic_Gate.aux_func_OR(sons_list)

    def aux_func_SUM(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        return sum(branches_values_list)

    def aux_func_PROD(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        p = 1
        for x in branches_values_list:
            p = p * x
        return p

    def aux_func_ABS(sons_list):
        # # assert len(sons_list) == 1
        return abs(sons_list[0].get_value())

    def aux_func_MINUS(sons_list):
        # # assert len(sons_list) == 1
        return -sons_list[0].get_value()

    def aux_func_INF(sons_list):
        for i in range(len(sons_list)-1):
            if sons_list[i].get_value() >= sons_list[i+1].get_value():
                return False
        return True
    
    def aux_func_INF0(sons_list):
        for i in range(len(sons_list)-1):
            A, B = sons_list[i].get_value(), sons_list[i+1].get_value()
            if A != 0 and B != 0 and A >= B:
                return False
        return True

    def aux_func_INFOREQU(sons_list):
        for i in range(len(sons_list)-1):
            if sons_list[i].get_value() > sons_list[i+1].get_value():
                return False
        return True

    def aux_func_SUP(sons_list):
        for i in range(len(sons_list)-1):
            if sons_list[i].get_value() <= sons_list[i+1].get_value():
                return False
        return True

    def aux_func_SUPOREQU(sons_list):
        for i in range(len(sons_list)-1):
            if sons_list[i].get_value() < sons_list[i+1].get_value():
                return False
        return True

    def aux_func_ANB(sons_list):
        # # assert len(sons_list) == 2
        return not sons_list[0].get_value() and not sons_list[1].get_value()

    def aux_func_BNA(sons_list):
        # # assert len(sons_list) == 2
        return not sons_list[1].get_value() and not sons_list[0].get_value()

    def aux_func_AONB(sons_list):
        # # assert len(sons_list) == 2
        return not sons_list[0].get_value() or not sons_list[1].get_value()

    def aux_func_BONA(sons_list):
        # # assert len(sons_list) == 2
        return not sons_list[1].get_value() or not sons_list[0].get_value()

    def aux_func_BIN(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        s = 0
        for i in range(len(branches_values_list)):
            s += branches_values_list[i] * 2**i
        return s

    def aux_func_POW(sons_list):
        # # assert len(sons_list) == 2
        return sons_list[0].get_value()**sons_list[1].get_value()

    def aux_func_DIV(sons_list):
        # # assert len(sons_list) == 2
        return sons_list[0].get_value()/sons_list[1].get_value()
    
    def aux_func_DIVINT(sons_list):
        # # assert len(sons_list) == 2
        return sons_list[0].get_value()//sons_list[1].get_value()

    def aux_func_MOD(sons_list):
        # # assert len(sons_list) == 2
        return sons_list[0].get_value() % sons_list[1].get_value()

    def aux_func_NONO(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        n = branches_values_list[0]  # number of groups of 1
        groups_of_1_needed = branches_values_list[1:1+n]  # every possible positive integer in that list
        line = branches_values_list[1+n:]  # only 0 and 1 in here
        line_string = ''.join([str(i) for i in line])
        groups_of_1 = [len(x) for x in line_string.split('0') if x != '']
        return groups_of_1_needed == groups_of_1

    def aux_func_DIST(sons_list):
        # # assert len(sons_list) == 4
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        [a, b, c, d] = branches_values_list
        return ((a-c)**2 + (b-d)**2)**(1/2)

    def aux_func_IN(sons_list):
        # # assert len(sons_list) > 1
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        return branches_values_list[0] in branches_values_list[1:]

    def aux_func_BETWEEN(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        n = branches_values_list.pop(0)
        b_list = []
        for i in range(n):
            a = branches_values_list.pop(0)
            b = branches_values_list.pop(0)
            c = branches_values_list.pop(0)
            b_list.append([a, b, c])
        for i in range(n):
            [a, b, c] = b_list[i]
            if b not in branches_values_list:
                return False
            for j in range(len(branches_values_list)):
                if branches_values_list[j] == b:
                    l0 = branches_values_list[:j]
                    l1 = branches_values_list[j+1:]
                    if not (a in l0 and c in l1 or c in l0 and a in l1):
                        return False
        return True

    def aux_func_JUMP(sons_list):
        branches_values_list = []
        for son in sons_list:
            branches_values_list.append(son.get_value())
        n = len(branches_values_list)
        # assert n%2 == 0
        # assert n >= 6
        sublists = []
        for i in range(n//2-2):
            bl = branches_values_list[2*i:2*i+6]
            sublists.append(bl)
        n_True = 0
        for bl in sublists:
            if bl in [[0, 1,
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
                 'ANB': aux_func_ANB,
                 'BNA': aux_func_BNA,
                 'AONB': aux_func_AONB,
                 'BONA': aux_func_BONA,
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
