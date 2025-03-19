# @leet start
class Solution:
    # max amount of water contained by start and end pillars
    def amount(self, start: int, end: int, height: List[int]) -> int:
        return min(height[start], height[end]) * (end - start)

    # direction 1 means traverse from left to right; -1 for versa
    def direction(self, start: int, end: int, height: List[int]) -> int:
        return 1 if height[start] <= height[end] else -1

    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_amount = self.amount(start, end, height)
        while start + 1 < end:
            d = self.direction(start, end, height) 
            if d == 1:
                start += 1
                max_amount = max(self.amount(start, end, height), max_amount)
            else:
                end -= 1
                max_amount = max(self.amount(start, end, height), max_amount)

        return max_amount


                




# @leet end
