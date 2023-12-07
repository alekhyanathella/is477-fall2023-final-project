import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/iris/iris.data", header=None, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

# Create text file for summary statistics
summary = df.describe().to_string()

with open('./results/summary.txt', 'w') as file:
    file.write(summary)

# Create a bar chart for iris data
sns.barplot(x='class', y='sepal length', data=df)
plt.xlabel('Class')
plt.ylabel('Average Sepal Length')
plt.title('Average Sepal Length by Class')
plt.savefig('./results/bar-plot.jpg')
