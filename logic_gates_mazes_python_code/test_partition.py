#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:42:14 2022

@author: blanc-sablon
"""

from powerset import powerset

if __name__ == "__main__":
    
    E = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = sum(E)
    print(len(E))
    print(s)
    
    subsets_list = powerset(E)
    
    for l in subsets_list:
        if sum(l) == s/2:
            print(l)
    
    