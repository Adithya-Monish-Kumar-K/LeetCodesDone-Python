class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = self.com(digits)
        num+=1
        digits=self.splitint(num)
        return digits
    def com(self, digits):
        num=""
        for i in digits:
            num +=str(i)
        return int(num)
    def splitint(self, num):
        num=str(num)
        s=[]
        for i in num:
            s.append(int(i))
        return s