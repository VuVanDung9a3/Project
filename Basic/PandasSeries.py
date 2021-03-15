import numpy as np
from pandas import Series
import pandas as pd
from numpy.random import randn

S1 = Series([10, 20, 30, 40], index=["A", "B", "C", "D"])
diem = [7, 8, 9, 10 ,11]	#gia tri
ten =  ["Tuan", "Tien", "Khiem", 'Dung', 'Long']	#index
S2 = Series(diem, index = ten)
S2.name = "Danh sach diem"
S3 = S2.index	#lay ra index
S4 = S3.values	#lay gia tri
l = list(range(1,4))
s1 = ['A', 'B', 'C']
s2 = ['A', 'B', 'C', 'D', 'E']
S5 = Series(l, index = s1)
S6 = S5.reindex(s2, fill_value = 0)		#lay gia tri cua S5, neu khong co gia tri cho bang 0
print(S1,'\n',S2,'\n',S3,'\n',S4)
print(S5)
print(S6)
print(type(S1))
