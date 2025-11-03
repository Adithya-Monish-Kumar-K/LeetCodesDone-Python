class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for j,k in d.items():
            if k>1:
                return True
        return False