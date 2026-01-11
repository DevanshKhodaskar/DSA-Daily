class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        i = 0
        for i in range(len(nums)-1):
            if nums[i] == target:
                return True
            else:
                if nums[i]>nums[i+1]:
                    part = i+1
                    break

        l = i+1
        r = len(nums) - 1
        print(f"l:{l}\tr:{r}")

        while l<=r:
            mid = (l+r)//2
            print(f"mid:{mid}")
            if nums[mid] == target:
                return True
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return False