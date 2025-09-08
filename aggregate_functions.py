import numpy as np

# AGGREGATE FUNCTIONS/REDUCTION FUNCTIONS

arr = np.array([[[1, 2, 3, 4],
                 [5, 6, 7, 8]],
                 
                 [[9, 10, 11, 12],
                  [13, 14, 15, 16]],
                  
                  [[17, 18, 19, 20],
                   [21, 22, 23, 24]]])
# we can use nan and inf with most of the aggregate functions -> print(np.nan(aggregate_function)(arr))

print(arr)
print(np.isnan(arr))
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.nansum(arr))
print(np.prod(arr))
print(np.nanprod(arr))
print(np.min(arr))
print('Index of minimum: ', np.argmin(arr))
print(np.max(arr))
print('Index of maximum: ', np.argmax(arr))
print(np.median(arr))
print(np.mean(arr))
print(np.average(arr))
print(np.var(arr))
print(np.std(arr))
print(np.percentile(arr, q=12))
print(np.cumsum(arr))
print(np.cumprod(arr))
print(np.all(arr))
print(np.any(arr))


import numpy as np

data = [2, 4, 6, 8, 10, 12, 14, 59]

# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print(f'Q1 is: {q1}')
print(f'Q2 is {q2}')
print(F'Q3 is {q3}')

# InterQuartile Range
iqr = q3 - q1
print(f'InterQuartile Range is: {iqr}')
# Outliers

lower_range = q1 - 1.5 * iqr
upper_range = q3 + 1.5 * iqr

print(f'The outlier range is: {lower_range},{upper_range}')
for x in data:
    if x < lower_range or x > upper_range:
        print(f'The Outlier is: {x}')
