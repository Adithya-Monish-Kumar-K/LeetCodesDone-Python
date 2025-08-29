# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)
    def height(self, node: Optional[TreeNode]) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height