import numpy as np

arr = np.array([12, 45, 67, 89, 34, 22, 90, 100])
filtered_arr = arr[(arr > 40) & (arr < 90)]
print("Filtered:", filtered_arr)
print("Mean:", filtered_arr.mean())
