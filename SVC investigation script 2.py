# Importing all required packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import sys
import statistics as statsx
from statsmodels.stats import weightstats as stests
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Creating colums and reading in the from CSV file
col=['sepal_length','sepal_width','petal_length','petal_width','class']
iris=pd.read_csv("iris.csv",names=col)
# Setting class for manipulations
# Iris setosa = ise / Iris virginica = ivi/ Iris versicolour = ive 
ise = iris[iris["class"]=="Iris-setosa"]
ivi = iris[iris["class"]=="Iris-virginica"]
ive = iris[iris["class"]=="Iris-versicolor"]
# Only SVC used here as rated best through testing on above website
# Setting up print to file
save_stdout = sys.stdout
fh = open("datafileC.csv","w")
sys.stdout = fh
x = 1
while x <= 7:
    y=1
    while y <=100:
        array = iris.values
        i = array[:,0:4]
        j = array[:,4]
        i_train, i_validation, j_train, j_validation = train_test_split(i,j, train_size=60, test_size=90)
        model = SVC(kernel = 'linear', gamma='auto',C=x)
        model.fit(i_train, j_train)
        predictions = model.predict(i_validation)
        print ((float(x)),",",accuracy_score(j_validation, predictions))
        y=y+1
    x=x+0.5
# Description of whole data set for the file
# closing the file:
sys.stdout = save_stdout
fh.close()
col=['C value','accuracy prediction']
data=pd.read_csv("datafileC.csv",names=col)
# print (data)
df1 = data[data['C value']==1]
df2 = data[data['C value']==1.5]
df3 = data[data['C value']==2]
df4 = data[data['C value']==2.5]
df5 = data[data['C value']==3]
df6 = data[data['C value']==3.5]
df7 = data[data['C value']==4]
df1ap = (df1['accuracy prediction'])
df2ap = (df2['accuracy prediction'])
df3ap = (df3['accuracy prediction'])
df4ap = (df4['accuracy prediction'])
df5ap = (df5['accuracy prediction'])
df6ap = (df6['accuracy prediction'])
df7ap = (df7['accuracy prediction'])
#print (df1)
# print (df1ap)
print ("Mean value =" ,df1ap.mean(),'\n',"standard deviation =" ,df1ap.std(),'\n',"varience =" ,df1ap.var())
#print (df2)
print ("Mean value =" ,df2ap.mean(),'\n',"standard deviation =" ,df2ap.std(),'\n',"varience =" ,df2ap.var())
#print (df2ap)
print ("Mean value =" ,df3ap.mean(),'\n',"standard deviation =" ,df3ap.std(),'\n',"varience =" ,df3ap.var())
#print (df3)
print ("Mean value =" ,df4ap.mean(),'\n',"standard deviation =" ,df4ap.std(),'\n',"varience =" ,df4ap.var())
#print (df3ap)
#print (df4)
#print (df4ap)
save_stdout = sys.stdout
fh = open("datafileC2.csv","w")
sys.stdout = fh
print ((1),",",df1ap.mean(),",",df1ap.std(),",",df1ap.var())
print ((1.5),",",df2ap.mean(),",",df2ap.std(),",",df2ap.var())
print ((2),",",df3ap.mean(),",",df3ap.std(),",",df3ap.var())
print ((2.5),",",df4ap.mean(),",",df4ap.std(),",",df4ap.var())
print ((3),",",df5ap.mean(),",",df5ap.std(),",",df5ap.var())
print ((3.5),",",df6ap.mean(),",",df6ap.std(),",",df6ap.var())
print ((4),",",df7ap.mean(),",",df7ap.std(),",",df7ap.var())
sys.stdout = save_stdout
fh.close()
col=['C value','mean','standard deviation','varience']
data=pd.read_csv("datafileC2.csv",names=col)
print(data)
plt.plot(data['C value'], data['mean'],'g')
plt.show()
plt.plot(data['C value'], data['standard deviation'],'r')
plt.show()
plt.plot(data['C value'], data['varience'],'y')
plt.show()