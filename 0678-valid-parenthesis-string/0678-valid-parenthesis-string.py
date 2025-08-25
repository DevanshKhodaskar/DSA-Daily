class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stack2 = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                stack2.append(i)
            else:
                if stack:
                    stack.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False

        while stack and stack2:
            if stack[-1] < stack2[-1]:
                stack.pop()
                stack2.pop()
            else:
                break

        return not stack