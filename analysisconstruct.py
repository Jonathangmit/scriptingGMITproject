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
print(df1)
print (x)
print("SECTION 4: IRIS VERSICOLOUR DATA SET AND DESCRIPTIVE STATS")
print(df2)
print(y)
print("SECTION 5: IRIS VIRGINICA DATA SET AND DESCRIPTIVE STATS")
print(df3)
print(z)
# Producing mean values for each aspect based on class
xm=df1.mean()
ym=df2.mean()
zm=df3.mean()
xstd=stats.tstd(x)
ystd=stats.tstd(y)
zstd=stats.tstd(z)
print(xm)
print(ym)
print(zm)
# Calculating the difference in values for each aspect between classes 
seve = xm - ym
sevi = xm - zm
vevi = ym - zm
print ("The difference between mean values of Iris setosa and Iris versicolour attributes are")
print (abs (seve))
print ("The difference between mean values of Iris setosa and Iris virginica attributes are")
print (abs (sevi))
print ("The difference between mean values of Iris versicolour and Iris virginica attributes are")
print (abs (vevi))
print (xstd)
print (ystd)
print (zstd)
print(abs (x-y))
# closing the file:
sys.stdout = save_stdout
fh.close()