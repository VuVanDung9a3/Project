def tong (*data):
	kq = []
	for i in data:
		t = 0
		for n in i:
			t = t + n
		kq.append(t)
	return kq
ketqua = tong([1,2,3],[3,4,5],[5,2])
print('kq = ',ketqua)