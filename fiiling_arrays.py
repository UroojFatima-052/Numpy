import numpy as np

# FILLING ARRAYS

# Full function -> Initalizes array with a specific value

arr = np.full((4, 4), 22)
print(arr)
print(arr.dtype)
arr = np.full((3, 3), 2, dtype='int32')
print(arr)
print(arr.dtype)


# Empty function -> Creates an array in the meomory with a default data type float if not specified. On printing shows the garbage value at that memory location.

arr = np.empty((2,2)) # dtype by default float
print(arr)
print(arr.dtype)
arr = np.empty((4, 6), dtype='int32')
print(arr)
print(arr.dtype)


# Ones funtion -> Creates an array of 1s.

arr = np.ones((4, 4))
print(arr)
print(arr.dtype)
arr = np.ones((2, 3), dtype='int32')
print(arr)
print(arr.dtype)


# Zeros function -> Creates an array of 0s.

arr = np.zeros((3, 2))
print(arr)
print(arr.dtype)
arr = np.zeros((3, 3), dtype='int64')
print(arr)
print(arr.dtype)

# Arange function -> (start, stop, step, dtype(optional))

arr = np.arange(12)
print(arr)
arr = np.arange(5, dtype='float32')
print(arr, arr.dtype)
arr = np.arange(1, 11, 2, dtype='int16')
print(arr, arr.dtype)