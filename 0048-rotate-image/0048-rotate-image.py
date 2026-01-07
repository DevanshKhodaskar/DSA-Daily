class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j] ,matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
        n = len(matrix) -1
        for j in range(len(matrix)):
            for k in range(len(matrix)//2):
                matrix[j][k],matrix[j][n-k] = matrix[j][n-k],matrix[j][k]
      