# -*- coding: utf-8 -*-
from data_distribute_feature import *



import numpy as np
from data_distribute_feature import cdf

class CdfScorer(object):
    def __init__(self):
        self.cdf_values_ = None
        self.cdf_scores_ = None
        self.minval_ = None
        self.maxval_ = None
        
    def fit(self, X):
        '''X is array-like
        '''
        self.cdf_values, self.cdf_scores = cdf(X, norm_flag=True)
        self.minval_ = X.min()
        self.maxval_ = X.max()
    
    def transform_one(self, x):
        '''x is an int or float value
        '''
        if x < self.minval_:
            return 0
            
        if x >= self.maxval_:
            return 1.
            
        for i, v in enumerate(self.cdf_values):
            if v > x:
                return self.cdf_scores[i-1]
        return 1.
        
    def transform(self, X):
        '''X is array-like
        '''
        return np.array([self.transform_one(x) for x in X])
            
    def fit_transform(self, X):
        '''X is array-like
        '''
        self.fit(X)
        return self.transform(X)
        
        

class TfIdf(object):
    def __init__(self):
        pass
    
    def fit(self, X):
        self.idf = np.log(len(X) / (sum(X!=0) + 1.))
        
        
    def transform(self, X):
        return X * self.idf
        
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
    
        
    
        

def log_score(X):
    m = X.max() + 1
    return np.array([np.log(x+1) * 1. / np.log(m) for x in X])

def find_pos(s, indices):
    for i, v in enumerate(indices):
        if v > s:
            return i - 1
    return i

def cdf_score(x):
    idx, cp = cdf(x)
    pos = np.array([find_pos(xi, idx) for xi in x])
    return cp[pos] * 1. / len(x)



    
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
    
    
