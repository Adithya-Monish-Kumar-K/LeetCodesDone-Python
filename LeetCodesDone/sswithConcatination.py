class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wl = len(words[0])
        wc = len(words)
        tl = wl * wc
        wm = Counter(words)
        res = []
        for i in range(wl):
            l = i
            r = i
            seen = Counter()
            while r + wl <= len(s):
                word = s[r:r+wl]
                r += wl
                if word in wm:
                    seen[word] += 1
                    while seen[word] > wm[word]:
                        seen[s[l:l+wl]] -= 1
                        l += wl
                    if r - l == tl:
                        res.append(l)
                else:
                    seen.clear()
                    l = r
        return res