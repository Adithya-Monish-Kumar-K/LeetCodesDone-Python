class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = dict()
        b = dict()
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = t[i]
            if t[i] not in b:
                b[t[i]] = s[i]
            if a[s[i]] != t[i] or b[t[i]] != s[i]:
                return False
        return True