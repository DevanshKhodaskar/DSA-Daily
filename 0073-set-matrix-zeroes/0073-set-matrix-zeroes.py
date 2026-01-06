class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        colm = set()


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    colm.add(j)

        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in colm:
            for j in range(len(matrix)):
                matrix[j][i] = 0

        return matrix
        