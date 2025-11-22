"""
While studying backtracking, I could not quite understand the statement that backtracking, despite being inefficient in
terms of time, it is quite efficient in terms of memory.

From my experiments, turns out the above is true IFF the partial answer object is mutable (e.g. list) and we pass in the
partial recursively and modify it within the recursive call. If we pass in an expression that returns a modified version
of the partial answer (e.g. partial + [original[1]]), then we are generating a new partial answer object on each
recursive call and the algorithm loses it's memory efficiency advantage.

Please note that if we take the first approach (the memory-efficient one), then we must take care than on return the object
is reversed to it\'s previous state. if not, the algorithm does not work correctly.
"""

from typing import List

def recursive(partial: List, idx: int, original: List):
    if idx == len(original):
        return

    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    partial.append(original[idx])
    recursive(partial, idx + 1, original)
    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # So each instance of `partial` points to the same object at every level of recursion, that is why it takes little
    # space. Because we use the append method on the same object on every call, we have to be careful to remove elements
    # when coming back into the parent level.

def recursive2(partial: List, idx: int, original: List):
    if idx == len(original):
        return

    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # partial.append(original[idx])
    recursive2(partial + [original[idx]], idx + 1, original)
    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # This approach now creates a new list for every call. Here, we need to be careful of the depth of the tree and the
    # space taken by each partial solution.

def main():
    original = [1, 2, 3]
    partial = []
    # recursive(partial, 0, original)
    recursive2(partial, 0, original)

if __name__ == "__main__":
    main()