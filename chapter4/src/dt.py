# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from ml_base import *




dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X_train, y_train)

classification_effect(y_train, dt.predict(X_train))
classification_effect(y_test, dt.predict(X_test))

#from sklearn.preprocessing import MinMaxScaler
#e = MinMaxScaler().fit_transform(X_train)
#a = np.ceil(e*10)
#
#from sklearn.datasets import make_classification
#dd = make_classification(n_samples=5000, n_features=500)
#print cross_val_score(DecisionTreeClassifier(), dd[0], dd[1], cv=8)