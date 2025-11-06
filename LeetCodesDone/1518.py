class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        t = numBottles
        e = numBottles
        while e >= numExchange:
            n = e // numExchange
            t += n
            e = e % numExchange + n
        return t