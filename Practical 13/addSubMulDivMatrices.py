import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Addition
addition_result = np.add(matrix1, matrix2)
print("Addition result:")
print(addition_result)

# Subtraction
subtraction_result = np.subtract(matrix1, matrix2)
print("\nSubtraction result:")
print(subtraction_result)

# Multiplication
multiplication_result = np.multiply(matrix1, matrix2)
print("\nMultiplication result:")
print(multiplication_result)

division_result = np.divide(matrix1, matrix2)
print("\nDivision result:")
print(division_result)
