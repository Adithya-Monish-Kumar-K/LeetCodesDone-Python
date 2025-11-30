class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = sum(nums)
        if (t + target) % 2 != 0 or t < abs(target):
            return 0
        s = (t + target) // 2
        d = [0] * (s + 1)
        d[0] = 1
        for num in nums:
            for j in range(s, num - 1, -1):
                d[j] += d[j - num]
        return d[s]