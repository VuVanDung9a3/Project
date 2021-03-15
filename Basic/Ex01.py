def countChar (*data) :
	dic = {}
	for item in data:
		for i in item:
			if i in dic:
				dic[i] = dic[i] + 1
			else :
				dic[i] = 1
	return dic
t = countChar('Vu Van Dung', 'Do Ngoc Tien', 'Tran Van Tuan')
print(t)
