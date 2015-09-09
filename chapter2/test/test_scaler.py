# -*- coding: utf-8 -*-


from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ax = plt.gca()
plt.grid() #开启网格
ax.xaxis.set_major_locator( MultipleLocator(20) )
ax.yaxis.set_major_locator( MultipleLocator(5) )

d = np.loadtxt('../data/height_weight.lst')
ID, height, weight = d[:, 0], d[:, 1], d[:, 2]
#plt.plot(*pdf2(height), c='k', linewidth=2); 
#plt.plot(*pdf2(weight), c='c', linewidth=2); 



height_mm_scaler = preprocessing.MinMaxScaler()
h_scaled = height_mm_scaler.fit_transform(height)
weight_mm_scaler = preprocessing.MinMaxScaler()
w_scaled = weight_mm_scaler.fit_transform(weight)

plt.plot(*pdf2(h_scaled), c='k', linewidth=2); 
plt.plot(*pdf2(w_scaled), c='c', linewidth=2); 


height_std_scaler = preprocessing.StandardScaler()
h_std_rslt = height_std_scaler.fit_transform(height)
weight_std_scaler = preprocessing.StandardScaler()
w_std_rslt = weight_std_scaler.fit_transform(weight)