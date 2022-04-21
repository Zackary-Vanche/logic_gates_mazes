# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:09:49 2022

@author: utilisateur
"""

import matplotlib.pyplot as plt

from os.path import exists as os_path_exists
from os import mkdir as os_mkdir

from Levels import Levels

from moindres_carres import moindres_carres

import numpy as np

# import random as rd

if __name__ == "__main__":
    
    # You cannot use this script anymore
    # because it is too long to end
    # because of the level Manhattan distance.
    # Finding the solution of level_manhattan_distance the way I do here
    # takes almost a day.

    if not os_path_exists('images'):
        os_mkdir('images')

    # l_solutions = []
    # for level in Game.levels_list:
    #     print(level.name)
    #     l_solutions.append(level.find_all_solutions(stop_at_first_solution = False, verbose = 2))  
    # Ces lignes permettent de calculer l'ensemble des solutions des niveaux
    # Comme la résolution est faite par force brute, elle est tres longue pour le niveau electricity
    # Elle ne prend que quelques secondes pour les niveaux plus faciles
    # On ne lance pas ces lignes car le calcul des solutions est déjà fait par la suite.

    # Calcul des solutions et enregistrement des resumes des niveaux (avec les solutions) sous forme de texte
    # Cette fonction est un peu longue, et sert uniquement de verification (d'où le sys.exit())
    # On ne doit pas l'appeler dans le code à exporter en .exe.
    # Game.save_levels_txt(verbose = 1, calculates_solutions = True)

    # calculations_times = [round(np.exp(10*i + 2*rd.random()),2) for i in range(16)]
    calculations_times = Levels.save_solutions_txt(verbose = 1) 
    # Cette fonction calcule les solutions, 
    # les enregistre dans un fichier texte
    # et renvoie le temps nécessaire pour calculer les solutions
    n = len(calculations_times)

    plt.figure(figsize=(20, 15))
    plt.xlabel('Level number')
    plt.ylabel('Time needed to solve the maze')
    plt.scatter([i for i in range(len(calculations_times))],
                calculations_times)
    plt.xticks(np.arange(0, n, step=1))

    A = np.zeros((n, 2))
    B = np.zeros((n, 1))
    for i in range(n):
        A[i][0] = i
        A[i][1] = 1
        B[i][0] = np.log(calculations_times[i])
    X, V, R, absR, varX, sigma_0_carre, PY, PX, PV = moindres_carres(A, B)

    f = lambda t : np.exp(X[0][0] * t + X[1][0])

    plt.plot([0, n], [f(0), f(n)], 'r')
    plt.yscale('log')
    plt.savefig('images/solving_time.png')
    plt.show()

    # Game.save_levels_txt()
