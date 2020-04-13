import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import sys
from operator import truediv
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
df2sl= (df2['sepal_length'])
df3sl= (df3['sepal_length'])
df2sw= (df2['sepal_width'])
df3sw= (df3['sepal_width'])
df2pl= (df2['petal_length'])
df3pl= (df3['petal_length'])
df2pw= (df2['petal_width'])
df3pw= (df3['petal_width'])
print (stats.ttest_ind(df2sl,df3sl))
print (stats.ttest_ind(df2sw,df3sw))
print (stats.ttest_ind(df2pl,df3pl))
print (stats.ttest_ind(df2pw,df3pw))