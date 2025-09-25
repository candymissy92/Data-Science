import numpy as np

arr = np.array([12, 45, 60, 75, 30, 95, 100, 20])
filtered_outside = arr[(arr < 40) | (arr > 90)]
print("Filtered:", filtered_outside)
print("Sum:", filtered_outside.sum())
print("Count:", filtered_outside.size)
