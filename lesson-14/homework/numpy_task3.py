import numpy as np


#Coefficent matrix A
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]]).astype(int)

#Constants the system Ax = b
b = np.array([7, 4, 5]).astype(int)

solution = np.linalg.solve(A, b)
print(solution)