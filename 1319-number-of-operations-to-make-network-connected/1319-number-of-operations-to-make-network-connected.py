class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n - 1:
            return -1



        par = [i for i in range(n)]
       

        def find(x):
            res = par[x]

            while res != par[res]:
                res = par[res]
            return res

        def union(a,b):
            pa,pb = find(a),find(b)

            if pa==pb:
                return 0

            else:
                par[pa] = par[pb]
            return 1

        ans = n 
        for n1,n2 in connections:
            ans-=union(n1,n2)

        return ans - 1
        