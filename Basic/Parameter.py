def sum(n1, n2, n3, *data, **l):
	t1 = t2 = t3 = 0
	t1 = n1 + n2 + n3
	for item in data:
		t2 = t2 + item
	for key, value in l.items():
		t3 = t3 +value
	t = [t1,t2,t3]
	return t
kq = sum(10,12,13,14,15,6,7,8,one = 25, two = 55, three = 77)
print(kq)