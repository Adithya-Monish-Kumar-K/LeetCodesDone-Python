class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a = set(nums)
        m = sum(x for x in a if x > 0)
        if m == 0:
            return max(nums)
        return m