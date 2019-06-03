# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:23:07 2018

@author: Asus
"""
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle
import matplotlib.pyplot as plt 
import numpy as np

#load X_train, X_test, y_train, y_test from train_test_data pickle
pfile = open('train_test_data', 'rb')
X_train = pickle.load(pfile)
X_test = pickle.load(pfile)
y_train = pickle.load(pfile)
y_test = pickle.load(pfile)

#train the model & fit the model


views = input("Views :: ")
dislikes = input("Dislikes :: ")
comments = input("Comments :: ")
#X_input=np.array([1,2,3])
X_input=np.array([[views, comments, dislikes]])

regressor = RandomForestRegressor()
regressor.fit(X_train, y_train.ravel())
#comments = X_test[:, 1]
X_input.reshape(1,-1)
pred = regressor.predict(X_input)
#plot graph
labels = ['train', 'test']
plt.scatter(X_train[:, 1], y_train)
#plt.scatter(X_test[:,1], y_test)
plt.title('comments vs likes')
plt.xlabel('comments')
plt.ylabel('likes')
plt.legend(labels)
plt.scatter(X_input[0][0], pred[0], color='red')
plt.show()
