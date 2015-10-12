# -*- coding: utf-8 -*-

import numpy as np

from ml_base import *
from sklearn.datasets import make_classification

d = make_classification(n_samples=1000)

from sklearn.svm import SVC

d = np.loadtxt('../data/classification_samples.lst')
X_train = d[:600, 1:] 
y_train = d[:600, 0] 
X_test = d[600:, 1:] 
y_test = d[600:, 0] 


svc = SVC(C=0.1)
svc.fit(X_train, y_train)
p = svc.predict(X_test)
classification_effect(y_test, p)
classification_effect(y_train, svc.predict(X_train))

#powers = np.arange(-10.0, 10.0)
#
#clist = 2**powers
#rlist = np.zeros(21)
#rlist[1:] = 2**powers
#paradict=dict(C=clist, gamma=rlist)
#
#
#from sklearn.grid_search import GridSearchCV
#from sklearn.cross_validation import cross_val_score
#
#print cross_val_score(SVC(C=0.5), X_train, y_train, cv=5)
#p = SVC(C=0.5).fit(X_train, y_train).predict(X_test)
#classification_effect(y_test, p)
#gsearch = GridSearchCV(SVC(), param_grid=paradict, cv=5)
#gsearch.fit(X_train, y_train)

