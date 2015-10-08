# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats




def savitzky_golay(y, window_size=100, order=3, deriv=0, rate=1):
    import numpy as np
    from math import factorial

    order_range = range(order+1)
    half_window = (window_size -1) // 2
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


def smooth(x):
    smooth_x = np.round(savitzky_golay(x, window_size=100))
    return smooth_x


def get_center(x):
    mean = np.mean(x)
    media = np.median(x)
    mode = np.argmax(np.bincount(x.astype(int)))
#    from collections import Counter
#    c = Counter(x)
#    mode = sorted(c.keys(), key=lambda x:c[x])[-1]
    return mean, media, mode


def get_center2(x, n_bins=20):
    mean = np.mean(x)
    media = np.median(x)
    mode = np.argmax(savitzky_golay(np.bincount(x), window_size=(max(x) - min(x)) // n_bins))
    return mean, media, mode


def get_scatter(x):
    var = np.var(x)
    std = np.std(x)
    #std = var ** 0.5
    cv = 100. * std / np.mean(x)
    return var, std, cv


def quantile(x):
    return [np.percentile(x, i) for i in [0, 25, 50, 75, 100]]

def count_bitmap(x):
    c = np.bincount(x)
    return c[min(x):]


def pdf(x, norm_flag=False, zoom=1.):
    x = np.array(x)
    bias = x.min()
    x = (x - bias) * zoom 
    x = x.astype(int)
    #c = np.bincount(x)
    c = count_bitmap(x)
    if norm_flag:
#        c = c * (x.max() - x.min()) * 1. / len(x) 
        c = c * zoom * 1. / len(x) 
    #return np.arange(x.min()+bias, x.max()+1+bias) * 1. / zoom, c    
    return np.arange(x.min(), x.max()+1) * 1. / zoom + bias, c     

def cdf(x, norm_flag=False):
    i, p = pdf(x, norm_flag=False)
    cp = np.add.accumulate(p)
    if norm_flag:
        cp = cp * 1. / len(x)
    return i, cp
    

def pdf2(x, norm_flag=False, n_bins=20, zoom=1):
    i, p = pdf(x, norm_flag, zoom=zoom)
    xp = savitzky_golay(p, window_size=len(p)//n_bins)
    xp[xp < 0] = 0
    return i, xp
    
def skewness(x):
    return stats.moment(x, moment=3) / (np.std(x) ** 3)
    
def kurtosis(x):
    return stats.moment(x, moment=4) / (np.var(x) ** 2) - 3