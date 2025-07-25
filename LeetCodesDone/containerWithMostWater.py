class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ar=0
        while l<r:
            ar = max(ar, (r -l)*min(height[l], height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ar