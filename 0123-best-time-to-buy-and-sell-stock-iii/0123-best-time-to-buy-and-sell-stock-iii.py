class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n

        lmin = prices[0]
        for i in range(1, n):
            lmin = min(lmin, prices[i])
            left[i] = max(left[i - 1], prices[i] - lmin)

        rmax = prices[-1]
        for j in range(n - 2, -1, -1):
            rmax = max(rmax, prices[j])
            right[j] = max(right[j + 1], rmax - prices[j])

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i])

        return ans