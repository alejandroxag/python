# DataCamp
# Statistical Thinking in Python I
# Graphical exploratory data analysis

# Plotting a histogram

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# import iris data
iris_df = pd.read_csv('iris.csv')
print(iris_df.head())
print(iris_df.shape[0])

# set seaborn
sns.set()

# Histogram of petals' lengths
_ = plt.hist(iris_df.loc[iris_df['variety']  == 'Versicolor']['petal.length'])
_ = plt.xlabel('Petal length')
_ = plt.ylabel('Frequency')
plt.show()

# Histogram of petals' lengths with custom number of bins
n_bins = int(np.sqrt(iris_df.shape[0]))

_ = plt.hist(iris_df.loc[iris_df['variety']  == 'Versicolor']['petal.length'], bins = n_bins)
_ = plt.xlabel('Petal length')
_ = plt.ylabel('Frequency')
plt.show()

# Plot all of your data

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x = 'variety', y = 'petal.length', data = iris_df)

# Label the axes
_ = plt.xlabel('variety')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()

# Computing ECDF

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(iris_df['petal.length'])

# Generate plot
_ = plt.plot(x_vers,y_vers, marker = '.', linestyle = 'none')

# Label the axes
_ = plt.xlabel('petal length')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()

x_set, y_set = ecdf(iris_df.loc[iris_df['variety']  == 'Setosa']['petal.length'])
x_vers, y_vers = ecdf(iris_df.loc[iris_df['variety']  == 'Versicolor']['petal.length'])
x_virg, y_virg = ecdf(iris_df.loc[iris_df['variety']  == 'Virginica']['petal.length'])

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker = '.', linestyle = 'none')
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
_ = plt.plot(x_virg, y_virg, marker = '.', linestyle = 'none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()