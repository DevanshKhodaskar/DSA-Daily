class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                    stack.pop()
            if stack and temperatures[stack[-1]]>temperatures[i]:
                ans.append(stack[-1]-i)
                stack.append(i)
            elif not stack:
                stack.append(i)
                ans.append(0)
        return ans[::-1]
