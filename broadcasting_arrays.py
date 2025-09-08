import numpy as np

# for broadcasting two numpy arrays:
# their dimensions must match 
# OR 
# either of their dimension has 1

# ALWAYS READ THE DIMENSIONS FROM LEFT SIDE

arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2) # a new 4x4 array
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr1 // arr2)

# MULTIPLICATION TABLE

arr1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)

