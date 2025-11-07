from typing import List

def recursive(partial: List, idx: int, original: List):
    if idx == len(original):
        return

    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    partial.append(original[idx])
    recursive(partial, idx + 1, original)
    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # So each instance of partial points to the same object at every level of recursion, that is why it takes little space.
    # That also means we have to be careful to remove elements when coming back into the parent level

def recursive2(partial: List, idx: int, original: List):
    if idx == len(original):
        return

    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # partial.append(original[idx])
    recursive(partial + [original[idx]], idx + 1, original)
    print(f"idx={idx} partial={partial} partial_obj={hex(id(partial))}")
    # So each instance of partial points to the same object at every level of recursion, that is why it takes little space.
    # That also means we have to be careful to remove elements when coming back into the parent level


def main():
    original = [1, 2, 3]
    partial = []
    recursive2(partial, 0, original)

if __name__ == "__main__":
    main()