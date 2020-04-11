import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
col=['sepal_length','sepal_width','petal_length','petal_width','class']
iris=pd.read_csv("iris.csv",names=col)
x = iris.describe()
print(x)
y = pd.pivot_table(iris, index=["class"],values = ['sepal_length', 'sepal_width'], columns= ['petal_length'], aggfunc=[np.sum],fill_value=0)
print(y)