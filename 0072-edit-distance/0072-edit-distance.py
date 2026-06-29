class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)


        dp = {}

        def helper(i,j):
            if i == n and j == m:
                return 0

            if i == n:
                return m - j

            if j == m:
                return n - i


            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:
                dp[(i,j)] = helper(i+1,j+1)            

            else:

                ans = 1+min(helper(i,j+1) , helper(i+1,j),helper(i+1,j+1))
                dp[(i,j)] = ans
            return dp[(i,j)]
        return helper(0,0)