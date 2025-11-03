class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        power = abs(n)
        while (power>0):
            if (power%2==1):
                ans*=x
            x*=x
            power//= 2
        return (ans) if (n>=0) else (1/ans)