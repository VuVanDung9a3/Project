import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

diem = [4, 6, 8, 10]
sinhVien = ['A', 'B', 'C', 'D']
data = {"Sinh vien":sinhVien, "Diem":diem}
df1 = DataFrame(data)
ind = "A B C D E F".split() #thay khoang trang bang dau ,
col = "col1 col2 col3 col4 col5 col6".split()
x = []
for i in range(36): #lay 36 phan tu
	x.append(np.random.randint(1,100))	#random tu 1->100, luu gia tri vao list x
x = np.array(x) #chuyen list thanh array
x = x.reshape(6,6) #chuyen thanh ma tran 6x6
df2 = DataFrame(x, index = ind, columns = col) #chuyen thanh DataFrame
ind1 = "A B C D E F G H I".split()
col1 = "col1 col2 col3 col4 col5 col6 col7 col8".split()
df3 = df2.reindex(ind1, fill_value = 0)		#them dong
df4 = df3.reindex(columns = col1, fill_value = 0)	#them cot


print(data,'\n',type(data))
print(df1,'\n')
print(x,'\n')
print(df2,'\n')
print(df3,'\n')
print(df4)
