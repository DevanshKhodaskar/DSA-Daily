class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = -1
        left = [-1]*len(height)
        right_max = -1
        right = [-1]*len(height)

        for i in range(len(height)):
                left[i] = left_max
                left_max = max(left_max,height[i])

        for i in range(len(height)-1,-1,-1):
                right[i] = right_max
                right_max = max(right_max,height[i])

        ans = 0
        


        for i in range(len(height) ):
            print(left[i] ,right[i])
            if left[i] == -1 or right[i] == -1:
                continue
            ans += max((min(left[i] ,right[i]) - height[i]) , 0)
        return ans