# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if root == None:
                return False, root

            if root.val == p.val:
                return True, root

            if root.val == q.val:
                return True, root

            leftContain, leftAncestor = dfs(root.left)
            rightContain, righAncestor = dfs(root.right)

            if not leftContain and not rightContain:
                return False, root

            if leftContain and rightContain:
                return True, root
            
            return True, leftAncestor if leftContain else righAncestor

        return dfs(root)[1]