# Definition for a binary tree n.
# class Treen:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        n = root
        while s or n:
            while n:
                s.append(n)
                n = n.left
            n = s.pop()
            k -= 1
            if k == 0:
                return n.val
            n = n.right