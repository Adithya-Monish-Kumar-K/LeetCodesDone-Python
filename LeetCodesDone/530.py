# Definition for a binary tree n.
# class Treen:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s = []
        n = root
        p = None
        md = float('inf')
        while s or n:
            while n:
                s.append(n)
                n = n.left
            n = s.pop()
            if p is not None:
                md = min(md, n.val - p)
            p = n.val
            n = n.right
        return md