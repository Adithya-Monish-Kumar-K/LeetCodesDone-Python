class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = dict()
        for s in strs:
            key = tuple(sorted(s))
            if key in a:
                a[key].append(s)
            else:
                a[key] = [s]
        return list(a.values())