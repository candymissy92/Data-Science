import numpy as np

a = np.array([[1, 2, 3]])       # shape (1, 3)
b = np.array([[10],
              [20],
              [30]])            # shape (3, 1)

result = a - b
print(result)
print("Shape:", result.shape)
