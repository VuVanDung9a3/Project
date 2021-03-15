import numpy as np
from pandas import Series
import pandas as pd
from numpy.random import randn

diem = [7, 8, 9, 10 ,11]
name =  ["Tuan", "Tien", "Khiem", 'Dung', 'Long']
S1 = Series(diem, index = name)
S2 = Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])
S3 = Series([5, 6, 7, 8, 9], index = ['A', 'B', 'C', 'D', 'E'])
nhan = S1 * 2
tong = S2 + S3
ind = "a b c d e f g h i k".split() # tao list ind
x = []
for i in range(10):
	x.append(np.random.randint(1,50)) # tao list x 10 phan tu random gia tri tu 1-50
S4 = Series(x, index = ind) 		

print(S1,'\n',nhan)
print(S1[['Tuan', 'Dung']])
print(S1[S1 < 9])
print(tong)
print(S4)
