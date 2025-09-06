class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        a=1
        b=1
        su=0
        if (s==""):
            return 0
        if (s[0] == '-'):
            a=-1
            s=s[1:]
        elif (s[0]=='+'):
            a=1
            s=s[1:]
        for i in s:
            if (i in ['0','1','2','3','4','5','6','7','8','9']):
                su=su*10+(int(i))
            else:
                break
        su=su*a
        if(su>((2**31)-1)):
            su=(2**31)-1
        elif(su<(-1*(2**31))):
            su=-1*(2**31)
        return su