# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r = []
        cl = [root]
        ltr = True
        while cl:
            lv = []
            nl = []
            for node in cl:
                lv.append(node.val)
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            if not ltr:
                lv.reverse()
            r.append(lv)
            cl = nl
            ltr = not ltr
        return r