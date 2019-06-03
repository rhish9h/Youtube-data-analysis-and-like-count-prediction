#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:56:21 2018

@author: rhishabh
"""

import pandas as pd

datasets = []
datasets.append(pd.read_csv('youtube-new/CAvideos.csv'))
datasets.append(pd.read_csv('youtube-new/DEvideos.csv'))
datasets.append(pd.read_csv('youtube-new/FRvideos.csv'))
datasets.append(pd.read_csv('youtube-new/GBvideos.csv'))
datasets.append(pd.read_csv('youtube-new/USvideos.csv'))

names = ['views', 'dislikes', 'comment_count', 'likes']

new_dataset = datasets[0][names]

for dataset in datasets[1:]:
    new_dataset = new_dataset.append(dataset[names], ignore_index='true')
    
new_dataset.to_csv('new_dataset.csv')