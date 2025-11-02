class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=sorted(nums)
        i=1
        b=list()
        b.append(0)
        for k in a:
            if k > 0:
                if (k!=b[len(b)-1]):
                    if (i==k):
                        i+=1
                        b.append(k)
                    else:
                        break
        i=int(i)
        return i