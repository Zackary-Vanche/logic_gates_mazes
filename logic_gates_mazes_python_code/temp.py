# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:23:53 2022

@author: utilisateur
"""

with open('levels/level_panex.py', 'r') as f:
    txt = ''.join(f.readlines())
    # for i in range(64, -1, -1):
    #     print(i)
    #     txt = txt.replace('S{0},'.format(i), 'S{0},'.format(i+4))
    # for i in range(64, -1, -1):
    #     txt = txt.replace('S{0}]'.format(i), 'S{0}]'.format(i+4))
    l = {8:8,
         9:9,
         10:10,
         11:'',
         12:11,
         13:12,
         14:13,
         15:'',
         16:14,
         17:15,
         18:16,
         19:'',
         20:17,
         21:18,
         22:19,
         23:'',
         24:20,
         25:21,
         26:22,
         27:'',
         28:23,
         29:24,
         30:25,
         31:'',
         32:26,
         33:27,
         34:28,
         35:'',
         36:29,
         37:30,
         38:31,
         39:'',
         40:32,
         41:33,
         42:34,
         43:'',
         44:35,
         45:36,
         46:37,
         47:'',
         48:38,
         49:39,
         50:40,
         51:'',
         52:41,
         53:42,
         54:43,
         55:'',
         56:44,
         57:45,
         58:46,
         59:'',
         60:47,
         61:48,
         62:49,
         63:'',
         64:50,
         65:51,
         66:52,
         67:'',
         }
    for i in l.keys():
        txt = txt.replace('S'+str(i), 'S'+str(l[i]))
    with open('levels/level_panex2.py', 'w') as fw:
        fw.write(txt)
        