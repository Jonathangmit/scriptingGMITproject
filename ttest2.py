import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import sys
from operator import truediv
from statsmodels.stats import weightstats as stests
# Creating colums reading in the CSV file
col=['sepal_length','sepal_width','petal_length','petal_width','class']
iris=pd.read_csv("iris.csv",names=col)
# Setting class for manipulations
iris_setosa=iris.loc[iris["class"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["class"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["class"]=="Iris-versicolor"]
# Splitting data (creating 3 different data sets) into classes for further manipulation
df1=iris[iris['class'] == 'Iris-setosa']
df2=iris[iris['class'] == 'Iris-versicolor']
df3=iris[iris['class'] == 'Iris-virginica']
df1sl= (df1['sepal_length'])
df2sl= (df2['sepal_length'])
df3sl= (df3['sepal_length'])
df1sw= (df1['sepal_width'])
df2sw= (df2['sepal_width'])
df3sw= (df3['sepal_width'])
df1pl= (df1['petal_length'])
df2pl= (df2['petal_length'])
df3pl= (df3['petal_length'])
df1pw= (df1['petal_width'])
df2pw= (df2['petal_width'])
df3pw= (df3['petal_width'])
print (stats.ttest_ind(df1sl,df2sl))
print (stats.ttest_ind(df1sl,df3sl))
print (stats.ttest_ind(df2sl,df3sl))
print (stats.ttest_ind(df1sw,df2sw))
print (stats.ttest_ind(df1sw,df3sw))
print (stats.ttest_ind(df2sw,df3sw))
print (stats.ttest_ind(df1pl,df2pl))
print (stats.ttest_ind(df1pl,df3pl))
print (stats.ttest_ind(df2pl,df3pl))
print (stats.ttest_ind(df1pw,df2pw))
print (stats.ttest_ind(df1pw,df3pw))
print (stats.ttest_ind(df2pw,df3pw))
ztest,ans = stests.ztest(df2sw,x2=df3sw,value=0,alternative='two-sided')
print (ans)
if ans < 0.01:
    print ("reject")
else:
    print ("accepted")