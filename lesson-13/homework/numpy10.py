import numpy as np
from numpy import random

matrix = random.randint(100, size= (4,4))

transpose = np.transpose(matrix)
print(transpose)