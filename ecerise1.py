import numpy as np

marks = np.array([45, 78, 23, 90, 67, 88, 34, 59])
filtered_marks = marks[marks > 50]
print("Filtered:", filtered_marks)
print("Sum:", filtered_marks.sum())
