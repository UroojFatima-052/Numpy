import numpy as np

# STACKING -> joins arrays along a new axis.
# The stacked array has one more dimension than the input arrays.
# Horizontal stack → concatenates arrays along existing axis
# Vertical stack → adds arrays as new rows.

# # 1d array
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])

# stacked = np.stack((arr1, arr2), axis=0)
# stacked = np.stack((arr1, arr2), axis=1)
# stacked = np.hstack((arr1, arr2))
# stacked = np.vstack((arr1, arr2))

# print(stacked)

# # 2d array
# arr1 = np.array([[1, 2, 3, 4],
#                  [11, 12, 13, 14]])
# arr2 = np.array([[5, 6, 7, 8],
#                 [15, 16, 17, 18]])

# # stacked = np.stack((arr1, arr2), axis=0)
# # stacked = np.stack((arr1, arr2), axis=1)
# # stacked = np.hstack((arr1, arr2))
# # stacked = np.vstack((arr1, arr2))

# print(stacked)

# # 3d array
# arr1 = np.array([[[1, 2, 3],
#                   [4, 5, 6]],
                  
#                   [[7, 8, 9],
#                    [10, 11, 12]]])
# arr2 = np.array([[[13, 14, 15],
#                   [16, 17, 18]],
                  
#                   [[19, 20, 21],
#                    [22, 23, 24]]])

# stacked = np.stack((arr1, arr2), axis=0)
# stacked = np.stack((arr1, arr2), axis=1)
# stacked = np.hstack((arr1, arr2))
# stacked = np.vstack((arr1, arr2))

# print(stacked)