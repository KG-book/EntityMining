# -*- coding: utf-8 -*-
import numpy as np

def mock_data(min_val=0, center=3., df=3, size=10000):
    p = np.random.chisquare(df=df, size=size) 
    p = p * ((center-min_val) * 1. / df) + min_val
    p = p.astype(int)
    return p

