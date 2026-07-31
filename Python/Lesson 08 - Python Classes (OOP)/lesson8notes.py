class Pet():
	def __init__(self, pet_name, age=0):
		self.name = pet_name
		self.years_old = age
	
	def meow(self):
		print(f'{self.name} meows')

# An object is an instance of a class

milo = Pet('Milo')
# milo.name
milo.meow()

rosie = Pet('Rosie', 7)
type(rosie)
rosie.meow()
print(rosie.name)
print(rosie.years_old)
rosie.years_old = 5
print(rosie.years_old)

def testfunc(namedpet: Pet):
	print(namedpet.name)

testfunc(rosie)