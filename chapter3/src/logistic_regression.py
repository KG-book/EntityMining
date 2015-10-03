# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
def sigmoid(x):
    return 1. / (1 + np.e ** -x)
    
    
X = np.arange(-10, 10, 0.01)
Y = map(sigmoid, X)
pl.plot(X, Y); pl.ylim(-0.1, 1.2)

Y2 = np.zeros(len(X))
Y2[len(Y2)/2: ] = 1
pl.plot(X, Y2, '--'); pl.ylim(-0.1, 1.2)


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(c=1.2)
#lr.fit(X, y)