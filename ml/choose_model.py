#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:16:50 2018

@author: rhishabh
"""

#choose model based on cross validation

import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import r2_score
#from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from tqdm import tqdm
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor
#import numpy as np
import pickle
import os

#load the dataset
names = ['likes', 'dislikes', 'comment_count', 'views']

cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(cur_dir)

dataset = pd.read_csv(root_dir + '/youtube-new/new_dataset.csv')
dataset = dataset[names]

#set inputs and outputs
training_set_inputs = dataset[['dislikes', 'comment_count', 'views']].values
training_set_outputs = dataset[['likes']].values

#plot scatter matrix
print('\nPlotting scatter matrix...')
scatter_matrix(dataset)
plt.show()
#plt.scatter(dataset[['likes']], dataset[['views']])
#plt.show()

#split the datapoints into training and testing parts
print('\nsplitting data into train and test...')
X_train, X_test, y_train, y_test = train_test_split(training_set_inputs, training_set_outputs, random_state=7, test_size=0.2)

#pickle X_train, X_test, y_train, y_test
print('\nPickling X_train, X_test, y_train, y_test into - train_test_data')
pfile = open('train_test_data', 'wb')
pickle.dump(X_train, pfile)
pickle.dump(X_test, pfile)
pickle.dump(y_train, pfile)
pickle.dump(y_test, pfile)
pfile.close()

#create list of models
models = []
models.append(('Rand_For', RandomForestRegressor()))
models.append(('Lin_Reg', LinearRegression()))
models.append(('Ridge', Ridge()))
models.append(('KNN_Reg', KNeighborsRegressor()))
models.append(('Dec_tree', DecisionTreeRegressor()))
models.append(('MLP_Reg', MLPRegressor()))
models.append(('Grad_boost', GradientBoostingRegressor()))

#print(models)

#evaluate each model
results = []
model_names = []

print('evaluating different models...')
for name, model in tqdm(models):
    #divide the training data further for cross validation
    kfold = model_selection.KFold(n_splits=7, random_state=7)
    cv_results = model_selection.cross_val_score(model, X_train, y_train.ravel(), cv=kfold, scoring='r2')
    results.append(cv_results)
    model_names.append(name)
    print('\n{} - {}'.format(name, cv_results.mean()*100))