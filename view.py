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
    def __init__(self):
        self.df = pd.read_pickle('data/paths.pkl.xz')


    def draw_path(self,to_draw):
        print("in draw")
        img = imread("paths0.png")
        imshow(img)
        df_by_obj = self.df.set_index(['filename', 'obj']).sort_index()
        for t in to_draw.index:
            oo = df_by_obj.loc[t]
            plot(oo.x, oo.y)
        show()


    def get_command(self):
        command=input("enter 1 for hours, 2 for date+hours ")
        return command


