class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        def backtrack(s: int, p: List[int]):
            r.append(p[:])
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                p.append(nums[i])
                backtrack(i + 1, p)
                p.pop()
        backtrack(0, [])
        return r