class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        t = sum(nums)
        c = sum(i * num for i, num in enumerate(nums))
        m = c
        for i in range(1, n):
            c += t - n * nums[n - i]
            m = max(m, c)
        return m