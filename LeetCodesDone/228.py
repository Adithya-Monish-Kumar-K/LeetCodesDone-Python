class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        r = []
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if s == nums[i - 1]:
                    r.append(str(s))
                else:
                    r.append(f"{s}->{nums[i - 1]}")
                s = nums[i]
        if s == nums[-1]:
            r.append(str(s))
        else:
            r.append(f"{s}->{nums[-1]}")
        return r