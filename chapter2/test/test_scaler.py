# -*- coding: utf-8 -*-


from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys
sys.path.append('../src')
from data_distribute_feature import *
from data_scaler import *

ax = plt.gca()
plt.grid() #开启网格
#plt.xlim(0, 220)
#plt.ylim(0, 0.03)
#
#ax.xaxis.set_major_locator( MultipleLocator(10) )
#ax.yaxis.set_major_locator( MultipleLocator(5) )


d = np.loadtxt('../data/height_weight.lst')
ID, height, weight = d[:, 0], d[:, 1], d[:, 2]



#plt.xlim(0, 225)
#plt.ylim(0, 0.03)
#ax.xaxis.set_major_locator( MultipleLocator(10) )
#
#plt.plot(*pdf2(height, norm_flag=True, n_bins=2), c='k', linewidth=2); 
#plt.plot(*pdf2(weight, norm_flag=True, n_bins=2), c='c', linewidth=2); 


#ax.xaxis.set_major_locator( MultipleLocator(0.1) )
#ax.yaxis.set_major_locator( MultipleLocator(5) )

height_mm_scaler = preprocessing.MinMaxScaler()
h_scaled = height_mm_scaler.fit_transform(height)
weight_mm_scaler = preprocessing.MinMaxScaler()
w_scaled = weight_mm_scaler.fit_transform(weight)
#
##plt.plot(height, h_scaled)
#
##plt.xlim(0, 1.05)
##plt.ylim(0, 3)
##ax.xaxis.set_major_locator( MultipleLocator(0.1) )
##plt.plot(*pdf2(h_scaled, zoom=100, n_bins=2, norm_flag=True), c='k', linewidth=2); 
##plt.plot(*pdf2(w_scaled, zoom=100, n_bins=2, norm_flag=True), c='c', linewidth=2); 
#
#
#height_std_scaler = preprocessing.StandardScaler()
#h_std_rslt = height_std_scaler.fit_transform(height)
#weight_std_scaler = preprocessing.StandardScaler()
#w_std_rslt = weight_std_scaler.fit_transform(weight)
##plt.plot(*pdf2(h_std_rslt, norm_flag=True, n_bins=2, zoom=20), c='k', linewidth=2); 
##plt.plot(*pdf2(w_std_rslt, norm_flag=True, n_bins=2, zoom=20), c='c', linewidth=2); 
#
##h_cdf = cdf_score(height)
##w_cdf = cdf_score(weight)
#from data_scaler import CdfScorer
#
#d = np.loadtxt('../data/customer.lst')
#ID, f, r, z, s = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4]
#
#cdfscorer = CdfScorer()
#sc = cdf_score(s)
#plt.plot(*pdf2(sc, zoom=1000, n_bins=8, norm_flag=True), c='k', linewidth=2); plt.ylim(0,2)

#s = np.loadtxt('../data/salary.lst')
#h_cdf = cdf_score(s)
#plt.plot(*pdf2(h_cdf, zoom=10000, norm_flag=True), c='c', linewidth=2); 
#plt.plot(*pdf2(h_cdf, zoom=1000, n_bins=10, norm_flag=True), c='k', linewidth=2);
#plt.plot(*pdf2(w_cdf, zoom=1000, n_bins=10, norm_flag=True), c='c', linewidth=2);



#from data_scaler import *
#sl = log_score(s)
#plt.subplot(211); 
#plt.plot(*pdf2(s, n_bins=8), c='k', linewidth=2); 
#plt.grid();
#
#plt.subplot(212); 
#plt.plot(*pdf2(sl, zoom=1000, n_bins=8, norm_flag=True), c='k', linewidth=2); 
#plt.grid(); 
#plt.ylim(0,3)


#tfidf = TfIdf()
#ftf = tfidf.fit_transform(f)
#rtf = tfidf.fit_transform(r)
#stf = tfidf.fit_transform(s)
#ztf = tfidf.fit_transform(z)
#plt.plot(*pdf2(ftf, zoom=1000, n_bins=8, norm_flag=True), c='k', linewidth=2)
#plt.plot(*pdf2(rtf, zoom=1000, n_bins=8, norm_flag=True), c='c', linewidth=2)
#plt.plot(*pdf2(stf, zoom=1000, n_bins=8, norm_flag=True), c='r', linewidth=2)
#plt.plot(*pdf2(ztf, zoom=1000, n_bins=8, norm_flag=True), c='g', linewidth=2)


from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(np.array(h_scaled).reshape(-1, 1),
       np.array(w_scaled).reshape(-1, 1))

import pylab as pl
height_sorted = sorted(h_scaled)
pl.scatter(h_scaled, w_scaled, c='w', marker='o')
pl.plot(height_sorted, 
        lr.predict(np.array(height_sorted).reshape(-1, 1)),
        c='k', linewidth=3)

lr.coef_, lr.intercept_

