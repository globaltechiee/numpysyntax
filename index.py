"""NumPy elements can be indexed using conditionals. The syntax to filter an array using a conditional is array_name[conditional].

The returned array will contain only the elements for which the conditional evaluates to True.
"""

import numpy as np

numbers = np.array([-5,4,0,2,3])
positives = numbers[numbers > 0]
print(positives)