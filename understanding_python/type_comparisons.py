"""

"""

# Taken from an Indently.io video, but I don't remember which.
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

# Taken from https://youtu.be/ankki-yKgSc?si=8ndeZf7EV6nXv6Qf
# `is` compares object ids, while `==` compares value

var_a: str = "bob"
var_b: str = "bob"

print(f'{id(var_a)=}') # 1234567890
print(f'{id(var_b)=}') # 1234567890

print(var_a is var_b) # True* # Sometimes but not guaranteed
print(var_a == var_b) # True

var_a: str = "bob"
var_b: str = "bob".lower()

print(f'{id(var_a)=}') # 1234567890
print(f'{id(var_b)=}') # Could be the same or different, no guarantee

print(var_a is var_b) # Likely False but could be True, no guarantee
print(var_a == var_b) # True