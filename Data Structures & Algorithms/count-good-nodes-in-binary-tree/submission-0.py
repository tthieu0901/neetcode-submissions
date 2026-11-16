# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue = -math.inf):
            if not root:
                return 0

            res = 0
            if root.val >= maxValue:
                maxValue = root.val
                res += 1

            return res + dfs(root.left, maxValue) + dfs(root.right, maxValue)

        return dfs(root)