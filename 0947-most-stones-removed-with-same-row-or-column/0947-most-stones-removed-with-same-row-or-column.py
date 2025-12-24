class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        offset = 10001
        par = {}

        def find(x):
            res = par[x]

            while res !=par[res]:
                res = par[res]
            return res

        def union(a,b):
            if find(a) == find(b):
                return 0
            else:
                pa = find(a)
                pb = find(b)
                par[pa] = pb


                return 1
        ans = set()
        for a,b in stones:
            if  a not in par:
                par[a] = a
            if b + offset not in par:
                par[b+offset] = b+offset
            
            union(a,b+offset)
        for i in par:
            ans.add(find(i))

        return len(stones) - len(ans)
            
            



 