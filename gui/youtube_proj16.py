# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_proj4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

from PyQt5.QtWidgets import QSizePolicy, QLabel
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from wordcloud import WordCloud, STOPWORDS 

from pandas.plotting import scatter_matrix

import os

from sklearn.ensemble import RandomForestRegressor
import pickle

plt.style.use('ggplot')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainpages = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainpages.setGeometry(QtCore.QRect(0, 0, 1980, 1080))
        self.mainpages.setObjectName("mainpages")
        
        ############Homepage --------------------------------------------------
        
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.toml = QtWidgets.QPushButton(self.homepage)
        self.toml.setGeometry(QtCore.QRect(510, 610, 211, 141))
        self.toml.setStyleSheet("background-image: url(:/ml/mlpic2.png);")
        self.toml.setText("")
        self.toml.setObjectName("toml")
        
        #go to ml page after clicking button
        self.toml.clicked.connect(self.gotoml)
        
        self.toanalysis = QtWidgets.QPushButton(self.homepage)
        self.toanalysis.setGeometry(QtCore.QRect(1110, 610, 211, 141))
        self.toanalysis.setStyleSheet("background-image: url(:/analytic/analytic2.png);")
        self.toanalysis.setText("")
        self.toanalysis.setObjectName("toanalysis")
        
        #go to analysis page after clicking button
        self.toanalysis.clicked.connect(self.gotoanalysis)
        
        self.likepred_text = QtWidgets.QTextBrowser(self.homepage)
        self.likepred_text.setGeometry(QtCore.QRect(570, 230, 681, 61))
        self.likepred_text.setStyleSheet("")
        self.likepred_text.setObjectName("likepred_text")
        self.youtube_logo = QtWidgets.QTextBrowser(self.homepage)
        self.youtube_logo.setGeometry(QtCore.QRect(710, 40, 391, 211))
        self.youtube_logo.setStyleSheet("background-image: url(:/youlogo/youtube-logo2.png);")
        self.youtube_logo.setObjectName("youtube_logo")
        self.textBrowser = QtWidgets.QTextBrowser(self.homepage)
        self.textBrowser.setGeometry(QtCore.QRect(515, 760, 201, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.homepage)
        self.textBrowser_2.setGeometry(QtCore.QRect(1140, 760, 161, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.toml.raise_()
        self.toanalysis.raise_()
        self.youtube_logo.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.likepred_text.raise_()
        self.mainpages.addWidget(self.homepage)
        
        ############ML page ---------------------------------------------------
        
        self.ml_page = QtWidgets.QWidget()
        self.ml_page.setObjectName("ml_page")
        self.MLheading = QtWidgets.QTextBrowser(self.ml_page)
        self.MLheading.setGeometry(QtCore.QRect(800, 40, 256, 51))
        self.MLheading.setObjectName("MLheading")
        self.home_but_2 = QtWidgets.QPushButton(self.ml_page)
        self.home_but_2.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.home_but_2.setStyleSheet("background-image: url(:/home/home-button2.png);")
        self.home_but_2.setText("")
        self.home_but_2.setObjectName("home_but_2")
        
        #go to home page
        self.home_but_2.clicked.connect(self.gotohome)
        
        self.enterinput = QtWidgets.QTextBrowser(self.ml_page)
        self.enterinput.setGeometry(QtCore.QRect(560, 120, 141, 41))
        self.enterinput.setObjectName("enterinput")
        self.views_ipbox = QtWidgets.QTextEdit(self.ml_page)
        self.views_ipbox.setGeometry(QtCore.QRect(730, 120, 150, 41))
        self.views_ipbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.views_ipbox.setObjectName("views_ipbox")
        self.views_ipbox.setFontPointSize(16)
        self.dislikes_ipbox = QtWidgets.QTextEdit(self.ml_page)
        self.dislikes_ipbox.setGeometry(QtCore.QRect(910, 120, 150, 41))
        self.dislikes_ipbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dislikes_ipbox.setObjectName("dislikes_ipbox")
        self.dislikes_ipbox.setFontPointSize(16)
        self.comments_ipbox = QtWidgets.QTextEdit(self.ml_page)
        self.comments_ipbox.setGeometry(QtCore.QRect(1090, 120, 150, 41))
        self.comments_ipbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comments_ipbox.setObjectName("comments_ipbox")
        self.comments_ipbox.setFontPointSize(16)
        self.views_text = QtWidgets.QTextBrowser(self.ml_page)
        self.views_text.setGeometry(QtCore.QRect(760, 180, 81, 31))
        self.views_text.setObjectName("views_text")
        self.dislikes_text = QtWidgets.QTextBrowser(self.ml_page)
        self.dislikes_text.setGeometry(QtCore.QRect(950, 180, 81, 31))
        self.dislikes_text.setObjectName("dislikes_text")
        self.comments_text = QtWidgets.QTextBrowser(self.ml_page)
        self.comments_text.setGeometry(QtCore.QRect(1110, 180, 111, 31))
        self.comments_text.setObjectName("comments_text")
        self.predict_but = QtWidgets.QPushButton(self.ml_page)
        self.predict_but.setGeometry(QtCore.QRect(590, 250, 201, 51))
        self.predict_but.setStyleSheet("background-color: rgb(222, 0, 0);\n"
"font: 22pt \"Sans Serif\";")
        self.predict_but.setObjectName("predict_but")
        
        #connect predict button to predict likes def
        self.predict_but.clicked.connect(self.predict_likes)
        
        self.pred_out = QtWidgets.QTextBrowser(self.ml_page)
        self.pred_out.setGeometry(QtCore.QRect(890, 240, 261, 71))
        self.pred_out.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pred_out.setObjectName("pred_out")
        self.pred_out.setFontPointSize(16)
        self.mainpages.addWidget(self.ml_page)
        
        ############Analysis page ---------------------------------------------
        
        self.analysis_page = QtWidgets.QWidget()
        self.analysis_page.setObjectName("analysis_page")
        self.days_but = QtWidgets.QPushButton(self.analysis_page)
        self.days_but.setGeometry(QtCore.QRect(875, 70, 111, 23))
        self.days_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_but.setObjectName("days_but")
        
        #go to days page
        self.days_but.clicked.connect(self.daysui)
        
        self.wordcld_but = QtWidgets.QPushButton(self.analysis_page)
        self.wordcld_but.setGeometry(QtCore.QRect(150, 70, 111, 23))
        self.wordcld_but.setStyleSheet("background-color: white;")
        self.wordcld_but.setObjectName("wordcld_but")
        
        #go to wordcld page
        self.wordcld_but.clicked.connect(self.wordcldui)
        
        self.countries_but = QtWidgets.QPushButton(self.analysis_page)
        self.countries_but.setGeometry(QtCore.QRect(500, 70, 111, 23))
        self.countries_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.countries_but.setObjectName("countries_but")
        
        #go to countries page
        self.countries_but.clicked.connect(self.countriesui)
        
        self.most_but = QtWidgets.QPushButton(self.analysis_page)
        self.most_but.setGeometry(QtCore.QRect(1250, 70, 111, 23))
        self.most_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_but.setObjectName("most_but")
        
        #go to most page
        self.most_but.clicked.connect(self.mostui)
        
        self.scatter_but = QtWidgets.QPushButton(self.analysis_page)
        self.scatter_but.setGeometry(QtCore.QRect(1600, 70, 111, 23))
        self.scatter_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.scatter_but.setObjectName("scatter_but")
        
        #go to scatter page
        self.scatter_but.clicked.connect(self.scatterui)
        
        self.sub_view = QtWidgets.QStackedWidget(self.analysis_page)
        self.sub_view.setGeometry(QtCore.QRect(20, 100, 1900, 980))
        self.sub_view.setObjectName("sub_view")
        self.scatter_page = QtWidgets.QWidget()
        self.scatter_page.setObjectName("scatter_page")
        self.sub_view.addWidget(self.scatter_page)
        
        ####word cloud page ---------------------------------------------------
        
        self.wordcld_page = QtWidgets.QWidget()
        self.wordcld_page.setObjectName("wordcld_page")
        self.word_us = QtWidgets.QPushButton(self.wordcld_page)
        self.word_us.setGeometry(QtCore.QRect(20, 50, 41, 41))
        self.word_us.setStyleSheet("background-color: white;")
        self.word_us.setObjectName("word_us")
        
        #connect to word us ui
        self.word_us.clicked.connect(self.word_us_ui)
        
        self.word_ca = QtWidgets.QPushButton(self.wordcld_page)
        self.word_ca.setGeometry(QtCore.QRect(20, 225, 41, 41))
        self.word_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_ca.setObjectName("word_ca")
        
        #connect to word ca ui
        self.word_ca.clicked.connect(self.word_ca_ui)
        
        self.word_gb = QtWidgets.QPushButton(self.wordcld_page)
        self.word_gb.setGeometry(QtCore.QRect(20, 400, 41, 41))
        self.word_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_gb.setObjectName("word_gb")
        
        #connect to word gb ui
        self.word_gb.clicked.connect(self.word_gb_ui)
        
        self.word_fr = QtWidgets.QPushButton(self.wordcld_page)
        self.word_fr.setGeometry(QtCore.QRect(20, 575, 41, 41))
        self.word_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_fr.setObjectName("word_fr")
        
        #connect to word fr ui
        self.word_fr.clicked.connect(self.word_fr_ui)
        
        self.word_de = QtWidgets.QPushButton(self.wordcld_page)
        self.word_de.setGeometry(QtCore.QRect(20, 750, 41, 41))
        self.word_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_de.setObjectName("word_de")
        
        #connect to word de ui
        self.word_de.clicked.connect(self.word_de_ui)
        
        self.sub_view.addWidget(self.wordcld_page)
        
        ####most page ---------------------------------------------------------
        
        self.most_page = QtWidgets.QWidget()
        self.most_page.setObjectName("most_page")
        self.most_ca = QtWidgets.QPushButton(self.most_page)
        self.most_ca.setGeometry(QtCore.QRect(20, 225, 41, 41))
        self.most_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_ca.setObjectName("most_ca")
        
        #connect to most ca ui
        self.most_ca.clicked.connect(self.most_ca_ui)
        
        self.most_de = QtWidgets.QPushButton(self.most_page)
        self.most_de.setGeometry(QtCore.QRect(20, 750, 41, 41))
        self.most_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_de.setObjectName("most_de")
        
        #connect to most de ui
        self.most_de.clicked.connect(self.most_de_ui)
        
        self.most_gb = QtWidgets.QPushButton(self.most_page)
        self.most_gb.setGeometry(QtCore.QRect(20, 400, 41, 41))
        self.most_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_gb.setObjectName("most_gb")
        
        #connect to most gb ui
        self.most_gb.clicked.connect(self.most_gb_ui)
        
        self.most_us = QtWidgets.QPushButton(self.most_page)
        self.most_us.setGeometry(QtCore.QRect(20, 50, 41, 41))
        self.most_us.setStyleSheet("background-color: white;")
        self.most_us.setObjectName("most_us")
        
        #connect to most us ui
        self.most_us.clicked.connect(self.most_us_ui)
        
        self.most_fr = QtWidgets.QPushButton(self.most_page)
        self.most_fr.setGeometry(QtCore.QRect(20, 575, 41, 41))
        self.most_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_fr.setObjectName("most_fr")
        
        #connect to most fr ui
        self.most_fr.clicked.connect(self.most_fr_ui)
        
        self.country_switch = QtWidgets.QStackedWidget(self.most_page)
        self.country_switch.setGeometry(QtCore.QRect(90, 20, 1810, 960))
        self.country_switch.setObjectName("country_switch")
        self.most_us_page = QtWidgets.QWidget()
        self.most_us_page.setObjectName("most_us_page")
        self.most_us_views = QtWidgets.QPushButton(self.most_us_page)
        self.most_us_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.most_us_views.setStyleSheet("background-color: white;")
        self.most_us_views.setObjectName("most_us_views")
        
        #connect to most us views ui
        self.most_us_views.clicked.connect(self.most_us_views_ui)
        
        self.most_us_likes = QtWidgets.QPushButton(self.most_us_page)
        self.most_us_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.most_us_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_us_likes.setObjectName("most_us_likes")
        
        #connect to most us likes ui
        self.most_us_likes.clicked.connect(self.most_us_likes_ui)
        
        self.most_us_dislikes = QtWidgets.QPushButton(self.most_us_page)
        self.most_us_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.most_us_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_us_dislikes.setObjectName("most_us_dislikes")
        
        #connect to most us dislikes ui
        self.most_us_dislikes.clicked.connect(self.most_us_dislikes_ui)
        
        self.most_us_comments = QtWidgets.QPushButton(self.most_us_page)
        self.most_us_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.most_us_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_us_comments.setObjectName("most_us_comments")
        
        #connect to most us comments ui
        self.most_us_comments.clicked.connect(self.most_us_comments_ui)
        
        self.country_switch.addWidget(self.most_us_page)
        self.most_ca_page = QtWidgets.QWidget()
        self.most_ca_page.setObjectName("most_ca_page")
        self.most_ca_views = QtWidgets.QPushButton(self.most_ca_page)
        self.most_ca_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.most_ca_views.setStyleSheet("background-color: white;")
        self.most_ca_views.setObjectName("most_ca_views")
        
        #connect to most ca views ui
        self.most_ca_views.clicked.connect(self.most_ca_views_ui)
        
        self.most_ca_likes = QtWidgets.QPushButton(self.most_ca_page)
        self.most_ca_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.most_ca_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_ca_likes.setObjectName("most_ca_likes")
        
        #connect to most ca likes ui
        self.most_ca_likes.clicked.connect(self.most_ca_likes_ui)
        
        self.most_ca_dislikes = QtWidgets.QPushButton(self.most_ca_page)
        self.most_ca_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.most_ca_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_ca_dislikes.setObjectName("most_ca_dislikes")
        
        #connect to most ca dislikes ui
        self.most_ca_dislikes.clicked.connect(self.most_ca_dislikes_ui)
        
        self.most_ca_comments = QtWidgets.QPushButton(self.most_ca_page)
        self.most_ca_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.most_ca_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_ca_comments.setObjectName("most_ca_comments")
        
        #connect to most ca comments ui
        self.most_ca_comments.clicked.connect(self.most_ca_comments_ui)
        
        self.country_switch.addWidget(self.most_ca_page)
        self.most_gb_page = QtWidgets.QWidget()
        self.most_gb_page.setObjectName("most_gb_page")
        self.most_gb_likes = QtWidgets.QPushButton(self.most_gb_page)
        self.most_gb_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.most_gb_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_gb_likes.setObjectName("most_gb_likes")
        
        #connect to most gb likes ui
        self.most_gb_likes.clicked.connect(self.most_gb_likes_ui)
        
        self.most_gb_comments = QtWidgets.QPushButton(self.most_gb_page)
        self.most_gb_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.most_gb_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_gb_comments.setObjectName("most_gb_comments")
        
        #connect to most gb comments ui
        self.most_gb_comments.clicked.connect(self.most_gb_comments_ui)
        
        self.most_gb_dislikes = QtWidgets.QPushButton(self.most_gb_page)
        self.most_gb_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.most_gb_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_gb_dislikes.setObjectName("most_gb_dislikes")
        
        #connect to most gb dislikes ui
        self.most_gb_dislikes.clicked.connect(self.most_gb_dislikes_ui)
        
        self.most_gb_views = QtWidgets.QPushButton(self.most_gb_page)
        self.most_gb_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.most_gb_views.setStyleSheet("background-color: white;")
        self.most_gb_views.setObjectName("most_gb_views")
        
        #connect to most gb views ui
        self.most_gb_views.clicked.connect(self.most_gb_views_ui)
        
        self.country_switch.addWidget(self.most_gb_page)
        self.most_fr_page = QtWidgets.QWidget()
        self.most_fr_page.setObjectName("most_fr_page")
        self.most_fr_dislikes = QtWidgets.QPushButton(self.most_fr_page)
        self.most_fr_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.most_fr_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_fr_dislikes.setObjectName("most_fr_dislikes")
        
        #connect to most fr dislikes ui
        self.most_fr_dislikes.clicked.connect(self.most_fr_dislikes_ui)
        
        self.most_fr_likes = QtWidgets.QPushButton(self.most_fr_page)
        self.most_fr_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.most_fr_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_fr_likes.setObjectName("most_fr_likes")
        
        #connect to most fr likes ui
        self.most_fr_likes.clicked.connect(self.most_fr_likes_ui)
        
        self.most_fr_views = QtWidgets.QPushButton(self.most_fr_page)
        self.most_fr_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.most_fr_views.setStyleSheet("background-color: white;")
        self.most_fr_views.setObjectName("most_fr_views")
        
        #connect to most fr views ui
        self.most_fr_views.clicked.connect(self.most_fr_views_ui)
        
        self.most_fr_comments = QtWidgets.QPushButton(self.most_fr_page)
        self.most_fr_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.most_fr_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_fr_comments.setObjectName("most_fr_comments")
        
        #connect to most fr comments ui
        self.most_fr_comments.clicked.connect(self.most_fr_comments_ui)
        
        self.country_switch.addWidget(self.most_fr_page)
        self.most_de_page = QtWidgets.QWidget()
        self.most_de_page.setObjectName("most_de_page")
        self.most_de_comments = QtWidgets.QPushButton(self.most_de_page)
        self.most_de_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.most_de_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_de_comments.setObjectName("most_de_comments")
        
        #connect to most de comments ui
        self.most_de_comments.clicked.connect(self.most_de_comments_ui)
        
        self.most_de_likes = QtWidgets.QPushButton(self.most_de_page)
        self.most_de_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.most_de_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_de_likes.setObjectName("most_de_likes")
        
        #connect to most de likes ui
        self.most_de_likes.clicked.connect(self.most_de_likes_ui)
        
        self.most_de_views = QtWidgets.QPushButton(self.most_de_page)
        self.most_de_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.most_de_views.setStyleSheet("background-color: white;")
        self.most_de_views.setObjectName("most_de_views")
        
        #connect to most de views ui
        self.most_de_views.clicked.connect(self.most_de_views_ui)
        
        self.most_de_dislikes = QtWidgets.QPushButton(self.most_de_page)
        self.most_de_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.most_de_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_de_dislikes.setObjectName("most_de_dislikes")
        
        #connect to most de dislikes ui
        self.most_de_dislikes.clicked.connect(self.most_de_dislikes_ui)
        
        self.country_switch.addWidget(self.most_de_page)
        self.sub_view.addWidget(self.most_page)
        
        ####countries page ----------------------------------------------------
        
        self.countries_page = QtWidgets.QWidget()
        self.countries_page.setObjectName("countries_page")
        
        self.countries_views = QtWidgets.QPushButton(self.countries_page)
        self.countries_views.setGeometry(QtCore.QRect(290, 840, 111, 23))
        self.countries_views.setStyleSheet("background-color: white;")
        self.countries_views.setObjectName("countries_views")
        
        #connect to countries views ui
        self.countries_views.clicked.connect(self.countries_views_ui)
        
        self.countries_likes = QtWidgets.QPushButton(self.countries_page)
        self.countries_likes.setGeometry(QtCore.QRect(640, 840, 111, 23))
        self.countries_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.countries_likes.setObjectName("countries_likes")
        
        #connect to countries likes ui
        self.countries_likes.clicked.connect(self.countries_likes_ui)
        
        self.countries_dislikes = QtWidgets.QPushButton(self.countries_page)
        self.countries_dislikes.setGeometry(QtCore.QRect(1020, 840, 111, 23))
        self.countries_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.countries_dislikes.setObjectName("countries_dislikes")
        
        #connect to countries dislikes ui
        self.countries_dislikes.clicked.connect(self.countries_dislikes_ui)
        
        self.countries_comments = QtWidgets.QPushButton(self.countries_page)
        self.countries_comments.setGeometry(QtCore.QRect(1390, 840, 111, 23))
        self.countries_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.countries_comments.setObjectName("countries_comments")
        
        #connect to countries comments ui
        self.countries_comments.clicked.connect(self.countries_comments_ui)   
        
        self.sub_view.addWidget(self.countries_page)
        
        ####days page ---------------------------------------------------------
        
        self.days_page = QtWidgets.QWidget()
        self.days_page.setObjectName("days_page")
        self.days_us = QtWidgets.QPushButton(self.days_page)
        self.days_us.setGeometry(QtCore.QRect(20, 50, 41, 41))
        self.days_us.setStyleSheet("background-color: white;")
        self.days_us.setObjectName("days_us")
        
        #connect button to days us ui
        self.days_us.clicked.connect(self.days_us_ui)
        
        self.days_de = QtWidgets.QPushButton(self.days_page)
        self.days_de.setGeometry(QtCore.QRect(20, 750, 41, 41))
        self.days_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_de.setObjectName("days_de")
        
        #connect button to days de ui
        self.days_de.clicked.connect(self.days_de_ui)
        
        self.days_ca = QtWidgets.QPushButton(self.days_page)
        self.days_ca.setGeometry(QtCore.QRect(20, 225, 41, 41))
        self.days_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_ca.setObjectName("days_ca")
        
        #connect button to days ca ui
        self.days_ca.clicked.connect(self.days_ca_ui)
        
        self.days_gb = QtWidgets.QPushButton(self.days_page)
        self.days_gb.setGeometry(QtCore.QRect(20, 400, 41, 41))
        self.days_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_gb.setObjectName("days_gb")
        
        #connect button to days gb ui
        self.days_gb.clicked.connect(self.days_gb_ui)
        
        self.days_fr = QtWidgets.QPushButton(self.days_page)
        self.days_fr.setGeometry(QtCore.QRect(20, 575, 41, 41))
        self.days_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_fr.setObjectName("days_fr")
        
        #connect button to days fr ui
        self.days_fr.clicked.connect(self.days_fr_ui)
        
        self.country_switch_3 = QtWidgets.QStackedWidget(self.days_page)
        self.country_switch_3.setGeometry(QtCore.QRect(90, 20, 1810, 960))
        self.country_switch_3.setObjectName("country_switch_3")
        self.days_us_page = QtWidgets.QWidget()
        self.days_us_page.setObjectName("days_us_page")
        self.days_us_views = QtWidgets.QPushButton(self.days_us_page)
        self.days_us_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.days_us_views.setStyleSheet("background-color: white;")
        self.days_us_views.setObjectName("days_us_views")
        
        #connect button to days us views ui
        self.days_us_views.clicked.connect(self.days_us_views_ui)
        
        self.days_us_likes = QtWidgets.QPushButton(self.days_us_page)
        self.days_us_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.days_us_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_us_likes.setObjectName("days_us_likes")
        
        #connect button to days us likes ui
        self.days_us_likes.clicked.connect(self.days_us_likes_ui)
        
        self.days_us_dislikes = QtWidgets.QPushButton(self.days_us_page)
        self.days_us_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.days_us_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_us_dislikes.setObjectName("days_us_dislikes")
        
        #connect button to days us dislikes ui
        self.days_us_dislikes.clicked.connect(self.days_us_dislikes_ui)
        
        self.days_us_comments = QtWidgets.QPushButton(self.days_us_page)
        self.days_us_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.days_us_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_us_comments.setObjectName("days_us_comments")
        
        #connect button to days us comments ui
        self.days_us_comments.clicked.connect(self.days_us_comments_ui)
        
        self.country_switch_3.addWidget(self.days_us_page)
        self.days_ca_page = QtWidgets.QWidget()
        self.days_ca_page.setObjectName("days_ca_page")
        self.days_ca_views = QtWidgets.QPushButton(self.days_ca_page)
        self.days_ca_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.days_ca_views.setStyleSheet("background-color: white;")
        self.days_ca_views.setObjectName("days_ca_views")
        
        #connect button to days ca views ui
        self.days_ca_views.clicked.connect(self.days_ca_views_ui)
        
        self.days_ca_likes = QtWidgets.QPushButton(self.days_ca_page)
        self.days_ca_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.days_ca_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_ca_likes.setObjectName("days_ca_likes")
        
        #connect button to days ca likes ui
        self.days_ca_likes.clicked.connect(self.days_ca_likes_ui)
        
        self.days_ca_dislikes = QtWidgets.QPushButton(self.days_ca_page)
        self.days_ca_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.days_ca_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_ca_dislikes.setObjectName("days_ca_dislikes")
        
        #connect button to days ca dislikes ui
        self.days_ca_dislikes.clicked.connect(self.days_ca_dislikes_ui)
        
        self.days_ca_comments = QtWidgets.QPushButton(self.days_ca_page)
        self.days_ca_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.days_ca_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_ca_comments.setObjectName("days_ca_comments")
        
        #connect button to days ca comments ui
        self.days_ca_comments.clicked.connect(self.days_ca_comments_ui)
        
        self.country_switch_3.addWidget(self.days_ca_page)
        self.days_gb_page = QtWidgets.QWidget()
        self.days_gb_page.setObjectName("days_gb_page")
        self.days_gb_likes = QtWidgets.QPushButton(self.days_gb_page)
        self.days_gb_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.days_gb_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_gb_likes.setObjectName("days_gb_likes")
        
        #connect button to days gb likes ui
        self.days_gb_likes.clicked.connect(self.days_gb_likes_ui)
        
        self.days_gb_comments = QtWidgets.QPushButton(self.days_gb_page)
        self.days_gb_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.days_gb_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_gb_comments.setObjectName("days_gb_comments")
        
        #connect button to days gb comments ui
        self.days_gb_comments.clicked.connect(self.days_gb_comments_ui)
        
        self.days_gb_dislikes = QtWidgets.QPushButton(self.days_gb_page)
        self.days_gb_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.days_gb_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_gb_dislikes.setObjectName("days_gb_dislikes")
        
        #connect button to days gb dislikes ui
        self.days_gb_dislikes.clicked.connect(self.days_gb_dislikes_ui)
        
        self.days_gb_views = QtWidgets.QPushButton(self.days_gb_page)
        self.days_gb_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.days_gb_views.setStyleSheet("background-color: white;")
        self.days_gb_views.setObjectName("days_gb_views")
        
        #connect button to days gb views ui
        self.days_gb_views.clicked.connect(self.days_gb_views_ui)
        
        self.country_switch_3.addWidget(self.days_gb_page)
        self.days_fr_page = QtWidgets.QWidget()
        self.days_fr_page.setObjectName("days_fr_page")
        self.days_fr_dislikes = QtWidgets.QPushButton(self.days_fr_page)
        self.days_fr_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.days_fr_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_fr_dislikes.setObjectName("days_fr_dislikes")
        
        #connect button to days fr dislikes ui
        self.days_fr_dislikes.clicked.connect(self.days_fr_dislikes_ui)
        
        self.days_fr_likes = QtWidgets.QPushButton(self.days_fr_page)
        self.days_fr_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.days_fr_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_fr_likes.setObjectName("days_fr_likes")
        
        #connect button to days fr likes ui
        self.days_fr_likes.clicked.connect(self.days_fr_likes_ui)
        
        self.days_fr_views = QtWidgets.QPushButton(self.days_fr_page)
        self.days_fr_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.days_fr_views.setStyleSheet("background-color: white;")
        self.days_fr_views.setObjectName("days_fr_views")
        
        #connect button to days fr views ui
        self.days_fr_views.clicked.connect(self.days_fr_views_ui)
        
        self.days_fr_comments = QtWidgets.QPushButton(self.days_fr_page)
        self.days_fr_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.days_fr_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_fr_comments.setObjectName("days_fr_comments")
        
        #connect button to days fr comments ui
        self.days_fr_comments.clicked.connect(self.days_fr_comments_ui)
        
        self.country_switch_3.addWidget(self.days_fr_page)
        self.days_de_page = QtWidgets.QWidget()
        self.days_de_page.setObjectName("days_de_page")
        self.days_de_comments = QtWidgets.QPushButton(self.days_de_page)
        self.days_de_comments.setGeometry(QtCore.QRect(1300, 820, 111, 23))
        self.days_de_comments.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_de_comments.setObjectName("days_de_comments")
        
        #connect button to days de comments ui
        self.days_de_comments.clicked.connect(self.days_de_comments_ui)
        
        self.days_de_likes = QtWidgets.QPushButton(self.days_de_page)
        self.days_de_likes.setGeometry(QtCore.QRect(550, 820, 111, 23))
        self.days_de_likes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_de_likes.setObjectName("days_de_likes")
        
        #connect button to days de likes ui
        self.days_de_likes.clicked.connect(self.days_de_likes_ui)
        
        self.days_de_views = QtWidgets.QPushButton(self.days_de_page)
        self.days_de_views.setGeometry(QtCore.QRect(200, 820, 111, 23))
        self.days_de_views.setStyleSheet("background-color: white;")
        self.days_de_views.setObjectName("days_de_views")
        
        #connect button to days de views ui
        self.days_de_views.clicked.connect(self.days_de_views_ui)
        
        self.days_de_dislikes = QtWidgets.QPushButton(self.days_de_page)
        self.days_de_dislikes.setGeometry(QtCore.QRect(930, 820, 111, 23))
        self.days_de_dislikes.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_de_dislikes.setObjectName("days_de_dislikes")
        
        #connect button to days de dislikes ui
        self.days_de_dislikes.clicked.connect(self.days_de_dislikes_ui)
        
        self.country_switch_3.addWidget(self.days_de_page)
        self.sub_view.addWidget(self.days_page)
        self.analysis_heading = QtWidgets.QTextBrowser(self.analysis_page)
        self.analysis_heading.setGeometry(QtCore.QRect(820, 10, 221, 61))
        self.analysis_heading.setObjectName("analysis_heading")
        self.analysis_heading.lower()
        self.home_but = QtWidgets.QPushButton(self.analysis_page)
        self.home_but.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.home_but.setStyleSheet("background-image: url(:/home/home-button2.png);")
        self.home_but.setText("")
        self.home_but.setObjectName("home_but")
        
        #go to home page
        self.home_but.clicked.connect(self.gotohome)
        
        self.mainpages.addWidget(self.analysis_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainpages.setCurrentIndex(0)
        self.sub_view.setCurrentIndex(1)
        self.country_switch.setCurrentIndex(0)
        self.country_switch_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    ########definitions of mainpage buttons-------------------------------------------  
    
    def change_mainpage(self, index):
        self.mainpages.setCurrentIndex(index)
    
    def gotoanalysis(self):
        self.change_mainpage(2)
        self.change_word_country_butcolor('us')
        self.change_buttoncolor('wordcld')
        self.sub_view.setCurrentIndex(1)
        self.plot_word(country='US')
        self.text_word('US')
    
    def gotoml(self):
        self.change_mainpage(1)
        self.plot_ml()
        
    def plot_ml(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        
        label = QLabel(self.mainpages)
        pixmap = QPixmap(root_dir + '/ml/pred_c_vs_l.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(320, 350)
        label.resize(1200, 620)
        label.show()
        
    def gotohome(self):
        self.change_mainpage(0)
    
    ########definitions of ml page buttons--------------------------------------------
    
    def predict_likes(self):
        self.pred_out.clear()
        views = dislikes = comments = None
        try:
            views = int(self.views_ipbox.toPlainText())
            dislikes = int(self.dislikes_ipbox.toPlainText())
            comments = int(self.comments_ipbox.toPlainText())
            
             #get path of pickle
            cur_dir = os.path.dirname(os.path.realpath(__file__))
            root_dir = os.path.dirname(cur_dir)
            
            #load trained model pickle
            with open(root_dir + '/ml/trained_model.pickle', 'rb') as tmpick:
                regressor = pickle.load(tmpick)
            
            #test the model
            iparray = np.array([[dislikes, comments, views]])
            ippred = regressor.predict(iparray)
            
            self.pred_out.setText(str(int(ippred[[0][0]])))
        except ValueError:
            self.pred_out.setText('Inputs cannot be empty. Inputs should be integer.')
       
       
    
    ########definitions of analysis page buttons--------------------------------------
    
    #definition to change color of button after clicking it
    def change_buttoncolor(self, but):
        self.wordcld_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.scatter_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.days_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.most_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.countries_but.setStyleSheet("background-color: rgb(131, 131, 131);")
        if(but == 'wordcld'):
            self.wordcld_but.setStyleSheet("background-color: white;")
        elif(but == 'countries'):
            self.countries_but.setStyleSheet("background-color: white;")
        elif(but == 'days'):
            self.days_but.setStyleSheet("background-color: white;")
        elif(but == 'most'):
            self.most_but.setStyleSheet("background-color: white;")
        elif(but == 'scatter'):
            self.scatter_but.setStyleSheet("background-color: white;")
    
    def change_subview(self, index):
        self.sub_view.setCurrentIndex(index)
    
    ###definitions of word cloud page--------------------------------------------
    
    def wordcldui(self):
        self.change_subview(1)
        self.change_buttoncolor('wordcld')
        self.change_word_country_butcolor('us')
        self.plot_word(country='US')
        self.text_word('US')
    
    #change the color of country button in word count page
    def change_word_country_butcolor(self, but):
        self.word_us.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.word_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'us'):
            self.word_us.setStyleSheet("background-color: white;")
        elif(but == 'ca'):
            self.word_ca.setStyleSheet("background-color: white;")
        elif(but == 'gb'):
            self.word_gb.setStyleSheet("background-color: white;")
        elif(but == 'fr'):
            self.word_fr.setStyleSheet("background-color: white;")
        elif(but == 'de'):
            self.word_de.setStyleSheet("background-color: white;")
    
    def plot_word(self, country='US'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        
        label = QLabel(self.sub_view)
        pixmap = QPixmap(root_dir + '/analytics/word_img/word_' + country + '.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(240, 70)
        label.resize(730, 730)
        label.show()
    
    def text_word(self, country='US'):      
        heading = QLabel(self.sub_view)
        heading.setText('Word Cloud')
        hfont = QtGui.QFont()
        hfont.setPointSize(30)
        heading.setFont(hfont)
        heading.move(1260, 70)
        heading.resize(700, 150)
        heading.setStyleSheet('color: white;')
        heading.show()
        
        label = QLabel(self.sub_view)
        label.setText('Size of each word indicates the frequency of it.\n               This word cloud is based on \n         the Channel Title of the country '+country)
        font = QtGui.QFont()
        font.setPointSize(20)
        label.setFont(font)
        label.move(1070, 170)
        label.resize(750, 200)
        label.setStyleSheet('color: white;')
        label.show()
    
    def word_us_ui(self):
        self.change_word_country_butcolor('us')
        self.plot_word(country='US')
        self.text_word('US')
    
    def word_ca_ui(self):
        self.change_word_country_butcolor('ca')
        self.plot_word(country='CA')
        self.text_word('CA')
    
    def word_gb_ui(self):
        self.change_word_country_butcolor('gb')
        self.plot_word(country='GB')
        self.text_word('GB')
        
    def word_fr_ui(self):
        self.change_word_country_butcolor('fr')
        self.plot_word(country='FR')
        self.text_word('FR')
        
    def word_de_ui(self):
        self.change_word_country_butcolor('de')
        self.plot_word(country='DE')
        self.text_word('DE')
        
    ###defintions of countries page----------------------------------------------
    
    def countriesui(self):
        self.change_subview(3)
        self.change_buttoncolor('countries')
        self.change_countries_catcolor('views')
        self.plot_countries('views')
        self.text_countries('views')
    
    #change the color of category button in countries us page
    def change_countries_catcolor(self, but):
        self.countries_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.countries_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.countries_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.countries_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.countries_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.countries_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.countries_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.countries_comments.setStyleSheet("background-color: white;")
    
    def plot_countries(self, cat='views'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        
        label = QLabel(self.sub_view)
        pixmap = QPixmap(root_dir + '/analytics/countries_img/countries_' + cat + '.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(240, 70)
        label.resize(730, 730)
        label.show()
    
    def text_countries(self, cat='views'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        pickle_root = root_dir + '/analytics/countries_pickles'
        #get sums from pickle
        with open(pickle_root+'/countries_'+cat, 'rb') as pfile:
            text = pickle.load(pfile)
        
        heading = QLabel(self.sub_view)
        heading.setText('Countries in absolute numbers')
        hfont = QtGui.QFont()
        hfont.setPointSize(30)
        heading.setFont(hfont)
        heading.move(1100, 70)
        heading.resize(700, 200)
        heading.setStyleSheet('color: white;')
        heading.show()
        
        label = QLabel(self.sub_view)
        label.setText(text)
        font = QtGui.QFont()
        font.setPointSize(20)
        label.setFont(font)
        label.move(1200, 230)
        label.resize(450, 300)
        label.setStyleSheet('color: white;')
        label.show()
    
    def countries_views_ui(self):
        self.change_countries_catcolor('views')
        self.plot_countries('views')
        self.text_countries('views')
    
    def countries_likes_ui(self):
        self.change_countries_catcolor('likes')
        self.plot_countries('likes')
        self.text_countries('likes')
    
    def countries_dislikes_ui(self):
        self.change_countries_catcolor('dislikes')
        self.plot_countries('dislikes')
        self.text_countries('dislikes')
        
    def countries_comments_ui(self):
        self.change_countries_catcolor('comments')
        self.plot_countries('comments')
        self.text_countries('comments')
    
    ###defintions of days page---------------------------------------------------
    
    def daysui(self):
        self.change_subview(4)
        self.change_buttoncolor('days')
        self.plot_days('US', 'views')
        self.change_days_us_catcolor('views')
        self.change_days_country_butcolor('us')
        self.text_days('US', 'views')
    
    #change the color of country button in days page
    def change_days_country_butcolor(self, but):
        self.days_us.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'us'):
            self.days_us.setStyleSheet("background-color: white;")
        elif(but == 'ca'):
            self.days_ca.setStyleSheet("background-color: white;")
        elif(but == 'gb'):
            self.days_gb.setStyleSheet("background-color: white;")
        elif(but == 'fr'):
            self.days_fr.setStyleSheet("background-color: white;")
        elif(but == 'de'):
            self.days_de.setStyleSheet("background-color: white;")
    
    def plot_days(self, country, cat):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        
        label = QLabel(self.sub_view)
        pixmap = QPixmap(root_dir + '/analytics/days_img/days_' + country + '_' + cat + '.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(240, 70)
        label.resize(730, 730)
        label.show()
    
    def text_days(self,country='US', cat='views'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        pickle_root = root_dir + '/analytics/days_pickles'
        #get sums from pickle
        with open(pickle_root+'/days_'+country+'_'+cat, 'rb') as pfile:
            text = pickle.load(pfile)
        
        heading = QLabel(self.sub_view)
        heading.setText('Days required to reach Trending')
        hfont = QtGui.QFont()
        hfont.setPointSize(30)
        heading.setFont(hfont)
        heading.move(1100, 70)
        heading.resize(700, 200)
        heading.setStyleSheet('color: white;')
        heading.show()
        
        label = QLabel(self.sub_view)
        label.setText(text)
        font = QtGui.QFont()
        font.setPointSize(20)
        label.setFont(font)
        label.move(1100, 230)
        label.resize(700, 500)
        label.setStyleSheet('color: white;')
        label.show()
    
    #change countries in days page
    def change_country_switch_3(self, index):
        self.country_switch_3.setCurrentIndex(index)
    
    #us-----------------------------------------------
    
    def days_us_ui(self):
        self.change_country_switch_3(0)
        self.change_days_country_butcolor('us')
        self.plot_days('US', 'views')
        self.change_days_us_catcolor('views')
        self.text_days('US', 'views')
    
    #change the color of category button in days us page
    def change_days_us_catcolor(self, but):
        self.days_us_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_us_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_us_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_us_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.days_us_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.days_us_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.days_us_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.days_us_comments.setStyleSheet("background-color: white;")
        
    def days_us_views_ui(self):
        self.change_days_us_catcolor('views')
        self.plot_days('US', 'views')
        self.text_days('US', 'views')
    
    def days_us_likes_ui(self):
        self.change_days_us_catcolor('likes')
        self.plot_days('US', 'likes')
        self.text_days('US', 'likes')
    
    def days_us_dislikes_ui(self):
        self.change_days_us_catcolor('dislikes')
        self.plot_days('US', 'dislikes')
        self.text_days('US', 'dislikes')
        
    def days_us_comments_ui(self):
        self.change_days_us_catcolor('comments')
        self.plot_days('US', 'comments')
        self.text_days('US', 'comments')
    
    #ca-----------------------------------------------
    
    def days_ca_ui(self):
        self.change_country_switch_3(1)
        self.change_days_country_butcolor('ca')
        self.plot_days('CA', 'views')
        self.change_days_ca_catcolor('views')
        self.text_days('CA', 'views')
    
    #change the color of category button in days ca page
    def change_days_ca_catcolor(self, but):
        self.days_ca_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_ca_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_ca_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_ca_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.days_ca_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.days_ca_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.days_ca_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.days_ca_comments.setStyleSheet("background-color: white;")
        
    def days_ca_views_ui(self):
        self.change_days_ca_catcolor('views')
        self.plot_days('CA', 'views')
        self.text_days('CA', 'views')
    
    def days_ca_likes_ui(self):
        self.change_days_ca_catcolor('likes')
        self.plot_days('CA', 'likes')
        self.text_days('CA', 'likes')
    
    def days_ca_dislikes_ui(self):
        self.change_days_ca_catcolor('dislikes')
        self.plot_days('CA', 'dislikes')
        self.text_days('CA', 'dislikes')
        
    def days_ca_comments_ui(self):
        self.change_days_ca_catcolor('comments')
        self.plot_days('CA', 'comments')
        self.text_days('CA', 'comments')
    
    #gb-----------------------------------------------
    
    def days_gb_ui(self):
        self.change_country_switch_3(2)
        self.change_days_country_butcolor('gb')
        self.plot_days('GB', 'views')
        self.change_days_gb_catcolor('views')
        self.text_days('GB', 'views')
    
    #change the color of category button in days gb page
    def change_days_gb_catcolor(self, but):
        self.days_gb_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_gb_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_gb_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_gb_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.days_gb_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.days_gb_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.days_gb_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.days_gb_comments.setStyleSheet("background-color: white;")
        
    def days_gb_views_ui(self):
        self.change_days_gb_catcolor('views')
        self.plot_days('GB', 'views')
        self.text_days('GB', 'views')
    
    def days_gb_likes_ui(self):
        self.change_days_gb_catcolor('likes')
        self.plot_days('GB', 'likes')
        self.text_days('GB', 'likes')
    
    def days_gb_dislikes_ui(self):
        self.change_days_gb_catcolor('dislikes')
        self.plot_days('GB', 'dislikes')
        self.text_days('GB', 'dislikes')
        
    def days_gb_comments_ui(self):
        self.change_days_gb_catcolor('comments')
        self.plot_days('GB', 'comments')
        self.text_days('GB', 'comments')
    
    #fr-----------------------------------------------
    
    def days_fr_ui(self):
        self.change_country_switch_3(3)
        self.change_days_country_butcolor('fr')
        self.plot_days('FR', 'views')
        self.change_days_fr_catcolor('views')
        self.text_days('FR', 'views')
    
    #change the color of category button in days fr page
    def change_days_fr_catcolor(self, but):
        self.days_fr_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_fr_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_fr_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_fr_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.days_fr_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.days_fr_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.days_fr_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.days_fr_comments.setStyleSheet("background-color: white;")
        
    def days_fr_views_ui(self):
        self.change_days_fr_catcolor('views')
        self.plot_days('FR', 'views')
        self.text_days('FR', 'views')
    
    def days_fr_likes_ui(self):
        self.change_days_fr_catcolor('likes')
        self.plot_days('FR', 'likes')
        self.text_days('FR', 'likes')
    
    def days_fr_dislikes_ui(self):
        self.change_days_fr_catcolor('dislikes')
        self.plot_days('FR', 'dislikes')
        self.text_days('FR', 'dislikes')
        
    def days_fr_comments_ui(self):
        self.change_days_fr_catcolor('comments')
        self.plot_days('FR', 'comments')
        self.text_days('FR', 'comments')
    
    #de-----------------------------------------------
        
    def days_de_ui(self):
        self.change_country_switch_3(4)
        self.change_days_country_butcolor('de')
        self.plot_days('DE', 'views')
        self.change_days_de_catcolor('views')
        self.text_days('DE', 'views')
        
    #change the color of category button in days de page
    def change_days_de_catcolor(self, but):
        self.days_de_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_de_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_de_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.days_de_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.days_de_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.days_de_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.days_de_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.days_de_comments.setStyleSheet("background-color: white;")
        
    def days_de_views_ui(self):
        self.change_days_de_catcolor('views')
        self.plot_days('DE', 'views')
        self.text_days('DE', 'views')
    
    def days_de_likes_ui(self):
        self.change_days_de_catcolor('likes')
        self.plot_days('DE', 'likes')
        self.text_days('DE', 'likes')
    
    def days_de_dislikes_ui(self):
        self.change_days_de_catcolor('dislikes')
        self.plot_days('DE', 'dislikes')
        self.text_days('DE', 'dislikes')
        
    def days_de_comments_ui(self):
        self.change_days_de_catcolor('comments')
        self.plot_days('DE', 'comments')
        self.text_days('DE', 'comments')
    
    ###defintions of most page---------------------------------------------------
    
    def mostui(self):
        self.change_subview(2)
        self.change_country_switch(0)
        self.change_buttoncolor('most')
        self.plot_most('US', 'views')
        self.change_most_us_catcolor('views')
        self.change_most_country_butcolor('us')
        self.text_most('US', 'views')
    
    #change the color of country button in most page
    def change_most_country_butcolor(self, but):
        self.most_us.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_ca.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_gb.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_fr.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_de.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'us'):
            self.most_us.setStyleSheet("background-color: white;")
        elif(but == 'ca'):
            self.most_ca.setStyleSheet("background-color: white;")
        elif(but == 'gb'):
            self.most_gb.setStyleSheet("background-color: white;")
        elif(but == 'fr'):
            self.most_fr.setStyleSheet("background-color: white;")
        elif(but == 'de'):
            self.most_de.setStyleSheet("background-color: white;")
    
    def plot_most(self, country='US', cat='views'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        
        label = QLabel(self.sub_view)
        pixmap = QPixmap(root_dir + '/analytics/most_img/most_' + country + '_' + cat + '.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(240, 70)
        label.resize(730, 730)
        label.show()
    
    def text_most(self,country='US', cat='views'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.dirname(cur_dir)
        pickle_root = root_dir + '/analytics/most_pickles'
        #get sums from pickle
        with open(pickle_root+'/most_'+country+'_'+cat, 'rb') as pfile:
            text = pickle.load(pfile)
        
        heading = QLabel(self.sub_view)
        heading.setText('Top 10 most popular videos')
        hfont = QtGui.QFont()
        hfont.setPointSize(30)
        heading.setFont(hfont)
        heading.move(1100, 70)
        heading.resize(700, 200)
        heading.setStyleSheet('color: white;')
        heading.show()
        
        label = QLabel(self.sub_view)
        label.setText(text)
        font = QtGui.QFont()
        font.setPointSize(20)
        label.setFont(font)
        label.move(1100, 230)
        label.resize(700, 500)
        label.setStyleSheet('color: white;')
        label.show()
    
    #change countries in most page
    def change_country_switch(self, index):
        self.country_switch.setCurrentIndex(index)
    
    #us-----------------------------------------------
    
    def most_us_ui(self):
        self.change_country_switch(0)
        self.change_most_country_butcolor('us')
        self.plot_most('US', 'views')
        self.change_most_us_catcolor('views')
        self.text_most('US', 'views')
    
    #change the color of category button in most us page
    def change_most_us_catcolor(self, but):
        self.most_us_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_us_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_us_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_us_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.most_us_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.most_us_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.most_us_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.most_us_comments.setStyleSheet("background-color: white;")
        
    def most_us_views_ui(self):
        self.change_most_us_catcolor('views')
        self.plot_most('US', 'views')
        self.text_most('US', 'views')
    
    def most_us_likes_ui(self):
        self.change_most_us_catcolor('likes')
        self.plot_most('US', 'likes')
        self.text_most('US', 'likes')
    
    def most_us_dislikes_ui(self):
        self.change_most_us_catcolor('dislikes')
        self.plot_most('US', 'dislikes')
        self.text_most('US', 'dislikes')
        
    def most_us_comments_ui(self):
        self.change_most_us_catcolor('comments')
        self.plot_most('US', 'comments')
        self.text_most('US', 'comments')
    
    #ca-----------------------------------------------
    
    def most_ca_ui(self):
        self.change_country_switch(1)
        self.change_most_country_butcolor('ca')
        self.plot_most('CA', 'views')
        self.change_most_ca_catcolor('views')
        self.text_most('CA', 'views')
    
    #change the color of category button in most ca page
    def change_most_ca_catcolor(self, but):
        self.most_ca_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_ca_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_ca_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_ca_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.most_ca_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.most_ca_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.most_ca_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.most_ca_comments.setStyleSheet("background-color: white;")
        
    def most_ca_views_ui(self):
        self.change_most_ca_catcolor('views')
        self.plot_most('CA', 'views')
        self.text_most('CA', 'views')
    
    def most_ca_likes_ui(self):
        self.change_most_ca_catcolor('likes')
        self.plot_most('CA', 'likes')
        self.text_most('CA', 'likes')
    
    def most_ca_dislikes_ui(self):
        self.change_most_ca_catcolor('dislikes')
        self.plot_most('CA', 'dislikes')
        self.text_most('CA', 'dislikes')
        
    def most_ca_comments_ui(self):
        self.change_most_ca_catcolor('comments')
        self.plot_most('CA', 'comments')
        self.text_most('CA', 'comments')
    
    #gb-----------------------------------------------
    
    def most_gb_ui(self):
        self.change_country_switch(2)
        self.change_most_country_butcolor('gb')
        self.plot_most('GB', 'views')
        self.change_most_gb_catcolor('views')
        self.text_most('GB', 'views')
    
    #change the color of category button in most gb page
    def change_most_gb_catcolor(self, but):
        self.most_gb_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_gb_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_gb_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_gb_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.most_gb_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.most_gb_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.most_gb_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.most_gb_comments.setStyleSheet("background-color: white;")
        
    def most_gb_views_ui(self):
        self.change_most_gb_catcolor('views')
        self.plot_most('GB', 'views')
        self.text_most('GB', 'views')
    
    def most_gb_likes_ui(self):
        self.change_most_gb_catcolor('likes')
        self.plot_most('GB', 'likes')
        self.text_most('GB', 'likes')
    
    def most_gb_dislikes_ui(self):
        self.change_most_gb_catcolor('dislikes')
        self.plot_most('GB', 'dislikes')
        self.text_most('GB', 'dislikes')
        
    def most_gb_comments_ui(self):
        self.change_most_gb_catcolor('comments')
        self.plot_most('GB', 'comments')
        self.text_most('GB', 'comments')
    
    #fr-----------------------------------------------
    
    def most_fr_ui(self):
        self.change_country_switch(3)
        self.change_most_country_butcolor('fr')
        self.plot_most('FR', 'views')
        self.change_most_fr_catcolor('views')
        self.text_most('FR', 'views')
    
    #change the color of category button in most fr page
    def change_most_fr_catcolor(self, but):
        self.most_fr_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_fr_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_fr_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_fr_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.most_fr_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.most_fr_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.most_fr_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.most_fr_comments.setStyleSheet("background-color: white;")
        
    def most_fr_views_ui(self):
        self.change_most_fr_catcolor('views')
        self.plot_most('FR', 'views')
        self.text_most('FR', 'views')
    
    def most_fr_likes_ui(self):
        self.change_most_fr_catcolor('likes')
        self.plot_most('FR', 'likes')
        self.text_most('FR', 'likes')
    
    def most_fr_dislikes_ui(self):
        self.change_most_fr_catcolor('dislikes')
        self.plot_most('FR', 'dislikes')
        self.text_most('FR', 'dislikes')
        
    def most_fr_comments_ui(self):
        self.change_most_fr_catcolor('comments')
        self.plot_most('FR', 'comments')
        self.text_most('FR', 'comments')
    
    #de-----------------------------------------------
        
    def most_de_ui(self):
        self.change_country_switch(4)
        self.change_most_country_butcolor('de')
        self.plot_most('DE', 'views')
        self.change_most_de_catcolor('views')
        self.text_most('DE', 'views')
        
    #change the color of category button in most de page
    def change_most_de_catcolor(self, but):
        self.most_de_views.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_de_likes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_de_dislikes.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.most_de_comments.setStyleSheet("background-color: rgb(135, 135, 135);")
        if(but == 'views'):
            self.most_de_views.setStyleSheet("background-color: white;")
        elif(but == 'likes'):
            self.most_de_likes.setStyleSheet("background-color: white;")
        elif(but == 'dislikes'):
            self.most_de_dislikes.setStyleSheet("background-color: white;")
        elif(but == 'comments'):
            self.most_de_comments.setStyleSheet("background-color: white;")
        
    def most_de_views_ui(self):
        self.change_most_de_catcolor('views')
        self.plot_most('DE', 'views')
        self.text_most('DE', 'views')
    
    def most_de_likes_ui(self):
        self.change_most_de_catcolor('likes')
        self.plot_most('DE', 'likes')
        self.text_most('DE', 'likes')
    
    def most_de_dislikes_ui(self):
        self.change_most_de_catcolor('dislikes')
        self.plot_most('DE', 'dislikes')
        self.text_most('DE', 'dislikes')
        
    def most_de_comments_ui(self):
        self.change_most_de_catcolor('comments')
        self.plot_most('DE', 'comments')
        self.text_most('DE', 'comments')
    
    ###defintions of scatter page------------------------------------------------
    
    def scatterui(self):
        self.change_subview(0)
        self.change_buttoncolor('scatter')
        label = QLabel(self.sub_view)
        pixmap = QPixmap('scattermatrix.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.move(240, 70)
        label.resize(1300, 750)
        label.show()
    
    ###--------------------------------------------------------------------------
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Mini Project"))
        self.likepred_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#fafafa;\">Like Prediction &amp; Analysis</span></p></body></html>"))
        self.youtube_logo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/youlogo/youtube-logo2.png\" /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Prediction (ML)</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Analysis</span></p></body></html>"))
        self.MLheading.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Prediction (ML)</span></p></body></html>"))
        self.enterinput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Enter Input</span></p></body></html>"))
        self.views_ipbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.dislikes_ipbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comments_ipbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.views_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Views</span></p></body></html>"))
        self.dislikes_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Dislikes</span></p></body></html>"))
        self.comments_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Comments</span></p></body></html>"))
        self.predict_but.setText(_translate("MainWindow", "Predict Likes"))
        self.days_but.setText(_translate("MainWindow", "Days from virality"))
        self.wordcld_but.setText(_translate("MainWindow", "Word Cloud"))
        self.countries_but.setText(_translate("MainWindow", "Countries"))
        self.most_but.setText(_translate("MainWindow", "Most"))
        self.scatter_but.setText(_translate("MainWindow", "Scatter Matrix"))
        self.word_us.setText(_translate("MainWindow", "US"))
        self.word_ca.setText(_translate("MainWindow", "CA"))
        self.word_gb.setText(_translate("MainWindow", "GB"))
        self.word_fr.setText(_translate("MainWindow", "FR"))
        self.word_de.setText(_translate("MainWindow", "DE"))
        self.most_ca.setText(_translate("MainWindow", "CA"))
        self.most_de.setText(_translate("MainWindow", "DE"))
        self.most_gb.setText(_translate("MainWindow", "GB"))
        self.most_us.setText(_translate("MainWindow", "US"))
        self.most_fr.setText(_translate("MainWindow", "FR"))
        self.most_us_views.setText(_translate("MainWindow", "Views"))
        self.most_us_likes.setText(_translate("MainWindow", "Likes"))
        self.most_us_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.most_us_comments.setText(_translate("MainWindow", "Comments"))
        self.most_ca_views.setText(_translate("MainWindow", "Views"))
        self.most_ca_likes.setText(_translate("MainWindow", "Likes"))
        self.most_ca_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.most_ca_comments.setText(_translate("MainWindow", "Comments"))
        self.most_gb_likes.setText(_translate("MainWindow", "Likes"))
        self.most_gb_comments.setText(_translate("MainWindow", "Comments"))
        self.most_gb_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.most_gb_views.setText(_translate("MainWindow", "Views"))
        self.most_fr_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.most_fr_likes.setText(_translate("MainWindow", "Likes"))
        self.most_fr_views.setText(_translate("MainWindow", "Views"))
        self.most_fr_comments.setText(_translate("MainWindow", "Comments"))
        self.most_de_comments.setText(_translate("MainWindow", "Comments"))
        self.most_de_likes.setText(_translate("MainWindow", "Likes"))
        self.most_de_views.setText(_translate("MainWindow", "Views"))
        self.most_de_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.countries_views.setText(_translate("MainWindow", "Views"))
        self.countries_likes.setText(_translate("MainWindow", "Likes"))
        self.countries_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.countries_comments.setText(_translate("MainWindow", "Comments"))
        self.days_us.setText(_translate("MainWindow", "US"))
        self.days_de.setText(_translate("MainWindow", "DE"))
        self.days_ca.setText(_translate("MainWindow", "CA"))
        self.days_gb.setText(_translate("MainWindow", "GB"))
        self.days_fr.setText(_translate("MainWindow", "FR"))
        self.days_us_views.setText(_translate("MainWindow", "Views"))
        self.days_us_likes.setText(_translate("MainWindow", "Likes"))
        self.days_us_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.days_us_comments.setText(_translate("MainWindow", "Comments"))
        self.days_ca_views.setText(_translate("MainWindow", "Views"))
        self.days_ca_likes.setText(_translate("MainWindow", "Likes"))
        self.days_ca_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.days_ca_comments.setText(_translate("MainWindow", "Comments"))
        self.days_gb_likes.setText(_translate("MainWindow", "Likes"))
        self.days_gb_comments.setText(_translate("MainWindow", "Comments"))
        self.days_gb_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.days_gb_views.setText(_translate("MainWindow", "Views"))
        self.days_fr_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.days_fr_likes.setText(_translate("MainWindow", "Likes"))
        self.days_fr_views.setText(_translate("MainWindow", "Views"))
        self.days_fr_comments.setText(_translate("MainWindow", "Comments"))
        self.days_de_comments.setText(_translate("MainWindow", "Comments"))
        self.days_de_likes.setText(_translate("MainWindow", "Likes"))
        self.days_de_views.setText(_translate("MainWindow", "Views"))
        self.days_de_dislikes.setText(_translate("MainWindow", "Dislikes"))
        self.analysis_heading.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Analysis</span></p></body></html>"))

    
    
#miniproj.qrc is stored in test
#convert it to rc and move to gui
import miniproj_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

