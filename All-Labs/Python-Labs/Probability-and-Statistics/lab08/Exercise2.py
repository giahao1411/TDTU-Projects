import pandas as pd
import numpy as np

# read data from population.csv file
data = pd.read_csv("population.csv", delimiter=",")
df = pd.DataFrame(data)

# get the first 5 data points
first_5_data_points = df.head(5)

print(first_5_data_points, "\n\n")

# group the data by year then compute the requirements
dt = df.groupby(["Country Name", "Country Code"]).agg(
    {"Year": ["count", "mean", "std", "min", "max"]}
)

# print the result to the screen
print(dt)
