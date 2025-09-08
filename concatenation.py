import numpy as np

# CONCATENATION

# # 1d array:
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])

# print(arr1.dtype, arr2.dtype)
# concatenated = np.concatenate((arr1, arr2), dtype='float32')
# print(concatenated, concatenated.dtype)


# # 2d array:
# arr1 = np.array([[1, 2, 3, 4],
#                  [11, 12, 13, 14]])
# arr2 = np.array([[5, 6, 7, 8],
#                 [15, 16, 17, 18]])
                
# print(arr1.dtype, arr2.dtype)                
# concatenated_by_rows = np.concatenate((arr1, arr2), axis=0, dtype='int16')
# print(concatenated_by_rows, concatenated_by_rows.dtype)
# concatenated_by_columns = np.concatenate((arr1, arr2), axis=1)
# print(concatenated_by_columns, concatenated_by_columns.dtype)


# # 3d array:
# arr1 = np.array([[[1, 2, 3],
#                   [4, 5, 6]],
                  
#                   [[7, 8, 9],
#                    [10, 11, 12]]])
# arr2 = np.array([[[13, 14, 15],
#                   [16, 17, 18]],
                  
#                   [[19, 20, 21],
#                    [22, 23, 24]]])

# print(arr1.dtype, arr2.dtype)                
# concatenated_by_rows = np.concatenate((arr1, arr2), axis=0, dtype='int16')
# print(concatenated_by_rows, concatenated_by_rows.dtype)
# concatenated_by_columns = np.concatenate((arr1, arr2), axis=2)
# print(concatenated_by_columns, concatenated_by_columns.dtype)
