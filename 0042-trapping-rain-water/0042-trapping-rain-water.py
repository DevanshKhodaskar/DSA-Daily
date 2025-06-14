class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        l = height[0]
        r = height[len(height)-1]

        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
            left_max.append(l)

            if height[len(height)-1-i] > r:
                r = height[len(height)-1-i]
            right_max.append(r)
        right_max.reverse()
        ans = 0
        for i in range(len(left_max)):
            ans+= (min(left_max[i],right_max[i]) - height[i]) if (min(left_max[i],right_max[i]) - height[i]) > 0 else 0

        return ans

        
        




        