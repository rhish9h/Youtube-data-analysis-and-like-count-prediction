#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:23:10 2018

@author: rhishabh
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import shutil

#set path of dataset file
cur_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(cur_dir)

#create directory for pickle folder
# =============================================================================
# pickle_root = cur_dir + '/countries_pickles'
# 
# if os.path.exists(pickle_root):
#     shutil.rmtree(pickle_root)       #deletes the directory (to replace directory if it exists)
# os.makedirs(pickle_root)             #create directory to save all pickles                   
# =============================================================================


cat_index = {
            'views' : 7,
            'likes' : 8,
            'dislikes' : 9,
            'comments' : 10
        }

for cat in cat_index:
    #read country dataset, locate requested column, sum it, for all countries
    sums = [
            pd.read_csv(root_dir + '/' + 'youtube-new/USvideos.csv').iloc[:, cat_index[cat]].sum(),
            pd.read_csv(root_dir + '/' + 'youtube-new/CAvideos.csv').iloc[:, cat_index[cat]].sum(),
            pd.read_csv(root_dir + '/' + 'youtube-new/GBvideos.csv').iloc[:, cat_index[cat]].sum(),
            pd.read_csv(root_dir + '/' + 'youtube-new/FRvideos.csv').iloc[:, cat_index[cat]].sum(),
            pd.read_csv(root_dir + '/' + 'youtube-new/DEvideos.csv').iloc[:, cat_index[cat]].sum()
            ]
    
    title =["US","CA","GB","FR","DE"]
       
    text = 'Country   Number of ' + cat + '\n\n'
    for index in range(5):
        text += ' '*4 + title[index] + ' '*10 + str(sums[index]) + '\n'
    
    print(text)
    
    #pickle the sums of every category
# =============================================================================
#     with open(pickle_root+'/countries_'+cat, 'wb') as pfile:
#         pickle.dump(text, pfile)
# =============================================================================
    
    
    # plotting bar graph of the above data
    barlist = plt.bar(x=title, height=sums, align='center')  
    barlist[0].set_color('y')
    barlist[1].set_color('m')
    barlist[2].set_color('k')
    barlist[3].set_color('c')
    barlist[4].set_color('orange')
    #ax.pie(sums, labels=title)
    plt.title("COUNTRIES " + cat.upper())
    plt.xlabel("COUNTRIES", fontsize=16)
    plt.ylabel(cat.upper(), fontsize=16)
    plt.tight_layout()
    
    #save as image
    #plt.savefig('countries_img/countries_'+cat, dpi=300)
   
    plt.show()
    
    
