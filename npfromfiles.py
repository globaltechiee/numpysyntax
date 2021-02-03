"""
Creating NumPy Arrays from files

NumPy Arrays can be created from data in CSV files or other delimited text by using the np.genfromtxt() method.

The named parameter delimiter is used to determine the delimiting character between values.

"""
import numpy as np

import_csv = np.genfromtxt("filename.txt", delimiter=",")
# This is example need to create a file