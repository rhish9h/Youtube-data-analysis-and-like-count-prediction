#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:49:27 2018

@author: rhishabh
"""

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(cur_dir)

path_dict = {
            'CA': root_dir + '/' + 'youtube-new/CAvideos.csv',
            'DE': root_dir + '/' + 'youtube-new/DEvideos.csv',
            'FR': root_dir + '/' + 'youtube-new/FRvideos.csv',
            'GB': root_dir + '/' + 'youtube-new/GBvideos.csv',
            'US': root_dir + '/' + 'youtube-new/USvideos.csv'
        }

stopwords = set(STOPWORDS)

for country in path_dict:
  #        country = 'US'
    df = pd.read_csv(path_dict[country])
    comment_words = ' '
    
    for val in df.iloc[3]: 
          
        # typecaste each val to string 
        val = str(val) 
      
        # split the value 
        tokens = val.split() 
          
        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
              
        for words in tokens: 
            comment_words = comment_words + words + ' '
    
    wordcloud = WordCloud(width = 800, height = 800, 
                        background_color ='white', 
                        stopwords = stopwords, 
                        min_font_size = 10).generate(comment_words) 
    
     # plot the WordCloud image         
    plt.rcParams.update({'font.size': 22})
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.title(country)
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    #to save image
    #plt.savefig('word_img/word_'+country, dpi=300)
    plt.show() 