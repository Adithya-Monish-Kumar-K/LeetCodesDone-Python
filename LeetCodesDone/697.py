class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d={}
        for i,n in enumerate(nums):
            if n in d:
                d[n][0]+=1
                d[n][2]=i
            else:
                d[n]=[1,i,i]
        x=max([v[0] for v in d.values()])
        r=len(nums)
        for v in d.values():
            if v[0]==x:
                r=min(r,v[2]-v[1]+1)
        return r