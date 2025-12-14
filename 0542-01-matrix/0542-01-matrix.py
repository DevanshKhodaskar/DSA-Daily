from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        a = len(mat)
        b = len(mat[0])

        ans = [[float("inf")] * b for _ in range(a)]
        q = deque()

        for i in range(a):
            for j in range(b):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            i,j = q.popleft()

            for p,x in directions:
                ni,nj = i-p,j-x 

                if 0<=ni<a and 0<=nj<b:
                    if ans[ni][nj] > ans[i][j] +1:
                        ans[ni][nj] = ans[i][j]+1
                        q.append((ni,nj))

        return ans

             

        