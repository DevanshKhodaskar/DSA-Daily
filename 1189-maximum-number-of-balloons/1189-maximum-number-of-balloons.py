from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bal = set()
        for x in "ballon":
            bal.add(x)

        count = defaultdict(int)

        for x in text:
            if x in bal:
                count[x]+=1

        ans = float("inf")
        if len(count)!=5:
            return 0
        for x in count:
            if x in ["l","o"]:
                ans = min(ans,count[x]//2)
            else:
                ans = min(ans,count[x])
        return ans
