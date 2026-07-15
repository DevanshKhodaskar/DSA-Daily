from collections import defaultdict
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        a = defaultdict(int)
        for i in nums:
            a[i]+=1
        
        ans = []
        for i in nums:
            if i not in a or a[i] == 1:
                left = i-1
                right = i+1
                if left not in a and right not in a:
                    ans.append(i)
        return ans