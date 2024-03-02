class Solution:
    def bitAdd(self, b1, b2, c):
        if b1 == "0" and b2 == "0" and c == "0":
            return "0", "0"
        if b1 == "0" and b2 == "0" and c == "1":
            return "0", "1"
        if b1 == "0" and b2 == "1" and c == "0":
            return "0", "1"
        if b1 == "0" and b2 == "1" and c == "1":
            return "1", "0"
        if b1 == "1" and b2 == "0" and c == "0":
            return "0", "1"
        if b1 == "1" and b2 == "0" and c == "1":
            return "1", "0"
        if b1 == "1" and b2 == "1" and c == "0":
            return "1", "0"
        if b1 == "1" and b2 == "1" and c == "1":
            return "1", "1"

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
            c, tempS = self.bitAdd(b1, b2, c)
            s = tempS + s
            i -= 1
        if c == "1":
            s = c + s
        return s
