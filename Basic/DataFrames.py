import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

df1 = pd.read_clipboard() #doc khung vua luu
df2 = DataFrame(np.arange(16).reshape(4,4), columns = "col1 col2 col3 col4".split(), index = list('ABCD'))
print(df1,'\n')
print(df1.columns,'\n')     #hien thi column
#print(df1.head(),'\n')		#5 row dau tien
print(df1[['col1', 'col3']])  #lay ra gia tri cot
print(df1[df1['col4'] > 50])	#lay gia tri col > 50
print(df1 > 50)					#kiem tra gia tri
print(df1.ix['A'])			#lay dong
print(df1.drop('B'))		#xoa dong
print(df1.drop('col3', axis = 1)) #xoa cot
print(df2)
print(df2.add(df1, fill_value = 0)) #phep cong 2 ma tran
print(df1.sum())			#tong moi cot
print(df1.sum(axis = 1))		#tong dong
print(df1.max())			#max cot
print(df1.idxmax())			#lay index de col max