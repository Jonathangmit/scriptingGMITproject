# Importing all anticipated packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import sys
from statsmodels.stats import weightstats as stests
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
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
# Splitting data sets futher to individual aspects of each class
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
# Set up for machine learning (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
array = iris.values
i = array[:,0:4]
j = array[:,4]
i_train, i_validation, j_train, j_validation = train_test_split(i,j, train_size=None, test_size=None)
model = SVC(kernel = 'linear', gamma='auto',C=1.5)
model.fit(i_train, j_train)
predictions = model.predict(i_validation)
# Creating plots for each catagory of measurement
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"petal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"petal_width").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"sepal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=2).map(sns.distplot,"sepal_width").add_legend()
# Creating pairplot for values
sns.pairplot(iris,hue="class")
plt.show()
# Box plots
df1.plot.box(grid='True')
plt.show()
df2.plot.box(grid='True')
plt.show()
df3.plot.box(grid='True')
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
print ('\n')
print("SECTION 4: IRIS VERSICOLOUR DATA SET AND DESCRIPTIVE STATS")
print ('\n')
print(df2)
print ('\n')
print("SECTION 4.1 : DESCRIPTIVE STATS")
print(y)
print ('\n')
print("SECTION 5: IRIS VIRGINICA DATA SET AND DESCRIPTIVE STATS")
print ('\n')
print(df3)
print ('\n')
print ("SECTION 5.1 : DESCRIPTIVE STATS")
print(z)
print ('\n')
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
print('\n')
# Conducting independant T-test on Iris versicolour and Iris virginica aspects
#print ('\n')
print ("SECTION 7 INDEPENDANT T-TEST FOR ASSOTIATION OF THE SAME ATTRIBUTE (IRIS VERSICOLOUR AND IRIS VIRGINICA ONLY) ")
print("CRITERIA p > 0.01 for acceptance of assotiation")
ttest,anssl = stats.ttest_ind(df2sl,df3sl)
print ("The T-test p value for comparison of sepal lengths is", anssl)
if anssl < 0.01:
    print ("The hypothesis is rejected identification can not be determined via this attribute")
else:
    print ("The hypothesis is accepted identification can be determined via this attribute")
print (" ")
ttest,anssw = stats.ttest_ind(df2sw,df3sw)
print ("The T-test p value for comparison of sepal widths is" , anssw)
if anssw < 0.01:
    print ("The hypothesis is rejected identification can not be determined via this attribute")
else:
    print ("The hypothesis is accepted identification can be determined via this attribute")
print (" ")
ttest,anspw = stats.ttest_ind(df2pw,df3pw)
print ("The T-test p value for comparison of petal widths is", anspw)
if anspw < 0.01:
    print ("The hypothesis is rejected identification can not be determined via this attribute")
else:
    print ("The hypothesis is accepted identification can be determined via this attribute")
print (" ")
ttest,anspl = stats.ttest_ind(df2pl,df3pl)
print ("The T-test p value for comparison of petal lengths is", anspl)
if anspl < 0.01:
    print ("The hypothesis is rejected identification can not be determined via this attribute")
else:
    print ("The hypothesis is accepted identification can be determined via this attribute")
print ('\n')
print ("SECTION 8, MACHINE LEARNING USING SVC package")
print ('\n')
print("ACCURANCY SCORE")
print ('\n')
print (accuracy_score(j_validation, predictions))
print ('\n')
print("CONFUSION MATRIX")
print ('\n')
print (confusion_matrix(j_validation, predictions,))
print ('\n')
print("CLASSIFICATION REPORT")
print ('\n')
print (classification_report(j_validation, predictions))
# closing the file:
sys.stdout = save_stdout
fh.close()