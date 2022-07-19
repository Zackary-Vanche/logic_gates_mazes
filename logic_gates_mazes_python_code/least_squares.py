# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:20:13 2021

@author: utilisateur
"""

import numpy as np

def least_squares(A, B, P = None):
    """
    Effectue l'estimation des moindres carrés.
    :param A: matrice de modèle,
    :type A: array
    :param B: matrice des observations (parfois appelée Y),
    :type B: array
    :param P: matrice de poids (inverse de la matrice de covariance),
    :type P: array
    :return: 
        la matrice X des estimations des paramètres,
        la matrice V des erreurs,
        la matrice R, ou vecteur des résidus normalisés. (parfois appelée W)
        la matrice absR, ou valeur absolue du vecteur des résidus normalisés.
        la matrice varX de variance de X.
        Le flottant sigma_0_carre : facteur unitaire de variance
        La matrice PY covariance a posteriori de Y
        La matrice PX covariance a posteriori de X
        La matrice PV covariance a posteriori de V
    return type: tuple(array, array, array, array, array, float, array, array, array)
    """
    # n est le nombre d'observations
    # p est le nombre de paramètres
    n, p = A.shape
    if type(P) == type(None):
        P = np.eye(n)
    tA = np.transpose(A)
    N = tA @ P @ A
    K = tA @ P @ B
    invN = np.linalg.pinv(N) 
    X = invN @ K # estimation du vecteur des paramètres
    V = B - A @ X # vecteur des erreurs
    sigma_0_carre = np.transpose(V) @ P @ V / (n-p)
    R = [] #vecteur des résidus normalisés
    invP = np.linalg.inv(P)
    matrice_denominateur = sigma_0_carre * (invP - A @ invN @ tA)
    for i in range(n):
        denominateur = np.sqrt(matrice_denominateur[i,i])
        R.append(V[i]/denominateur)
    absR = np.abs(R)
    varX = sigma_0_carre * invN
    # Matrices de covariance a posteriori
    PY = sigma_0_carre * P
    invM = tA @ invP @ A
    M = np.linalg.pinv(invM)
    PX = sigma_0_carre * M
    PV = sigma_0_carre * (P - A @ M @ tA)
    sigma_0_carre = sigma_0_carre[0][0]
    return X, V, R, absR, varX, sigma_0_carre, PY, PX, PV