#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:58:06 2018

@author: rhishabh
"""

import pandas as pd
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(cur_dir)

datasets = []
datasets.append(pd.read_csv(root_dir + '/' + 'youtube-new/CAvideos.csv'))
datasets.append(pd.read_csv(root_dir + '/' + 'youtube-new/DEvideos.csv'))
datasets.append(pd.read_csv(root_dir + '/' + 'youtube-new/FRvideos.csv'))
datasets.append(pd.read_csv(root_dir + '/' + 'youtube-new/GBvideos.csv'))
datasets.append(pd.read_csv(root_dir + '/' + 'youtube-new/USvideos.csv'))

new_dataset = datasets[0]

for dataset in datasets[1:]:
    new_dataset = new_dataset.append(dataset, ignore_index='true')
    
new_dataset.to_csv('full_combined.csv')