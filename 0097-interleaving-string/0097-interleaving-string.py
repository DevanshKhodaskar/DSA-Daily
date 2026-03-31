class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def helper(i, j, k):
            if (i, j) in dp:
                return dp[(i, j)]

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i] == s3[k]:
                if helper(i + 1, j, k + 1):
                    dp[(i, j)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if helper(i, j + 1, k + 1):
                    dp[(i, j)] = True
                    return True

            dp[(i, j)] = False
            return False

        return helper(0, 0, 0)