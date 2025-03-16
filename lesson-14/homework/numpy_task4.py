import numpy as np


#Coefficent matrix A
A = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]]).astype(int)

#Constants the system Ax = b
b = np.array([12, -5, 15]).astype(int)

solution = np.linalg.solve(A, b)
print(solution)