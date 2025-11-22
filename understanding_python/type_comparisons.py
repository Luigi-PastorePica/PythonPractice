class Animal:
	...

class Dog(Animal):
	...

# type() is strict, isinstance respects inheritance and is directional
print(type(Animal()))
print(type(Dog()))
print(type(Animal()) == type(Dog())) # False
print(isinstance(Dog(), Animal)) # True
print(isinstance(Animal(), Dog)) # False