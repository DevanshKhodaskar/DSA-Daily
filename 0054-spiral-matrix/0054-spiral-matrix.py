class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        ix = len(matrix) -1

        j = 0
        jx = len(matrix[0]) -1
        ans = []

        while (i <= ix and j <= jx):
           
            for a in range(j,jx+1):
                ans.append(matrix[i][a])

            for a in range(i+1,ix+1):
                ans.append(matrix[a][jx])

            if i < ix:  
                for b in range(jx-1,j-1,-1):
                    ans.append(matrix[ix][b])
            
            if i < jx:
                for b in range(ix-1 ,i,-1):
                    ans.append(matrix[b][j])
            i+=1
            ix-=1
            j+=1
            jx-=1
        return ans
