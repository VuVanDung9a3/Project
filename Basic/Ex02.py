def myRange (*thamso) :
	start = length = step = 0
	if (len(thamso) == 3):
		start = thamso[0]
		length = thamso[1]
		step = thamso[2]
	elif (len(thamso) == 2) :
		start = thamso[0]
		length = thamso[1]
		step = 1
	else :
		start = 0
		length = thamso[0]
		step = 1
	i = start
	while (i < length) :
		yield i
		i = i + step
l = myRange(0, 7, 2)
print(list(l))
