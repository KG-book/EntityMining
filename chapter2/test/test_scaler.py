# -*- coding: utf-8 -*-


from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys
sys.path.append('../src')
from data_distribute_feature import *

#ax = plt.gca()
#plt.grid() #开启网格
##plt.xlim(0,7)
#plt.ylim(0, 0.06)

#ax.xaxis.set_major_locator( MultipleLocator(1) )
#ax.yaxis.set_major_locator( MultipleLocator(5) )

d = np.loadtxt('../data/height_weight.lst')
ID, height, weight = d[:, 0], d[:, 1], d[:, 2]
#plt.plot(*pdf2(height, norm_flag=True), c='k', linewidth=2); 
#plt.plot(*pdf2(weight, norm_flag=True), c='c', linewidth=2); 


#ax.xaxis.set_major_locator( MultipleLocator(0.1) )
#ax.yaxis.set_major_locator( MultipleLocator(5) )

height_mm_scaler = preprocessing.MinMaxScaler()
h_scaled = height_mm_scaler.fit_transform(height)
weight_mm_scaler = preprocessing.MinMaxScaler()
w_scaled = weight_mm_scaler.fit_transform(weight)
plt.plot(*pdf2(h_scaled, zoom=70, norm_flag=True), c='k', linewidth=2); 
plt.plot(*pdf2(w_scaled, zoom=70, norm_flag=True), c='c', linewidth=2); 


height_std_scaler = preprocessing.StandardScaler()
h_std_rslt = height_std_scaler.fit_transform(height)
weight_std_scaler = preprocessing.StandardScaler()
w_std_rslt = weight_std_scaler.fit_transform(weight)
#plt.plot(*pdf2(h_std_rslt, norm_flag=True, zoom=20), c='k', linewidth=2); 
#plt.plot(*pdf2(w_std_rslt, norm_flag=True, zoom=20), c='c', linewidth=2); 

#h_cdf = cdf(height, norm_flag=True)[1]
#w_cdf = cdf(weight, norm_flag=True)[1]
#
#plt.plot(*pdf2(w_cdf, zoom=1000), c='c', linewidth=2); 