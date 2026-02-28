class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(triangle) - 1:
                return triangle[i][j]

            left = helper(i + 1, j)
            right = helper(i + 1, j + 1)

            memo[(i, j)] = triangle[i][j] + min(left, right)
            return memo[(i, j)]

        return helper(0, 0)