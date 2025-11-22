"""
Using the enumerate() function
"""

# Taken from https://youtu.be/ankki-yKgSc?si=U_KwC2EpoD6o3QOy
# Do not add 1 to index returned by enumerate. enumerate has a kwarg that denotes what the first index should be.

print("Adding to index")
for idx, value in enumerate(["A", "B", "C", "D"]):
	print(f"{idx + 1}: {value}") # Unnecessary

print("\nStarting index at 1")
for idx, value in enumerate(["A", "B", "C", "D"], start=1):
	print(f"{idx}: {value}")

print("\nStarting at arbitrary index")
for idx, value in enumerate(["A", "B", "C", "D"], start=-3):
	print(f"{idx}: {value}")
