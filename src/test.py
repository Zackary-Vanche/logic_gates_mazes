# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:56:54 2024

@author: utilisateur
"""

import matplotlib.pyplot as plt
import numpy as np

y = [152, 246, 824, 1677, 2588,
     5842, 5752, 12176, 10824, 19136,
     20548, 33082, 36934, 54060, 68071,
     99834, 111740, 154571, 185811, 255531,
     274800, 358848, 415512, 534860, 563259,
     684864, 782964, 935678, 945087, 1059097,
     1129712, 1229858]

y = [235, 516, 2970, 4590, 16030,
     21204, 53594, 65067, 133489, 154965,
     282707, 323360, 559659, 632496, 1050269,
     1184219, 1914891, 2134237, 3300163, 3663726,
     5493120, 6029298, 8664363, 9471658, 13231655,
     14322767, 19282859, 20791695, 27179206, 28992262,
     36365593, 38514684, 46426706, 48535770, 55990196,
     58033273, 64576772, 66235489, 71393006, 72736933]

y = np.array(y)
x = np.arange(len(y))

plt.figure(figsize=(20, 10))
plt.plot(x[::2], y[::2])
plt.plot(x[1::2], y[1::2])
plt.yscale('log')
plt.grid()
plt.show()

y_diff = y[1:]-y[:-1]
x_diff = np.arange(len(y_diff))

plt.figure(figsize=(20, 10))
plt.plot(x_diff, y_diff, color='r')
plt.plot(x_diff[::2], y_diff[::2], color='k')
plt.plot(x_diff[1::2], y_diff[1::2], color='k')
#plt.yscale('log')
plt.grid()
plt.show()