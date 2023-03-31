# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("student_scores.csv")
print(df.shape)
#check for outliers
print(df.describe())
#checking for missing values
print(df.isnull().sum())
#dropping the duplicate values
df = df.drop_duplicates()
print(df)
#check for datatype
print(df.dtypes)

#EDA
df.plot(x='Hours',y='Scores', style='1')
plt.title('Hours vs percentage')
plt.xlabel('Hours studied')
plt.ylabel('percentage Score')
print(plt.show())

print(df.corr())

#coverting the dataframe to numpy array to make it faster

X = df.loc[:,("Hours")].values
y = df.loc[:,("Scores")].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 7)

print(X_train.shape, X_test.shape)

#model Linear regression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

print(regressor.intercept_)
