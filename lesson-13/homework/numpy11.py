import numpy as np
from numpy import random

matrix = random.randint(100, size= (3, 3))

determinant = np.linalg.det(matrix)

print(determinant)