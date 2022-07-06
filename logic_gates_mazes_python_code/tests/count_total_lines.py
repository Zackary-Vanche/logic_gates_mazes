# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:50:56 2022

@author: utilisateur
"""

import os

if __name__ == "__main__":
    racine = __file__
    racine = racine.split('\\')
    del racine[-1]
    racine = '/'.join(racine)
    n_lines = 0
    l = []
    for file in os.listdir(racine):
        file = '/'.join([racine,file])
        if file.split('.')[-1] == 'py':
            with open(file, 'r') as f_r:
                n = len(f_r.readlines())
                l.append([file.split('/')[-1].replace('.py', ''), n])
                n_lines += n
    l.sort(key=lambda x : x[1])
    for x in l:
        print(x[0], ':', x[1])
    print('total :', n_lines)
