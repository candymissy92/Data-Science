
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


column_sum = [matrix[0][i] + matrix[1][i] for i in range(len(matrix[0]))]


print("Matrix:")
for row in matrix:
    print(row)


print("\nSum of each element (column-wise):", column_sum)










