import numpy as np
from numpy import random

matrix1 = random.randint(100, size = (3,4))
matrix2 = random.randint(100, size = (4,3))


dot_product = np.dot(matrix1, matrix2)

print(dot_product)