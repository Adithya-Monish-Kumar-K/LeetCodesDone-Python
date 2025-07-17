class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        for i in range(len(words)):
            if len(words[i])> maxWidth:
                return []
        if not words:
            return []
        l = []
        c = []
        cl = 0
        for word in words:
            if cl+len(word)+len(c) > maxWidth:
                for i in range(maxWidth-cl):
                    c[i%(len(c)-1 or 1)] += ' '
                l.append(''.join(c))
                c = [word]
                cl = len(word)
            else:
                c.append(word)
                cl += len(word)
        if c:
            l.append(' '.join(c) + ' ' * (maxWidth - cl - len(c) + 1))
        return l