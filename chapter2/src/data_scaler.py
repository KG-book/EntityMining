# -*- coding: utf-8 -*-
from data_distribute_feature import *
import numpy as np

    
    
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


def pearson(X, Y):
    import scipy as sp
    return sp.stats.pearsonr(X, Y)[0]