class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        have = {}
        formed = 0
        required = len(need)
        l = 0
        res = [float('-inf'), float('inf')]
        for r in range(len(s)):
            c = s[r]
            if c in need:
                have[c] = have.get(c, 0) + 1
                if have[c] == need[c]:
                    formed += 1
            while formed == required:
                if (r - l) < (res[1] - res[0]):
                    res = [l, r]
                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        formed -= 1
                l += 1
        if res[0] == float('-inf'):
            return ""
        return s[res[0]:res[1]+1]
