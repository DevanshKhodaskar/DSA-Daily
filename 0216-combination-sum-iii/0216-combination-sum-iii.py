class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1,2,3,4,5,6,7,8,9]


        def helper(Sum,ans,final_ans,i,digits,k,n):
            if len(ans)>k:
                return

            if len(ans) == k:
                if Sum == n:
                    final_ans.append(ans[:])
                return
            
            if i == len(digits):
                return

            ans.append(digits[i])

            helper(Sum+digits[i],ans,final_ans,i+1,digits,k,n)

            ans.pop()
            helper(Sum,ans,final_ans,i+1,digits,k,n) 
        
        final_ans = []
        helper(0,[],final_ans,0,digits,k,n)
        return final_ans