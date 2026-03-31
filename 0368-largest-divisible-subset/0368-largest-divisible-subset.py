class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        m = len(nums)
        nums.sort()
        dp = [1]*m
        prev = [-1]*m
        mx = 0


        for i in range(1,m):
            for j in range(i):

                if nums[i]%nums[j] == 0 and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
                    prev[i] = j
            if dp[i] > dp[mx]:
                mx = i
        ans = []

        i  =mx
        while i>=0:
            ans.append(nums[i])
            i = prev[i]
        return ans
                
        