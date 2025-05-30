class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        final_ans = []
        ans = []
        i = 0
        def helper(candidates,summ,ans,i):
            if i>=len(candidates):
                return
            if summ>target:
                return
            if summ == target:
                final_ans.append(ans.copy())
                return
            
            ans.append(candidates[i])
            summ = summ+candidates[i]

            helper(candidates,summ,ans,i)
            
            ans.pop()
            summ = summ-candidates[i]
            helper(candidates,summ,ans,i+1)

        helper(candidates,0,ans,0)
        return final_ans