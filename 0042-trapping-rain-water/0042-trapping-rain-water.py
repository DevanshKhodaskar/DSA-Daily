from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        def calc(arr, height):
            if len(arr) < 2:
                return 0
            threshold = min(height[arr[0]], height[arr[-1]])
            ans = 0
            for i in range(1, len(arr) - 1):
                ans += max(0, threshold - height[arr[i]])
            return ans

        stack = []
        ans = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break  
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(i)

        return ans
