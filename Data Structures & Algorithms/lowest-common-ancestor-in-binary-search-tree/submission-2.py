# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return -1

        curr = root

        while curr:
            if p.val <= curr.val <= q.val or q.val <= curr.val <= p.val:
                return curr
            elif max(p.val, q.val) < curr.val:
                curr = curr.left
            else:
                curr = curr.right
