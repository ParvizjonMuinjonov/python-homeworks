import numpy as np
from numpy import random

matrix = random.randint(100, size = (5,5))

row_wise = np.sum(matrix, axis= 1)  #Row-wise sum

col_wise = np.sum(matrix, axis=0) #Column-wise sum
print("*" * 20)
print(f"Matrix: {matrix}")
print("*" * 20)
print(f"Its Row-wise sum: {row_wise}")
print("*" * 20)
print(f"Its Column-wise sum: {col_wise}")
print("*" * 20)