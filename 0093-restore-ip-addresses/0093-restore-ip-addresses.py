class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s)>12:
            return ans

        
        def helper(i,dots,curIP):
            if dots == 4 and i == len(s):
                ans.append(curIP[:-1])
                return 
            if dots>4:
                return
            
            for j  in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<256 and ((int(s[i:j+1])== 0 and len(s[i:j+1]) == 1) or s[i]!="0" ):
                    helper(j+1,dots+1,curIP+s[i:j+1]+".")
        helper(0,0,"")
        return ans

