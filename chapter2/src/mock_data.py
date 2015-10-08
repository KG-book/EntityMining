# -*- coding: utf-8 -*-
import numpy as np

def mock_data(min_val=0, center=3., df=3, size=10000):
    p = np.random.chisquare(df=df, size=size) 
    p = p * ((center-min_val) * 1. / df) + min_val
    p = p.astype(int)
    return p



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