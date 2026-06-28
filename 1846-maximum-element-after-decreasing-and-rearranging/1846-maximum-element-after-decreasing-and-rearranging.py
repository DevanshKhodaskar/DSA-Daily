class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        margin = 0
        
        for i in range(len(arr)):
            if i == 0:
                arr[i] = arr[i] if arr[i] == 1 else 1
            else:
                arr[i] = min(arr[i-1]+1 ,arr[i])
        return arr[-1]