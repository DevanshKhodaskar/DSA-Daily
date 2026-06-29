class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = target
        maxx = max(nums)
        dp =  [0]*(n+maxx)

        for i in nums:
            dp[i] = 1
        
        for j in range(len(dp) -maxx):
            if dp[j] >0:

                for k in nums:
                    dp[j+k]+=dp[j]
        return dp[n]