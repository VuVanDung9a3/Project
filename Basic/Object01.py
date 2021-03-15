class Car :
	fuel = "Xang"
	maxSpeed = 150
	def drive (self) :
		#print("Xe chay voi van toc: ", self.maxSpeed)
	def drive (self, maxSpeed) :
		print("xe chay voi van toc: ", maxSpeed)
c = Car()
c.drive(160)