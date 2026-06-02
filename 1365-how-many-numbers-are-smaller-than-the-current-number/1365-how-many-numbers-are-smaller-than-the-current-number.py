class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*500

        for i in nums:
            arr[i]+=1
        summ =[0]
        for i in range(1,len(arr)):
            summ.append(arr[i-1]+summ[i-1])
        return [summ[i] for i in nums]