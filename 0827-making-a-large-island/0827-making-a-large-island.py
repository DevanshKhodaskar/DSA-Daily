class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        par = [  i for i in range(n*n)]
        size = [1]*(n*n)


        def find(x):
            res = x
            while res!=par[res]:
                res = par[res]
            return res
            
        def union(a,b):
            pa,pb = find(a),find(b)

            if pa == pb:
                return 
            else:
                par[pb] = pa
                size[pa]+=size[pb]



        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for d1,d2 in directions:
                        xa,xb = i-d1,j-d2

                        if 0<=xa<n and 0<=xb<n and grid[xa][xb]:
                            union(i*n+j,xa*n+xb)
        
        ans = max(size)
        for i in range(n):
            for j in range(n):
                s=set()
                if grid[i][j] == 0:
                    cur = 1
                    for d1,d2 in directions:
                        xa,xb = i-d1,j-d2
                        if 0<=xa<n and 0<=xb<n and grid[xa][xb]:
                            s.add(find(par[xa*n+xb]))
                    while s:
                        cur += size[s.pop()]
                    ans = max(ans,cur)

        return ans

            


