class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        d2 = dict()
        for c in magazine:
            d[c]=d[c]+1 if c in d else 1
        for c in ransomNote:
            d2[c]=d2[c]+1 if c in d2 else 1
        for c in d2:
            if c not in d or d2[c] > d[c]:
                return False
        return True