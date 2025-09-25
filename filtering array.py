import numpy as np
array=np.array([[50,60,40,89,90],
                [89,78,56,75,99]])
marks=array[array > 40]
print(marks)
updated_marks = [(array < 40)]
print(updated_marks)
