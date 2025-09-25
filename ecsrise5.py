import numpy as np

array = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
filtered_elements = array[(array > 30) & (array < 80)]
print("Filtered:", filtered_elements)
print("Sum:", filtered_elements.sum())
