import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 3), columns=["N1", "N2", "N3"])
print(df, "\n\n")

# head(n) method shows first n rows
print(df.head(5), "\n\n")

# tail(n) method shows last n rows
print(df.tail(5), "\n\n")

# for accessing the specific columns use "[]"
N2 = df["N2"]
print(N2, "\n\n")

# to select mutiple comlumns
N12 = df[["N1", "N2"]]
print(N12, "\n\n")

# for access number of rows we can get it just like we get it from the python list
N = df[1:-2]
print(N)
