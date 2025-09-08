class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = list()
        num.extend(nums1)
        num.extend(nums2)
        num.sort()
        if (len(num)%2==0):
            return (num[int((len(num)+1)/2)] + num[int(((len(num)+1)/2)-1)])/2
        else:
            return num[int(len(num)/2)]