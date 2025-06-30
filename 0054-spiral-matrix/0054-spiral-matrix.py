class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        ver = len(mat)
        hor = len(mat[0])

        top, bottom = 0, ver - 1
        left, right = 0, hor - 1
        ans = []

        while top <= bottom and left <= right:
           
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

           
            for j in range(top, bottom + 1):
                ans.append(mat[j][right])
            right -= 1
            
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    ans.append(mat[bottom][k])
                bottom -= 1

            if left <= right:
                for l in range(bottom, top - 1, -1):
                    ans.append(mat[l][left])
                left += 1

        return ans