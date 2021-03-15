import numpy as np
x = []
y = []
for i in range(10):
	x.append(np.random.randint(1,10))	#them vao list a
	y.append(np.random.randint(1,10))
a = np.array(x)		#chuyen thanh mang	
b = np.array(y)
tong = np.add(a,b)
maxAB = np.maximum(a,b) 	#lay ra phan tu lon hon giua 2 mang
minAB = np.minimum(a,b)		#lay ra phan tu nho hon giua 2 mang
canBacHai = np.sqrt(a)
binhPhuong = np.square(a) 
chia = np.divide(a,b)		#a/b
muAB = np.power(a,b)		#a^b
tangDan = a.sort()
uniqueA = np.unique(a)		#loai cac phan tu giong nhau
soSanh = np.greater(a,b)	#so sanh cac phan tu cua a > b
soSanh2 = np.equal(a,b)		#so sanh neu phan tu giong nhau tra lai True
print("1: ", a, '\n'"2: ", b, '\n'"3: ", tong, '\n'"4: ", maxAB, '\n'"5: ", minAB, '\n'"6:",canBacHai )
print("7: ", binhPhuong, '\n'"8: ", chia, '\n'"9: ", muAB)
print("10: ", tangDan, '\n'"11: ", uniqueA,'\n'"12: ", soSanh, '\n'"13: ",soSanh2)