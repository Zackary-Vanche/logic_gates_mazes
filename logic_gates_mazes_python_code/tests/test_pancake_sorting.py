# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:54:50 2022

@author: utilisateur
"""

def flip(l, lk):
    l_bis = list(l)
    for k in lk:
        l_bis[:k] = list(reversed(l_bis[:k]))
    return tuple(l_bis)

if __name__ == "__main__":
    n = 6
    l = [i+1 for i in range(n)]
    lk = [i for i in range(2, n+1)]
    print('lk', lk)
    l_visited = []
    l_to_visit = [()]
    while l_to_visit != []:
        sol = l_to_visit.pop(0)
        r = flip(l, sol)
        if not r in l_visited:
            l_visited.append(r)
            for k in lk:
                l_to_visit.append(sol + (k,))
    # print('l_visited[0]', l_visited[0])
    print('l_visited[-1]', l_visited[-1])