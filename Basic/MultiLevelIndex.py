import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

ind1 = "A A A B B B".split() #thay khoang trang bang dau ,
ind2 = "a b c a b c".split()
col1 = "C1 C1 C2 C3 C3".split()
col2 = "col1 col2 col3 col4 col5".split()
x = []
for i in range(30): #lay 30 phan tu
	x.append(np.random.randint(1,100))	#random tu 1->100, luu gia tri vao list x
x = np.array(x) #chuyen list thanh array
x = x.reshape(6,5) #chuyen thanh ma tran 6x5
df = DataFrame(x, index = [ind1, ind2], columns = [col1, col2])
print(df)
print(df.ix['A'])