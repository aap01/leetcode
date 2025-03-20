# @leet start
class Solution:

    def has_zero(self, num):
        return "0" in str(num)

    def getNoZeroIntegers(self, n: int) -> List[int]:

        for a in range(1, n):
            b = n - a
            if not self.has_zero(a) and not self.has_zero(b):
                return [a, b]


# @leet end

