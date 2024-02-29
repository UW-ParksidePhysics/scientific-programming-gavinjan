import numpy as np


matrix = np.array([[2, 3], [7, 11]])
vector = np.array([[5], [13]])

print(f'A = {matrix}')

determinant = np.linalg.det(matrix)
print(f'Determinant of A = {determinant}')
inverse = np.linalg.inv(matrix)
print(f'Inverse of A = {inverse}')

solution = np.dot(inverse, vector)
print(f'Solution of Ax = b is x = {solution}')

fast_solution = np.linalg.solve(matrix, vector)
print(f'Solution of Ax = b is x = {fast_solution}')
