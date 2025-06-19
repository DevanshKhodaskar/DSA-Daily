class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                j ,a = stack.pop()
                ans = max(ans,a*(i-j))
                start = j

            stack.append([start,heights[i]])


        for i,h in stack:
            ans = max(ans,h*(len(heights)-i))

        return ans

        