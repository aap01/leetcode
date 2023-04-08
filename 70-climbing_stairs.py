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
    The solution is the permutation of 1s(repeatitive) and 2s(repeatitive) that sum upto n
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
