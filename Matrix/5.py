import numpy as np
matrix1 = np.array([[6,3,9],[4,7,5],[6,3,9]])
matrix2 = np.array([[1,6,4],[8,2,4],[5,3,9]])

print("Matrix addition:\n",matrix1 + matrix2)
print("Matrix substraction:\n",matrix1 - matrix2)
print("Matrix multiplication:\n",np.matmul(matrix1, matrix2))
print("Matrix division:\n",np.divide(matrix1,matrix2))
