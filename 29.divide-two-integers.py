#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (17.04%)
# Likes:    2656
# Dislikes: 9292
# Total Accepted:    460.9K
# Total Submissions: 2.7M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
# 
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
# 
# Return the quotient after dividing dividend by divisor.
# 
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31
# - 1, and if the quotient is strictly less than -2^31, then return -2^31.
# 
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# 
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
# 
# 
#

# @lc code=start
from unittest import result


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # O(n) TLE
        # quotient = 0
        # sign = True
        # if dividend < 0:
        #     dividend = - dividend
        #     sign = not sign
        # if divisor < 0:
        #     divisor = - divisor
        #     sign = not sign
        # while dividend >= divisor:
        #     dividend -= divisor
        #     quotient += 1
        # return quotient if sign else - quotient
        result = 1 if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor > dividend:
            return 0
        d = divisor
        while 2 * d <= dividend:
            result *= 2
            d *= 2
        sign = 1
        if result < 0:
            sign = -sign
            result = -result
        subRes = self.divide(dividend=dividend - d, divisor=divisor)
        if sign > 0:
            return min(2147483647, result + subRes)
        else:
            return max(-2147483648, sign * (result + subRes))
        
        
# @lc code=end

