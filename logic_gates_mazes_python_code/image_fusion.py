import os
import cv2
from Game import Game
from Levels import Levels
from pyautogui import size as pyautogui_size

def divisor_closest_to_sqrt(n):
    from numpy import ceil, sqrt
    d = 1
    for k in range(1, int(ceil(sqrt(n)))):
        if n%k == 0:
            d = k
    return d
    
def main():

    # TOTAL_SIZE = pyautogui_size()
    # Game(save_image=1, time_between_level_changing=0, show_help=0).play()
    # TOTAL_SIZE = [1920, 1055]
    Game(is_fullscreen=True, save_image=True).play()


    racine = __file__
    racine = racine.split('\\')
    del racine[-1]
    racine.append('images')
    racine = '/'.join(racine)
    n_levels = Levels.number_of_levels
    m = divisor_closest_to_sqrt(n_levels)
    n = n_levels//m
    for size in [[1920, 1080]]: # [1346, 668], [1920, 1001], [1920, 1055], 
        try:
            WIDTH, HEIGHT = size
            string = "WIDTH_{}_HEIGHT_{}".format(WIDTH, HEIGHT)
            dico = {}
            for file in os.listdir(racine):
                if string in file and not "HELP" in file and not "concat" in file:
                    k = int(file.split('_')[1])
                    dico[k] = '/'.join([racine, file])
            file_list = []
            for k in sorted(dico.keys()):
                file_list.append(dico[k])

            assert m <= n 
            assert m*n==len(file_list), """{0}, {1}, {2}""".format(m, n, len(file_list))
            l_img_h = []
            for i in range(m):
                l = file_list[n*i:n*i+n]
                l = [cv2.imread(file) for file in l]
                im_h = cv2.hconcat(l)
                l_img_h.append(im_h)
            img = cv2.vconcat(l_img_h)
            filename = r'images/concat_levels_{}.jpg'.format(string)
            cv2.imwrite(filename, img)
            print(filename)
            # cv2.imwrite(r'images/concat_line_levels_{}.jpg'.format(string),
            #             cv2.hconcat([cv2.imread(file) for file in file_list]))
        except:
            raise
        try:
            WIDTH, HEIGHT = size
            string = "WIDTH_{}_HEIGHT_{}".format(WIDTH, HEIGHT)
            dico = {}
            for file in os.listdir(racine):
                if string in file and "HELP" in file and not "concat" in file:
                    k = int(file.split('_')[2])
                    dico[k] = '/'.join([racine, file])
            file_list = []
            for k in sorted(dico.keys()):
                file_list.append(dico[k])

            assert m <= n
            assert m*n==len(file_list)
            l_img_h = []
            for i in range(m):
                l = file_list[n*i:n*i+n]
                l = [cv2.imread(file) for file in l]
                im_h = cv2.hconcat(l)
                l_img_h.append(im_h)
            img = cv2.vconcat(l_img_h)
            filename = r'images/concat_levels_HELP_{}.jpg'.format(string)
            cv2.imwrite(filename, img)
            print(filename)
            # cv2.imwrite(r'images/concat_line_levels_HELP_{}.jpg'.format(string),
            #             cv2.hconcat([cv2.imread(file) for file in file_list]))
        except:
            raise

if __name__ == "__main__":
    
    main()