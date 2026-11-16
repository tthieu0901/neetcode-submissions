# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root, height = 0):
            if not root:
                return
            if height == len(res):
                res.append([])
            res[height].append(root.val)

            dfs(root.left, height + 1)
            dfs(root.right, height + 1)

        dfs(root)
        return res