# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:14:03 2018

@author: Antika
"""
#MULTIPLE LINEAR REGRESSION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
dataset = pd.read_csv('C:\\Users\\ASUS\Desktop\\Linear_algebra\\50_Startups.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values
 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder = LabelEncoder()
x[:, 3] = encoder.fit_transform(x[:,3])
onehotencoder = OneHotEncoder(categorical_features= [3])
x= onehotencoder.fit_transform(x).toarray()
x[:,3]

#avoid the dummy variable trap
x= x[:, 1:]

# Splitting the Dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= 0.2,random_state=0)

#fitting multiple linear regression model to trainning set
from sklearn.linear_model import LinearRegression
regression =LinearRegression() 
regression.fit(x_train,y_train)

#predicting the test set

y_predict = regression.predict(x_test)

#make optimal multiple linear regression using BACKWARD ELEMINATION(SL=50%)
import statsmodels.formula.api as sm
#adding a column of values 1
x=np.append(arr= np.ones((50,1)).astype(int), values=x, axis=1)

x_optimal = x[:, [0,1,2,3,4,5]]
regression_OLS = sm.OLS(endog =y,exog =x_optimal).fit()
regression_OLS.summary()

x_optimal = x[:, [0,1,3,4,5]]
regression_OLS = sm.OLS(endog =y,exog =x_optimal).fit()
regression_OLS.summary()
















