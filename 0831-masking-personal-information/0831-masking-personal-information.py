class Solution:
    def maskPII(self, s: str) -> str:
        k = 0
        if "@" in s:
            temp = s.split('@')
            temp[0] = temp[0].lower()
            temp[0] = temp[0][0]+"*****"+temp[0][-1]
            
            ans = temp[0]+"@"+temp[1].lower()
            return ans
        else:
            last = ""
            
            contact = [x for x in s if x.isnumeric()]
            n = len(contact) - 10 if len(contact)-10>0 else 0
            country = contact[:n]
            last = "".join(contact[len(contact)-4:])
            print(last)
            print(country)
            print(contact)

            if n == 0:
                return "***-***-" + last
            elif n == 1:
                return "+*-***-***-" + last
            elif n == 2:
                return "+**-***-***-" + last
            else:  # n == 3
                return "+***-***-***-" + last
        return "-1"