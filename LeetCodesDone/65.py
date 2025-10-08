class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        n = False
        d = False
        e = False
        na = True
        for i, char in enumerate(s):
            if char.isdigit():
                n = True
                na = True
            elif char == '.':
                if d or e:
                    return False
                d = True
            elif char in ('e', 'E'):
                if e or not n:
                    return False
                e = True
                na = False
            elif char in ('+', '-'):
                if i != 0 and s[i - 1] not in ('e', 'E'):
                    return False
            else:
                return False
        return n and na