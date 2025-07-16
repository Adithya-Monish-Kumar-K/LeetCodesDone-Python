class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        rs= [''] * numRows
        cr = 0
        a = False
        for i in s:
            rs[cr] += i
            if cr == 0:
                a = True
            elif cr == numRows - 1:
                a = False
            
            if a:
                cr += 1
            else:
                cr -= 1
        s2 = ""
        for i in rs:
            s2 += i
        return s2
        