"""
NumPy element-wise arithmetic operations

NumPy Arrays support element-wise operations, meaning that arithmetic operations on arrays are applied to each value in the array.

Multiple arrays can also be used in arithmetic operations, provided that they have the same lengths.

"""
import numpy as np

odds = np.array([1,3,5,7,9])
evens = odds + 1
print(evens)


array1 = np.array([1,2,3])
array2 = np.array([4,3,2])
new_array = array1 + array2
print(new_array)





