class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lengthOfLIS(nums: List[int]) -> int:
            
            ans = []
            visited = set()
            ans.append(nums[0])
            visited.add(nums[0])

            def lower(ele):
                l = 0
                r = len(ans)-1
                while l<=r:
                    m = (l+r)//2
                    if ans[m] >ele:
                        r = m-1
                    else:
                        l = m+1
                return l



            for i in range(1,len(nums)):

                if nums[i]>ans[-1]:
                    ans.append(nums[i])
                
                elif nums[i]<ans[-1] and nums[i] not in visited:
                    temp =lower(nums[i]) 
                    visited.remove(ans[temp])
                    ans[temp] = nums[i]
                visited.add(nums[i])
            return len(ans)


            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return lengthOfLIS([envelopes[i][1] for i in range(len(envelopes))])