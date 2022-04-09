#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (50.29%)
# Likes:    4819
# Dislikes: 527
# Total Accepted:    814.9K
# Total Submissions: 1.6M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def bitAdd(self, b1, b2):
        if b1 == "1":
            if b2 == "0":
                return "0", "1"
            else:
                return "1", "0"
        else:
            return "0", b2

    def addBinary(self, a: str, b: str) -> str:
        s = ""
        c = "0"
        lenA = len(a)
        lenB = len(b)
        i = max(lenA, lenB)
        a = "0" * (i - lenA) + a
        b = "0" * (i - lenB) + b
        i -= 1
        
        while i >= 0:
            b1 = a[i]
            b2 = b[i]
            add = self.bitAdd(b1, b2)
            print(add)
            tempS = self.bitAdd(add[1], c)
            s = tempS[1] + s
            c = "1" if add[0] == "1" or tempS[0] == "1" else "0" 
            i -= 1
        if c == "1":
            s = c + s
        return s
                    
                    
                    
                    
            
        
# @lc code=end

