from collections import deque
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a = [0]
        b = deque()
        b.append(0)
        temp = 0
        for i in range(len(nums)-1):
            temp += nums[i] 
            a.append(temp)
        temp = 0
        for j in range(len(nums)-1,0,-1):
            temp+=nums[j]
            b.appendleft(temp)
        
        ans = []
        print(a)
        print(b)
        for i in range(len(a)):
            ans.append(abs(a[i]-b[i]))
        return ans