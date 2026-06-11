class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            memo = {}

            def helper(i):
                if i < 0:
                    return 0
                elif i == 0:
                    return arr[0]
                elif i in memo:
                    return memo[i]
                else:
                    left = helper(i - 1)
                    right = helper(i - 2) + arr[i]

                    memo[i] = max(left, right)
                    return memo[i]

            return helper(len(arr) - 1)

        return max(solve(nums[:-1]), solve(nums[1:]))