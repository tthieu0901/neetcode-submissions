# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, -math.inf, math.inf
                
            isLeftValid = isRightValid = True
            maxRight = maxLeft = -math.inf
            minLeft = minRight = math.inf
            if root.left: isLeftValid, minLeft, maxLeft = dfs(root.left)
            if not isLeftValid: return False, 0, 0
            if root.right: isRightValid, minRight, maxRight = dfs(root.right)
            if not isRightValid: return False, 0, 0
            if not (maxLeft < root.val < minRight): return False, 0, 0
            return True, min(minLeft, root.val), max(maxRight, root.val)

        return dfs(root)[0]