class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
            def helper(nums):
                if not nums:
                    return 0
                nums.sort()
                max_count = 1
                curr_count = 1

                for i in range(1, len(nums)):
                    if nums[i] == nums[i - 1] + 1:
                        curr_count += 1
                        max_count = max(max_count, curr_count)
                    else:
                        curr_count = 1

                return max_count

            h = helper(hBars)
            v = helper(vBars)

            ans = min(h,v)+1

            return ans*ans