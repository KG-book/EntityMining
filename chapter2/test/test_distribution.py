# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.pyplot import hist
x = np.loadtxt('../data/salary.lst')
hist(x, bins=100)


from scipy import stats
stats.skew(x)
stats.kurtosis(x)
