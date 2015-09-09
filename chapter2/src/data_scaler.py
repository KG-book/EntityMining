# -*- coding: utf-8 -*-
from data_distribute_feature import *
import numpy as np

def height_weight_mock(min_height=145, mid_height=175, df=6, size=1000):
    h = mock_data(min_val=min_height, center=mid_height, df=df, size=size)
    h[h>220] = mid_height + int(np.random.normal(scale=5))
    w = h - 105
    w += np.random.normal(scale=w/5.)
    return h, w


def height_weight_file(save_path, size=1000):
    h, w = height_weight_mock(size=size)
    i = np.arange(1, size+1)
    d = np.hstack((i.reshape(-1, 1), 
                   h.reshape(-1, 1), 
                   w.reshape(-1, 1)))
    np.savetxt(save_path, d, fmt='%s')
    
    
def line_regress(height, weight):

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    
    lr.fit(np.array(height).reshape(-1, 1),
           np.array(weight).reshape(-1, 1))
    
    import pylab as pl
    height_sorted = sorted(height)
    pl.scatter(height, weight, c='w', marker='o')
    pl.plot(height_sorted, 
            lr.predict(np.array(height_sorted).reshape(-1, 1)),
            c='k', linewidth=3)

    return lr.coef_, lr.intercept_


