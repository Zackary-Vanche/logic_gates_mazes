from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Color import Color
from Levels_colors_list import Levels_colors_list
from random import random as rd_random
from random import shuffle as rd_shuffle

def f(): 

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
    

    Slist = [S0, S1, S2, S3, S4, S5]
    
    dx = 1
    dy = 1
    ex = 0.75
    ey = 0.75
    
    R0 = Room(name='R0',
                position=[-0.5*dx, 7.5*dy, 9*ex, ey/2],
                switches_list=Slist)
    R1 = Room(name='R1',
                position=[1*dx, 6*dy, ex, ey],
                switches_list=[S6])
    R2 = Room(name='R2',
                position=[-0.5*dx, 5*dy, ex, ey],
                switches_list=[S7])
    R3 = Room(name='R3',
                position=[1.5*dx, 2.5*dy, ex, ey],
                switches_list=[S8])
    R4 = Room(name='R4',
                position=[3.5*dx, 2.5*dy, ex, ey],
                switches_list=[S9])
    R5 = Room(name='R5',
                position=[5.5*dx, 5*dy, ex, ey],
                switches_list=[S10])
    R6 = Room(name='R6',
                position=[4*dx, 6*dy, ex, ey],
                switches_list=[S11])
    RE = Room(name='RE',
              position=[5.5*dx, 2.5*dy, ex, ey],
              is_exit=True)
    
    Rl = [R1, R2, R3, R4, R5, R6]
    rd_shuffle(Rl)

    D0 = Door(two_way=False,
                tree=Tree(tree_list=['INFOREQU', Tree.tree_list_SUM(6), [None]],
                          name='T0',
                          switches=[S0, S1, S2, S3, S4, S5, 2]),
                name='D0',
                room_departure=R0,
                room_arrival=R1)
    
    p = 1/2
    
    Dl = []
    Ra = Rl.pop()
    Rb = Rl.pop()
    R_couples_list = []
    if rd_random() < p:
        R_couples_list.append([Ra, Rb])
        connect_Ra_Rb = True
    else:
        connect_Ra_Rb = False
    for iR, R in enumerate(Rl):
        a = rd_random()
        if a < 1/5 or iR==0 and not connect_Ra_Rb:
            R_couples_list.extend([[R, Ra], [R, Rb]])
        elif a < 3/5:
            R_couples_list.append([R, Ra])
        else:
            R_couples_list.append([R, Rb])
    for i in range(len(Rl)):
        for j in range(i):
            if rd_random() < 1/2:
                R_couples_list.append([Rl[i], Rl[j]])
    R_couples_list.sort(key=lambda c : [c[0].name, c[1].name])
    Sdict = {'R1':S0,
             'R2':S1,
             'R3':S2,
             'R4':S3,
             'R5':S4,
             'R6':S5,}
    for kR, R_couple in enumerate(R_couples_list):
        Ri, Rj = R_couple
        Si = Sdict[Ri.name]
        Sj = Sdict[Rj.name]
        Tk = Tree(tree_list=Tree.tree_list_OR(2),
                  name=f'T{kR+1}',
                  switches=[Si, Sj])
        Dk = Door(two_way=True,
                  tree=Tk,
                  name=f'D{kR+1}',
                  room_departure=Ri,
                  room_arrival=Rj)
        Dl.append(Dk)
    
    Dn = Door(two_way=False,
                tree=Tree(tree_list=Tree.tree_list_AND(6),
                            name=f'T{len(Dl)+1}',
                            switches=[S6, S7, S8, S9, S10, S11]),
                name=f'D{len(Dl)+1}',
                room_departure=R5,
                room_arrival=RE)

    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[R0, R1, R2, R3, R4, R5, R6, RE],
                 doors_list=[D0] + Dl + [Dn],
                 fastest_solution=None,
                 level_color=get_color(),
                 name='Random dominating set',
                 keep_proportions=True,
                 door_window_size=450,
                 random=True)
    
    initial_try = [Sdict[Ra.name].name, Sdict[Rb.name].name, 'D0']
    solutions_that_work, nb_iterations, nb_operations = level.find_all_solutions(stop_at_first_solution=True,
                                                                                 initial_try=initial_try)
    sol = ' '.join(solutions_that_work[0])
    level.fastest_solution = sol
    
    return level

def get_color():
    hu = rd_random()
    lcolor = Levels_colors_list.FROM_HUE(hu=hu+0.5, sa=0.35, li=0.15)
    lcolor.surrounding_color = Color.IVORY
    lcolor.contour_color = Color.IVORY
    return lcolor