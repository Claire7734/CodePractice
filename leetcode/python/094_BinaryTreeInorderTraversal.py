# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root
        ans = []
        stack = []
        cur = root
        while (cur != None) or len(stack) != 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right #!!!
        return ans

class Solution:
    # recursive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root, ans):
        if root != None:
            self.inorder(root.left, ans)
            ans.append(root.val)
            self.inorder(root.right, ans)
