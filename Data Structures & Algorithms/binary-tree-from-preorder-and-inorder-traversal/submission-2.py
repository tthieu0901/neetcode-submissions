# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxMap = {num: idx for idx, num in enumerate(inorder)}
        preIdx = 0
        def dfs(left, right):
            nonlocal preIdx
            if left > right:
                return None
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            idxNode = idxMap[root.val]
            root.left = dfs(left, idxNode - 1)
            root.right = dfs(idxNode + 1, right)
            return root
            
        return dfs(0, len(preorder) - 1)
                

