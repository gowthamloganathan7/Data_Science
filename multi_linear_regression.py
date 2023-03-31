# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:44:07 2023

@author: Gowtham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("petrol_consumption.csv")
print(df.shape,df.columns)

# check for null value
print(df.isnull().sum())

# dropping down the dupplicate value
df= df.drop_duplicates()
print(df.shape)
print(df.dtypes)

#check for outliers

print(df.describe())

'''iqr = df['Petrol_tax'].quantile(0.75) - df['Petrol_tax'].quantile(0.25)
upper_threshold = df['Petrol_tax'].quantile(0.75) + (1.5 * iqr)
lower_threshold = df['Petrol_tax'].quantile(0.25) - (1.5 * iqr)
upper_threshold, lower_threshold
df.Petrol_tax = df.Petrol_tax.clip(lower_threshold, upper_threshold)
'''

#EDA
df.groupby("Petrol_tax")["Petrol_Consumption"].mean().plot()
#df.plot(x= "Petrol_tax", y= "Petrol_Consumption", style="o")
plt.title("Petrol_tax vs petrol_consumption")
plt.xlabel("petrol_tax")
plt.ylabel("petrol_consumption")
plt.show()

print(df[["Petrol_tax","Petrol_Consumption"]].corr())
#there is linear relationship between tax and consumption
#petrol tax increases so petrol consumption decreases
#no tansformation is required

df.plot(x="Average_income", y="Petrol_Consumption", style="o")
plt.title("Average income vs consumption")
plt.xlabel("income")
plt.ylabel("consumption")
plt.show()
print(df[["Average_income","Petrol_Consumption"]].corr())

df["transformed"]=np.exp(df["Paved_Highways"])
df.plot(x="transformed",y="Petrol_Consumption", style="o")
plt.title("highway vs consumption")
plt.xlabel("hignway")
plt.xlabel("consumption")
plt.show()
print(df[["transformed","Petrol_Consumption"]].corr())
#1 there is no linear relationship
#2 we have tried all the transformation methods
#3 so we have desided to drop the feature

df.plot(x="Population_Driver_licence(%)", y= "Petrol_Consumption", style="o")
plt.title("driver_licence vs petrol_consumption")
plt.xlabel("driver_licence")
plt.ylabel("petrol_consumption")
plt.show()
print(df[["Population_Driver_licence(%)","Petrol_Consumption"]].corr())
#1 there is linear relationship
#2 no transformation is required

#coverting the dataframe into array
X=df[["Petrol_tax","Average_income","Population_Driver_licence(%)"]].values
y=df[["Petrol_Consumption"]].values
# spliting the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2, random_state=0)

#scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

#modeling

from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(X_train_scaled,y_train)

print(regressor.intercept_)

print(regressor.coef_)

#coeff_df = pd.DataFrame(regressor.coef_,['Petrol_tax','Average_income','Population_Driver_licence(%)'],columns=["coefficient"])

y_pred=regressor.predict(X_test_scaled)
print(y_pred)

#evaluaton metrics
from sklearn import metrics
print("r2_score:", metrics.r2_score(y_test,y_pred))


