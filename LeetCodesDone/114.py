# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node):
            if not node:
                return None
            left = flatten_tree(node.left)
            right = flatten_tree(node.right)
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            return right if right else left if left else node
        flatten_tree(root)
        