class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        counter = 0
        for i in s:
            if i == "(":
                left+=1
            elif i == ")":
                right+=1

            if left == right:
                ans = max(left*2,ans)
            elif right>left:
                counter = 0
                left = 0
                right  = 0

        left = 0
        right = 0
        for i in s[::-1]:
            if i == "(":
                left+=1
            elif i == ")":
                right+=1

            if left == right:
                ans = max(left*2,ans)
            elif right<left:
                counter = 0
                left = 0
                right  = 0
            
        return ans