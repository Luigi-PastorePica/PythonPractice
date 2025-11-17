"""
It is an anti-pattern to place a return, continue, or break in a `try` or `catch` block as well as in a `finally` block.
This is because the return, continue, or break statement in the finally overrides the corresponding statement in the
blocks.
Starting with Python 3.14, the code below will raise a SyntaxWarning

This example is taken from https://youtube.com/shorts/dXMS-uLQkYI?si=J5ynpsbgSKIl7Ypk
"""

from typing import List

def dont_use_return_in_finally(my_list: List, index: int):
	try:
		value = my_list[index]
		print("The index worked")
		return value * 100
	except IndexError:
		print("The index did not work")
	finally:
		return True

def main():
	my_list = [1, 2, 3]
	index1 = 1
	index2 = 4

	print(dont_use_return_in_finally(my_list, index1))

	print(dont_use_return_in_finally(my_list, index2))

if __name__  == "__main__":
	main()