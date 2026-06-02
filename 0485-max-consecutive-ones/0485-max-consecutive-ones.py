class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for i in nums:
            if i == 0:
                temp = 0
            else:
                temp+=1
                ans = max(temp,ans)
        return ans