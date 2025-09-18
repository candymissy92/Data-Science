import numpy as np  


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = np.array(lst)

print("1. result[1:8] → Elements from index 1 to 7:", result[1:8])
print("2. result[1:]  → Elements from index 1 to end:", result[1:])
print("3. result[:1]  → Elements from start to index 0:", result[:1])
