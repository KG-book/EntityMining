# -*- coding: utf-8 -*-

import numpy as np
import numpy

def jaccard(X, Y):
    return len(X.intersection(Y)) * 1. / len(X.union(Y))
    
def dice(X, Y):
    return 2. * len(X.intersection(Y)) / (len(X) + len(Y))
    
def cover(X, Y):
    return len(X.intersection(Y)) * 1. / min(len(X), len(Y))
    
def VecCosSim(x1, x2):
    inner = numpy.dot(x1, x2)
    x1Norm = numpy.linalg.norm(x1)
    x2Norm = numpy.linalg.norm(x2)
    return inner * 1.0 / (x1Norm * x2Norm)


def pearson(X, Y):
    import scipy as sp
    return sp.stats.pearsonr(X, Y)[0]
