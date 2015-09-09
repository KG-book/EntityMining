# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.pyplot import hist
x = np.loadtxt('../data/salary.lst')
hist(x, bins=100)