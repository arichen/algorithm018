# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not all([preorder, inorder]):
            return

        root = TreeNode(preorder[0])
        length, index = len(preorder), inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: index + 1], inorder[: index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root