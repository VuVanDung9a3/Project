try:
	a = 1
	b = 0
	x = a/b
except ZeroDivisionError as error:
	print("loi: ", error)