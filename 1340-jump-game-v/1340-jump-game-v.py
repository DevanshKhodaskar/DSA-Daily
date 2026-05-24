class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        visited = [-1]*len(arr)
        
        def helper(i,count):
            if visited[i] != -1:
                return visited[i]
            ans = 1
            j = i-1
            x  = d
            while j>=0 and arr[i]>arr[j] and x>0:
                ans = max(ans,1+helper(j,count+1))
                j-=1
                x-=1
            j = i+1
            x  = d
            while j<len(arr) and arr[i]>arr[j] and x>0:
                ans = max(ans,1+helper(j,count+1))
                j+=1
                x-=1
            visited[i] = ans
        
            return ans


        return max(helper(i,0) for i in range(len(arr)))

           