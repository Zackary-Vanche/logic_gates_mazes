# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:50:35 2022

@author: utilisateur
"""

from random import random as rd_random
from random import randint as rd_randint
from random import shuffle as rd_shuffle
from numpy import array
from numpy import zeros as np_zeros
from Binary_Logic_Gate import Binary_Logic_Gate

class Tree:
    """
    Nous utilisons ici des arbres binaires.
    Les feuilles de l'arbre sont des booléens.
    Chaque noeud de l'arbre est une porte logique.
    Les arbres binaires sont donc ici des expressions logiques
    et nous pouvons associer à leur racine un booléen.
    La valeur d'un arbre est ce booléen.
    """
    tree_list_and_2  = ['AND', [None], [None]]
    tree_list_and_3  = ['AND', tree_list_and_2, [None]]
    tree_list_and_4  = ['AND', tree_list_and_2, tree_list_and_2]
    tree_list_and_5  = ['AND', tree_list_and_4, [None]]
    tree_list_and_6  = ['AND', tree_list_and_4, tree_list_and_2]
    tree_list_and_7  = ['AND', tree_list_and_4, tree_list_and_3]
    tree_list_and_8  = ['AND', tree_list_and_4, tree_list_and_4]
    tree_list_and_9  = ['AND', tree_list_and_4, tree_list_and_5]
    tree_list_and_10 = ['AND', tree_list_and_5, tree_list_and_5]
    
    tree_list_or_2  = ['OR', [None], [None]]
    tree_list_or_3  = ['OR', tree_list_or_2, [None]]
    tree_list_or_4  = ['OR', tree_list_or_2, tree_list_or_2]
    tree_list_or_5  = ['OR', tree_list_or_4, [None]]
    tree_list_or_6  = ['OR', tree_list_or_4, tree_list_or_2]
    tree_list_or_7  = ['OR', tree_list_or_4, tree_list_or_3]
    tree_list_or_8  = ['OR', tree_list_or_4, tree_list_or_4]
    tree_list_or_9  = ['OR', tree_list_or_4, tree_list_or_5]
    tree_list_or_10 = ['OR', tree_list_or_5, tree_list_or_5]
    
    tree_list_nor = ['NOR', [None], [None]]
    tree_list_anb = ['ANB', [None], [None]]
    tree_list_bna = ['BNA', [None], [None]]
    tree_list_xor = ['XOR', [None], [None]]
    tree_list_nand = ['NAND', [None], [None]]
    tree_list_aonb = ['AONB', [None], [None]]
    tree_list_bona = ['BONA', [None], [None]]
    
    tree_list_FFF = ['ANB', ['OR', [None], [None]], [None]]
    tree_list_TFF = ['AND', [None], ['NOR', [None], [None]]] 
    tree_list_FTF = ['ANB', ['BNA', [None], [None]], [None]] 
    tree_list_FFT = ['AND', ['NOR', [None], [None]], [None]]  
    tree_list_FTT = ['NAND', [None], ['NOR', [None], [None]]] 
    tree_list_TFT = ['BNA', ['BNA', [None], [None]], [None]] 
    tree_list_TTF = ['NAND', ['NOR', [None], [None]], [None]] 
    tree_list_TTT = tree_list_and_3
    
    tree_list_XOR3 = ['OR', ['OR', tree_list_TFF, tree_list_FTF], tree_list_FFT]
    tree_list_XNOR3 = ['OR', ['OR', tree_list_FTT, tree_list_TFT], tree_list_TTF]
    
    def __init__(self, 
                 tree_list = None, 
                 empty = None, 
                 name = 'T', 
                 switches = [], 
                 easy_logical_expression_PN = None,
                 root_depth = 0):
        self.name = name
        assert name == '' and root_depth != 0 or self.name[0] == 'T' 
        self.is_leaf = None
        self.empty   = empty
        # La racine sera soit un booléen si il s'agit d'une feuille, soit d'une porte logique binaire.
        self.root    = None
        # Les fils gauche et droite valent None s'il s'agit d'une feuille, ou sont des arbres sinon.
        self.left    = None 
        self.right   = None
        self.door    = None
        self.root_depth = root_depth
        
        # Chaque interrupteur actionne plusieurs feuilles.
        # Soit la liste des interrupteurs est vide,
        # soit c'est une liste de liste qui contient toutes les feuilles.
        # Les feuilles sont alors répertoriées par leurs numéros.
        
        # Chaque feuille est actionnée par un interrupteur.
        # Deux feuilles ou plus peuvent être actionnées par le même interrupteur.
        # Si la liste des interrupteurs est vide, on ne les prend pas en compte.
        
        # Deux listes sont attachées à un arbre et expliquent ses interrupteurs.
        # La première est same_switches_list.
        # C'est une liste de liste.
        # Si deux indices sont dans la même sous-liste de self.same_switches_list,
        # cela signifie que les feuilles correspondantes sont actionnées par le même interrupteur.
        # La deuxième est switches_list.
        
        self.switches_list = switches
        for switch in self.switches_list:
            switch.tree = self
            if self.door != None:
                switch.add_door(self.door)
        self.same_switches_list = []
        
        if tree_list != None:
            if len(tree_list) == 1:
                self.root = tree_list[0]
                self.is_leaf = True
            else:
                try:
                    assert len(tree_list) == 3
                except:
                    print(tree_list)
                    raise
                [root, left, right] = tree_list
                self.root  = Binary_Logic_Gate(root)
                self.left  = Tree(left,  root_depth = root_depth+1, name = self.name + 'L')
                self.right = Tree(right, root_depth = root_depth+1, name = self.name + 'R')
                self.is_leaf = False      
        self.leafs_switches_updates = False
        self.raw_logical_expression_RPN = None 
        self.easy_logical_expression_PN = easy_logical_expression_PN
        self.logical_expression_RPN_simplified = None 

    def update_leafs_switches(self, switches = None):
        if not self.leafs_switches_updates:
            self.leafs_switches_updates = True
            if switches == None:
                switches = self.switches_list
            if self.is_leaf:
                self.switches_list = [switches[0]]
                del switches[0]
                return switches
            else:
                switches = self.left.update_leafs_switches(switches)
                switches = self.right.update_leafs_switches(switches)
                return switches
            
    def get_easy_logical_expression_PN(self):
        if self.easy_logical_expression_PN != None and self.easy_logical_expression_PN != '':
            return self.easy_logical_expression_PN
        self.update_leafs_switches()
        if self.is_leaf:
            return self.switches_list[0].name
        else:
            root = self.root
            A    = self.left.get_easy_logical_expression_PN()
            B    = self.right.get_easy_logical_expression_PN()
            root_name = root.name
            if len(A) > len(B):
                A, B = B, A
                root_name = root.invert_A_B_gate_name()
            if len(A) == len(B) and B < A:
                A, B = B, A
                root_name = root.invert_A_B_gate_name()
            if ' ' in A:
                if '(' in A:
                    A = '[ ' + A + ' ]'
                else:
                    A = '( ' + A + ' )'
            if ' ' in B:
                if '(' in B:
                    B = '[ ' + B + ' ]'
                else:
                    B = '( ' + B + ' )'
            self.easy_logical_expression_PN = ' '.join([root_name, A, B])
            
            if root_name == 'FALSE':
                self.easy_logical_expression_PN = 'F'
            if root_name == 'AND':
                self.easy_logical_expression_PN = '& {} {}'.format(A, B)
            if root_name == 'OR':
                self.easy_logical_expression_PN = '| {} {}'.format(A, B)
            if root_name == 'NOR':
                self.easy_logical_expression_PN = '-| {} {}'.format(A, B)
            if root_name == 'ANB':
                self.easy_logical_expression_PN = '& {} - {}'.format(A, B)
            if root_name == 'BNA':
                self.easy_logical_expression_PN = '& - {} {}'.format(A, B)
            if root_name == 'NB':
                self.easy_logical_expression_PN = ' '.join(['-', B])
            if root_name == 'NA':
                self.easy_logical_expression_PN = ' '.join(['-', A])
            if root_name == 'AONB':
                self.easy_logical_expression_PN = '| {0} - {1}'.format(A, B)
            if root_name == 'BONA':
                self.easy_logical_expression_PN = '| - {0} {1}'.format(A, B)
            if root_name == 'A':
                self.easy_logical_expression_PN = A
            if root_name == 'B':
                self.easy_logical_expression_PN = B
            if root_name == 'TRUE':
                self.easy_logical_expression_PN = 'T'
        return self.easy_logical_expression_PN
        
    def get_raw_logical_expression_RPN(self):
        if self.raw_logical_expression_RPN != None:
            return self.raw_logical_expression_RPN
        self.update_leafs_switches()
        if self.is_leaf:
            return self.switches_list[0].name
        else:
            root  = self.root
            left  = self.left
            right = self.right
            root_name = root.name
            self.raw_logical_expression_RPN = ' '.join([left.get_raw_logical_expression_RPN(), right.get_raw_logical_expression_RPN(), root_name])
            return self.raw_logical_expression_RPN
        
    def get_logical_expression_RPN_simplified(self, only_and_or_not = True):
        if self.logical_expression_RPN_simplified != None:
            return self.logical_expression_RPN_simplified
        self.update_leafs_switches()
        if self.is_leaf:
            self.logical_expression_RPN_simplified = self.switches_list[0].name
        else:
            root  = self.root
            left  = self.left
            right = self.right
            root_name = root.name
            A = left.get_logical_expression_RPN_simplified(only_and_or_not)
            B = right.get_logical_expression_RPN_simplified(only_and_or_not)
            if len(A) < len(B):
                A, B = B, A
                root_name = root.invert_A_B_gate_name()
            if len(A) == len(B) and A < B:
                A, B = B, A
                root_name = root.invert_A_B_gate_name()
            if root_name == 'FALSE':
                self.logical_expression_RPN_simplified = 'F'
            if root_name == 'AND':
                self.logical_expression_RPN_simplified = ' '.join([A, B, '&'])
            if root_name == 'ANB':
                self.logical_expression_RPN_simplified = ' '.join([A, B, '-', '&'])
            if root_name == 'A':
                self.logical_expression_RPN_simplified = A
            if root_name == 'BNA':
                self.logical_expression_RPN_simplified = ' '.join([A, '-', B, '&'])
            if root_name == 'B':
                self.logical_expression_RPN_simplified = B
            if root_name == 'XOR':
                if not only_and_or_not:
                    self.logical_expression_RPN_simplified = '{0} {1} {2}'.format(A, B, root_name)
                else:
                    self.logical_expression_RPN_simplified = '{0} {1} - & {0} - {1} & |'.format(A, B)
            if root_name == 'OR':
                self.logical_expression_RPN_simplified = ' '.join([A, B, '|'])
            if root_name == 'NOR':
                root_name = '| -'
                self.logical_expression_RPN_simplified = ' '.join([A, B, root_name])
            if root_name == 'XNOR':
                if not only_and_or_not:
                    self.logical_expression_RPN_simplified = '{0} {1} {2}'.format(A, B, root_name)
                else:
                    self.logical_expression_RPN_simplified = '{0} {1} & {0} - {1} - & |'.format(A, B)
            if root_name == 'NB':
                self.logical_expression_RPN_simplified = ' '.join([B, '-'])
            if root_name == 'AONB':
                self.logical_expression_RPN_simplified = '{0} {1} - |'.format(A, B)
            if root_name == 'NA':
                self.logical_expression_RPN_simplified = ' '.join([A, '-'])
            if root_name == 'BONA':
                self.logical_expression_RPN_simplified = '{0} - {1} |'.format(A, B)
            if root_name == 'NAND':
                root_name = '& -'
                self.logical_expression_RPN_simplified = ' '.join([A, B, root_name])
            if root_name == 'TRUE':
                self.logical_expression_RPN_simplified = 'T'
        return self.logical_expression_RPN_simplified
            
    def get_logical_expression_PN_simplified(self):
        l = self.get_logical_expression_RPN_simplified().split(' ')
        l.reverse()
        l =  ' '.join(l)
        l = l.replace('- |', '-|')
        l = l.replace('- &', '-&')
        return l
        
    def get_root(self):
        return self.root
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def switch_leafs(self, root_depth = 0):
        self.empty = False
        switch_list = self.switches_list
        try:
            assert len(switch_list) == self.number_of_leafs()
        except:
            print(len(switch_list), self.number_of_leafs(), root_depth)
            print(switch_list)
            raise
        if self.is_leaf:
            self.is_leaf = True
            self.root = switch_list[0].value
            self.switches_list = [switch_list[0]]
            new_switches_list = switch_list[1:]
        else:
            new_switches_list = switch_list[:]
            self.is_leaf = False
            nb_switches_left = self.left.number_of_leafs()
            nb_switches_right = self.right.number_of_leafs()
            try:
                assert self.number_of_leafs() == nb_switches_left + nb_switches_right
            except:
                print(self.number_of_leafs(), nb_switches_left, nb_switches_right)
                raise
            self.left.switches_list = new_switches_list[:nb_switches_left]
            self.right.switches_list = new_switches_list[-nb_switches_right:]
            self.left.switch_leafs(root_depth+1)
            self.right.switch_leafs(root_depth+1)
        # Cette fonction change la valeur des feuilles de l'arbre afin de prendre en compte les interrupteurs
    
    def get_value(self):
        # Si la liste des interrupteurs n'est pas vide,
        # on met à jour les interrupteurs
        if len(self.switches_list) == self.number_of_leafs():
            self.switch_leafs()
        if self.is_leaf: 
            # On a une feuille qu'on peut renvoyer.
            return self.root
        else: 
            # Dans ce cas, on a un noeud.
            return self.root.func(self.left.get_value(), self.right.get_value())
        
    def get_depth(self):
        if self.is_leaf:
            return 1
        else:
            return 1 + max(self.left.get_depth(), self.right.get_depth())
        
    def random_tree(empty = False, root_depth = 0, max_depth = 3, p_feuille = 0, n_switches = 'alea'):
        T = Tree()
        T.empty = empty
        if rd_random() < 1-p_feuille and root_depth+1 < max_depth:
            results_list  = [rd_randint(0,1) for i in range(4)]
            T.root        = Binary_Logic_Gate(results_list)
            T.left        = Tree.random_tree(empty, root_depth + 1)
            T.right       = Tree.random_tree(empty, root_depth + 1)
            T.is_leaf  = False
        else:
            if empty :
                T.root = None
            else:
                T.root  = rd_randint(0,1)
            T.left  = None
            T.right = None
            T.is_leaf = True  
        # Ajout des interupteurs
        if n_switches != 0 and root_depth == 0:
            if n_switches == 'alea':
                n_leafs = T.number_of_leafs()
                n_switches = rd_randint(2, n_leafs)
                leafs = [i for i in range(n_leafs)]
                rd_shuffle(leafs)
                switches_list = []
                for i in range(n_switches):
                    switches_list.append([leafs[i]])
                for i in range(n_switches, n_leafs):
                    switches_list[rd_randint(0, n_switches-1)].append(leafs[i])
                T.same_switches_list = switches_list   
        return T 
    
    def number_of_leafs(self):
        if self.is_leaf: 
            return 1
        else: 
            return self.left.number_of_leafs() + self.right.number_of_leafs()
        
    def leafs_list(self):
        if self.is_leaf: 
            return [self.get_root()]
        else: 
            return self.left.leafs_list() + self.right.leafs_list()
        
    def copy(self, new_leafs_list = None, root_depth = 0):
        # mettre à jour cette fonction si on l'utilise plus
        if type(new_leafs_list) == type(None):
            new_leafs_list = self.leafs_list()
        try:
            assert len(new_leafs_list) == self.number_of_leafs() or root_depth != 0
        except:
            print(len(new_leafs_list), self.number_of_leafs())
            raise
        T = Tree(name = self.name)
        if self.is_leaf:
            T.is_leaf = True
            T.root = new_leafs_list[0]
            new_leafs_list = new_leafs_list[1:]
        else:
            T.is_leaf = False
            T.root = self.get_root()
            T.left, new_leafs_list  = self.left.copy(new_leafs_list, root_depth+1)
            T.right, new_leafs_list = self.right.copy(new_leafs_list, root_depth+1)
        T.same_switches_list = self.same_switches_list
        if root_depth != 0:
            return T, new_leafs_list
        else:
            return T
            
    def empty_truth_table(n_leafs):
        table = np_zeros((2**n_leafs, n_leafs+1))
        for ileaf in range(n_leafs):
            for ipossibility in range(2**n_leafs):
                table[ipossibility,ileaf] = (ipossibility//2**ileaf)%2
        return table
    
    def truth_table(self):
        n_leafs = self.number_of_leafs()
        table = Tree.empty_truth_table(n_leafs)
        for ipossibility in range(2**n_leafs):
            line = table[ipossibility][:-1]
            T_copy = self.copy(line)
            try:
                assert (T_copy.leafs_list() == line).all()
            except:
                print("T_copy.leafs_list() =", T_copy.leafs_list())
                print("line =", line)
                raise
            table[ipossibility,-1] = T_copy.get_value()
        return table
    
    def possibilities_switches_list(self):
        possibilities_list = []
        n_leafs = self.number_of_leafs()
        table = Tree.empty_truth_table(n_leafs)
        for ipossibility in range(2**n_leafs):
            line = table[ipossibility][:-1]
            T_copy = self.copy(line)
            if T_copy.switch_configuration_possible():
                possibilities_list.append(1)
            else:
                possibilities_list.append(0)
        return array(possibilities_list)
    
    def switch_configuration_possible(self):
        leafs_list = self.leafs_list()
        switches   = self.same_switches_list
        for i in range(len(switches)):
            l_switch = []
            for j in switches[i]:
                l_switch.append(leafs_list[j])
            if 1 in l_switch and 0 in l_switch:
                return False
        return True
    
    def number_of_1_in_truth_table(self):
        table = self.truth_table()
        return int(sum(table[:,-1]))
    
    def number_of_0_in_truth_table(self):
        return 2**self.number_of_leafs() - self.number_of_1_in_truth_table()
    
    def number_of_possibles_1_in_truth_table(self):
        table = self.truth_table()
        return int(sum(table[:,-1]*self.possibilities_switches_list()))
    
    def number_of_possibles_0_in_truth_table(self):
        table = self.truth_table()
        return int(sum((1-table[:,-1])*self.possibilities_switches_list()))
    
    def invert_root(self):
        if self.is_leaf:
            self.root = int(not self.root)
        else:
            self.root.invert_gate()
    
    def str_table(self):
        table = self.truth_table()
        possibilities_switches = self.possibilities_switches_list()
        (m, n) = table.shape
        txt_lines_list = []
        for i in range(m):
            txt_line = '|   '
            for j in range(n):
                if j == n-1:
                    txt_line += ' |'
                txt_line += ' ' + str(int(table[i, j]))
            if bool(possibilities_switches[i]):
                txt_line += ' X'
            txt_lines_list.append(txt_line)
        return '\n' + '\n'.join(txt_lines_list)
    
    def __str__(self):
        txt = ''
        if self.root_depth == 0:
            txt += '\n|   Tree {} :\n'.format(self.name)
            txt += '|   Raw logical expression :\n|      {}\n'.format(self.get_raw_logical_expression_RPN())
            txt += '|   Logical expression :\n|      {}\n'.format(self.get_logical_expression_RPN_simplified()) 
        assert self.is_leaf != None
        if self.is_leaf:
            txt += '|   '*self.root_depth + '|' + '-'*7 + '> ' + str(self.get_root())
        else:
            self.left.root_depth = self.root_depth + 1
            self.right.root_depth = self.root_depth + 1
            self.root.depth = self.root_depth
            txt += """{}\n{}\n{}""".format(str(self.get_root()), str(self.get_left()), str(self.get_right()))
        if self.root_depth == 0 or not self.is_leaf:
            txt += """\n{}value : {}""".format('|   '*(self.root_depth+1), self.get_value())
        if self.root_depth == 0:
            txt += "\n|   Number of leafs : {}".format(self.number_of_leafs())
            txt += "\n|   depth of the Tree : {}".format(self.get_depth())
        if self.root_depth == 0:
            txt += '\n|   Truth table :{}'.format(self.str_table())
            txt += '\n|   Number of 0 in truth table : {}'.format(self.number_of_0_in_truth_table())
            txt += '\n|   Number of 1 in truth table : {}'.format(self.number_of_1_in_truth_table())
            txt += '\n|   Number of possibles 0 in truth table : {}'.format(self.number_of_possibles_0_in_truth_table())
            txt += '\n|   Number of possibles 1 in truth table : {}'.format(self.number_of_possibles_1_in_truth_table())
        if self.root_depth == 0:
            txt += '\n|   Same switches list :\n|      {}'.format(self.same_switches_list)
            txt += '\n|   Switches list :\n|      {}'.format([switch.name for switch in self.switches_list])
        return txt
        
    def to_list(self):
        if self.is_leaf: 
            # On a une feuille qu'on peut renvoyer.
            return [self.root]
        else: 
            # Dans ce cas, on a un noeud.
            if self.root == None:
                return [None, None, None]
            else:
                return [self.root.get_results_list(), self.left.to_list(), self.right.to_list()]

    def update_same_switches_list(self):
        if self.switches_list != []:
            same_switches_set = set()
            for i in range(self.switches_list):
                l = []
                for j in range(self.switches_list):
                    if self.switches_list[i] == self.switches_list[j]:
                        l.append(j)
                same_switches_set.append(l)
            self.same_switches_list = list(same_switches_set)