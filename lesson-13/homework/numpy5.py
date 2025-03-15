from numpy import random
import numpy as np

matrix = random.randint(random.randint(100), size = (10,10))
matrix_max = np.max(matrix)
matrix_min = np.min(matrix)



print(f"Maximum value in the matrix is {matrix_max}")
print(f"Minimum value in the matrix is {matrix_min}")