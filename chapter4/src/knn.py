# -*- coding: utf-8 -*-

import numpy as np
from collections import Counter


class KNN(object):
    def __init__(self, k=20):
        self.k = k
    
    def fit(self, X, y):
        self.dataset = X
        self.labels = y
        
    def predict_one(self, x):
        dist = np.linalg.norm(np.tile(x, (self.dataset.shape[0], 1)) - self.dataset, axis=1)
        sorted_indices = dist.argsort()[:self.k]
        cnt = Counter(self.labels[sorted_indices])
        return max(cnt.keys(), key=lambda a:cnt[a])

    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])



d = np.loadtxt('../data/classification_samples.lst')
X_train = d[:600, 1:] 
y_train = d[:600, 0] 
X_test = d[600:, 1:] 
y_test = d[600:, 0] 


knn = KNN()
knn.fit(X_train, y_train)
r = knn.predict(X_test)
print sum(p==y_test) * 1. / len(p)


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
        
        
    