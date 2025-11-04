class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        l = []
        for i in range(n - k + 1):
            c = {}
            for j in range(i, i + k):
                c[nums[j]] = c.get(nums[j], 0) + 1
            s = sorted(c.items(), key=lambda t: (-t[1], -t[0]))
            t = [num for num, count in s[:x]]
            xs = sum(num * c[num] for num in t)
            l.append(xs)
        return l