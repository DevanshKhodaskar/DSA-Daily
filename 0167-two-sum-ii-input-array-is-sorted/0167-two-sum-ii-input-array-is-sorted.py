from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low = 0 
        high = len(numbers) - 1

        while low<=high:
            total = numbers[low] + numbers[high]

            if target == total:
                return [low+1,high+1]
            elif target > total:
                low+=1
            elif target<total:
                high-=1
        return[-1,-1]