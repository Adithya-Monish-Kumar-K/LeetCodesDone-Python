class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = set(nums)
        ls = 0
        for num in n:
            if num - 1 not in n:
                c = num
                cs = 1
                while c + 1 in n:
                    c += 1
                    cs += 1
                ls = max(ls, cs)
        return ls