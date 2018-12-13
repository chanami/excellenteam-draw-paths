import cv2
import numpy
from matplotlib import  pyplot

np = numpy
plt = pyplot
import pandas as pd
from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *
import controller


class View:
    def set_attr(self,pic):
        # self.df = pd.read_pickle(file) #'data/paths.pkl.xz'
        self.img= imread(pic)#"paths0.png"
        # self.index_file = self.df.set_index(['filename', 'obj']).sort_index()


    # def draw_path(self,to_draw):
    #     print("in draw")
    #     imshow(self.img)
    #     # df_by_obj = self.df.set_index(['filename', 'obj']).sort_index()
    #     for t in to_draw.index:
    #         oo = self.index_file.loc[t]
    #         # imshow(self.img)
    #         plot(oo.x, oo.y)
    #         # show()
    #     show()

    def draw_path(self, to_draw):
        print("in draw")
        imshow(self.img)
        for x,y in to_draw:
            plot(x,y)
        show()


    def get_filter(self):
        command = input("""enter filter selection:
              1. filter by hours range
              2. filter by date and hours range
              3. filter by selected area
              4. filter by specific areas
              5. no filter 
              6. exit\n""")
        return command

    def get_files(self):
        # command = self.get_filter()
        file = input("enter file\n")
        picture = input("enter picture\n")
        return ( file, picture)# command,

    def edit(self):
        command = input("""choose edit:
                1. add filter
                2, change filter
                3. no edit\n""")
        return command

    def draw_grid(self):
        size = 10
        i = 0
        ab = range(size * size)
        im = cv2.imread("paths0.png", 1)
        h, w = im.shape[:2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        dx, dy = w // size, h // size
        for y in range(size):
            for x in range(size):
                x_place, y_place = int((x * dx + dx / 2) - size), int(y * dy + dy - size)
                cv2.putText(im, str(ab[i]), (x_place, y_place), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
                i += 1
        for i in range(dy, h, dy):
            im[i:i + 2, :] = 0
        for i in range(dx, w, dx):
            im[:, i:i + 2] = 0
        cv2.imwrite("grid_img.png", im)
        img = imread("grid_img.png")
        imshow(img)
        show()
        # print("in grid")
        # img =self.img
        # h, w = img.shape[:2]
        # dx = w // 10
        # dy = h // 10
        # for i in range(dy, h, dy):
        #     img[i:i + 2, :] = 0
        # for i in range(dx, w, dx):
        #     img[:, i:i + 2] = 0
        # imshow(img)
        # show()

