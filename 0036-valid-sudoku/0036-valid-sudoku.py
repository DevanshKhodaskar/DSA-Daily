class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(matrix):
            a = [False]*9

            for i in matrix:
                for j in i:
                    if j == ".":
                        continue
                    else:
                        temp = int(j) -1
                    if a[temp] == True:
                        return False
                    else:
                        a[temp] = True
            return True

        for i in board:
            if helper([i]) == False:
                return False
        for j in range(len(board[0])):
            enter = []
            for i in range(9):
                enter.append(board[i][j])
            if helper([enter]) == False:
                return False

        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                
                if helper([board[k][i:i+3] for k in range(j,j+3)]) == False:
                    return False
        return True
        