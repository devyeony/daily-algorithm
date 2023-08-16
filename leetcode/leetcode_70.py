# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, next = 1, 1
        for i in range(1, n):
            temp = next
            next = prev + next
            prev = temp
        return next


num1: int = 2
num2: int = 3
sol: Solution = Solution()
print(sol.climbStairs(num1))
print(sol.climbStairs(num2))
