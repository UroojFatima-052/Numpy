import numpy as np

# nan -> not a number -> can be used to fill empty data cells 

print(np.nan)
print(np.sqrt(-1))

x = np.sqrt(-1)
print(np.isnan(x))

# inf -> infinity -> can be used in place of infinite anwers

print(np.inf)
print(np.array([5]) / 0)

y = np.array([23]) / 0
print(np.isinf(y))