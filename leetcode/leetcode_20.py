# https://leetcode.com/problems/valid-parentheses/
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        opening: List[str] = list()

        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                opening.append(s[i])
            else:
                if len(opening) == 0:
                    return False

                prev = opening.pop()
                if (prev == '(' and s[i] == ')') or (prev == '[' and s[i] == ']') or (prev == '{' and s[i] == '}'):
                    continue
                else:
                    return False
        if len(opening) == 0:
            return True
        else:
            return False



s1: str = "()"
s2: str = "()[]{}"
s3: str = "(]"
sol: Solution = Solution()
print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))
