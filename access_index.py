"""
Accessing NumPy Array elements by index

Individual NumPy Array elements can be accessed by index, using syntax identical to Python lists: array[index] for a single element, or array[start:end] for a slice, where start and end are the starting and ending indexes for the slice.

Nested Arrays or elements can be accessed by adding additional comma-separated parameters.

"""

import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matrix[0,0])

print(matrix[1,:])

