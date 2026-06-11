class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        memo = {}

        def helper(summ, i):
            if summ == target:
                return True
            if i >= len(nums) or summ > target:
                return False

            if (summ, i) in memo:
                return memo[(summ, i)]

            memo[(summ, i)] = (
                helper(summ, i + 1) or
                helper(summ + nums[i], i + 1)
            )
            return memo[(summ, i)]

        return helper(0, 0)