class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        if s == "" or s== "-":
            return 0
        b = s.split()
        if not b:
            return 0
        ans = ""
        for i in range(len(b[0])):
            if i == 0 and b[0][i] == "-":
                ans+="-"
            elif i == 0 and b[0][i] == "+":
                continue
            else:
                if b[0][i] not in numbers:
                    break
                else:
                    ans+=b[0][i]
        if ans == "" or ans == "-":
            return 0
        ans = int(ans)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX

        return ans