from collections import defaultdict
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        d= defaultdict(int)
        a = set()

        for x in nums:
            d[x]+=1
            a.add(x)
        ans = 1
        print(d)
        for i in range(len(nums)):
            ele = nums[i]
            count = 0
            while ele in a :
                if d[ele]  < 2 or ele ==1:
                    count+=1
                    break

                count+=1
                ele = ele**2
            count = (count-1)*2 + 1

            
            ans= max(count,ans)
        if 1 in a:
            ans = max(ans , d[1] if d[1]%2 !=0 else d[1] - 1)
        return ans