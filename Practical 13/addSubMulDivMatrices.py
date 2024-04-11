import numpy as np

# Creating two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Performing operations
addition = np.add(matrix1, matrix2)
subtraction = np.subtract(matrix1, matrix2)
multiplication = np.matmul(matrix1, matrix2)
# Division operation is not directly supported for matrices in numpy

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Addition:")
print(addition)
print("Subtraction:")
print(subtraction)
print("Multiplication:")
print(multiplication)
