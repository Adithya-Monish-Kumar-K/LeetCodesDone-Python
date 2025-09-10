"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        otn = {}
        def dfs(n: 'Node') -> 'Node':
            if n in otn:
                return otn[n]
            x = Node(n.val)
            otn[n] = x
            for n in n.neighbors:
                x.neighbors.append(dfs(n))
            return x
        return dfs(node)