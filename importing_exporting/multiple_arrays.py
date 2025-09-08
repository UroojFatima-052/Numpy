import numpy as np

# SAVE & LOAD -> UNCOMPRESSED VERSION
# arr1 = np.arange(5)
# arr2 = np.ones((2, 3))
# arr3 = np.zeros((3, 2, 4))
# arr4 = np.empty((2, 2))
# arr5 = np.full((3, 3), 12)

# np.savez('uncompressed.npz', first=arr1, second=arr2, third=arr3, fourth=arr4, fifth=arr5)

# loaded = np.load('importing_exporting/uncompressed.npz')
# print(loaded['first'])
# print(loaded['fifth'])
# print(loaded['third'])



# SAVE & LOAD -> COMPRESSED VERSION
# arr1 = np.arange(5)
# arr2 = np.ones((2, 3))
# arr3 = np.zeros((3, 2, 4))
# arr4 = np.empty((2, 2))
# arr5 = np.full((3, 3), 12)

# np.savez('compressed.npz', first=arr1, second=arr2, third=arr3, fourth=arr4, fifth=arr5)

# loaded = np.load('importing_exporting/compressed.npz')
# print(loaded['first'])
# print(loaded['fifth'])
# print(loaded['third'])