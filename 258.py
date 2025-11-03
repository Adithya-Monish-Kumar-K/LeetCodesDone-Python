class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        if len(s)<=1:
            return int(s)
        n=0
        for i in s:
            n+=int(i)
        return self.addDigits(n)