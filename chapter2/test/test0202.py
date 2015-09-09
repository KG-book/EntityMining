# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
from data_distribute_feature import *

x = np.loadtxt('../salary.lst');
x = x.astype(int)
x_mean, x_median, x_mod = get_center(x)

pl.plot(pdf(x))
pl.plot(cdf(x))

pl.plot(p,'--', c='c'); pl.plot(s, c='black')