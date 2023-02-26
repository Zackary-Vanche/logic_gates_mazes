# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:54:20 2022

@author: utilisateur
"""


def linear_function(xa, ya, xb, yb):
    assert xa != xb
    pente = (yb - ya)/(xb - xa)
    coeff = ya - pente*xa
    return (pente, coeff)
