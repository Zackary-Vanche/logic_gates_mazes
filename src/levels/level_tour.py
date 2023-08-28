from Switch import Switch
from Tree import Tree
from Door import Door
from Room import Room
from Maze import Maze
from Levels_colors_list import Levels_colors_list

def level_tour(): 

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

    Slist = [S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23]


    Vlist = []


    dx = 1
    dy = 1
    ex = 0.5
    ey = 0.5

    R0 = Room(name='R0',
                position=[0*dx, 1*dy, ex, ey],
                switches_list=[])
    R1 = Room(name='R1',
                position=[0*dx, 2*dy, ex, ey],
                switches_list=[])
    R2 = Room(name='R2',
                position=[0*dx, 3*dy, ex, ey],
                switches_list=[])
    R3 = Room(name='R3',
                position=[0*dx, 4*dy, ex, ey],
                switches_list=[])
    R4 = Room(name='R4',
                position=[1*dx, 0*dy, ex, ey],
                switches_list=[])
    R5 = Room(name='R5',
                position=[1*dx, 1*dy, ex, ey],
                switches_list=[])
    R6 = Room(name='R6',
                position=[1*dx, 2*dy, ex, ey],
                switches_list=[])
    R7 = Room(name='R7',
                position=[1*dx, 3*dy, ex, ey],
                switches_list=[])
    R8 = Room(name='R8',
                position=[1*dx, 4*dy, ex, ey],
                switches_list=[])
    R9 = Room(name='R9',
                position=[2*dx, 0*dy, ex, ey],
                switches_list=[])
    R10 = Room(name='R10',
                position=[2*dx, 1*dy, ex, ey],
                switches_list=[])
    R11 = Room(name='R11',
                position=[2*dx, 2*dy, ex, ey],
                switches_list=[])
    R12 = Room(name='R12',
                position=[2*dx, 3*dy, ex, ey],
                switches_list=[])
    R13 = Room(name='R13',
                position=[2*dx, 4*dy, ex, ey],
                switches_list=[])
    R14 = Room(name='R14',
                position=[3*dx, 0*dy, ex, ey],
                switches_list=[])
    R15 = Room(name='R15',
                position=[3*dx, 1*dy, ex, ey],
                switches_list=[])
    R16 = Room(name='R16',
                position=[3*dx, 2*dy, ex, ey],
                switches_list=[])
    R17 = Room(name='R17',
                position=[3*dx, 3*dy, ex, ey],
                switches_list=[])
    R18 = Room(name='R18',
                position=[3*dx, 4*dy, ex, ey],
                switches_list=[])
    R19 = Room(name='R19',
                position=[4*dx, 0*dy, ex, ey],
                switches_list=[])
    R20 = Room(name='R20',
                position=[4*dx, 1*dy, ex, ey],
                switches_list=[])
    R21 = Room(name='R21',
                position=[4*dx, 2*dy, ex, ey],
                switches_list=[])
    R22 = Room(name='R22',
                position=[4*dx, 3*dy, ex, ey],
                switches_list=[])
    R23 = Room(name='R23',
                position=[4*dx, 4*dy, ex, ey],
                switches_list=[])
    RE = Room(name='RE',
              position=[0*dx, 0*dy, ex, ey],
              is_exit=True)
    
    level = Maze(start_room_index=0,
                 exit_room_index=-1,
                 rooms_list=[RE],
                 doors_list=[D0, D1, D2, D3, D4, D5, D6, D7, D8, D9,
                             D10, D11, D12, D13, D14, D15, D16, D17, D18, D19,
                             D20, D21, D22, D23, D24, D25, D26, D27, D28, D29,
                             D30, D31, D32, D33, D34, D35, D36, D37, D38, D39,
                             D40, D41, D42, D43, D44, D45, D46, D47, D48, D49,
                             D50, D51, D52, D53, D54, D55, D56, D57, D58, D59,
                             D60, D61, D62, D63, D64, D65, D66, D67, D68, D69,
                             D70, D71, D72, D73, D74, D75, D76, D77, D78, D79,
                             D80, D81, D82, D83, D84, D85, D86, D87, D88, D89,
                             D90, D91, D92, D93, D94, D95, D96, D97, D98, D99,
                             D100, D101, D102, D103, D104, D105, D106, D107, D108, D109,
                             D110, D111, D112, D113, D114, D115, D116, D117, D118, D119,
                             D120, D121, D122, D123, D124, D125, D126, D127, D128, D129,
                             D130, D131, D132, D133, D134, D135, D136, D137, D138, D139,
                             D140, D141, D142, D143, D144, D145, D146, D147, D148, D149,
                             D150, D151, D152, D153, D154, D155, D156, D157, D158, D159,
                             D160, D161, D162, D163, D164, D165, D166, D167, D168],
                 fastest_solution=None,
                 level_color=Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.5),
                 name='TODO',
                 keep_proportions=True,
                 door_window_size=300)
    
    return level