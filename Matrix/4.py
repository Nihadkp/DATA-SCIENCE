import numpy as np
matrix = np.array([[6,3,9],[4,7,5],[6,3,9]])
column,row = matrix.shape
print("sum of diagonals:",sum(np.diag(matrix)))
# sum=0
# for i in range(row):
#     for j in range(column):
#         if i==j:
#             sum = sum + matrix[i][j]
# print("sum of diagonals:",sum)
