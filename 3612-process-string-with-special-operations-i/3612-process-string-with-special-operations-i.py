class Solution:
    def processStr(self, s: str) -> str:
        
        ans = []
        for i in s:
            if i == "*":
                if ans:
                    ans.pop()
            elif i == "#":
                ans = ans+ans
            elif i == "%":
                ans = ans[::-1]
            else:
                ans.append(i)
        return "".join(ans)