#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:31:51 2018

@author: rhishabh
"""

#plot graphs based on popularity vs days required to get to trending page

import pandas as pd
import os
import matplotlib.pyplot as plt
import shutil
import pickle

plt.style.use('fivethirtyeight')
#import pickle

#plt.style.available

#set path of dataset file
cur_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(cur_dir)


#create dir for adding pickles
pickle_path = cur_dir+'/days_pickles'

if (os.path.exists(pickle_path)):
    shutil.rmtree(pickle_path)      #remove existing dir
os.makedirs(pickle_path)            #create new dir


#create list of all datapaths 
data_path = []
data_path.append(('CA', (root_dir + '/' + 'youtube-new/CAvideos.csv')))
data_path.append(('DE', (root_dir + '/' + 'youtube-new/DEvideos.csv')))
data_path.append(('FR', (root_dir + '/' + 'youtube-new/FRvideos.csv')))
data_path.append(('GB', (root_dir + '/' + 'youtube-new/GBvideos.csv')))
data_path.append(('US', (root_dir + '/' + 'youtube-new/USvideos.csv')))

for name, path in data_path:
    print('\n' + '*'*75 + '\n\n' + name + '\n\n')
    #read the datset
    dataset = pd.read_csv(path)
    
    #insert new column for publish_date 
    #split old publish_time column into publish_date and publish_time
    dataset.insert(5, 'publish_date', pd.to_datetime(dataset.publish_time).dt.date)
    dataset['publish_time'] = pd.to_datetime(dataset.publish_time).dt.time
    
    #match the format of trending date to publish date
    dataset['trending_date'] = pd.to_datetime(dataset.trending_date, format='%y.%d.%m').dt.date
    
    #insert column for difference between publish date and trending date
    dataset.insert(5, 'trend-publish', (dataset['trending_date']-dataset['publish_date']).dt.days)
    
    #countries = ['CA', 'DE', 'FR', 'GB', 'US']
    #get top 10 videos based on likes, dislikes, views, comments
    sort_likes = dataset[['video_id', 'title', 'likes', 'trend-publish']].sort_values('likes', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_dislikes = dataset[['video_id', 'title', 'dislikes', 'trend-publish']].sort_values('dislikes', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_views = dataset[['video_id', 'title', 'views', 'trend-publish']].sort_values('views', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    sort_comments = dataset[['video_id', 'title', 'comment_count', 'trend-publish']].sort_values('comment_count', ascending=False).drop_duplicates(subset='title', keep='first').head(10)
    
    #plot bar graphs of top 10 videos vs time required to get to trending
    
    #likes---------------------------------------------------------------------
    plt.bar(x=sort_likes['video_id'], height=sort_likes['trend-publish'])
    plt.xticks(range(10), sort_likes['title'], rotation=90)
    plt.ylabel('NO OF DAYS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('DAYS' + ' ' + name + ' ' + 'LIKES')
    #to save as image
    #plt.savefig('days_img/days_'+name+'_likes', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    likes_text_head = name + ' Video Title                        No of Days - Likes\n\n' 
    likes_text_1 = ''
    likes_text_2 = ''
    for index in sort_likes.index:
        likes_text_1 += str(sort_likes.loc[index,'title'])[:30] + '...' 
        likes_text_2 += str(sort_likes.loc[index,'trend-publish']) + '\n'
    
    print(likes_text_head)
    
    
    #create pickle
    with open(pickle_path+'/days_'+name+'_likes', 'wb') as pfile:
        pickle.dump(likes_text_head, pfile)
        pickle.dump(likes_text_1, pfile)
        pickle.dump(likes_text_2, pfile)
 
    
    #dislikes------------------------------------------------------------------
    plt.bar(x=sort_dislikes['video_id'], height=sort_dislikes['trend-publish'])
    plt.xticks(range(10), sort_likes['title'], rotation=90)
    plt.ylabel('NO OF DAYS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('DAYS' + ' ' + name + ' ' + 'DISLIKES')
    #to save as image
    #plt.savefig('days_img/days_'+name+'_dislikes', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    dislikes_text = name + ' Video Title                        No of Days - Dislikes\n\n' 
    for index in sort_dislikes.index:
        dislikes_text += str(sort_dislikes.loc[index,'title'])[:30] + '...       ' + str(sort_dislikes.loc[index,'trend-publish']) + '\n'
    
    print(dislikes_text)
    
    #create pickle
    with open(pickle_path+'/days_'+name+'_dislikes', 'wb') as pfile:
        pickle.dump(dislikes_text, pfile)
    
    #views---------------------------------------------------------------------
    plt.bar(x=sort_views['video_id'], height=sort_views['trend-publish'])
    plt.xticks(range(10), sort_likes['title'], rotation=90)
    plt.ylabel('NO OF DAYS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('DAYS' + ' ' + name + ' ' + 'VIEWS')
    #to save as image
    #plt.savefig('days_img/days_'+name+'_views', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    views_text = name + ' Video Title                        No of Days - Views\n\n' 
    for index in sort_views.index:
        views_text += str(sort_views.loc[index,'title'])[:30] + '...       ' + str(sort_views.loc[index,'trend-publish']) + '\n'
    
    print(views_text)
    
    #create pickle
    with open(pickle_path+'/days_'+name+'_views', 'wb') as pfile:
        pickle.dump(views_text, pfile)
    
    #comments------------------------------------------------------------------
    plt.bar(x=sort_comments['video_id'], height=sort_comments['trend-publish'])
    plt.xticks(range(10), sort_likes['title'], rotation=90)
    plt.ylabel('NO OF DAYS', fontsize=14)
    plt.xlabel('VIDEO TITLES', fontsize=14)
    plt.title('DAYS' + ' ' + name + ' ' + 'COMMENTS')
    #to save as image
    #plt.savefig('days_img/days_'+name+'_comments', dpi=300, bbox_inches = 'tight')
    plt.show()
    
    comments_text = name + ' Video Title                        No of Days - Comments\n\n' 
    for index in sort_comments.index:
        comments_text += str(sort_comments.loc[index,'title'])[:30] + '...       ' + str(sort_comments.loc[index,'trend-publish']) + '\n'
    
    print(comments_text)
    
    #create pickle
    with open(pickle_path+'/days_'+name+'_comments', 'wb') as pfile:
        pickle.dump(comments_text, pfile)