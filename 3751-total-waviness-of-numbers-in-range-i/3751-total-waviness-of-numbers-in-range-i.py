class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1,num2+1):
            st = str(i)
            arr = list(map(int,st.strip()))
            for i in range(1,len(arr)-1):
                if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                    count+=1
                elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    count+=1
        return count