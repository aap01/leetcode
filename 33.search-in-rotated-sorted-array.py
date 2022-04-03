#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (37.66%)
# Likes:    13536
# Dislikes: 872
# Total Accepted:    1.4M
# Total Submissions: 3.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# from typing import List
# @lc code=start
class Solution:
    # First find the index where the rotation has started
    # For [4, 5, 6, 7, 0, 1, 2] rotation index is 3 [4, 5, 6, *7, 0, 1, 2]
    def findRotIndex(self, nums: List[int], l, h) -> int:
        if h == l:
            return h
        
        p = (h + l)//2
        low = nums[l]
        piv = nums[p]
        
        if piv > low:
            return self.findRotIndex(nums, p, h)
        else:
            return self.findRotIndex(nums, l, p)
        
    def binSearch(self, nums, l, h, target):
        if l > h or h >= len(nums):
            return -1

        p = (l + h)//2
        piv = nums[p]
        if target > piv:
            return self.binSearch(nums, p + 1, h, target)
        elif target < piv:
            return self.binSearch(nums, l, p - 1, target)
        else:
            return p
        
    def search(self, nums: List[int], target: int) -> int:
        rotIndex = self.findRotIndex(nums, 0, len(nums) - 1)
        leftRes = self.binSearch(nums, 0, rotIndex, target) 
        rightRes = self.binSearch(nums, rotIndex + 1, len(nums) - 1, target)
        if leftRes != -1:
            return leftRes
        return rightRes
        

# if __name__  == '__main__':
#     print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
# @lc code=end

