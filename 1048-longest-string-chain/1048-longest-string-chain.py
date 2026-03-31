from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> List[str]:

        def helper(a, b):
            if len(a) != len(b) + 1:
                return False

            i = j = 0
            skipped = False

            while i < len(a):
                if j < len(b) and a[i] == b[j]:
                    i += 1
                    j += 1
                elif not skipped:
                    skipped = True
                    i += 1
                else:
                    return False

            return True

        m = len(words)
        words.sort(key=len)   

        dp = [1] * m
        prev = [-1] * m
        mx = 0

        for i in range(m):
            for j in range(i):
                if helper(words[i], words[j]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > dp[mx]:
                mx = i

        ans = []
        i = mx
        while i != -1:
            ans.append(words[i])
            i = prev[i]

        return len(ans)   