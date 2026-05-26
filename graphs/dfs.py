class Solution:
    def dfs(self, v, adj, visited, result):
        visited[v] = True
        result.append(v)
        for u in adj[v]:
            if not visited[u]:
                self.dfs(u, adj, visited, result)


def main():
    V = 5
    adj = [[] for _ in range(V)]
    adj[0] = [1, 2]
    adj[1] = [0, 3]
    adj[2] = [0, 4]
    adj[3] = [1]
    adj[4] = [2]
    visited = [False] * V
    result = []
    sol = Solution()
    sol.dfs(0, adj, visited, result)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
