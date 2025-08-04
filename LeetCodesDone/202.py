class Solution:
    def isHappy(self, n: int) -> bool:
        def next(number):
            sum = 0
            while number > 0:
                d = number % 10
                sum += d * d
                number //= 10
            return sum

        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = next(n)
        return n == 1