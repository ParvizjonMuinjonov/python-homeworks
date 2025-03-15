import numpy as np
from numpy import random

matrix1 = random.randint(100, size = (3,3))
matrix2 = random.randint(100, size = (3, 1))


linear_system = np.linalg.solve(matrix1, matrix2)

print(linear_system)