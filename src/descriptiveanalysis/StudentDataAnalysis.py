import pandas
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

names = ['student', 'Age', 'Course', 'stream', 'Results', 'Gender', 'sucess']
data = pandas.read_csv('Student.csv')
description = data.describe()
print(description)

data.shape

data.head()

data.dtypes

data.corr()


# plot data

scatter_matrix(data)
plt.show()


hist = data.hist(bins=3)

ax = data.plot.box()

