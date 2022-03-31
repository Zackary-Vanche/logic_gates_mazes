# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:28:03 2022

@author: utilisateur
"""

def base_2(k, list_size):
    """
    :param k: entier que l'on veut traduire en binaire
    :type k: int
    :param taille_liste: taille minimale de la liste renvoyée
    :type taille_liste: int
    :return: k en binaire
    :rtype: int
    """
    b2 = []
    while k != 0 or len(b2) < list_size:
        b2.append(k%2)
        k = k // 2
    return b2