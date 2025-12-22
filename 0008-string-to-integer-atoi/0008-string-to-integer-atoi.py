class Solution:
    def myAtoi(self, s: str) -> int:
        a = ""
        s = s.lstrip()  
        if len(s) == 0:
            return 0

        if s[0] == '-' or s[0] == '+':
            a += s[0]
            s = s[1:]

        for i in s:
            if i.isdigit():
                a += i
            else:
                break

        if a == "" or a == "+" or a == "-":
            return 0

        ans = int(a)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        return max(INT_MIN, min(INT_MAX, ans))
