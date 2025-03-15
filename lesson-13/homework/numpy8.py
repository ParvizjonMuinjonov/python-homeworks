import numpy as np
from numpy import random

matrix1 = random.randint(100, size = (5,3))
matrix2 = random.randint(100, size = (3,2))

mult_matrix = np.dot(matrix1, matrix2)

print(mult_matrix)