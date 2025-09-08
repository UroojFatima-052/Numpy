import numpy as np


# # SHAPE & RESHAPE
# arr = np.array([1, 2, 3, 4, 5])
# print(arr.shape)
# print(arr.reshape(5, 1)) # doesn't change the original array
# print(arr)

# arr = np.array([[1, 2, 3, 10],
#                 [4, 5, 6, 11],
#                 [7, 8, 9, 12]])
# print(arr.shape)
# print(arr.reshape(6, 2))
# print(arr.reshape(3, 1, 4))
# print(arr)


# FLATTEN & RAVEL
# flatten -> flats the whole array and return the copy of original array 
# Ravel -> flats the whole array but make changes direct in original array

# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])

# print(arr.flatten())
# print(arr)

# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])

# print(arr.ravel())

# # HOW FLATTEN AND RAVEL WORKS:
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])
# flated_arr = arr.flatten()
# arr[1, 4] = 100
# print(flated_arr)
# print(arr)

# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])
# ravel_arr = arr.ravel()
# arr[1, 4] = 100
# print(ravel_arr)
# print(arr)

# # RESIZE -> makes changes in original array and returns a new array.
#             # If enlarging: New elements are filled with zeros.
#             # If shrinking: Extra elements are discarded.

# arr = np.array([[1, 2, 3, 4],
#                [5, 6, 7, 8]])
# print(arr.size)
# # arr.resize(4, 2)
# # arr.resize(4, 1)
# # arr.resize(3, 2)
# # arr.resize(5, 5)
# print(arr)


# # TRANSPOSE -> doesn't change the original array.

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])
# print(arr.transpose())
# print(arr.T)

# arr = np.array([[[1, 2, 3],
#                  [4, 5, 6]],
                 
#                  [[7, 8, 9],
#                   [10, 11, 12]]])

# print(arr)
# print(arr.transpose())
# print(arr.T)

