import numpy as np

# doing mathematical operations on array is just like performing calculcations on a matrix.

# BASIC MATHS OPERATIONS

l1 = [2, 4, 6, 8, 10]
l2 = [1, 3, 5, 7, 9]

arr1 = np.array(l1)
arr2 = np.array(l2)

print(l1 * 5) # this returns the list that is repeated five times.
print(arr1 * 5) # this returns an array with each number multilplied with five.

# print(l1 + 5) # same result for -, /, and //.
print(arr1 + 5) # same result for -, /, and //.

print(l1 + l2)
print(arr1 + arr2)

# print(l1 - l2)
print(arr1 - arr2)

# print(l1 / l2)
print(arr1 / arr2)

# print(l1 * l2)
print(arr1 * arr2)

# print(l1 // l2)
print(arr1 // arr2)

# BUILT IN MATHEMIATICAL FUNCTIONS

arr = np.array([[1, 2, 3, 4,],
                [5, 6, 7, 8]])

print(np.sqrt(arr))
print(np.sin(arr))
print(np.tan(arr))
print(np.cos(arr))