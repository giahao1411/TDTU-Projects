import matplotlib.pyplot as plt
import pandas as pd

# read data from company_sales_data.csv
data = pd.read_csv("company_sales_data.csv", delimiter=",")
df = pd.DataFrame(data)

"""First requirement"""
months = df["month_number"]
total_profit = df["total_profit"]

# plot the total_profit using line
plt.plot(months, total_profit)
plt.xlabel("Month")
plt.ylabel("Total profit")
plt.show()

"""Second requirement"""
toothpaste_sales_data = df["toothpaste"]

# plot the toothpaste sales data using scatter
fig, ax = plt.subplots(1, 1)

ax.scatter(months, toothpaste_sales_data)
ax.set_title("Toothpaste sales data")
ax.set_xlabel("Month")
ax.set_ylabel("Toothpaste sale")
plt.show()

"""Third requirement"""
facecream_sales_data = df["facecream"]
facewash_sales_data = df["facewash"]

plt.title("face cream and face wash sales data", fontstyle="italic")
plt.xlabel("Face Cream")
plt.ylabel("Face Wash")
plt.bar(facecream_sales_data, facewash_sales_data, width=50)
plt.show()
