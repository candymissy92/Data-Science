import numpy as np

scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
filtered_scores = scores[scores > 60]
print("Filtered:", filtered_scores)
print("Count:", filtered_scores.size)
print("Average:", filtered_scores.mean())
