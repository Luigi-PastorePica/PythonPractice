# Problem taken from Pathrise backtracking workshop.
# This is a hybrid between a subset and a permutations problem
# - The valid answers have fixed length (permutations)
# - Each step chooses to add an element to the partial solution among a set of possible elements (permutations).
# - However, each step has the same branching factor (subset).

# from collections.abc import Collection
from typing import List, Set

class BalancedStringGenerator():
    def __init__(self, opening: str, closing: str):
        if len(opening) != 1 or len(closing) != 1:
            raise ValueError("BalancedStringGenerator can only handle single character opening and closing, e.g. '(' and ')' or 'a' and 'z'")
        self.opening, self.closing = opening, closing
        self.permutations = 0

    def find_balanced(self, pairs: int) -> Set[str]:
        root = ""
        solutions = set()
        self.backtracking(root, pairs, solutions)
        return solutions

    def backtracking(self, partial: str, pairs: int, solutions: Set[str]) -> None:
        if pairs == 0:
            raise (ValueError, "`pairs` must be greater than 0.")
        # missing pruning
        if len(partial) == (pairs * 2):
            self.permutations += 1
            if self.is_balanced(partial):
                solutions.add(partial)
            return
        self.backtracking(partial + self.opening, pairs, solutions)
        self.backtracking(partial + self.closing, pairs, solutions)

    def is_balanced(self, partial: str) -> bool:
        open_count = 0
        for char in partial:
            if char == '(':
                open_count += 1
            elif char == ')':
                open_count -= 1
            if open_count < 0:
                return False

        if open_count != 0:
            return False

        return True



def main():
    pairs = 10
    opening = '('
    closing = ')'
    bsg = BalancedStringGenerator(opening, closing)
    balanced_pairs = bsg.find_balanced(pairs)
    print(f"Result = {balanced_pairs}")
    print(f"Result count = {len(balanced_pairs)}")
    print(f"Possible permutations = {bsg.permutations}")

if __name__ == "__main__":
    main()