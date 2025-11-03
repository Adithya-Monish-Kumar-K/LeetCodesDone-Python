class Solution:
    def smallestNumber(self, n: int) -> int:
        val = 0
        s=''
        while True:
            if val<n:
                power=len(s)
                val+=2**(power)
                s+="1"
            else:
                break
        return val