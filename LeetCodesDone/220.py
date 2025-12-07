class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        b = {}
        w = valueDiff + 1
        for i, n in enumerate(nums):
            if i > indexDiff:
                ob = nums[i - indexDiff - 1] // w
                if ob in b:
                    del b[ob]
            bi = n // w
            if bi in b:
                return True
            if bi - 1 in b and abs(n - b[bi - 1]) <= valueDiff:
                return True
            if bi + 1 in b and abs(n - b[bi + 1]) <= valueDiff:
                return True
            b[bi] = n
        return False