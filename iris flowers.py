import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("iris.csv")

sns.pairplot(df, hue="class")
plt.show()