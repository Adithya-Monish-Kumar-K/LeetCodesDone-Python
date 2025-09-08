class Solution:
    def sumZero(self, n: int) -> List[int]:
        if(n%2==0):
            l=list()
            a=0
            for i in range(int(n/2)):
                a+=1
                l.append(a)
            a=0
            for i in range(int(n/2)):
                a-=1
                l.append(a)
        else:
            l=list()
            l.append(0)
            a=0
            for i in range(int((n-1)/2)):
                a+=1
                l.append(a)
            a=0
            for i in range(int((n-1)/2)):
                a-=1
                l.append(a)
        return l