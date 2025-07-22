class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        t = 0
        m = float("inf")
        while r< len(nums):
            t += nums[r]
            while t >= target:
                m = min(m, r-l+1)
                t -= nums[l]
                l += 1
            r += 1
        return m if m != float("inf") else 0