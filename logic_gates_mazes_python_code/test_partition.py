#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:42:14 2022

@author: blanc-sablon
"""

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    p = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return list(p)

if __name__ == "__main__":
    
    E = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = sum(E)
    print(len(E))
    print(s)
    
    subsets_list = powerset(E)
    
    for l in subsets_list:
        if sum(l) == s/2:
            print(l)
    
    