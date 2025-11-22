"""
If you assign a variable pointing to a list to another variable, you only have two variables referencing the same list
object.

Example 1

a --> [1, 2, 3] <-- b
"""

a = [1, 2, 3]
b = a

b.append(4)

print("Example 1")
print(f"{b=}") # b=[1, 2, 3, 4]
print(f"{a=}") # a=[1, 2, 3, 4]
print(f"{id(b)=}") # Same as a's
print(f"{id(a)=}") # Same as b's

"""
If you use copy to assign a copy of the list object to another variable, then you get two distinct list objects where 
each of the list's elements points to the same element objects as the original. If we alter one of the list objects, 
then the other list object remains untouched.

To be a bit more precise, using copy creates a new list object with new pointers for each element. These pointers could
could point to the same objects that the original list points to, or to other objects.

Example 2

     a
     | 
  ⌄  ⌄  ⌄ 
 [1, 2, 3] 4
  ^  ^  ^  ^ 
     |
     b
     
Example 3

		 a
		 | 
	  ⌄  ⌄  ⌄ 
  11 [1, 2, 3] 4
  ^      ^  ^  ^ 
     |
     b
     
"""
a = [1, 2, 3]
b = a.copy()

b.append(4)

print("\nExample 2")
print(f"{b=}") # b=[1, 2, 3, 4]
print(f"{a=}") # a=[1, 2, 3]
print(f"{id(b)=}") # Different from a's
print(f"{id(a)=}") # Different from b's

b[0] = 11

print("\nExample 3")
print(f"{b=}") # b=[11, 2, 3, 4]
print(f"{a=}") # a=[1, 2, 3]


"""
However, if the underlying element's object is mutable and we modify it via one of the list objects, that will also be 
visible in the other list object. In this case, we'll need to perform a deepcopy. A deepcopy copies every single element.

Example 4

		 a
		 | 
	  ⌄      ⌄      ⌄ 
  11 [1, ["A", "B"] 3]
  ^          ^      ^ 
             |
             b

Example 5

         a                       b
         |                       |
  ⌄      ⌄       ⌄        ⌄      ⌄       ⌄ 
 [1, ["A", "B"], 3]      [1, ["A", "B"], 3]
"""

from copy import deepcopy

a = [1, ["A", "B"], 3]
b = a.copy()

b[1][1] = "C"

print("\nExample 4")
print(f"{b=}") # [1, ["A", "C"], 3]
print(f"{a=}")  # [1, ["A", "C"], 3] # a gets modified too!
print(f"{id(b)=}") # Different from a's
print(f"{id(a)=}") # Different from b's
print(f"{id(b[0])=} {id(b[1])=} {id(b[2])=}")
print(f"{id(a[0])=} {id(a[1])=} {id(a[2])=}")


a = [1, ["A", "B"], 3]
b = deepcopy(a)

b[1][1] = "C"

print("\nExample 5")
print(f"{b=}") # [1, ["A", "C"], 3]
print(f"{a=}")  # [1, ["A", "B"], 3] # a does not get modified!
print(f"{id(b)=}") # Different from a's
print(f"{id(a)=}") # Different from b's
print(f"{id(b[0])=} {id(b[1])=} {id(b[2])=}")
print(f"{id(a[0])=} {id(a[1])=} {id(a[2])=}")
# Notice that a[1] is a different object from b[1]. However, a[0] == b[0] and a[2] == b[2] because the underlying objects are immutable.
