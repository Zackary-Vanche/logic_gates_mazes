# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:29:06 2022

@author: utilisateur
"""

def from_binary(l):
    s = 0
    for i in range(len(l)):
        s = l[i]*2**i
    return s

# 010 01010 0 0 0 
#   1 1   1      
# 010 010 0 0 0 0 
# 1       1       
# 010101010 0 0 0 
#                
# 0 0 0 0 0 0 0 0 
#                
# 0 0 0 0 0 0 0 0 
#                
# 0 0 0 0 0 0 0 0 
#                
# 0 0 0 0 0 0 0 0 
#                
# 0 0 0 0 0 0 0 0 
        