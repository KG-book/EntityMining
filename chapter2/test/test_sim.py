# -*- coding: utf-8 -*-
import numpy as np
from data_dist import *

d = np.loadtxt('../data/height_weight.lst')
ID, height, weight = d[:, 0], d[:, 1], d[:, 2]

height_mm_scaler = preprocessing.MinMaxScaler()
h_scaled = height_mm_scaler.fit_transform(height)
weight_mm_scaler = preprocessing.MinMaxScaler()
w_scaled = weight_mm_scaler.fit_transform(weight)

height_std_scaler = preprocessing.StandardScaler()
h_std_rslt = height_std_scaler.fit_transform(height)
weight_std_scaler = preprocessing.StandardScaler()
w_std_rslt = weight_std_scaler.fit_transform(weight)

print VecCosSim(height, weight), VecCosSim(h_scaled, w_scaled), VecCosSim(h_std_rslt, w_std_rslt)

print pearson(height, weight), pearson(h_scaled, w_scaled), pearson(h_std_rslt, w_std_rslt)