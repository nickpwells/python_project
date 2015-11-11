class Vehicle:

	def __init__(self, name, color):
		self.__name = name
		self.__color = color

	def getColor(self):
		return self.__color

	def setColor(self, color):
		self.__color = color

	def getName(self):
		return self.__name

class Car(Vehicle):

	def __init__(self, name, color, model):
		#call parent constructer to set name and color
		super().__init__(name, color)
		self.__model = model

	def getDescription(self):
		return self.getName() + self.__model + " in " + self.getColor() + " color"

#in method getDescription we are able to call getName and getColor because they are
# accessible to child class through inheritence

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())
