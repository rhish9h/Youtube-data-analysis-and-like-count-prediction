#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:59:18 2018

@author: rhishabh
"""

#train random forest model with the combined dataset


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle
import matplotlib.pyplot as plt 

#load X_train, X_test, y_train, y_test from train_test_data pickle
pfile = open('train_test_data', 'rb')
X_train = pickle.load(pfile)
X_test = pickle.load(pfile)
y_train = pickle.load(pfile)
y_test = pickle.load(pfile)

#train the model & fit the model
regressor = RandomForestRegressor()
regressor.fit(X_train, y_train.ravel())

#check feature importance
names = ['dislikes', 'comment_count', 'views']
i=0
for name in names:    
    print(name, regressor.feature_importances_[i])
    i+=1

#test the model
pred = regressor.predict(X_test)
accuracy = r2_score(y_test, pred)     #r2 used to get accuracy in regression

print('\naccuracy of random forest regression : {0:.3f}'.format(accuracy*100))

comments = X_test[:, 1]

#plot graph
labels = ['train', 'test']
plt.scatter(X_train[:, 1], y_train)
plt.scatter(X_test[:,1], y_test)
plt.title('comments vs likes')
plt.xlabel('comments')
plt.ylabel('likes')
plt.legend(labels)
plt.plot(comments, pred, color='red')
#save graph to png format
#plt.savefig('pred_c_vs_l', dpi=300)
plt.show()
