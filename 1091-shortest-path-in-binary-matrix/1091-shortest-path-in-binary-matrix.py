from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        minn  =  float("+inf")
        width = len(grid)
        length = len(grid[0])
        grid2 = [[False] * length for _ in range(width)]
        stack = deque()
        if grid[0][0] == 1:
            return -1
        else:
            grid[0][0] =True
            stack.append((0,0,1))
            directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            while stack:
                a,b,c = stack.popleft()

                if a == width -1 and b == length -1:
                    minn  = min(minn,c)

                for i,j in directions:
                    xi = a+i
                    xj = b+j

                    if 0<=xi<width and 0<=xj<length and not grid2[xi][xj]:
                        if grid[xi][xj] == 0:
                            grid2[xi][xj] = True
                            stack.append((xi,xj,c+1))


                
        return minn if minn != float("+inf") else -1