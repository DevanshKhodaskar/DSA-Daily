class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid_index(array, row, col):
            return 0 <= row < len(array) and 0 <= col < len(array[row])

        def helper(board ,prev_indexes,word_index,word,current_index):
            
            i = current_index[0]
            j = current_index[1]

            if word_index == len(word):
                return True

            

            indexes_check = [[i-1,j],[i+1,j],[i,j+1],[i,j-1]]

            for k in  indexes_check:
                if is_valid_index(board,k[0],k[1]) and k not in prev_indexes :
                    if board[k[0]][k[1]] == word[word_index] :
                        temp = prev_indexes.copy()
                        temp.append(k)
                        if helper(board ,temp,word_index+1,word,k):
                            return True
                     
                
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if helper(board,[[i,j]],1,word,[i,j]):
                        return True
        return False
        