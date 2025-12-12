class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            a=s[:i]+s[1+i::]
            if s[i] in a:
                pass
            else:
                return i
        return -1