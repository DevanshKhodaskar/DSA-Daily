class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []


        def helper(i,summ,arr):
            
            if summ>n or len(arr)>k:
                return
            
            elif summ == n and len(arr) == k:
                ans.append(arr[:])
                return
            if i==10:
                return 
            else:
                helper(i+1,summ,arr)
                arr.append(i)
                
                helper(i+1,summ+i,arr)

                arr.pop()
        helper(1,0,[])
        return ans