class Student:
	"""docstring for ClassName"""
	def __init__(self, name, age):
		print('Name: ', name,'\n''Age: ', age)
	def __str__ (self):
		return ("..........................")
	def __del__(self):
		print("destroyed")
dung = Student("Van Dung", 20)
print(dung)