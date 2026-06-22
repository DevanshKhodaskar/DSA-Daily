class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        def applicableoffer(needed,offer):
            for i in range(len(needed)):
                if needed[i]<offer[i]:
                    return False
            return True

        def helper(needed):
            if tuple(needed) in memo:
                return memo[tuple(needed)]
            ans = float("inf")
            for offer in special:
                
                if applicableoffer(needed,offer):
                    temp = needed[:]
                    for x in range(len(temp)):
                        temp[x]-=offer[x]
                    left  = helper(temp)
                    ans = min(ans,left+offer[-1])
            temp = 0
            for x in range(len(price)):
                temp+=price[x]*needed[x]
            ans = min(ans,temp)
            memo[tuple(needed)] =  ans
            return memo[tuple(needed)]

        return helper(needs)


                

