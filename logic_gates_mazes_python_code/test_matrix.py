# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:14:52 2022

@author: utilisateur
"""

import numpy as np

if __name__ == '__main__':
    
    M = np.array([[2,  13, 31, 53, 73],
                  [3,  17, 37, 59, 79],
                  [5,  19, 41, 61, 83],
                  [7,  23, 43, 67, 89],
                  [11, 29, 47, 71, 97]])
    
    a = np.array([[0],
                  [1],
                  [2],
                  [1],
                  [3]])
    
    b = M@a
    
    print(b)
    
    print(np.linalg.pinv(M) @ M)