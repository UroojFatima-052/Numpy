import numpy as np

# SPLITTING -> Split an array into multiple sub-arrays
# np.hsplit → horizontal split (axis=1 for 2D, axis=0 for 1D)
# np.vsplit → vertical split (axis=0 for 2D)
# np.dsplit → depth split (axis=2 for 3D)


# # 1d array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.split(arr, 2, axis=0))
print(np.hsplit(arr, 2))
print(np.split(arr, 4))
print(np.split(arr, 8))


# 2d array

arr = np.array([[1, 2, 3, 4, 5, 10],
                [6, 7, 8, 9, 12, 13]])

print(np.split(arr, 2, axis=0))
print(np.split(arr, 3, axis=1))
            # OR
print(np.hsplit(arr, 3)) # axis = 1
print(np.vsplit(arr, 2)) # axis = 0

# 3d array

arr = np.array([[[1, 2, 3, 4],
                 [5, 6, 7, 8]],
                 
                 [[9, 10, 11, 12],
                  [13, 14, 15, 16]],
                  
                  [[17, 18, 19, 20],
                   [21, 22, 23, 24]]])

print(np.split(arr, 3, axis=0)) # split layers.
print(np.split(arr, 2, axis=1)) # split rows in each layer.
print(np.split(arr, 2, axis=2)) # split columns.
print(np.split(arr, 4, axis=2)) # split columns.
            # OR
print(np.vsplit(arr, 3)) # split layers.
print(np.hsplit(arr, 2)) # split rows in each layer.
print(np.dsplit(arr, 2)) # split columns.