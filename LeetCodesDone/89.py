class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = []
        for i in range(1 << n):
            l.append(i ^ (i >> 1))
        return l
