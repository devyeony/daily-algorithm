# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join(str(i) for i in digits)
        next_digits_str = str(int(digits_str) + 1)
        next_digits = list(map(int, list(next_digits_str)))
        return next_digits


digits1: List[int] = [1, 2, 3]
digits2: List[int] = [4, 3, 2, 1]
digits3: List[int] = [9]

sol = Solution()
print(sol.plusOne(digits1))
print(sol.plusOne(digits2))
print(sol.plusOne(digits3))
