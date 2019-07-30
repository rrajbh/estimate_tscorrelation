# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Find collinearity of two time series... 
#https://www.datacamp.com/community/tutorials/time-series-analysis-tutorial

# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set()

#load data into data frame
df = pd.read_csv('data/multiTimeline.csv', skiprows=1)
#change column names
df.columns = ['month', 'diet', 'gym', 'finance']

#turn the 'month' column into a DateTime data type and make it the index of the DataFrame.
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)

print (df.head())

df.plot(figsize=(20,10), linewidth=2, fontsize=12)
plt.xlabel('Year', fontsize=12);


#First-order differencing to remove trend
#df.diff().plot(figsize=(20,10), linewidth=5, fontsize=20)
#plt.xlabel('Year', fontsize=20)

print(df.diff().corr())

