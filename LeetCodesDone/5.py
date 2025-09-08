class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        p=list()
        m=""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if (self.isPalindrome(s[i:j])):
                    if(len(m)<len(s[i:j])):
                        m=s[i:j]
        return m

    def isPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        return False
