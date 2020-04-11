import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
col=['sepal_length','sepal_width','petal_length','petal_width','class']
iris=pd.read_csv("iris.csv",names=col)
df1=iris[iris['class'] == 'Iris-setosa']
df2=iris[iris['class'] == 'Iris-versicolor']
df3=iris[iris['class'] == 'Iris-virginica']
x=df1.describe()
y=df2.describe()
z=df3.describe()
print("SETOSA")
print(df1)
print (x)
print("IRIS VERSICOLOUR")
print(df2)
print(y)
print("IRIS VIRGINICA")
print(df3)
print(z)
