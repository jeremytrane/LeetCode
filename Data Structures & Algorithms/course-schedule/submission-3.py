class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[dest].append(src)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True

            visited.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            adj[course] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True