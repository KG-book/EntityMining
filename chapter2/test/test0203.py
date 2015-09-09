# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
import pylab as pl
from data_distribute_feature import *
from sklearn import preprocessing

x = np.loadtxt('../salary.lst');



#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#i, p = pdf2(x_scaled, zoom=10000)
#pl.plot(*pdf2(x_scaled, zoom=10000))
##pl.plot(*pdf2(x_scaled, zoom=10000))


std_scaler = preprocessing.StandardScaler()
x_std = std_scaler.fit_transform(x)
pl.plot(*pdf2(x_std, zoom=10000))