import numpy as np  


nested_lst = [
    [1, 2, 3, 5, 9, 8],
    [4, 5, 6, 7, 8, 9]
]

new_arr = np.array(nested_lst)

print("6. new_arr[1, 0:4]     → Row 1, columns 0 to 3:", new_arr[1, 0:4])
print("7. new_arr[0:2, 1]     → Rows 0 and 1, column 1:", new_arr[0:2, 1])
print("8. new_arr[0:2, 1:4]   → Rows 0 and 1, columns 1 to 3:", new_arr[0:2, 1:4])
