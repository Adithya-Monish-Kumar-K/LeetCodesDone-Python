class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for j,k in d.items():
            if k<2:
                return j
        return