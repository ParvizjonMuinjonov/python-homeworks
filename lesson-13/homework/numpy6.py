import numpy as np
from numpy import random

matrix = random.randint(30, size=(1,30), dtype=int)
matrix_sum = np.sum(matrix)

mean_value = matrix_sum / 30
print(f"{mean_value:.2f}")