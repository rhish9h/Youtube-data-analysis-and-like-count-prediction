#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 07:40:24 2018

@author: rhishabh
"""


#most likes, dislikes, views, comment_count 

import os
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import shutil

plt.style.use('ggplot')

cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(cur_dir)

#create dir for adding pickles
# =============================================================================
# pickle_path = cur_dir+'/most_pickles'
# 
# if (os.path.exists(pickle_path)):
#     shutil.rmtree(pickle_path)      #remove existing dir
# os.makedirs(pickle_path)            #create new dir
# =============================================================================

data_path = []
data_path.append(('CA', (root_dir + '/' + 'youtube-new/CAvideos.csv')))
data_path.append(('DE', (root_dir + '/' + 'youtube-new/DEvideos.csv')))
data_path.append(('FR', (root_dir + '/' + 'youtube-new/FRvideos.csv')))
data_path.append(('GB', (root_dir + '/' + 'youtube-new/GBvideos.csv')))
data_path.append(('US', (root_dir + '/' + 'youtube-new/USvideos.csv')))

for name, path in data_path:    
    print('\n' + '*' * 75 + '\n' + name + '\n\n')
    df = pd.read_csv(path)
    
    sort_likes = df[['title', 'likes']].sort_values('likes', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_dislikes = df[['title', 'dislikes']].sort_values('dislikes', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_views = df[['title', 'views']].sort_values('views', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_comments = df[['title', 'comment_count']].sort_values('comment_count', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
     
#    print ('\nTop 10 Most Liked\n', sort_likes)
#    print ('\nTop 10 Most Disliked\n', sort_dislikes)
#    print ('\nTop 10 Most Viewed\n', sort_views)
#    print ('\nTop 10 Most Commented\n', sort_comments)
    
    #likes---------------------------------------------------------------------
    plt.bar(x=sort_likes['title'], height=sort_likes['likes'])
    plt.xticks(range(10), sort_likes['title'], rotation=90)
    plt.ylabel('NO OF LIKES', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('MOST' + ' ' + name + ' ' + 'LIKES')
    #to save as image
    #plt.savefig('most_img/most_'+name+'_likes', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    likes_text = name + ' Video Title                        No of Likes\n\n' 
    for index in sort_likes.index:
        likes_text += str(sort_likes.loc[index,'title'])[:30] + '...    ' + str(sort_likes.loc[index,'likes']) + '\n'
    
    print(likes_text)
    
    #create pickle
# =============================================================================
#     with open(pickle_path+'/most_'+name+'_likes', 'wb') as pfile:
#         pickle.dump(likes_text, pfile)
# =============================================================================
    
    #dislikes------------------------------------------------------------------
    plt.bar(x=sort_dislikes['title'], height=sort_dislikes['dislikes'])
    plt.xticks(range(10), sort_dislikes['title'], rotation=90)
    plt.ylabel('NO OF DISLIKES', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('MOST' + ' ' + name + ' ' + 'DISLIKES')
    #to save as image
    #plt.savefig('most_img/most_'+name+'_dislikes', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    dislikes_text = name + ' Video Title                        No of Dislikes\n\n'
    for index in sort_dislikes.index:
        dislikes_text += str(sort_dislikes.loc[index,'title'])[:30] + '...    ' + str(sort_dislikes.loc[index,'dislikes']) + '\n'
    
    print(dislikes_text)
    
    #create pickle
# =============================================================================
#     with open(pickle_path+'/most_'+name+'_dislikes', 'wb') as pfile:
#         pickle.dump(dislikes_text, pfile)
# =============================================================================
    
    #views---------------------------------------------------------------------
    plt.bar(x=sort_views['title'], height=sort_views['views'])
    plt.xticks(range(10), sort_views['title'], rotation=90)
    plt.ylabel('NO OF VIEWS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('MOST' + ' ' + name + ' ' + 'VIEWS')
    #to save as image
    #plt.savefig('most_img/most_'+name+'_views', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    views_text = name + ' Video Title                        No of Views\n\n' 
    for index in sort_views.index:
        views_text += str(sort_views.loc[index,'title'])[:30] + '...    ' + str(sort_views.loc[index,'views']) + '\n'
    
    print(views_text)
    
    #create pickle
# =============================================================================
#     with open(pickle_path+'/most_'+name+'_views', 'wb') as pfile:
#         pickle.dump(views_text, pfile)
# =============================================================================
    
    #comments------------------------------------------------------------------
    plt.bar(x=sort_comments['title'], height=sort_comments['comment_count'])
    plt.xticks(range(10), sort_comments['title'], rotation=90)
    plt.ylabel('NO OF COMMENTS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('MOST' + ' ' + name + ' ' + 'COMMENTS')
    #to save as image
    #plt.savefig('most_img/most_'+name+'_comments', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    comments_text = name + ' Video Title                        No of Comments\n\n'
    for index in sort_comments.index:
        comments_text += str(sort_comments.loc[index,'title'])[:30] + '...    ' + str(sort_comments.loc[index,'comment_count']) + '\n'
    
    print(comments_text)
    
    #create pickle
# =============================================================================
#     with open(pickle_path+'/most_'+name+'_comments', 'wb') as pfile:
#         pickle.dump(comments_text, pfile)
# =============================================================================
