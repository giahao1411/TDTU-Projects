import matplotlib.pyplot as plt
import pandas as pd

# read data from iris.csv
data = pd.read_csv("iris.csv", delimiter=",")
df = pd.DataFrame(data)

"""First requirement"""
# get the x and y from DataFrame
sepal_length = df["sepal_length"]
sepal_width = df["sepal_width"]

# create subplot
fig, ax = plt.subplots(1, 1)

# plot to scatter
ax.scatter(sepal_length, sepal_width)
ax.set_title("Scatter Plot")
ax.set_xlabel("sepal_length")
ax.set_ylabel("sepal_width")
plt.show()

"""Second requirement"""
# read the sepal_length and show it in histogram with bins=20
fig, ax = plt.subplots(1, 1)

ax.hist(sepal_length, bins=[0, 20, 40, 60, 80, 100])
ax.set_title("Hisogram of Sepal length")
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.set_xlabel("marks")
ax.set_ylabel("no. of sepal length")
plt.show()
