# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def preorder(root):
            nonlocal k, res
            if not root:
                return False

            if preorder(root.left): return True
            k -= 1
            if k == 0:
                res = root.val
                return True
            if preorder(root.right): return True

            return False
        preorder(root)
        return res
