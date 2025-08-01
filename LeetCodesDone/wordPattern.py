class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        a = dict()
        b = dict()
        for p, w in zip(pattern, words):
            if p not in a:
                a[p] = w
            if w not in b:
                b[w] = p
            if a[p] != w or b[w] != p:
                return False    
        return True