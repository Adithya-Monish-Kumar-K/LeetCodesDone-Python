class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            a = (l + r) // 2
            if nums[a] == target:
                return True
            if nums[l] == nums[a] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[a]:
                if nums[l] <= target < nums[a]:
                    r = a - 1
                else:
                    l = a + 1
            else:
                if nums[a] < target <= nums[r]:
                    l = a + 1
                else:
                    r = a - 1
        return False