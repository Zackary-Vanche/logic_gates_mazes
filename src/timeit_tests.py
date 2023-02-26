# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:10:15 2022

@author: utilisateur
"""

from timeit import timeit
import numpy as np

if __name__ == "__main__":
    
    a = [1, 1, 1, 1, 1]
    
    print('AND')
    print(timeit('(np.array(a) == 1).all()', 'a = [1]*20; import numpy as np', number=10000))
    print(timeit('not 0 in a', 'a = [1]*20', number=10000))
    print(timeit('all(a[i] == 1 for i in range(len(a)))', 'a = [1]*20', number=10000))
    print('EQU')
    print(timeit('a.count(a[0]) == len(a)', 'a = [1]*20', number=10000))
    print('EQUSET')
    print(timeit('sorted(a[:len(a)//2]) == sorted(a[len(a)//2:])', 'a = [1, 2]*10 + [1, 2]*10', number=10000))
    print(timeit('set(a[:len(a)//2]) == set(a[len(a)//2:])', 'a = [1, 2]*10 + [1, 2]*10', number=10000))
    print('DIFF')
    print(timeit('len(set(l)) == len(l)', 'l = [i for i in range(20)]', number=10000))