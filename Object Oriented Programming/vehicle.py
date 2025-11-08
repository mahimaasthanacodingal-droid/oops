# create class
class Vehicle:

	# create init method
    def __init__(self,name, max_speed, mileage):

		# bind the arguments
        self.name= name
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle("BMW",240, 10)
modelY = Vehicle("Audi",250, 11)

# access the variables inside init method
print("Model Name: ", modelX.name)
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)
print("Model Name: ", modelY.name)
print("Model Max Speed:",modelY.max_speed)
print("Model Mileage:", modelY.mileage)