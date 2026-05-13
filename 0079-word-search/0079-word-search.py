class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def helper(i,j,e,checked):
            if e==len(word):
                return True
            
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
            for ai,aj in directions:
                ni = i+ai
                nj = j+aj

                if 0<=ni<len(board) and 0<=nj<len(board[0]):
                    if board[ni][nj] == word[e]  and (ni, nj) not in checked:
                        checked.append((ni,nj))
                        if helper(ni,nj,e+1,checked)   :
                            return True     
                        checked.pop()
            return False





        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    ans = helper(i,j,1,[(i,j)])
                    if ans == True:
                        return True
        return False
        