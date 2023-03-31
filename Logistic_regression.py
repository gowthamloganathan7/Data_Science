# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:58:33 2023

@author: Gowtham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

candidates = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
              'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
              'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
              'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]
              }

df = pd.DataFrame(candidates,columns=['gmat','gpa','work_experience','admitted'])
print(df)

#check for missing value
print(df.isnull().sum())

#drop duplicate values
df = df.drop_duplicates()
print(df)

print(df.describe())
print(df.dtypes)

#eda
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.scatterplot(x='gmat', y='work_experience', hue='admitted', data=df, s=200)
plt.title("Educational Quanlification data", y=1.015, fontsize=20)
plt.xlabel("GMAT", labelpad=13)
plt.ylabel("Work Experience", labelpad=13)
ax = plt.gca()

plt.figure(figsize=(10,8))
sns.scatterplot(x="gmat", y="gpa", hue="admitted", data=df, s=200)
plt.title("Gmat vs gpa", fontsize=20)
plt.xlabel("gmat", labelpad = 13)
plt.ylabel("gpa", labelpad=13)
ax =plt.gca()

plt.figure(figsize=(10,8))
sns.scatterplot(x="gpa",y='work_experience', hue="admitted", data=df,s=200)
plt.title("gpa vs work_experience", y=1.015, fontsize=20)
plt.xlabel("GPA", labelpad = 13)
plt.ylabel("work_experience", labelpad= 13)
ax= plt.gca()

#spliting the data
X= df[['gmat','gpa','work_experience']].values
y=df['admitted'].values
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=0)

#model

from sklearn.linear_model import LogisticRegression
logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred= logistic_regression.predict(X_test)
print(y_pred)

# evaluation metrics AUROC metrics
from sklearn.metrics import plot_roc_curve

plot_roc_curve(logistic_regression,X_test,y_test)
'''
from sklearn.metrics import accuracy_score, plot_roc_curve, confusion_matrix, f1_score
#logistic_regression.score(X_test,y_test) # accuracy
#confusion_matrix(y_test,y_pred)
#f1_score(y_test,y_pred) # f1 score
# logistic_regression.score(X_test,y_test)
plot_roc_curve(logistic_regression, X_test, y_test) #AUROC
accuracy_score(y_test,y_pred) #accuracy
'''


