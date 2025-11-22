class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        y = x & -x
        num1, num2 = 0, 0
        for num in nums:
            if num & y:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]