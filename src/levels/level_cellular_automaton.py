from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Level_color import Level_color
from random import choice as rd_choice
from random import random as rd_random

from levels.solutions_cellular_automaton import dico_sol

def level_cellular_automaton(fast_solution_finding=False):
    
    Svalue_end_int = rd_choice(list(dico_sol.keys()))
    sol = dico_sol[Svalue_end_int]
    
    S0 = Switch(name='S0')
    S1 = Switch(name='S1')
    S2 = Switch(name='S2')
    S3 = Switch(name='S3')
    S4 = Switch(name='S4')
    S5 = Switch(name='S5')
    S6 = Switch(name='S6')
    S7 = Switch(name='S7')
    S8 = Switch(name='S8')
    S9 = Switch(name='S9')
    S10 = Switch(name='S10')
    S11 = Switch(name='S11')
    S12 = Switch(name='S12')
    S13 = Switch(name='S13')
    S14 = Switch(name='S14')
    S15 = Switch(name='S15')
    S16 = Switch(name='S16')
    S17 = Switch(name='S17')
    S18 = Switch(name='S18')
    S19 = Switch(name='S19')
    S20 = Switch(name='S20')
    S21 = Switch(name='S21')
    S22 = Switch(name='S22')
    S23 = Switch(name='S23')
    S24 = Switch(name='S24')
    S25 = Switch(name='S25')
    S26 = Switch(name='S26')
    S27 = Switch(name='S27')
    S28 = Switch(name='S28')
    S29 = Switch(name='S29')
    S30 = Switch(name='S30')
    S31 = Switch(name='S31')
    S32 = Switch(name='S32')
    S33 = Switch(name='S33')
    S34 = Switch(name='S34')
    S35 = Switch(name='S35')
    S36 = Switch(name='S36')
    S37 = Switch(name='S37')
    S38 = Switch(name='S38')
    S39 = Switch(name='S39')
    S40 = Switch(name='S40')
    S41 = Switch(name='S41', value=1)
    S42 = Switch(name='S42')
    S43 = Switch(name='S43')
    S44 = Switch(name='S44')
    S45 = Switch(name='S45')
    S46 = Switch(name='S46')
    S47 = Switch(name='S47')
    S48 = Switch(name='S48')
    S49 = Switch(name='S49')

    ##################################################
    Slist_0 = [S0, S1, S2, S3, S4, S5, S6, S7]
    ##################################################
    Slist_1 = [S8, S9, S10, S11]
    ##################################################
    Slist_2 = [S12, S13, S14]
    Slist_3 = [S15, S16, S17, S18]
    Slist_4 = [S19, S20, S21]
    Slist_5 = [S22, S23, S24, S25]
    Slist_6 = [S26, S27, S28]
    ##################################################
    Slist_7 = [S29, S30, S31, S32]
    ##################################################
    Slist_8 = [S33, S34, S35]
    Slist_9 = [S36, S37, S38, S39]
    Slist_10 = [S40, S41, S42]
    Slist_11 = [S43, S44, S45, S46]
    Slist_12 = [S47, S48, S49]
    ##################################################
    
    Sl0 = Slist_2 + Slist_3 + Slist_4 + Slist_5 + Slist_6
    Sl1 = Slist_8 + Slist_9 + Slist_10 + Slist_11 + Slist_12
    
    def get_V_bin(Slist_bin, name):
        return Tree(tree_list=Tree.tree_list_BIN(len(Slist_bin)),
                    name=name,
                    switches=Slist_bin)
    
    def get_V(i):
        Slv = [Slist_0,
               Slist_1,
               Slist_2, Slist_3, Slist_4, Slist_5, Slist_6,
               Slist_7,
               Slist_8, Slist_9, Slist_10, Slist_11, Slist_12][i]
        return get_V_bin(Slv, f'V{i}')
        
    V0 = get_V(0)
    V1 = get_V(1)
    V2 = get_V(2)
    V3 = get_V(3)
    V4 = get_V(4)
    V5 = get_V(5)
    V6 = get_V(6)
    V7 = get_V(7)
    V8 = get_V(8)
    V9 = get_V(9)
    V10 = get_V(10)
    V11 = get_V(11)
    V12 = get_V(12)

    V13 = get_V_bin([Sl0[-1]] + Sl0[:2], name='V13')
    V14 = get_V_bin(Sl0[0:3], name='V14')
    V15 = get_V_bin(Sl0[1:4], name='V15')
    V16 = get_V_bin(Sl0[2:5], name='V16')
    V17 = get_V_bin(Sl0[3:6], name='V17')
    V18 = get_V_bin(Sl0[4:7], name='V18')
    V19 = get_V_bin(Sl0[5:8], name='V19')
    V20 = get_V_bin(Sl0[6:9], name='V20')
    V21 = get_V_bin(Sl0[7:10], name='V21')
    V22 = get_V_bin(Sl0[8:11], name='V22')
    V23 = get_V_bin(Sl0[9:12], name='V23')
    V24 = get_V_bin(Sl0[10:13], name='V24')
    V25 = get_V_bin(Sl0[11:14], name='V25')
    V26 = get_V_bin(Sl0[12:15], name='V26')
    V27 = get_V_bin(Sl0[13:16], name='V27')
    V28 = get_V_bin(Sl0[14:17], name='V28')
    V29 = get_V_bin(Sl0[15:18] + [Sl0[0]], name='V29')
    
    Vlist = [V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29]
    
    VSdict = {}
    for S in Sl1:
        Slist_V = []
        i = int(S.name.replace('S', '')) - int(Sl1[0].name.replace('S', ''))
        Vx = Vlist[i]
        for j in range(len(Slist_0)):
            Slist_V.extend([Slist_0[j], Vx, j])
        VSdict[S.name] = Tree(tree_list=['SUM'] + [['PROD', [None], Tree.tree_list_EQU(2)]]*8,
                              name=f'V{S.name}',
                              switches=Slist_V,
                              cut_expression_depth_1=True)

    def get_tree_1(i):
        return Tree(tree_list=Tree.tree_list_EQU(2),
                    name=f'T{i}',
                    switches=[[V1, V2, V3, V4, V5, V6][i-1], [V7, V8, V9, V10, V11, V12][i-1]])
        
    def get_tree_8(Slist_i, name):
        Slist_Ti = []
        for S in Slist_i:
            Slist_Ti.extend([S, VSdict[S.name]])
        return Tree(tree_list=["AND"] + [Tree.tree_list_EQU(2)]*len(Slist_i),
                    name=name,
                    switches=Slist_Ti)
        
    T0 = Tree(tree_list=[None],
                name='T0',
                switches=[1])
    # T0 = Tree(tree_list=Tree.tree_list_EQU(2),
    #             name='T0',
    #             switches=[V0, 57])
    T1 = get_tree_1(1)
    T2 = get_tree_1(2)
    T3 = get_tree_1(3)
    T4 = get_tree_1(4)
    T5 = get_tree_1(5)
    T6 = get_tree_1(6)
    T7 = Tree(tree_list=["EQU", Tree.tree_list_SUM(2), [None]],
              name='T7',
              switches=[V1, 1, V7])
    T8 = get_tree_8(Slist_8, name='T8')
    T9 = get_tree_8(Slist_9, name='T9')
    T10 = get_tree_8(Slist_10, name='T10')
    T11 = get_tree_8(Slist_11, name='T11')
    T12 = get_tree_8(Slist_12, name='T12')
    T13 = Tree(tree_list=["AND",
                          Tree.tree_list_EQU(3),
                          ['EQU', Tree.tree_list_BIN(len(Sl0)), [None]]],
                name='T13',
                switches=[V1, V7, 8] + Sl0 + [Svalue_end_int])

    ex = 1
    ey = 4
    dx = ex+1
    dy = ey+1
    ex0 = 2
    eye = 3

    ##################################################
    R0 = Room(name='R0',
                position=[-1*dx-ex0+ex, 0*dy, ex0, ey],
                switches_list=Slist_0)
    ##################################################
    R1 = Room(name='R1',
                position=[-1*dx, dy, ex, ey],
                switches_list=Slist_1)
    ##################################################
    R2 = Room(name='R2',
                position=[0*dx, 0*dy, ex, ey],
                switches_list=Slist_2)
    R3 = Room(name='R3',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=Slist_3)
    R4 = Room(name='R4',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=Slist_4)
    R5 = Room(name='R5',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=Slist_5)
    R6 = Room(name='R6',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=Slist_6)
    ##################################################
    R7 = Room(name='R7',
                position=[5*dx, dy, ex, ey],
                switches_list=Slist_7)
    ##################################################
    R8 = Room(name='R8',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=Slist_8)
    R9 = Room(name='R9',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=Slist_9)
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=Slist_10)
    R11 = Room(name='R11',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=Slist_11)
    R12 = Room(name='R12',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=Slist_12)
    ##################################################
    RE = Room(name='RE',
              position=[5*dx, 0*dy, ex, eye],
              is_exit=True)
    ##################################################
    
    Ra = Room(name='',
              position=[ex, ey, dx-ex, dy-ey],
              switches_list=[])
    Rb = Room(name='',
              position=[dx+ex, ey, dx-ex, dy-ey],
              switches_list=[])
    Rc = Room(name='',
              position=[2*dx+ex, ey, dx-ex, dy-ey],
              switches_list=[])
    Rd = Room(name='',
              position=[3*dx+ex, ey, dx-ex, dy-ey],
              switches_list=[])
    
    if fast_solution_finding:
        R1.room_of_possible_switches = R7
        R2.room_of_possible_switches = R8
        R3.room_of_possible_switches = R9
        R4.room_of_possible_switches = R10
        R5.room_of_possible_switches = R11
        R6.room_of_possible_switches = R12

    D0 = Door(two_way=False,
                tree=T0,
                name='D0',
                room_departure=R0,
                room_arrival=R1,
                relative_departure_coordinates=[(ex0-ex/2)/ex0, 1/2])
    D1 = Door(two_way=False,
                tree=T1,
                name='D1',
                room_departure=R1,
                room_arrival=R2)
    D2 = Door(two_way=False,
                tree=T2,
                name='D2',
                room_departure=R2,
                room_arrival=R3)
    D3 = Door(two_way=False,
                tree=T3,
                name='D3',
                room_departure=R3,
                room_arrival=R4)
    D4 = Door(two_way=False,
                tree=T4,
                name='D4',
                room_departure=R4,
                room_arrival=R5)
    D5 = Door(two_way=False,
                tree=T5,
                name='D5',
                room_departure=R5,
                room_arrival=R6)
    D6 = Door(two_way=False,
                tree=T6,
                name='D6',
                room_departure=R6,
                room_arrival=R7)
    D7 = Door(two_way=False,
                tree=T7,
                name='D7',
                room_departure=R7,
                room_arrival=R8)
    D8 = Door(two_way=False,
                tree=T8,
                name='D8',
                room_departure=R8,
                room_arrival=R9)
    D9 = Door(two_way=False,
                tree=T9,
                name='D9',
                room_departure=R9,
                room_arrival=R10)
    D10 = Door(two_way=False,
                tree=T10,
                name='D10',
                room_departure=R10,
                room_arrival=R11)
    D11 = Door(two_way=False,
                tree=T11,
                name='D11',
                room_departure=R11,
                room_arrival=R12)
    D12 = Door(two_way=False,
                tree=T12,
                name='D12',
                room_departure=R12,
                room_arrival=R1)
    D13 = Door(two_way=False,
                tree=T13,
                name='D13',
                room_departure=R7,
                room_arrival=RE)
    
    # hu_min = 0.85
    # hu_max = 0.5
    hu = rd_random()*0.65-0.15
    li = 0.2
    c0 = Color.color_hls(hu, li=li, sa=1)
    c1 = Color.color_hls(hu, li=li, sa=0.1)
    lcolor = Level_color(background_color=c0,
                         room_color=c1,
                         letters_color=Color.WHITE,
                         contour_color=Color.WHITE,
                         inside_room_color=Color.WHITE,
                         surrounding_color=Color.WHITE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12,
                             Ra, Rb, Rc, Rd,
                             RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13],
                 fastest_solution=sol,
                 level_color=lcolor,
                 name='Automaton',
                 keep_proportions=True,
                 door_window_size=250,
                 random=True)
    
    # solutions = level.find_all_solutions(verbose=3, save_solutions_txt=True)
    # print('\n')
    # print(len(solutions[0]))
    # print('\n')
    # with open('cellular_automaton_solutions.txt', 'w') as fw:
    #     for sol in solutions[0]:
    #         print(' '.join(sol))
    #         fw.write(' '.join(sol))
    #         fw.write('\n')
    
    # with open('levels/cellular_automaton_solutions.txt', 'r') as fr:
    #     solutions = fr.readlines()
    # for i in range(len(solutions)):
    #     solutions[i] = solutions[i].replace('\n', '')
        
    # dico_int = {}
    # dico_sol = {}
    # for sol in solutions:
    #     sol_R0 = sol.split('D0 ')[0]
    #     level.try_solution(sol)
    #     Svalue_end = [S.value for S in level.switches_list if 12 <= int(S.name.replace('S', '')) <= 28]
    #     Svalue_end_int = sum([Svalue_end[i] * 2 ** i for i in range(len(Svalue_end))])
    #     dico_int[sol_R0] = Svalue_end_int
    #     dico_sol[Svalue_end_int] = sol
        
    # from collections import Counter
    
    # dico_count = dict(Counter(dico_int.values()))
    # dico_final = {}
    # for Svalue_end_int in dico_count:
    #     if dico_count[Svalue_end_int] == 1:
    #         dico_final[Svalue_end_int] = dico_sol[Svalue_end_int]
    
    # Svalue_end_int = rd_choice(list(dico_final.keys()))
    # sol = dico_final[Svalue_end_int]
    
    # for Svalue_end_int in dico_final.keys():
    #     print(Svalue_end_int, ': "', dico_final[Svalue_end_int], '",')
            
    # D13 = Door(two_way=False,
    #             tree=T13,
    #             name='D13',
    #             room_departure=R7,
    #             room_arrival=RE)
    
    return level