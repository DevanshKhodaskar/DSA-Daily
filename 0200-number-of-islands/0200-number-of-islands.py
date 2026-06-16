class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = []

        def dfs(i,j):
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            stack= [(i,j)]

            while stack:
                ni,nj = stack.pop()
                visited.add((ni,nj))

                for a,b in directions:
                    xi = ni-a
                    xj = nj-b

                    if 0<=xi<len(grid) and 0<=xj<len(grid[0]) and grid[xi][xj] == "1" and (xi,xj) not in visited:
                        stack.append((xi,xj))
                    


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i,j) not in visited:
                        ans.append((i,j))
                        dfs(i,j)
        return len(ans)

