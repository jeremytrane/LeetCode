# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr, maxVal, minVal):
            if not curr:
                return True
            if not minVal < curr.val < maxVal:
                return False
            return (dfs(curr.left, curr.val, minVal) and dfs(curr.right, maxVal, curr.val))

        return dfs(root, float("inf"), float("-inf"))
