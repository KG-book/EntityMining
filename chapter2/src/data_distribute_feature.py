# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats


def height_weight_mock(min_height=145, mid_height=175, df=6, size=1000):
    h = mock_data(min_val=min_height, center=mid_height, df=df, size=size)
    h[h>220] = mid_height + int(np.random.normal(scale=5))
    w = h - 105
    w += np.random.normal(scale=w/5.)
    return h, w


def height_weight_file(save_path, size=1000):
    h, w = height_weight_mock(size=size)
    i = np.arange(1, size+1)
    d = np.hstack((i.reshape(-1, 1), 
                   h.reshape(-1, 1), 
                   w.reshape(-1, 1)))
    np.savetxt(save_path, d, fmt='%s')

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
        c = c * 1. / len(x) 
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
    return i, savitzky_golay(p, window_size=len(x)//n_bins)
    
    
def skewness(x):
    return stats.moment(x, moment=3) / (np.std(x) ** 3)
    
def kurtosis(x):
    return stats.moment(x, moment=4) / (np.var(x) ** 2) - 3