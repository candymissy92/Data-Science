import numpy as np

np.random.seed(0) 
array2d = np.random.randint(10, 100, (3, 4))
filtered_vals = array2d[array2d > 50]

print("Array:\n", array2d)
print("Filtered (>50):", filtered_vals)
print("Max:", filtered_vals.max())
