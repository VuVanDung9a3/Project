class Person:
	"""docstring for Person"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def info(self):
		print('Name: ', self.name,'\n''Age: ',self.age)
class Student(Person):
	"""docstring for Student"""
	def __init__(self, name, age, id):
		Person.__init__(self,name,age)
		self.id = id
	def infoS(self):
		print('Id: ', self.id)

s = Student('Vu Van', 20, 'IT1111')
s.info()
s.infoS()
		