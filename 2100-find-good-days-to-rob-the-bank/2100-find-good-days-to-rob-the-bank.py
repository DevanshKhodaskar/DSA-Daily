class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        i = 0
        inc = [len(security)] *len(security)
        for j in range(1,len(security)):
            if security[j-1]>security[j]:
                for k in range(i,j):
                    inc[k] = j-1
                i = j

        dec = [-1] *len(security)
        i = len(security) -1
        for j in range(len(security)-2,-1,-1):
            if security[j+1]>security[j]:
                for k in range(i,j,-1):

                    dec[k] = j+1
                i = j
   
        ans  = []
        for i in range(time , len(security) -time):
            if dec[i] <= i-time and inc[i] >=i+time:
                ans.append(i)
        return ans





















