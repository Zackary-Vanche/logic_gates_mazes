#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:52:41 2022

@author: blanc-sablon
"""

from powerset import powerset

if __name__ == "__main__":
    
    KP = [[2, 8],
          [3, 9],
          [4, 10],
          [5, 12],
          [6, 12],
          [7, 18],
          [8, 20],
          [9, 21]]
    
#    KP = [[1, 2],
#          [2, 3],
#          [3, 4],
#          [4, 5],
#          [5, 6],
#          [6, 7],
#          [7, 8],
#          [8, 9],
#          [9, 10],
#          [10, 11]
#          ]
    
    maxp0 = 11
    maxi = 0
    for l in powerset(KP):
        p0 = sum([x[0] for x in l])
        p1 = sum([x[1] for x in l])
        if p0 <= maxp0:
            if p1 > maxi:
                maxi = p1
                print(l, p0, p1)