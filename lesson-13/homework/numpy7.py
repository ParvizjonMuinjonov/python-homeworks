import numpy as np
from numpy import random

matrix = random.randint(random.randint(100), size = (5,5))
normalize_matrix = matrix / np.linalg.norm(matrix)
print(normalize_matrix)