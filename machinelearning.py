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
# split out validation data set
array = iris.values
i = array[:,0:4]
j = array[:,4]
i_train, i_validation, j_train, j_validation = train_test_split(i,j, test_size=None)
model = SVC(gamma='auto')
model.fit(i_train, j_train)
predictions = model.predict(i_validation)
print(accuracy_score(j_validation, predictions))
print(confusion_matrix(j_validation, predictions))
print(classification_report(j_validation, predictions))