# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        r = []
        q = deque([root])
        while q:
            ls = 0
            lc = len(q)
            for _ in range(lc):
                node = q.popleft()
                ls += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            r.append(ls / lc)
        return r