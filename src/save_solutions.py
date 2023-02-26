import matplotlib.pyplot as plt

from os.path import exists as os_path_exists
from os import mkdir as os_mkdir

from Levels import Levels

from least_squares import least_squares

import numpy as np

# import random as rd

plt.rcParams["figure.figsize"] = (32,18)

if __name__ == "__main__":

    if not os_path_exists('images'):
        os_mkdir('images')

    # l_solutions = []
    # for level in Game.levels_list:
    #     print(level.name)
    #     l_solutions.append(level.find_all_solutions(stop_at_first_solution = False, verbose = 2))  

    # Calcul des solutions et enregistrement des resumes des niveaux (avec les solutions) sous forme de texte
    # Cette fonction est un peu longue, et sert uniquement de verification (d'où le sys.exit())
    # On ne doit pas l'appeler dans le code à exporter en .exe.
    # Game.save_levels_txt(verbose = 1, calculates_solutions = True)

    # calculations_times = [round(np.exp(10*i + 2*rd.random()),2) for i in range(16)]
    # calculations_times, nb_iterations_list, nb_operations_list = Levels.save_solutions_txt(verbose=1,
    #                                                                                        multithreads=False,
    #                                                                                        do_it_fast=True,
    #                                                                                        max_calculation_time=1)
    only_if_not_yet_calculated = True
    calculations_times, nb_iterations_list, nb_operations_list = Levels.save_solutions_txt(verbose=1,
                                                                                           multithreads=False,
                                                                                           do_it_fast=False,
                                                                                           max_calculation_time=float('inf'),
                                                                                           only_if_not_yet_calculated=only_if_not_yet_calculated)
    calculations_times = list(filter(lambda item: item is not None, calculations_times))
    # Cette fonction calcule les solutions,
    # les enregistre dans un fichier texte
    # et renvoie le temps nécessaire pour calculer les solutions

    l_ylabel = ['Time needed to solve the maze (s)',
                'Number of iterations',
                'Number of elementary operations']
    for ylabel in l_ylabel:
    
        if ylabel == l_ylabel[0]:
            if only_if_not_yet_calculated:
                continue
            x_list = calculations_times
        if ylabel == l_ylabel[1]:
            x_list = nb_iterations_list
        if ylabel == l_ylabel[2]:
            x_list = nb_operations_list

        n = len(x_list)
        plt.figure()
        plt.xlabel('Level number', fontsize=20)
        plt.ylabel(ylabel, fontsize=20)
        plt.scatter([i for i in range(len(x_list))],
                    x_list)
        plt.xticks(np.arange(0, n, step=1))
        A = np.zeros((n, 2))
        B = np.zeros((n, 1))
        for i in range(n):
            A[i][0] = i
            A[i][1] = 1
            B[i][0] = np.log(x_list[i])
        X, V, R, absR, varX, sigma_0_carre, PY, PX, PV = least_squares(A, B)
        f = lambda t : np.exp(X[0][0] * t + X[1][0])
        plt.plot([0, n], [f(0), f(n)], 'r')
        plt.yscale('log')
        plt.grid()
        plt.xticks(rotation=90, fontsize=15)
        plt.yticks(rotation=0, fontsize=20)
        plt.tight_layout()

        if ylabel == l_ylabel[0]:
            print('images/solving_time.jpg')
            plt.savefig('images/solving_time.png')
        if ylabel == l_ylabel[1]:
            print('images/nb_iterations.jpg')
            plt.savefig('images/nb_iterations.png')
        if ylabel == l_ylabel[2]:
            print('images/nb_operations.jpg')
            plt.savefig('images/nb_operations.png')
        plt.close()
    
    with open('solutions/nb_iterations.txt', 'w') as f:
        for i in range(len(nb_iterations_list)):
            f.write(Levels.get_level(i).name + '\n' + str(nb_iterations_list[i]) + '\n\n')
    
    with open('solutions/nb_operations.txt', 'w') as f:
        for i in range(len(nb_operations_list)):
            f.write(Levels.get_level(i).name + '\n' + str(nb_operations_list[i]) + '\n\n')

    # Game.save_levels_txt()
