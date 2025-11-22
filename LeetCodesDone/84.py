class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = 0
        heights.append(0)
        for i in range(len(heights)):
            while s and heights[i] < heights[s[-1]]:
                h = heights[s.pop()]
                w = i if not s else i - s[-1] - 1
                m = max(m, h * w)
            s.append(i)
        return m