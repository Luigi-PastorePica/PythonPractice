"""
Taken from https://youtu.be/-RgtgHvdYP4?si=U1Q3Kel4UhxYM_op
"""

#As a separator. The interpreter will ignore the underscores, they are there as a visual aid to the developer only.
big_number = 1_000_000_000_000
print(big_number)

big_float = 1_000_000.000_001
print(big_float)

# As a marker for an unimportant variable.
stats: tuple[str, str, int] = ("Bob", "Programmer", 27)

name, _, age = stats

print(f"{name=}")
print(f"{age=}")
print(f"{_=}") # be careful, this is a valid variable.

# As a marker for an unimportant range
values: list[int] = [1, 2, 3, 4, 5, 6]
first, *_, last = values
print(f"{first=}") # Gives us 1
print(f"{last=}") # Gives us 2
print(f"{_=}") # Gives us [2, 3, 4, 5]
print(first, last, sep=", ") # A small trick with print

first, second, *_, last = values
print(f"{first=}") # Gives us 1
print(f"{second=}") # Gives us 2
print(f"{last=}") # Gives us 6
print(_) # Gives us [3, 4, 5]

first, *_ = values
print(f"{first=}") # Gives us 1
print(_) # Gives us [2, 3, 4, 5, 6]

# As a marker for unimportant values in a for loop
elements = [1, 2, 3]
for _ in elements:
	print("here I am")

print([print('yo') for _ in elements]) # Note that this line produces a list of size len(elements) filled with `None`

# Internal variables and name mangling
from uuid import uuid4, UUID
class Lamp:
	def __init__(self, brand: str) -> None:
		self.brand = brand
		self._id = uuid4()
		self.__hidden_id = uuid4()

	def get_id(self) -> UUID:
		return self._id

	def get_hidden_id(self) -> UUID:
		return self.__hidden_id

pam: Lamp = Lamp(brand="PAM")
# Both will work
print(f"{pam.get_id()=}")
print(f"{pam._id=}") # But a linter may complain about accessing a protected value.

print(f"{pam.get_hidden_id=}")
# print(f"{pam.__hidden_id=}") # This will result in an error.
print(f"{pam._Lamp__hidden_id=}") # This is the mangled name. A linter will likely not recognize it.

# Dunder methods
from typing import Self # Used to represent the current object's class as a type.

class CustomNumber:
	def __init__(self, value: int) -> None:
		self.value = value

	def __repr__(self) -> str:
		return f"CustomNumber(value={self.value})"

	def __str__(self) -> str:
		return f"{self.value}"

	def __add__(self, other: Self) -> Self:
		return CustomNumber(self.value + other.value)

	def __or__(self, other: Self) -> Self:
		return CustomNumber(self.value | other.value)

# Use reserved keywords for a different purpose... kind of
class_ = type
for_ = "bob"
in_ = CustomNumber(3)

# Wildcard/catch all
name = "bob"

match name:
	case "bob":
		print("recipient")
	case "alice":
		print("sender")
	case _:
		print("MIM")
