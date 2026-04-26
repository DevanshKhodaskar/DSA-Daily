class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j, pi, pj, char):
            if visited[i][j]:
                return True

            visited[i][j] = True

            directions = [(-1,0), (0,1), (1,0), (0,-1)]

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == char:
                    if (ni, nj) == (pi, pj):
                        continue
                    if dfs(ni, nj, i, j, char):
                        return True

            return False

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False