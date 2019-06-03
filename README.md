## YouTube Video Data Analysis and Like Count Predictor

This is a tool for getting youtube video like count prediction. A Random Forest model was used for training on a large dataset of ~200,000 videos. Feature engineering, Data cleaning, Data selection and many other techniques were used for this task.

## Report

`documents/mini_proj_report.docx` contains a detailed explanation of different steps and techniques that were used for this task.

## Presentation

`documents/project_ppt.pptx` contains a brief overview of the project.

## Tools Used

* spyder 3
* python 3.7
* Pandas
* NumPy
* Matplotlib
* PyQt5
* PyQt5 designer


## Dataset
	
	Following is used to see the datasets required for the project.
	It contains datasets according to countries - US, CA, GB, FR, DE.
	
	'''terminal
	~/miniproj$ cd youtube-new
	'''

## How to run :

1. **GUI**
	
	'''terminal
	~/miniproj/gui$ python3 youtube_proj16.py
	'''

2. **Machine Learning**

	2.1 **Combine datasets**
	
	'''terminal
	~/miniproj/ml$ python3 combine_csv.py
	'''
	
	2.2 **Choose model**
	
	'''terminal
	~/miniproj/ml$ python3 choose_model.py
	'''
	
	2.3 **Train model**
	
	'''terminal
	~/miniproj/ml$ python3 train_model.py
	'''
	
	2.4 **Create pickle of trained model**
	
	'''terminal
	~/miniproj/ml$ python3 create_model_pickle.py
	'''

3. **Analytics**
	
	3.1 **Word Cloud**
	
	'''terminal
	~/miniproj/analytics$ python3 all_in_one_wordcld_2.py
	'''
	
	3.2 **Countries in absolute numbers**
	
	'''terminal
	~/miniproj/analytics$ python3 countries_full_2.py
	'''
	
	3.3 **Days from virality**
	
	'''terminal
	~/miniproj/analytics$ python3 days_from_vir_2.py
	'''
	
	3.4 **Most popular videos**
	
	'''terminal
	~/miniproj/analytics$ python3 most_v3.py
	'''
