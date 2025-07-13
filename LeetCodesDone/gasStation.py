class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tot, start, current = 0, 0, 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            current += gas[i] - cost[i]
            if current < 0:
                start = i + 1
                current = 0
        return start if tot>=0 else -1