class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}

        def helper(l, r):
            if r - l == 1:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            ans = 0
            for i in range(l + 1, r):
                ans = max(
                    ans,
                    helper(l, i)
                    + helper(i, r)
                    + nums[l] * nums[i] * nums[r]
                )

            memo[(l, r)] = ans
            return ans

        return helper(0, len(nums) - 1)