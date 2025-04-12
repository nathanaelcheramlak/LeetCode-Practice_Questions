class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        adj = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)

        print(adj)
        def dfs(vertex):
            visited[vertex] = 1
            for v in adj[vertex]:
                if visited[v] != 0: continue
                dfs(v)
        
        components = 0
        visited = [0] * N
        for i in range(N):
            if visited[i] != 0: continue
            components += 1
            dfs(i)
        
        return components