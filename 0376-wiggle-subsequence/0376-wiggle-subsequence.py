class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        arr = []

        if len(nums) <= 1:
            return len(nums)

        for i in range(1, len(nums)):
            arr.append(nums[i] - nums[i - 1])

        o = 0
        while o < len(arr) and arr[o] == 0:
            o += 1

        arr = arr[o:]

        if not arr:
            return 1

        flag = arr[0] > 0
        ans = 1

        for i in range(1, len(arr)):
            if arr[i] == 0:
                continue

            flag2 = arr[i] > 0

            if flag != flag2:
                ans += 1
                flag = flag2

        return ans + 1