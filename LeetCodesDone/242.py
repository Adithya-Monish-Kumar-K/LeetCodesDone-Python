class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = dict()
        b= dict()
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i] = 1
        for i in t:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        for i in a:
            if i not in b or a[i]!=b[i]:
                return False
        return True