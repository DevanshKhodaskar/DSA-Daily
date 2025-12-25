class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par =[i for i in range(len(accounts))] 


        def find(x):
            res = par[x]
            while res!=par[res]:
                res=par[res]
            return res

        def union(a,b):
            pa,pb = find(a),find(b)

            if pa == pb:return 0
            else:
                par[pb] = pa

                return 1



        email_index = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]

                if email in email_index:
                    union(i,email_index[email])
                else:
                    email_index[email] = i
        merged = {}

        for email,idx in email_index.items():
            root = find(idx)
            if  root not in merged:
                merged[root] = []
            merged[root].append(email)

        ans = []

        for root in merged:
            ans.append([accounts[root][0]] + sorted(merged[root]))


        return ans
