import numpy as np

matrix = np.array([[23, 45, 67],
                   [89, 12, 34],
                   [56, 78, 90]])
evens = matrix[matrix % 2 == 0]
print("Evens:", evens)
print("Max:", evens.max())
print("Min:", evens.min())
