class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        # DFS
        def dfs(i, j, seen):
            seen.add((i, j))
            for x, y in directions:
                r, c = i + x, j + y
                if inbound(r, c) and heights[i][j] <= heights[r][c] and (r, c) not in seen:
                    dfs(r, c, seen)
            return seen
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    pacific_set = pacific_set.union(dfs(i, j, set()))
                if i == row - 1 or j == col - 1:
                    atlantic_set = atlantic_set.union(dfs(i, j, set()))
        
        return list(pacific_set.intersection(atlantic_set))