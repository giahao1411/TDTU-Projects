import pandas as pd
import matplotlib.pyplot as plt


# plot the line chart
def plot_line_chart(month, data, seq):
    plt.plot(month, data)
    plt.xlabel("Month")
    plt.ylabel(seq)
    plt.show()


data = pd.read_csv("company_sales_data.csv", delimiter=",")
df = pd.DataFrame(data)

# requirement: read all month of toothpaste, shampoo, facecream and show using line chart
months = df["month_number"]
facecream = df["facecream"]
toothpaste = df["toothpaste"]
shampoo = df["shampoo"]

# plot the data to the line chart
plot_line_chart(months, facecream, "Face Cream")
plot_line_chart(months, toothpaste, "Toothpaste")
plot_line_chart(months, shampoo, "Shampoo")
