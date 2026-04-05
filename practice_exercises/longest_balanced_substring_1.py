"""
Source id: 6 # Personal reference.
You are given a string s consisting of lowercase English letters.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.

Example 1:
Input: s = "abbac"
Output: 4
Explanation:
The longest balanced substring is "abba" because both distinct characters 'a' and
'b'
each appear exactly 2 times.

Example 2:
Input: s = "zzabccy"
Output: 4
Explanation:
The longest balanced substring is "zabc" because the distinct characters '2', 'a',
'b', and 'c' each appear exactly 1 time.

Example 3:
Input: s = "aba"
Output: 2
Explanation:
One of the longest balanced substrings is "ab" because both distinct characters 'a' and
'b' each appear exactly 1 time. Another longest balanced substring is "ba" .

Constraints:
• 1 <= s.length <= 1000
• s consists of lowercase English letters.
"""
from collections import defaultdict

from utilities.decorators import timer

# Solution 7 - N**2 Traversal
# Optimization of solution 6:
# - Counter DS is an array
# NVM, this is way slower than solutions 4, 5, and 6.
class Solution7:
    @timer
    def longestBalanced(self, s: str):
        n = len(s)
        current_longest = 1
        char_counter = [0] * (ord("z") + 1)

        for i in range(n):
            for j in range(i, n):
                char_counter[ord(s[j])] += 1
                substr_len = j - i + 1

                if not self.isBalanced(char_counter):
                    continue
                if substr_len <= current_longest:
                    continue
                current_longest = substr_len

            for idx in range(len(char_counter)):
                char_counter[idx] = 0

        return current_longest

    def isBalanced(self, char_counter):
        count_set = set(char_counter)
        count_set.discard(0)  # We will always have a 0
        if len(count_set) == 1:
            return True
        return False

# Solution 6 - N**2 Traversal
# Closer to the official solution
# Faster than any other solution I tried
# Optimization of solution 5:
# - defaultdict
# - count elements in counter value set
class Solution6:
    @timer
    def longestBalanced(self, s: str):
        n = len(s)
        current_longest = 1

        for i in range(n):
            char_counter = defaultdict(int)
            for j in range(i, n):
                char_counter[s[j]] += 1
                substr_len = j - i + 1
                # Guard clauses, with a continue or break seems justified in this circumstance
                if not self.isBalanced(char_counter):
                    continue
                if substr_len <= current_longest:
                    continue
                current_longest = substr_len
            for char in char_counter.keys():
                char_counter[char] = 0

        return current_longest

    def isBalanced(self, char_counter):
        if len(set(char_counter.values())) == 1:
            return True
        return False


# Solution 5 - N**2 Traversal
# The official solution uses an O(N**2) traversal
# This passes, but it's slow.
# Optimization of solution 4:
# - Just one counter and one string object.
# - Count only new char included in iteration.
class Solution5:
    @timer
    def longestBalanced(self, s: str):
        n = len(s)
        current_longest = 1
        char_counter = {chr(char_code): 0 for char_code in range(ord('a'), ord('z') + 1)}

        for i in range(n):
            for j in range(i, n):
                char_counter[s[j]] += 1
                substr_len = j - i + 1
                # Guard clauses, with a continue or break seems justified in this circumstance
                if not self.isBalanced(char_counter):
                    continue
                if substr_len <= current_longest:
                    continue
                current_longest = substr_len
            for char in char_counter.keys():
                char_counter[char] = 0

        return current_longest

    def isBalanced(self, char_counter):

        most_frequent = max(char_counter.values())
        for count in char_counter.values():
            if count > 0 and count != most_frequent:
                return False

        return True


# Solution 4 - N**2 Traversal
# The oficial solution uses an O(N**2) traversal
# This works for many cases but longer strings cause a timeout.
class Solution4:
    @timer
    def longestBalanced(self, s: str):
        n = len(s)
        current_longest = 1
        for i in range(n):
            for j in range(i, n):
                substring = s[i: j + 1]
                # Guard clauses, with a continue or break seems justified in this circumstance
                if not self.isBalanced(substring):
                    continue
                if len(substring) <= current_longest:
                    continue
                current_longest = len(substring)

        return current_longest

    def isBalanced(self, substring):
        counter = {chr(char_code): 0 for char_code in range(ord('a'), ord('z') + 1)}
        for char in substring:
            counter[char] += 1
        most_frequent = max(counter.values())
        for count in counter.values():
            if count > 0 and count != most_frequent:
                return False

        return True


