import numpy as np

matrix1 = np.arange(9).reshape(3,3)
matrix2 = np.arange(9).reshape(3,3)

dot_matrix = np.dot(matrix1, matrix2)

print(dot_matrix)