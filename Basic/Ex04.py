def giaiThua(n):
	if n<1:
		print("False")
		return
	elif n == 1:
		return 1
	else :
		return n * giaiThua(n-1)
kq = giaiThua(5)
print(kq)
def convert(n):
	if n>1:
		convert(n//2)
	print(n%2,end=" ")
convert(10)