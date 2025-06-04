class Solution:
    def solveNQueens(self, n: int):
        def placeQueen(row, diag, antiDiag, colSet, board):
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in colSet or (row - col) in diag or (row + col) in antiDiag:
                    continue

                board[row][col] = 'Q'
                colSet.add(col)
                diag.add(row - col)
                antiDiag.add(row + col)

                placeQueen(row + 1, diag, antiDiag, colSet, board)

                board[row][col] = '.'
                colSet.remove(col)
                diag.remove(row - col)
                antiDiag.remove(row + col)

        ans = []
        tempBoard = [['.'] * n for _ in range(n)]
        placeQueen(0, set(), set(), set(), tempBoard)
        return ans
