import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
filtered_not = arr[~(arr > 40)]
print("Filtered:", filtered_not)
print("Mean:", filtered_not.mean())
