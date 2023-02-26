# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:27:11 2022

@author: utilisateur
"""

from levels.level_panex import level_panex
from Tree import Tree

if __name__ == "__main__":
    level = level_panex()
    doors_dict = level.doors_dict()
    D37 = doors_dict["D37"]
    switches_dict = level.switches_dict
    S0 = switches_dict['S0']
    S1 = switches_dict['S1']
    S2 = switches_dict['S2']
    S3 = switches_dict['S3']
    S4 = switches_dict['S4']
    S5 = switches_dict['S5']
    S6 = switches_dict['S6']
    S7 = switches_dict['S7']
    S15 = switches_dict['S15']
    S19 = switches_dict['S19']
    S23 = switches_dict['S23']
    S27 = switches_dict['S27']
    S55 = switches_dict['S55']
    S59 = switches_dict['S59']
    S63 = switches_dict['S63']
    S67 = switches_dict['S67']
    door_exit_str_list = ['FFFFFFFFTFFFFTTT']
    for i in range(len(door_exit_str_list)):
        T37 = Tree(tree_list=Tree.tree_list_from_str(door_exit_str_list[i]),
                  empty=True,
                  name='T37',
                  switches = [S0, S1, S2, S3, S4, S5, S6, S7,
                              S15,
                              S19,
                              S23,
                              S27,
                              S55,
                              S59,
                              S63,
                              S67,],
                  cut_expression=True)
        D37.set_tree(T37)
        solutions = level_panex().find_all_solutions(verbose=1,
                                                     stop_at_first_solution=True,
                                                     nb_iterations_print=10**4)