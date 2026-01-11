class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calculateArea(nums:list):
            ans = 0
            for i in range(len(nums)):
                left = i
                right = i
                lc = 0
                rc = 0
                ele = nums[i]
                while left>=0 and nums[left]>=ele:
                    left-=1
                    lc+=1
                while right<=len(nums)-1 and nums[right]>=ele:
                    right+=1
                    rc+=1
                wid = lc+rc-1
                
                ans = max(ans,(wid*ele))
                
                
            return ans

  
        def calculateHeight(mat:list[list]):
            n = len(mat)
            m = len(mat[0])
            ans = []
            for i in range(m):
                j = n- 1
                temp= 0
                while j>=0 and mat[j][i] == '1':
                    temp+=1
                    j-=1
                ans.append(temp)
            return ans
        
        ans = 0
        for i in range(len(matrix)):
            
            heights = calculateHeight(matrix[:i+1])
            area = calculateArea(heights)
            
            ans = max(area,ans)
        return ans
  
  
  
  
  



