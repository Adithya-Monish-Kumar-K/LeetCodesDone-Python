class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirstPosition(nums, target):
            left, right = 0, len(nums) - 1
            firstPosition = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    firstPosition = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return firstPosition

        def findLastPosition(nums, target):
            left, right = 0, len(nums) - 1
            lastPosition = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    lastPosition = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return lastPosition

        firstPosition = findFirstPosition(nums, target)
        lastPosition = findLastPosition(nums, target)
        return [firstPosition, lastPosition]