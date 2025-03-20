# @leet start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if len(spaces) == 0:
            return s
        count = 0
        result = ""
        space = " "
        for i in range(0, len(s)):
            if i == spaces[count]:
                result += space
                count += 1
            if count == len(spaces):
                return result + s[i:]
            result += s[i]

        return result


# @leet end

