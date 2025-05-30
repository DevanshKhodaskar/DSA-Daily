class Solution:
    def helper(self,arr,ind,ans,final_ans):
        if ind >= len(arr):
            final_ans.append(ans[:])
            return

        else:
            ans.append(arr[ind])
            self.helper(arr,ind+1,ans,final_ans)
            ans.pop()
            self.helper(arr,ind+1,ans,final_ans)
        return final_ans


    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_ans = []
        self.helper(nums,0,[],final_ans)
        return final_ans
        