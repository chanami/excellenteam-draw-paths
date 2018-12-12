import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot

np = numpy
plt = pyplot
import pandas as pd
from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *
import controller


class View():
    def set_attr(self,file,pic):
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
              2, filter by date and hours range
              3. filter by selected area
              4. filter by specific areas
              5. no filter 
              6. exit\n""")
        return command

    def get_command(self):
        command = self.get_filter()
        file = input("enter file\n")
        picture = input("enter picture\n")
        return (command, file, picture)

    def edit(self):
        command = input("""choose edit:
                1. add filter
                2, change filter
                3. no edit\n""")
        return command

