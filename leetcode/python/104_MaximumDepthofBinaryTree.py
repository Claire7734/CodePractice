# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return self.maxSearch(root, 1)
        else:
            return 0

    def maxSearch(self, root, len):
        left = len
        right = len
        if root.left != None:
            left = self.maxSearch(root.left, len+1)
        if root.right != None:
            right = self.maxSearch(root.right, len+1)
        if left > right:
            return left
        else:
            return right
