class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        ans =""


        for i in range(len(num)):
            if not stack:
                stack.append(num[i])
            else:
                
                while stack and num[i]<stack[-1] and k>0:
                    stack.pop()
                    k-=1
                stack.append(num[i])

        for i in range(k):
            stack.pop()

        ans = ''.join(stack).lstrip('0')

        return ans if ans else "0"



        