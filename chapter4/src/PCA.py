# -*- coding: utf-8 -*-
from sklearn import preprocessing

import matplotlib.pyplot as plt
import numpy as np


d = np.loadtxt('../../chapter2/data/height_weight.lst')

scaler = preprocessing.MinMaxScaler()
d_scaled = scaler.fit_transform(d[:, 1:])

from sklearn.decomposition import PCA
pca = PCA()
v = pca.fit_transform(d_scaled)
print pca.explained_variance_ratio_

plt.scatter(d_scaled[:,0], d_scaled[:,1], c='w')

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(np.array(d_scaled[:, 0]).reshape(-1, 1),
       np.array(d_scaled[:, 1]).reshape(-1, 1))
       
height_sorted = np.array(sorted(d_scaled[:, 0]))

plt.plot(height_sorted, 
        lr.predict(height_sorted.reshape(-1, 1)),
        c='k', linewidth=3)
        

weight_sorted = np.array(sorted(d_scaled[:, 1]))     
plt.plot(weight_sorted, -1./lr.coef_ [0][0]* weight_sorted+1.35, 'k--', linewidth=3);plt.xlim(0,1);plt.ylim((0,1))