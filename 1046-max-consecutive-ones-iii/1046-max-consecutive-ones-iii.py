from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        ans = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                q.append(i)
            if len(q)>k:
                l = q.popleft() + 1
            ans = max(ans,i-l+1)


        return ans


                    


                

        

        