import numpy as np
from numpy import random

matrix1 = random.randint(100, size = (3,3))
matrix2 = matrix1[:, 0]
dot_product = np.dot(matrix1, matrix2)
print(dot_product)