"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            q, r = [], []
            for node in queue:
                r.append(node.val)
                q += node.children
            queue = q
            res.append(r)
        return res