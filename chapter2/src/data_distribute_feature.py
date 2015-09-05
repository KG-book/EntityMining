# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter


def mock_data(min_val=0, center=3., df=3, size=10000):
    p = np.random.chisquare(df=df, size=size) 
    p = p * ((center-min_val) * 1. / df) + min_val
    p = p.astype(int)
    return p



def savitzky_golay(y, window_size=100, order=3, deriv=0, rate=1):
    import numpy as np
    from math import factorial

    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


def smooth(x, window_size=100, order=3, deriv=0, rate=1):
    smooth_x = np.round(savitzky_golay(x, window_size=(max(x) - min(x)) // 20))
    return smooth_x.astype(int)


def get_center(x):
    mean = np.mean(x)
    media = np.median(x)
    mode = np.argmax(np.bincount(x))
    return mean, media, mode


def get_center2(x):
    mean = np.mean(x)
    media = np.median(x)
    mode = np.argmax(savitzky_golay(np.bincount(x), window_size=(max(x) - min(x)) // 20))
    return mean, media, mode



def pdf(x, norm_flag=False):
    c = np.bincount(x)
    if norm_flag:
        c = c * 1. /sum(x)
    return c    




def cdf(x):
    pass