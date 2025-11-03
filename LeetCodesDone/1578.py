class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        t = 0
        n = len(colors)
        i = 0
        while i < n:
            j = i + 1
            m = neededTime[i]
            g = neededTime[i]
            while j < n and colors[j] == colors[i]:
                g += neededTime[j]
                m = max(m, neededTime[j])
                j += 1
            t += g - m
            i = j
        return t