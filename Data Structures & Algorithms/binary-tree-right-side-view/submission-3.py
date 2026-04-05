class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            lastSeenNode = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lastSeenNode = node
            if lastSeenNode:
                res.append(lastSeenNode.val)
        return res
