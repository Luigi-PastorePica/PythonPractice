# You have a binary string s (a string consisting only of '0's and '1's).
# Count the number of non-empty substrings that comply with the following:
# 1. The substring's first half consists of only '1's or only '0's.
# 2. The substring's second half consists of the other character.
# Internal substrings also count.
# Example: s = "001100110"
# Valid substrings are "0011", "01", "1100", "10", "0011", "01", "10", a total of 7.
# 0 <= string length <= 10**5
# NOTE: I tried with backtracking but the recursion depth is too large. A different approach is needed.

# [0 0 0 1 1 0 0 1]
#  l r
#    f

import logging

logging.basicConfig(level=logging.DEBUG)

log = False

def counter(s: str) -> int:
    if len(s) < 2:
        return 0
    l = 0
    r = 1
    flip_at = None
    flip_back_at = None
    count = 0

    while r < len(s):
        # Find point of flip
        bit_at_l = s[l]
        bit_at_r = s[r]
        if bit_at_l == bit_at_r:
            flip_at = find_next_flip(s, r)
        flip_back_at = find_next_flip(s, flip_at)
        r = flip_back_at -1

        # [ 0 0 0 1 1 0 0 1 ]
        #   l     f r fb
        # [ 0 0 1 1 1 0 0 1 ]
        #   l   f   r fb

        if log: logging.debug(f'{flip_at - l} > {r - flip_at + 1}?')
        while flip_at - l > r - flip_at + 1:
            l += 1

        if log: logging.debug(f'{flip_at - l} < {r - flip_at + 1}?')
        while flip_at - l < r - flip_at + 1:
            r -= 1

        count += (r - l + 1) // 2
        if log: logging.debug(count)
        l = flip_at
        r = flip_back_at
        flip_at = flip_back_at

    return count

def find_next_flip(s: str, r: int) -> int:
    bit_val_r = s[r]
    while r < len(s) and bit_val_r == s[r]:
        r += 1
    return r

if __name__ == '__main__':
    import random

    string = "00011001" # 0011, 01, 1100, 10, 01; 5 in total
    string2 = "00111001" # 0011, 01, 1100, 10, 01; 5 in total
    very_long_bit_seq = "".join([random.choice(["0", "1"]) for _ in range(int(10e5))])
    print(counter(string))
    print(counter(string2))
    print(counter(very_long_bit_seq))
