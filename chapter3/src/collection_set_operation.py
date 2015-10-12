# -*- coding: utf-8 -*-

def jaccard(X, Y):
    return len(X.intersection(Y)) * 1. / len(X.union(Y))
    
def dice(X, Y):
    return 2. * len(X.intersection(Y)) / (len(X) + len(Y))
    
def cover(X, Y):
    return len(X.intersection(Y)) * 1. / min(len(X), len(Y))