# # Solution 3 - Two pointers I didnt even finish it, too complex
# class Solution3:
#     @timer
#     def longestBalanced(self, s: str) -> int:
#         l = 0
#         r = 0
#         max_len = 0
#         counter = self._get_counter(s)
#
#         while r < len(s):
#             if self._is_balanced(counter): # Needs optimization
#                 max_len = max(max_len, r - l + 1)
#                 pass
#
#     def _is_balanced(self, counter) -> bool:
#         pass
#
#     def _get_counter(self, s: str) -> dict[chr, int]:
#         counter = {chr(char_code): 0 for char_code in range(ord('a'), ord('z') + 1) }
#         for char in s:
#             counter.get(char) = counter.get(char, 0) + 1
#
#         return counter

# Solution 2 - Backtracking with DS optimization
class Solution2:
    @timer
    def longestBalanced(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        counter = self._get_counter(s)
        # print(counter)
        max_len = self._analyze_substring_recursively(s, l, r, counter)
        return max_len

    def _get_counter(self, s: string) -> list[int]:
        chars_in_alpha = ord('z') - ord('a') + 1
        counter = [0]*(chars_in_alpha)
        for char in s:
            counter[ord(char) - ord('a')] += 1
        return counter

    def _analyze_substring_recursively(self, s: str, start: int, end: int, counter: list, excluded_char: str = None):
        max_len: int = None

        # print(f"before {start=} {end=} {excluded_char=} {counter=}")

        if excluded_char:
            idx = ord(excluded_char) - ord('a')
            counter[idx] -= 1

        # print(f"during {start=} {end=} {excluded_char=} {counter=}")
        if end - start < 1:
            max_len = 1

        if self._is_balanced(counter):
            max_len = end - start + 1

        if not max_len:
            max_len_1 = self._analyze_substring_recursively(s, start, end - 1, counter, s[end])
            max_len_2 = self._analyze_substring_recursively(s, start + 1, end, counter, s[start])
            max_len = max(max_len_1, max_len_2)

        if excluded_char:
            counter[idx] += 1

        # print(f"after {start=} {end=} {excluded_char=} {counter=}")

        return max_len

    def _is_balanced(self, counter: list):

        expected = max(counter)
        for val in counter:
            if val != expected and val != 0:
                return False

        return True

# Solution 1 - Naive Backtracking - Too slow
class Solution1:
    @timer
    def longestBalanced(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        chars_in_alpha = ord('z') - ord('a') + 1
        counter = [0]*(chars_in_alpha)
        max_len = self._analyze_substring_recursively(s, l, r)
        return max_len

    def _analyze_substring_recursively(self, s: str, start: int, end: int):

        if end - start < 1:
            return 1

        if self._is_balanced(s, start, end):
            return end - start + 1

        max_len_1 = self._analyze_substring_recursively(s, start, end - 1)
        max_len_2 = self._analyze_substring_recursively(s, start + 1, end)

        return max(max_len_1, max_len_2)


    def _is_balanced(self, s: str, start: int, end: int):
        occurrences = {chr(char): 0 for char in range(ord('a'), ord('z') + 1)}
        idx = start

        while idx <= end:
            occurrences[s[idx]] += 1
            idx += 1

        expected = max(occurrences.values())
        for val in occurrences.values():
            if val != expected and val != 0:
                return False

        return True

if __name__ == "__main__":
    string = "aabbccddefgceeffggabdijjiji" # The string is balanced 27 total.
    string = string + "a" # The string is balanced up to the penultimate character, 27 total.
    # string = string*2 # The string is balanced, 54 characters.
    print(string)

    sol1 = Solution1()
    sol2 = Solution2()
    # sol3 = Solution3()
    sol4 = Solution4()
    sol5 = Solution5()
    sol6 = Solution6()
    sol7 = Solution7()
    print(sol1.longestBalanced(string))
    print(sol2.longestBalanced(string))
    # print(sol3.longestBalanced(string))
    print(sol4.longestBalanced(string))
    print(sol5.longestBalanced(string))
    print(sol6.longestBalanced(string))
    print(sol7.longestBalanced(string))