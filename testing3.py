import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
col=['sepal_length','sepal_width','petal_length','petal_width','class']
iris=pd.read_csv("iris.csv",names=col)
print(iris)
iris_setosa=iris.loc[iris["class"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["class"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["class"]=="Iris-versicolor"]
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"petal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"petal_width").add_legend()
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"sepal_length").add_legend()
sns.FacetGrid(iris,hue="class",height=3).map(sns.distplot,"sepal_width").add_legend()
sns.pairplot(iris,hue="class")
plt.show()