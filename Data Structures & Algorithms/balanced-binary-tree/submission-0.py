# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, height = 0):
            if root == None:
                return True, height

            left, hLeft = dfs(root.left, height + 1)
            if not left: return False, height

            right, hRight = dfs(root.right, height + 1)
            if not right: return False, height
            
            return abs(hLeft - hRight) <= 1, max(hLeft, hRight)


        return dfs(root)[0]