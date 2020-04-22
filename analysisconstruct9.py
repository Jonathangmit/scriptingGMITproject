# Importing all required packages
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
iris_setosa= ise = iris.loc[iris["class"]=="Iris-setosa"]
iris_virginica= ivi = iris.loc[iris["class"]=="Iris-virginica"]
iris_versicolor= ive = iris.loc[iris["class"]=="Iris-versicolor"]
# Splitting data sets futher to individual aspects of each class
#df1 is Iris setosa
#df2 is iris virginica
#df3 is Iris versicolour
#e.g df1sl is a data set containing Iris setosa's sepal lengths
df1sl= (ise['sepal_length'])
df2sl= (ivi['sepal_length'])
df3sl= (ive['sepal_length'])
df1sw= (ise['sepal_width'])
df2sw= (ivi['sepal_width'])
df3sw= (ive['sepal_width'])
df1pl= (ise['petal_length'])
df2pl= (ivi['petal_length'])
df3pl= (ive['petal_length'])
df1pw= (ise['petal_width'])
df2pw= (ivi['petal_width'])
df3pw= (ive['petal_width'])
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
# Creating pairplot and box plot for values
sns.pairplot(iris,hue="class")
iris_setosa.plot.box(grid='True')
iris_virginica.plot.box(grid='True')
iris_versicolor.plot.box(grid='True')
plt.show()
# Describing the statistics
# Setting up print to file
save_stdout = sys.stdout
fh = open("analysis output.txt","w")
sys.stdout = fh
# Description of whole data set for the file
a = iris.describe()
print ("SECTION 1: COMPLETE FISHER'S IRIS DATA SET")
print(iris)
print ("SECTION 2: DESCRIPTIVE STATS FOR THE DATA SET")
print(a)
# Creating descriptive statistics of each separate class
x=iris_setosa.describe()
y=iris_virginica.describe()
z=iris_versicolor.describe()
print("SECTION 3: SETOSA DATA SET AND DESCRIPTIVE STATS",'\n',(iris_setosa),'\n' )
print("SECTION 3.1 : DESCRIPTIVE STATS",'\n',(x),'\n')
print("SECTION 4: IRIS VERSICOLOUR DATA SET AND DESCRIPTIVE STATS"'\n',(iris_virginica),'\n')
print("SECTION 4.1 : DESCRIPTIVE STATS",'\n',(y),'\n')
print("SECTION 5: IRIS VIRGINICA DATA SET AND DESCRIPTIVE STATS"'\n',(iris_versicolor),'\n')
print ("SECTION 5.1 : DESCRIPTIVE STATS",'\n',(z),'\n')
# Calculating the difference in values for each aspect between classes as produced by describe
print ("SECTION 6: DIFFERENCE IN STATISTICAL OUTPUTS BETWEEN CLASSES",'\n')
print ("The difference between mean values of Iris setosa and Iris versicolour attributes are",'\n',abs (x-y),'\n')
print ("The difference between mean values of Iris setosa and Iris virginica attributes are",'\n',abs (x-z),'\n')
print ("The difference between mean values of Iris versicolour and Iris virginica attributes are",'\n',abs (y-z),'\n')
# Conducting independant T-test on Iris versicolour and Iris virginica aspects
rej = "The hypothesis is rejected identification can not be determined via this attribute"
acc = "The hypothesis is accepted identification can be determined via this attribute"
print ("SECTION 7 INDEPENDANT T-TEST FOR ASSOTIATION OF THE SAME ATTRIBUTE (IRIS VERSICOLOUR AND IRIS VIRGINICA ONLY) ")
print("CRITERIA p > 0.01 for acceptance of assotiation",'\n')
ttest,anssl = stats.ttest_ind(df2sl,df3sl)
print ("The T-test p value for comparison of sepal lengths is", anssl)
if anssl < 0.01:
    print (rej,'\n')
else:
    print (acc,'\n')
ttest,anssw = stats.ttest_ind(df2sw,df3sw)
print ("The T-test p value for comparison of sepal widths is" , anssw)
if anssw < 0.01:
    print (rej,'\n')
else:
    print (acc,'\n')
ttest,anspw = stats.ttest_ind(df2pw,df3pw)
print ("The T-test p value for comparison of petal widths is", anspw)
if anspw < 0.01:
    print (acc,'\n')
else:
    print (rej,'\n')
ttest,anspl = stats.ttest_ind(df2pl,df3pl)
print ("The T-test p value for comparison of petal lengths is", anspl)
if anspl < 0.01:
    print (acc,'\n')
else:
    print (rej,'\n')
print ('\n',"SECTION 8, MACHINE LEARNING USING SVC package",'\n',"ACCURANCY SCORE",'\n')
print (accuracy_score(j_validation, predictions))
print('\n',"CONFUSION MATRIX",'\n')
print (confusion_matrix(j_validation, predictions,))
print('\n',"CLASSIFICATION REPORT",'\n')
print (classification_report(j_validation, predictions))
# closing the file:
sys.stdout = save_stdout
fh.close()