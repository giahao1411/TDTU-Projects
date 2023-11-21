import numpy as np
import pandas as pd

data = np.loadtxt("sample.txt", delimiter=",")
print(data, "\n\n")

# alternative way to read file as a cvs file
data = pd.read_csv("sample.txt", delimiter=",")
print(data, "\n\n")

data = pd.read_csv("anothersample.txt", delimiter=",")
print(data)
print("Print column score")
print(data.Score)
