import numpy as np

data = np.array([120, 56, 89, 45, 38, 99, 140, 110])
filtered_data = data[data < 100]
print("Filtered:", filtered_data)
print("Min:", filtered_data.min())
