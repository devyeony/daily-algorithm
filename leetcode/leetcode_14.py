# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer: str = ""
        str_min_len: int = min(list(len(s) for s in strs))
        for i in range(0, str_min_len):
            prefix: str = strs[0][i]
            is_going_on: bool = True
            for j in range(0, len(strs)):
                if prefix != strs[j][i]:
                    is_going_on = False
                    break
                if j == len(strs) - 1:
                    answer += prefix
            if not is_going_on:
                break
        return answer


strs1: List[str] = ["flower", "flow", "flight"]
strs2: List[str] = ["dog", "racecar", "car"]

sol = Solution()
print(sol.longestCommonPrefix(strs1))
print(sol.longestCommonPrefix(strs2))
