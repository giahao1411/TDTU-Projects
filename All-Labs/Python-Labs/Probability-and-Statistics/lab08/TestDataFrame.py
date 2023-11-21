import pandas as pd

df = pd.DataFrame({"numbers": [1, 2, 3], "colors": ["red", "white", "blue"]})

print(df, "\n\n")

# to specify the order, use the columns parameter
df = pd.DataFrame(
    {"numbers": [1, 2, 3], "colors": ["red", "white", "blue"]},
    columns=["numbers", "colors"],
)

print(df)
