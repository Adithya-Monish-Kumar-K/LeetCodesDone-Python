class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [float('inf')] * (amount + 1)
        a[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                a[x] = min(a[x], a[x - coin] + 1)
        return a[amount] if a[amount] != float('inf') else -1