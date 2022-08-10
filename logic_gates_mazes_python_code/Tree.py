# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:50:35 2022

@author: utilisateur
"""

# from random import random as rd_random
# from random import randint as rd_randint
# from random import shuffle as rd_shuffle
from numpy import array
from numpy import cumsum
from numpy import zeros as np_zeros
from Logic_Gate import Logic_Gate

class Tree:
    """
    Nous utilisons ici des arbres binaires.
    Les feuilles de l'arbre sont des booléens.
    Chaque noeud de l'arbre est une porte logique.
    Les arbres binaires sont donc ici des expressions logiques
    et nous pouvons associer à leur racine un booléen.
    La valeur d'un arbre est ce booléen.
    """
    max_tree_depth = 0
    
    tree_list_not = ['NOT', [None]]
    tree_list_NOT = ['NOT', [None]]
    
    def tree_list_AND(n):
        return ['AND'] + [[None]]*n
    
    def tree_list_OR(n):
        return ['OR'] + [[None]]*n
    
    def tree_list_NAND(n):
        return ['NAND'] + [[None]]*n
    
    def tree_list_NOR(n):
        return ['NOR'] + [[None]]*n
    
    def tree_list_XOR(n):
        return ['XOR'] + [[None]]*n
    
    def tree_list_XNOR(n):
        return ['XNOR'] + [[None]]*n
    
    def tree_list_XORN(n):
        return ['XOR'] + [Tree.tree_list_not]*n
    
    def tree_list_BIN(n):
        return ['BIN'] + [[None]]*n
    
    def tree_list_SUM(n):
        return ['SUM'] + [[None]]*n

    def tree_list_NONO(n):
        return ['NONO'] + [[None]]*n
    
    def tree_list_IN(n):
        return ['IN'] + [[None]]*n
    
    def tree_list_DIFF(n):
        return ['DIFF'] + [[None]]*n
    
    def tree_list_BETWEEN(n):
        return ['BETWEEN'] + [[None]]*n
    
    def tree_list_from_str(txt, CNF=False):
        def tree_list_and_from_str(txt):
            assert txt.replace('T', '').replace('F', '') == ''
            if txt == 'T':
                return [None]
            if txt == 'F':
                return ['NOT', [None]]
            n = len(txt)
            if n == 2:
                if CNF:
                    tree_list = ['OR']
                else:
                    tree_list = ['AND']
            else:
                if CNF:
                    tree_list = ['OR']
                else:
                    tree_list = ['AND']
            for i in range(n):
                b = txt[i]
                if b == 'T':
                    tree_list.append([None])
                if b == 'F':
                    tree_list.append(['NOT', [None]])
            return tree_list
        txtl = txt.split(' ')
        assert len(txtl) > 0
        if len(txtl) == 1:
            return tree_list_and_from_str(txt) 
        else:
            n = len(txtl)
            if n == 2:
                if CNF:
                    tree_list = ['AND']
                else:
                    tree_list = ['OR']
            else:
                if CNF:
                    tree_list = ['AND']
                else:
                    tree_list = ['OR']
            for i in range(n):
                tree_list.append(tree_list_and_from_str(txtl[i]))
            return tree_list
    
    def __init__(self, 
                 tree_list = [None], 
                 empty = None, 
                 name = 'T', 
                 switches = [], 
                 easy_logical_expression_PN = None,
                 root_depth = 0, 
                 cut_expression = False,
                 cut_expression_separator = ')'):
        
        # assert not (root_depth == 0 and switches == []), name
        
        self.name = name
        assert self.name[0] == 'T' 
        self.is_leaf = None
        self.empty = empty
        # La racine sera soit un booléen si il s'agit d'une feuille, soit d'une porte logique binaire.
        self.root = None
        self.sons_list = []
        self.door = None
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
        # assert len(list(set(self.switches_list))) == len(self.switches_list), self.name
        # assert not (self.root_depth == 0 and self.switches_list == []), self.name
        for switch in self.switches_list:
            switch.tree = self
            if self.door != None:
                switch.add_door(self.door)
        self.same_switches_list = []
        
        assert isinstance(tree_list, list), self.name
        
        if len(tree_list) == 1:
            self.root = tree_list[0]
            self.is_leaf = True
        else:
            root = tree_list[0]
            self.root = Logic_Gate(root)
            sons_list = tree_list[1:]
                
            for k in range(len(sons_list)):
                son = sons_list[k]
                assert isinstance(son, list), """{},{} : {}""".format(self.name, str(k), str(son))
                self.sons_list.append(Tree(son, 
                                           root_depth = root_depth+1, 
                                           name = self.name + '_' + str(k),
                                           switches = self.switches_list))
            self.is_leaf = False      
        self.leafs_switches_updates = False
        self.raw_logical_expression_RPN = None 
        self.easy_logical_expression_PN = easy_logical_expression_PN
        self.logical_expression_RPN_simplified = None 
        self.cut_expression = cut_expression
        self.cut_expression_separator = cut_expression_separator

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
                for son in self.sons_list:
                    switches = son.update_leafs_switches(switches)
                return switches
            
    def get_easy_logical_expression_PN(self):
        if not (self.easy_logical_expression_PN != None and self.easy_logical_expression_PN != ''):
            self.update_leafs_switches()
            if self.is_leaf:
                self.easy_logical_expression_PN = self.switches_list[0].name
            else:
                root = self.root
                root_name = root.name
                if root_name == 'EQUSET':
                    n = len(self.sons_list)//2
                    l1 = ' ; '.join([t.get_easy_logical_expression_PN() for t in self.sons_list[:n]])
                    l2 = ' ; '.join([t.get_easy_logical_expression_PN() for t in self.sons_list[n:]])
                    self.easy_logical_expression_PN = '~ ' + '[' + l1 + '] [' + l2 + ']'
                elif root_name == 'NONO':
                    n = self.sons_list[0].get_value() # number of groups of 1
                    groups_of_1_needed = self.sons_list[1:1+n]
                    line = self.sons_list[1+n:]
                    l1 = ' '.join([t.get_easy_logical_expression_PN() for t in groups_of_1_needed])
                    l2 = ' '.join([t.get_easy_logical_expression_PN() for t in line])
                    self.easy_logical_expression_PN = '# ' + '[' + l1 + '] (' + l2 + ')'
                elif root_name == 'IN':
                    s0 = self.sons_list[0].get_easy_logical_expression_PN()
                    lin = ' '.join([t.get_easy_logical_expression_PN() for t in self.sons_list[1:]])
                    self.easy_logical_expression_PN = 'i ' + s0 + ' [' + lin + ']'
                elif root_name == 'BETWEEN':
                    n = self.sons_list[0].get_value()
                    self.easy_logical_expression_PN = root_name + ' '
                    for i in range(n):
                        a = self.sons_list[3*i+1]
                        b = self.sons_list[3*i+2]
                        c = self.sons_list[3*i+3]
                        l1 = ' '.join([t.get_easy_logical_expression_PN() for t in [a, b, c]])
                        self.easy_logical_expression_PN = self.easy_logical_expression_PN + '(' + l1 + ')'
                    l2 = ' '.join([t.get_easy_logical_expression_PN() for t in self.sons_list[3*n+1:]])
                    self.easy_logical_expression_PN = self.easy_logical_expression_PN + '[' + l2 + ']'
                elif len(self.sons_list) == 1: 
                    if root_name == 'NOT': 
                        self.easy_logical_expression_PN = '¬ ' + self.sons_list[0].get_easy_logical_expression_PN()
                    elif root_name == 'ABS': 
                        self.easy_logical_expression_PN = '@ ' + self.sons_list[0].get_easy_logical_expression_PN()
                    elif root_name == 'MINUS': 
                        self.easy_logical_expression_PN = '- ' + self.sons_list[0].get_easy_logical_expression_PN()
                    elif root_name == 'BIN':
                        pass # Don't need to do anything since BIN doesn't change anything here
                    else:
                        self.easy_logical_expression_PN = root_name + self.sons_list[0].get_easy_logical_expression_PN()
                elif len(self.sons_list) == 2:
                    son_A = self.sons_list[0]
                    son_B = self.sons_list[1]
                    A = son_A.get_easy_logical_expression_PN()
                    B = son_B.get_easy_logical_expression_PN()
                    if son_A.get_depth() > 3 and len(son_A.sons_list) >= 2 and ' ' in A:
                        if '(' in A:
                            A = '[ ' + A + ' ]'
                        else:
                            A = '( ' + A + ' )'
                    if son_B.get_depth() > 3 and len(son_B.sons_list) >= 2 and ' ' in B:
                        if '(' in B:
                            B = '[ ' + B + ' ]'
                        else:
                            B = '( ' + B + ' )'
                    self.easy_logical_expression_PN = ' '.join([root_name, A, B])
                    if root_name == 'FALSE':
                        self.easy_logical_expression_PN = 'F'
                    elif root_name == 'ANB':
                        self.easy_logical_expression_PN = '& {} ¬ {}'.format(A, B)
                    elif root_name == 'BNA':
                        self.easy_logical_expression_PN = '& ¬ {} {}'.format(A, B)
                    elif root_name == 'NB':
                        self.easy_logical_expression_PN = ' '.join(['¬', B])
                    elif root_name == 'NA':
                        self.easy_logical_expression_PN = ' '.join(['¬', A])
                    elif root_name == 'AONB':
                        self.easy_logical_expression_PN = '| {0} ¬ {1}'.format(A, B)
                    elif root_name == 'BONA':
                        self.easy_logical_expression_PN = '| ¬ {0} {1}'.format(A, B)
                    elif root_name == 'A':
                        self.easy_logical_expression_PN = A
                    elif root_name == 'B':
                        self.easy_logical_expression_PN = B
                    elif root_name == 'TRUE':
                        self.easy_logical_expression_PN = 'T'
                    elif root_name == 'BIN':
                        self.easy_logical_expression_PN = 'b {0} {1}'.format(A, B)
                    elif root_name == 'POW':
                        self.easy_logical_expression_PN = '** {0} {1}'.format(A, B)
                    elif root_name == 'DIV':
                        self.easy_logical_expression_PN = '/ {0} {1}'.format(A, B)
                    elif root_name == 'MOD':
                        self.easy_logical_expression_PN = '% {0} {1}'.format(A, B)
                    else:
                        self.easy_logical_expression_PN = '{0} {1} {2}'.format(root_name, A, B)
                else: 
                    txt = ''
                    for son in self.sons_list:
                        son_PN = son.get_easy_logical_expression_PN()
                        txt = txt + son_PN + ' '
                    if '(' in txt:
                        txt = root_name + ' [ ' + txt + '] '
                    else:
                        txt = root_name + ' ( ' + txt + ') '
                    self.easy_logical_expression_PN = txt
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('NOT ', '¬ ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('NAND ', '¬& ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('AND ', '& ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('XOR ', '^ ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('XNOR ', '¬^ ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('NOR ', '¬| ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('OR ', '| ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('SUM ', '+ ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('PROD ', '* ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('DIFF ', '≠ ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('SUPOREQU ', '>= ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('INFOREQU ', '<= ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('EQU ', '= ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('NEQ ', '¬= ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('INF ', '< ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('SUP ', '> ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('BIN ', 'b ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('DIST ', 'd ')
            self.easy_logical_expression_PN = self.easy_logical_expression_PN.replace('BETWEEN ', '<< ')
            if self.cut_expression:
                l_elePN = self.easy_logical_expression_PN.split(self.cut_expression_separator)
                elePN = ''
                for i in range(len(l_elePN)):
                    if i < len(l_elePN)-2:
                        if len(l_elePN[i+1]) < 6:
                            elePN = elePN + l_elePN[i] + self.cut_expression_separator
                        else:
                            elePN = elePN + l_elePN[i] + self.cut_expression_separator + '\n'
                    elif i == len(l_elePN)-2:
                        elePN = elePN + l_elePN[i] + self.cut_expression_separator
                    else:
                        elePN = elePN + l_elePN[i]
                self.easy_logical_expression_PN = elePN
        return self.easy_logical_expression_PN
        
    def get_root(self):
        return self.root
    
    def switch_leafs(self, root_depth = 0):
        self.empty = False
        switch_list = self.switches_list
        assert len(switch_list) == self.number_of_leafs(), """name : {}\n switch_list : {}\n number_of_leafs : {}\n root_depth : {}\n""".format(self.name, [s.name for s in switch_list], self.number_of_leafs(), root_depth)
        if self.is_leaf:
            self.is_leaf = True
            self.root = switch_list[0].value
            self.switches_list = [switch_list[0]]
            new_switches_list = switch_list[1:]
        else:
            new_switches_list = switch_list[:]
            self.is_leaf = False
            nb_switches_list = []
            for son in self.sons_list:
                nb_switches_list.append(son.number_of_leafs())
            assert self.number_of_leafs() == sum(nb_switches_list)
            nb_switches_list = array(nb_switches_list)
            nb_switches_sum = cumsum(nb_switches_list)
            for k in range(len(self.sons_list)):
                son = self.sons_list[k]
                a, b = nb_switches_sum[k], nb_switches_list[k]
                son.switches_list = new_switches_list[a-b:a]
                son.switch_leafs(root_depth+1)
        # Cette fonction change la valeur des feuilles de l'arbre afin de prendre en compte les interrupteurs
        
    def sons_list_values(self):
        slv = []
        for son in self.sons_list:
            slv.append(son.get_value())
        return slv
    
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
            return self.root.func(self.sons_list_values())

    def get_depth(self):
        if self.is_leaf:
            return 1
        else:
            maxi = -float('inf')
            for son in self.sons_list:
                maxi = max(son.get_depth(), maxi)
            return 1 + maxi
    
    def number_of_leafs(self):
        if self.is_leaf: 
            return 1
        else: 
            n_leafs = 0
            for son in self.sons_list:
                n_leafs += son.number_of_leafs()
            return n_leafs
                
        
    def leafs_list(self):
        if self.is_leaf: 
            return [self.get_root()]
        else: 
            ll = []
            for son in self.sons_list:
                ll.extend(son.leafs_list())
            return ll
        
    def copy(self, new_leafs_list = None, root_depth = 0):
        # mettre à jour cette fonction si on l'utilise plus
        if type(new_leafs_list) == type(None):
            new_leafs_list = self.leafs_list()
        assert len(new_leafs_list) == self.number_of_leafs() or root_depth != 0, "{} {}".format(len(new_leafs_list), self.number_of_leafs())
        # assert self.switches_list != [], self.name
        T = Tree(name = self.name + '_copy')
        if self.is_leaf:
            T.is_leaf = True
            T.root = new_leafs_list[0]
            new_leafs_list = new_leafs_list[1:]
        else:
            T.is_leaf = False
            T.root = self.get_root()
            T.sons_list = []
            for son in self.sons_list:
                son, new_leafs_list  = son.copy(new_leafs_list, root_depth+1)
                T.sons_list.append(son)
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
            # assert (T_copy.leafs_list() == line).all(), "T_copy.leafs_list() = {}\n line = {}".format(T_copy.leafs_list(), line)
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
            for k in range(len(self.sons_list)):
                self.sons_list[k].root_depth = self.root_depth + 1
            self.root.depth = self.root_depth
            txt += """{}\n""".format(str(self.get_root()))
            for son in self.sons_list:
                txt += """{}\n""".format(son)
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
                self_list = [self.root.get_results_list()]
                for son in self.sons_list:
                    self_list.append(self.son.to_list())
                return self_list

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