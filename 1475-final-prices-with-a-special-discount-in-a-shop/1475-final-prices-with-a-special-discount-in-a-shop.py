class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(prices)-1,-1,-1):

            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack:
                ans = ans+[prices[i]-stack[-1]]
                stack.append(prices[i])
            elif not stack:
                ans = ans+[prices[i]]
                stack.append(prices[i])
        return ans[::-1]
