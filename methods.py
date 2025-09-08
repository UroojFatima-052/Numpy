import numpy as np

# # APPEND METHOD -> add new values at the end of the array.

# # 1d array 
# arr =  np.array([1, 2, 3, 4])
# print(arr.size)
# print(np.append(arr, [5, 6, 7, 8])) # returns the copy of array
# print(arr.size)

# # 2d array 
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8]])

# print(np.append(arr, [9, 10, 11, 12]))
# # when axis = 0 -> append rows, the shape must match along all axes except axis = 0 

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8]])

# print(np.append(arr, [[9, 10, 11, 12] , [13, 14, 15, 16]], axis=0))

# # when axis = 1 -> append columns, the shape must match along all axes except axis = 1 

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8]])
# print(np.append(arr, [[12, 16], [13, 15]], axis=1))

# # 3d array 
# arr = np.array([[[1, 2, 3]],
#                  [[4, 5, 6]],
#                  [[7, 8, 9]]])

# print(np.append(arr, [10, 11]))

# # when axis = 0 -> append rows, the shape must match along all axes except axis = 0 
# arr = np.array([[[1, 2, 3]],
#                  [[4, 5, 6]],
#                  [[7, 8, 9]]])

# print(np.append(arr, [[[10, 11, 12]]], axis=0))

# # when axis = 1 -> append columns, the shape must match along all axes except axis = 1
# arr = np.array([[[1, 2, 3]],
#                  [[4, 5, 6]],
#                  [[7, 8, 9]]])

# print(np.append(arr, [[[10, 10, 10]], [[12, 12, 12]], [[13, 13, 13]]], axis=1))



# # INSERT METHOD -> add new values at the specific index. (array's name, index, values)

# # 1d array
# arr = np.array(['a', 'b', 'c', ' d'])
# print(arr.size)
# print(np.insert(arr, 2, ['u', 'r', 'o', 'o', 'j'])) # returns the copy of array
# print(arr.size)

# # 2d array
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# print(np.insert(arr, 2, 55)) # flattens the array

# # when axis = 0 -> insert rows, the shape must match along all axes except axis = 0 
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# print(np.insert(arr, 1, [55], axis=0))
# print(np.insert(arr, 3, [10, 11, 12], axis=0))

# # when axis = 1 -> insert columns, the shape must match along all axes except axis = 1
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# print(np.insert(arr, 2, [55, 56, 57], axis=1)) # insert before column index 2 along axis=1 for all rows
# print(np.insert(arr, [2], [55, 56, 57], axis=1)) # Insert before column index 2 for each row separately.

# # 3d array 

# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]]])

# print(np.insert(arr, 2, 78))

# # when axis = 0 -> insert rows
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]]])

# print(np.insert(arr, 3, [78, 67, 90], axis=0))

# # when axis = 1 -> insert columns
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]]])

# print(np.insert(arr, 1, [[[78, 67, 90]], [[12, 13, 14]], [[34, 45, 56]], [[70, 90, 80]]], axis=1))



# # DELETE METHOD -> delete the element from the index given (array, index or slice, axis(optional))

# # 1d array
# arr = np.array([1, 2, 3, 4])
# print(arr.size)
# print(np.delete(arr, 3)) # returns the copy of array 
# print(arr.size)

# # 2d array

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])

# print(np.delete(arr, 6)) 

# # when axis = 0 -> delete rows
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])

# print(np.delete(arr, 0, axis=0)) 

# # when axis = 1 -> delete columns
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])

# print(np.delete(arr, 2, axis=1)) 

# # 3d array
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]],
#                 [[13, 14, 15]]])

# print(np.delete(arr, 10))

# # when axis = 0 -> delete rows
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]],
#                 [[13, 14, 15]]])

# print(np.delete(arr, 4, axis=0))

# # when axis = 1 -> delete columns
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]],
#                 [[13, 14, 15]]])

# print(np.delete(arr, 0, axis=1)) # 0 is the only valid index here.

# arr = np.array([[[1, 2, 3],
#                 [4, 5, 6]],

#                 [[7, 8, 9],
#                 [10, 11, 12]]])
# print(arr)
# print(np.delete(arr, 1, axis=1))

# # when axis = 2 -> delete elements inside each column.
# arr = np.array([[[1, 2, 3]],
#                 [[4, 5, 6]],
#                 [[7, 8, 9]],
#                 [[10, 11, 12]],
#                 [[13, 14, 15]]])

# print(np.delete(arr, 1, axis=2))