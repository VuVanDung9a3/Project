import numpy as np
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = [8, 9, 1, 4]
arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)

print(type(arr1))
print(arr1)
sumArr = np.array([arr1, arr2, arr3])
print(sumArr)
print(sumArr.shape)
a1 = np.arange(10)
print(a1)
print(type(a1))