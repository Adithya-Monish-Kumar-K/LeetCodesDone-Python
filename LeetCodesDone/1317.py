class Solution:
    def calc(self,n,s):
        if (not('0' in str(n-s)) and not('0' in str(s))):
                return [n-s,s]
        elif('0' in str(n-s) or ('0' in str(s))):
            return self.calc(n, s+1)
        
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if (n==0):
            return [0,0]
        d = self.calc(n,1)
        return d
