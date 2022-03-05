import os
import cv2

if __name__ == "__main__":
    racine = __file__
    racine = racine.split('\\')
    del racine[-1]
    racine.append('images')
    racine = '/'.join(racine)
    for size in [[1346, 668], [1920, 1001], [1920, 1055]]:
        try:
            print(size)
            WIDTH, HEIGHT = size
            string = "WIDTH_{}_HEIGHT_{}".format(WIDTH, HEIGHT)
            dico = {}
            for file in os.listdir(racine):
                if string in file and not "HELP" in file and not "concat" in file:
                    n = int(file.split('_')[1])
                    dico[n] = '/'.join([racine,file])
            file_list = []
            for n in sorted(dico.keys()):
                file_list.append(dico[n])
                
            # l_img_h = []
            # for i in range(4):
            #     l = file_list[4*i:4*i+4]
            #     l = [cv2.imread(file) for file in l]
            #     im_h = cv2.hconcat(l)
            #     l_img_h.append(im_h)
            # img = cv2.vconcat(l_img_h)
            
            # cv2.imwrite('images/concat_levels_{}.jpg'.format(string), img)
            
            cv2.imwrite('images/concat_line_levels_{}.jpg'.format(string), cv2.hconcat([cv2.imread(file) for file in file_list]))
        except:
            pass