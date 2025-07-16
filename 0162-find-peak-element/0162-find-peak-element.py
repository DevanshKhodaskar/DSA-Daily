class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       if len(nums)==1:
        return 0 
       if len(nums)==2:
        if nums[0]>nums[1]:
            return 0
        else:
            return 1

       max=nums[0]
       counter=0 
       for i in range(1,len(nums)-1):
        if nums[i-1]<nums[i] and nums[i] > nums[i+1]:
            print("Returned here")
            return i
        if nums[i]>max:
            max=nums[i]
            counter=i
       if max<nums[len(nums)-1]: 
           return len(nums)-1
       return counter