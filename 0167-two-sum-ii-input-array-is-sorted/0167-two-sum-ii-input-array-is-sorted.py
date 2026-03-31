from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bs(arr, t):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high)//2
                if arr[mid] == t:
                    return mid
                elif arr[mid] < t:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        for i in range(len(numbers)):
            ele = numbers[i]
            idx = bs(numbers[i+1:], target - ele)

            if idx != -1:
                return [i + 1, i + 1 +1+ idx]  

        return [-1, -1]