class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        states = [0] * n # 0 -> unvisited, 1 -> visiting, 2 -> done
        def dfs(u):
            if states[u] == 1:
                return False
            if states[u] == 2:
                return True
            
            states[u] = 1
            for v in adj[u]:
                if states[v] != 2:
                    dfs(v)
            states[u] = 2
            return True
    
        count = 0
        for i in range(n):
            if states[i] == 0:
                dfs(i)
                count += 1
        return count
                