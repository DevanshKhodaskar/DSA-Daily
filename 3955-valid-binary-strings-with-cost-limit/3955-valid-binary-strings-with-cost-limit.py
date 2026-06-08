class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        
        ans = []

        def helper(temp,prev,rem):
            if rem<0:
                return 
            if len(temp) == n:

                ans.append(temp)
                return
                
            if prev == True:
                helper(temp+"0",False,rem)
            else:
                helper(temp+"0",False,rem)
                helper(temp+"1",True,rem-len(temp))
        helper("",False,k)
        return ans
