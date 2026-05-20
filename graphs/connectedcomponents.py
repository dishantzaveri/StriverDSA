from collections import deque

class Solution:
    def countComponents(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * V
        components = 0
        for i in range(V):
            if not visited[i]:
                components += 1
                q = deque()
                q.append(i)
                visited[i] = True
                while q:
                    node = q.popleft()
                    for nbr in adj[node]:
                        if not visited[nbr]:
                            visited[nbr] = True
                            q.append(nbr)
        return components

V = 5
edges = [[0, 1], [1, 2], [3, 4]]
sol = Solution()
print("Number of Connected Components:", sol.countComponents(V, edges))