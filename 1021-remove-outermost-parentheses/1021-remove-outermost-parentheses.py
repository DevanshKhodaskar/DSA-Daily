class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        temp = ""
        ans = ""

        for i in s:
            print(temp)
            if len(stack) == 0:
                if len(temp) !=0:
                    ans+=temp[1:len(temp)-1]
                temp = ""

            if i == "(":
                stack.append("(")
                temp+="("
            elif i == ")":
                stack.pop()
                temp+=")"
        if len(temp) !=0:
            ans+=temp[1:len(temp)-1]

            
        return ans

        