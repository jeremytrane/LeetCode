# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        if not root:
            return []

        maxVal = root.val

        def dfs(curr, maxVal):
            if not curr:
                return None

            if curr.val >= maxVal:
                self.res += 1
            maxVal = max(maxVal, curr.val)

            left = dfs(curr.left, maxVal)
            right  = dfs(curr.right, maxVal)
            return maxVal

        dfs(root, maxVal)
        return self.res
        


