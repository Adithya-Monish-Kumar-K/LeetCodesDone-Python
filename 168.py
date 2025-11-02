class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        i=columnNumber
        r=""
        while (i>=1):
            i-=1
            rem = i%26
            r = chr(65+rem)+r
            i//=26
        return r