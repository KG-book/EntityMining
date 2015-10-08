# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
from mock_data import *

import numpy as np


f = mock_data(min_val=0, center=5, df=3.5, size=2000)
r = mock_data(min_val=0, center=10, df=3, size=2000)
s = mock_data(min_val=0, center=40, df=3.5, size=2000)
z = mock_data(min_val=0, center=4, df=1, size=2000)


z[np.random.random_integers(0, len(z)-1, 700)] = 0
f[np.random.random_integers(0, len(f)-1, 400)] = 0
r[np.random.random_integers(0, len(r)-1, 200)] = 0
s[np.random.random_integers(0, len(s)-1, 100)] = 0


i = np.arange(1, 2001)
d = np.hstack((i.reshape(-1, 1), 
               z.reshape(-1, 1), 
               f.reshape(-1, 1),
r.reshape(-1, 1),
s.reshape(-1, 1)
))


import matplotlib.pyplot as plt
plt.subplot(221); plt.plot(*pdf2(f), linewidth=2); 
plt.subplot(222); plt.plot(*pdf2(r), linewidth=2); plt.ylim(0, 300)
plt.subplot(223); plt.plot(*pdf2(z), linewidth=2); plt.ylim(0, 1300) 
plt.subplot(224); plt.plot(*pdf2(s), linewidth=2); plt.ylim(0, 40) 


def show_plot(x):
    i, c = pdf(x)
    plt.plot(i, np.log(c))
    
    
#show_plot(f);
#show_plot(r);
#show_plot(z);
#show_plot(s);