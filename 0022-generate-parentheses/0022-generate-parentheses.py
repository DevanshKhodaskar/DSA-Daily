class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(r,ans,ob,cb,final_ans):
            if r == 0:
                final_ans.append(ans)

                return 
            else:
                if ob>cb and cb<n:
                    helper(r-1,ans+")",ob,cb+1,final_ans)
                if ob<n:
                    helper(r,ans+"(",ob+1,cb,final_ans)
                

        final_ans = []

        helper(n,"",0,0,final_ans)

        return final_ans