# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:18:12 2023

@author: zackary.vanche
"""

# import os

# if not os.path.exists('temp'):
#     os.mkdir('temp')
    
# txt = 'empty=True,'

# for file in os.listdir('levels/'):
#     if file.split('.')[-1] == 'py':
#         file_old = 'levels/' + file
#         file_new = 'temp/' + file
#         with open(file_old, 'r') as fr:
#             with open(file_new, 'w') as fw:
#                 line_list = fr.readlines()
#                 for line in line_list:
#                     if txt in line:
#                         print(file)
#                         line = line.replace(txt, '')
#                         if line.replace('\n', '').replace(' ', '') == '':
#                             continue
#                     fw.write(line)