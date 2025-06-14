class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            max_ele = -1
            find = False
            for j in range(i+1,len(nums)):
                # print(f"for i:{i} j:{j}")
                if nums[j] > nums[i]:
                    # print(f"nums[j]:{nums[j]}")
                    max_ele = nums[j]
                    find = True
                    break
            if find == False:
                for k in range(0,i):
                    if nums[k] > nums[i]:
                        max_ele = nums[k]
                        break

            ans.append(max_ele)


        return ans    