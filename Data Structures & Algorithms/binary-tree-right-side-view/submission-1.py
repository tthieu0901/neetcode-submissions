# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        def dfs(root, height = 0):
            if not root:
                return
            
            if len(rightSide) == height:
                rightSide.append(root.val)

            dfs(root.right, height + 1)
            dfs(root.left, height + 1)

        dfs(root)
        return rightSide