class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            min_sum = nums[i] + nums[i + 1] + nums[i + 2]

            if min_sum > target:
                if abs(min_sum - target) < abs(closest - target):
                    closest = min_sum
                break

   
            max_sum = nums[i] + nums[-1] + nums[-2]

            if max_sum < target:
                if abs(max_sum - target) < abs(closest - target):
                    closest = max_sum
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return target

        return closest