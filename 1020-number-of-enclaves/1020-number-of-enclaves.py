class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        ans = set()
        def dfs(oi,oj):
            stack = []
            stack.append((oi,oj))
            ans.add((oi,oj))
            directions = [(0,1),(1,0),(-1,0),(0,-1)]

            while stack:
                z,y = stack.pop()
                for xi,xj in directions:
                    ni = z-xi
                    nj = y - xj
                    if  0<=ni<a and 0<=nj<b and grid[ni][nj] == 1 and (ni,nj) not in ans:
                        ans.add((ni,nj))
                        stack.append((ni,nj))


        for i in range(a):
            if grid[i][b-1] == 1:
                dfs(i,b-1)
        for i in range(a):
            if grid[i][0] == 1:
                dfs(i,0)
        for i in range(b):
            if grid[0][i] == 1:
                dfs(0,i)
        for i in range(b):
            if grid[a-1][i] == 1:
                dfs(a-1,i)
        
        count = 0
        for i in range(a):
            for j  in range(b):
                if grid[i][j] == 1 and (i,j) not in ans:
                    count +=1
        return count


        
        