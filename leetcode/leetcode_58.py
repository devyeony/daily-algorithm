# https://leetcode.com/problems/length-of-last-word/
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s1: str = "Hello World"
s2: str = "   fly me   to   the moon  "
s3: str = "luffy is still joyboy"

sol: Solution = Solution()
print(sol.lengthOfLastWord(s1))
print(sol.lengthOfLastWord(s2))
print(sol.lengthOfLastWord(s3))
