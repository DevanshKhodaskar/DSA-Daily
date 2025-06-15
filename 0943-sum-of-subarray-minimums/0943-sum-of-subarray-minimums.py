class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(arr)):

            while stack and arr[i] < stack[-1][1]:
                j ,m = stack.pop()

                l = j - stack[-1][0] if stack else 1+j
                r = i - j
                ans += l*r*m

            stack.append([i,arr[i]])

        for i in range(len(stack)):
            j ,m = stack.pop()

            l = j - stack[-1][0] if stack else 1+j
            r = len(arr) - j
            ans += l*r*m

        return ans%(10**9 + 7)
        



        
        