# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lca = None

    def hasNodes(self, root, targets):
        if not root:
            return False

        occur = (root in targets) + self.hasNodes(root.left, targets) + self.hasNodes(root.right, targets)
        if occur >= 2:
            # target nodes are at either (root, left tree), (root, right tree), or (left tree, right tree)
            self.lca = root

        return occur > 0


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.hasNodes(root, [p, q])
        return self.lca