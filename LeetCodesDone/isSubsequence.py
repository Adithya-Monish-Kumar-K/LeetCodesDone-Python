class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) ==0:
            return True
        if len(t) ==0:
            return False
        for i in s:
            a = len(t)
            for j in range(len(t)):
                if i == t[j]:
                    t=t[j+1::]
                    j=0
                    break
            if len(t)==a:
                return False
        return True