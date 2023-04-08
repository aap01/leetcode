# Climbing Stairs
#
# [Easy] [AC:52.2% 2.3M of 4.4M] [filetype:python3]
#
# You are climbing a staircase. It takes n steps to reach the
# top.
#
# Each time you can either climb 1 or 2 steps. In how many
# distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
#
# Output: 2
#
# Explanation: There are two ways to climb to the top.
#
# 1. 1 step + 1 step
#
# 2. 2 steps
#
# Example 2:
#
# Input: n = 3
#
# Output: 3
#
# Explanation: There are three ways to climb to the top.
#
# 1. 1 step + 1 step + 1 step
#
# 2. 1 step + 2 steps
#
# 3. 2 steps + 1 step
#
# Constraints:
#
# 1 <= n <= 45
#
# [End of Description]:


class Solution:
    def factorial(
        self,
        number: int,
    ) -> int:
        if number == 0:
            return 1
        return number * self.factorial(number - 1)

    def waysFor(
        self,
        oneCount: int,
        twoCount: int,
    ) -> int:
        return self.factorial(oneCount + twoCount) // (
            self.factorial(oneCount) * self.factorial(twoCount)
        )

    """
    The solution is the permutation of 1s(repetitive) and
    2s(repetitive) that sum upto n
    """

    def climbStairs(
        self,
        n: int,
    ) -> int:
        oneCount = n
        twoCount = 0
        ways = 0
        while oneCount >= 0:
            ways += self.waysFor(
                oneCount=oneCount,
                twoCount=twoCount,
            )
            twoCount = twoCount + 1
            oneCount = oneCount - 2
        return ways
