class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r=0
        for i in columnTitle:
            r=r*26+(ord(i)-ord("A")+1)
        return r
            