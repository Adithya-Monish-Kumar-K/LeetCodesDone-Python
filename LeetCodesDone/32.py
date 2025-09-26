class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ml = 0
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ml = max(ml, 2 * r)
            elif r > l:
                l = r = 0
        l = r = 0
        for c in reversed(s):
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ml = max(ml, 2 * l)
            elif l > r:
                l = r = 0
        return ml