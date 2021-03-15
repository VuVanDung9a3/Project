import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
sum1 = arr + arr
tich = arr * 3
mu = arr ** 3
#Transpose
a = np.arange(30).reshape(6, 5) 	#ma tran 6x5
b = np.arange(15)
b1 = b[:10]
b1[:3] = 10

print("1:",sum1, '\n'"2: ", tich, '\n'"3: ", mu, '\n'"4: ", b, '\n'"5:", b1, '\n'"6: ", a)
print("7: ", a[1][1], '\n'"8: ", a[2:5,1:4], '\n'"tong mang b:", b.sum())