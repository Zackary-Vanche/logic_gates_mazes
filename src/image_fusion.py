from os import mkdir as os_mkdir
from os import listdir as os_listdir
from os.path import exists as os_path_exists
from os import remove as os_remove
from cv2 import imread as cv2_imread
from cv2 import hconcat as cv2_hconcat
from cv2 import vconcat as cv2_vconcat
from cv2 import imwrite as cv2_imwrite
from Game import Game
from Levels import Levels
from pyautogui import size as pyautogui_size
import matplotlib.pyplot as plt
from Levels_colors_list import Levels_colors_list 

def divisor_closest_to_sqrt(n):
    from numpy import ceil, sqrt
    d = 1
    for k in range(1, int(ceil(sqrt(n))) + 1):
        if n % k == 0:
            d = k
    return min(n // d, d)

if __name__ == "__main__":
    
    racine = __file__
    racine = racine.split('\\')
    del racine[-1]
    racine.append('images')
    racine = '/'.join(racine)
    if not os_path_exists(racine):
        os_mkdir(racine)
    for file in os_listdir(racine):
        file = racine + '/' + file
        if 'level' in file:
            os_remove(file)

    # TOTAL_SIZE = pyautogui_size()
    # Game(save_image=1, time_between_level_changing=0, show_help=0).play()
    # TOTAL_SIZE = [1920, 1055]
    game_color = Levels_colors_list.FROM_HUE(hu=0, sa=0, li=0.4)
    game_color = None
    Game(is_fullscreen=0, save_image=1, game_color=game_color).play()
    #Game(is_fullscreen=1, save_image=1, game_color=game_color).play()

    if not os_path_exists('images'):
        os_mkdir('images')

    if not os_path_exists('images/concat'):
        os_mkdir('images/concat')
    
    n_levels = 2*Levels.number_of_levels
    n = divisor_closest_to_sqrt(n_levels)
    m = n_levels // n
    for size in [[1920, 1200],
                 [1920, 1080],
                 [1366, 768]]:  # [1346, 668], [1920, 1001], [1920, 1055],
        try:
            WIDTH, HEIGHT = size
            string = "WIDTH_{}_HEIGHT_{}".format(WIDTH, HEIGHT)
            dico = {}
            for file in os_listdir(racine):
                if string in file:# and not "concat" in file:
                    if "HELP" in file:
                        k = int(file.split('_')[2])
                        dico[(k, 0)] = '/'.join([racine, file])
                    else:
                        k = int(file.split('_')[1])
                        dico[(k, 1)] = '/'.join([racine, file])
            file_list = []
            for k in sorted(dico.keys()):
                file_list.append(dico[k])
            
            if len(file_list) == 0:
                print('no images')
                continue
    
            assert m >= n, f'~ {m} <= {n}'
            assert m * n == len(file_list), "{0}, {1}, {2}".format(m, n, len(file_list))
            l_img_h = []
            for i in range(m):
                l = file_list[n * i:n * i + n]
                l = [cv2_imread(file) for file in l]
                im_h = cv2_hconcat(l)
                l_img_h.append(im_h)
                filename = r'images/concat/concat_{}_levels_{}.jpg'.format(i, string)
                cv2_imwrite(filename, im_h)
            img = cv2_vconcat(l_img_h)
            plt.imshow(img)
            #plt.close()
            filename = r'images/concat/concat_levels_{}.jpg'.format(string)
            cv2_imwrite(filename, img)
            print(filename)
        except TypeError:
            pass
    
    n_levels = len(Levels.levels_list)
    lx = [i for i in range(n_levels, n_levels+30)]
    ly = []
    for i in lx:
        a = divisor_closest_to_sqrt(i)
        b = i//a
        a, b = min(a, b), max(a, b)
        ly.append(a/b)
    plt.plot(lx, ly)
    plt.scatter(lx, ly)
    plt.grid(True)