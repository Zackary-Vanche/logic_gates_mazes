#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:53:52 2022

@author: blanc-sablon
"""

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    p = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return list(p)