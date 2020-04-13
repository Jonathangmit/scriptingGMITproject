import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import sys
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
# Creating plots for each catagory of measurement
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"petal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"petal_width").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"sepal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"sepal_width").add_legend()
# Creating pairplot for values
sns.pairplot(iris,hue="class")
plt.show()
# Describing the statistics
# Setting up print to file
save_stdout = sys.stdout
fh = open("test1.txt","w")
sys.stdout = fh
# Description of whole data set
a = iris.describe()
print ("SECTION 1: COMPLETE FISHER'S IRIS DATA SET")
print(iris)
print ("SECTION 2: DESCRIPTIVE STATS FOR THE DATA SET")
print(a)
# Creating descriptive statistics of each separate class
x=df1.describe()
y=df2.describe()
z=df3.describe()
print("SECTION 3: SETOSA DATA SET AND DESCRIPTIVE STATS")
print ('\n')
print(df1)
print ('\n')
print("SECTION 3.1 : DESCRIPTIVE STATS")
print (x)
print("SECTION 4: IRIS VERSICOLOUR DATA SET AND DESCRIPTIVE STATS")
print ('\n')
print(df2)
print ('\n')
print("SECTION 4.1 : DESCRIPTIVE STATS")
print(y)
print("SECTION 5: IRIS VIRGINICA DATA SET AND DESCRIPTIVE STATS")
print ('\n')
print(df3)
print ('\n')
print ("SECTION 5.1 : DESCRIPTIVE STATS")
print(z)
# Calculating the difference in values for each aspect between classes as produced by describe
print ("SECTION 6: DIFFERENCE IN STATISTICAL OUTPUTS BETWEEN CLASSES")
print ('\n')
print ("The difference between mean values of Iris setosa and Iris versicolour attributes are")
print ('\n')
print (abs (x-y))
print ('\n')
print ("The difference between mean values of Iris setosa and Iris virginica attributes are")
print ('\n')
print (abs (x-z))
print ('\n')
print ("The difference between mean values of Iris versicolour and Iris virginica attributes are")
print ('\n')
print (abs (y-z))
# closing the file:
sys.stdout = save_stdout
fh.close()