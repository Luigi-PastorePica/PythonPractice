"""
Strings are immutable. Every concatenation means creating a new string object, even if we are using the += syntactic
sugar to assign to the same variable.

Taken from https://youtu.be/ankki-yKgSc?si=U_KwC2EpoD6o3QOy
"""

from timeit import timeit

def append_text() -> str:
	text: str = ""
	for i in range(100):
		text += 'text'
	return text

def join_text() -> str:
	elements: list[str]= []
	for i in range(100):
		elements.append("text")
	return "".join(elements)


def main():
	# Concatenation results in a completely new object
	str_a = "Hello"
	str_b = "World"
	print(f"{id(str_a)=}")
	print(f"{id(str_b)=}")

	str_a += f" {str_b}"
	print(f"{id(str_a)=}") # This will give us a different id


	# Concatenation vs join efficiency
	print(f"Same result? {append_text() == join_text()}")
	warm_up: float = timeit(append_text)

	append_time: float = timeit(append_text)
	join_time: float = timeit(join_text)

	print(f"Warm up result: {warm_up:.5f}s") # Sample result: 2.36116s
	print(f"Append result: {append_time:.5f}s") # Sample result: 2.36533s
	print(f"Join result: {join_time:.5f}s") # Sample result: 2.13091s

if __name__ == "__main__":
	main()