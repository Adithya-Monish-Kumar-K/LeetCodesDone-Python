class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def func(ss: str) -> int:
            if len(ss) < k:
                return 0
            c = {}
            for i in ss:
                c[i] = c.get(i, 0) + 1
            for j in range(len(ss)):
                if c[ss[j]] < k:
                    n = j + 1
                    while n < len(ss) and c[ss[n]] < k:
                        n += 1
                    return max(func(ss[:j]), func(ss[n:]))
            return len(ss)
        return func(s)