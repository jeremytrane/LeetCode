class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        states = [0] * numCourses # 0 -> unvisited, 1 -> visiting, 2 -> done
        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True

            states[course] = 1
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False

            states[course] = 2
            res.append(course)
            return True
            
        for i in range(numCourses):
            if states[i] == 0:
                if not dfs(i):
                    return []
        return res