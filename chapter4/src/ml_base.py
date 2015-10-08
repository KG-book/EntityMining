# -*- coding: utf-8 -*-
import numpy as np

def classification_effect(y, r):
    print "accuracy=%s" % (sum(y==r) * 1. / len(y))
    for i in set(y):
        p = sum(y == i)
        tp = sum(r[y == i] == i)
        pp = sum(r == i)
        precision = tp * 1. / pp
        recall = tp * 1. / p
        f1 = 2 * precision * recall / (precision + recall)
        print i, "\tprecision=%s" % precision, "\trecall=%s" % recall, "\tf1=%s" % f1   


d = np.loadtxt('../data/classification_samples.lst')
X_train = d[:600, 1:] 
y_train = d[:600, 0] 
X_test = d[600:, 1:] 
y_test = d[600:, 0] 