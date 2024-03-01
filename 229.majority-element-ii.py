#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (42.12%)
# Likes:    4599
# Dislikes: 272
# Total Accepted:    278.4K
# Total Submissions: 661K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
#
#
# Example 1:
#
#
# Input: nums = [3,2,3]
# Output: [3]
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?
#
#


# @lc code=start
# from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        minRepeat = length // 3
        m1 = None
        c1 = 0
        m2 = None
        c2 = 0
        for ithNum in nums:
            if ithNum == m1:
                c1 += 1
            elif ithNum == m2:
                c2 += 1
            elif c1 == 0:
                m1 = ithNum
                c1 = 1
            elif c2 == 0:
                m2 = ithNum
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
            # print(f'{m1}:{c1}, {m2}:{c2}')

        c1 = 0
        c2 = 0
        for num in nums:
            if num == m1:
                c1 += 1
            elif num == m2:
                c2 += 1
        res = []
        if c1 > minRepeat:
            res.append(m1)
        if c2 > minRepeat:
            res.append(m2)

        return res


# if __name__=='__main__':
#     print(Solution().majorityElement([2, 1, 1, 3, 1, 4, 5, 6]))


# @lc code=end
