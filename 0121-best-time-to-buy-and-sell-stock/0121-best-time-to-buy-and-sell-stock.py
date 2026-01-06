class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        ans = 0
        if len(prices) == 1:
            return 0
        else:
            low = prices[0]
            for i in range(1,len(prices)):
                if prices[i]<low:
                    low = prices[i]
                ans = max(ans,prices[i]-low)

        return ans