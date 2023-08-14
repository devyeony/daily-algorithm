# https://leetcode.com/problems/single-number/
import operator
from functools import reduce
from typing import List


# first trial
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        answer: int = 0
        dic: dict = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for k, v in dic.items():
            if v == 1:
                answer = k
                break

        return answer


# second trial
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)


nums1: List[int] = [2, 2, 1]
nums2: List[int] = [4, 1, 2, 1, 2]
nums3: List[int] = [1]
sol: Solution2 = Solution2()
print(sol.singleNumber(nums1))
print(sol.singleNumber(nums2))
print(sol.singleNumber(nums3))
