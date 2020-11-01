# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode, path: list = None) -> List[int]:
        path = path or []
        if not root:
            return path

        path += self.inorderTraversal(root.left)
        path.append(root.val)
        path += self.inorderTraversal(root.right)
        return path