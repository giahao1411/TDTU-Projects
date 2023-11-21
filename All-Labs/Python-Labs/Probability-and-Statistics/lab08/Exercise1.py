import pandas as pd
import numpy as np


# count function
def count(data):
    count = 0
    for i in range(0, len(data) + 1):
        count += 1
    return count


# compute mean function
def mean(data):
    n = count(data)
    sum = data.sum()
    return sum / n

# 
# compute standard deviation function
def std(data):
    n = count(data)
    m = mean(data)
    square_diff = [(x - m) ** 2 for x in data]
    mean_square_diff = sum(square_diff) / n
    std = mean_square_diff ** (1 / 2)
    return std


# find min function
def min(data):
    return data.min()


# find max function
def max(data):
    return data.max()


# read data from iris.csv file
data = pd.read_csv("iris.csv", delimiter=",")
df = pd.DataFrame(data)

# the first 5 data points
first_5_data_point = df.head(5)
print(first_5_data_point, "\n\n")

# initiate the variables for each data rows
s1 = df["sepal_length"]  # sepal_length
s2 = df["sepal_width"]  # sepal_width
s3 = df["petal_length"]  # petal_length
s4 = df["petal_width"]  # petal_width

# compute the requirements
dt = pd.DataFrame(
    {
        "sepal_length": [count(s1), mean(s1), std(s1), min(s1), max(s1)],
        "sepal_width": [count(s2), mean(s2), std(s2), min(s2), max(s2)],
        "petal_length": [count(s3), mean(s3), std(s3), min(s3), max(s3)],
        "petal_width": [count(s4), mean(s4), std(s4), min(s4), max(s4)],
    }
)

# rename the index label to the requirements
new_row_name = ["count", "mean", "std", "min", "max"]
dt = dt.set_index(pd.Index(new_row_name))

# print to screen the final result
print(dt)
