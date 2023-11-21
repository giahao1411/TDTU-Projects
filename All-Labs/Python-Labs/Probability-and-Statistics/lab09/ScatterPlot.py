import matplotlib.pyplot as plt
import numpy as np

girls_grades = np.random.randint(100, size=30)
boys_grades = np.random.randint(100, size=30)
grades_range = np.random.randint(100, size=30)

fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0, 0, 1, 1])

ax.scatter(grades_range, girls_grades, color="r")
ax.scatter(grades_range, boys_grades, color="b")
ax.set_xlabel("Grades Range")
ax.set_ylabel("Grades Scored")
ax.set_title("Scatter Plot")
plt.show()
