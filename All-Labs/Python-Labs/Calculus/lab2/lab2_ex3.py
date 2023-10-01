import numpy as np

centigrade = np.array([0, 12, 56, 48, 45.5, 99.9])
C = np.array(centigrade)

print("Values in Centigrade degrees:")
print(C)
print("Values in Fahrenheit degrees:")
print(np.round((9*C/5 + 32), 2))
