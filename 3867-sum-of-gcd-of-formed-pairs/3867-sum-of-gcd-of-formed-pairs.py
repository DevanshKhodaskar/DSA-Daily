import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        mxi = float("-inf")
        ans = []
        for i in range(len(nums)):
            mxi = max(mxi ,nums[i])
            ans.append(math.gcd(mxi , nums[i]))

        ans.sort()
        ret = 0
        n = len(ans)
        for i in range(n//2):
            if i != n-i-1:
                ret+=(math.gcd(ans[i] ,ans[n-i-1]))
        return ret