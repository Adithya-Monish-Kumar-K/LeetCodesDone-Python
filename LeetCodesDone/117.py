"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        current = [root]
        while current:
            for i in range(len(current)):
                node = current[i]
                if i < len(current) - 1:
                    node.next = current[i + 1]
            current = [child for n in current for child in (n.left, n.right) if child]
        return root