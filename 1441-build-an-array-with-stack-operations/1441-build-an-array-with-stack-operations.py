class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        counter = 0
        ans = []
        for i in range(1,n+1):

            if counter<len(target) and target[counter] == i:
                ans.append("Push")
                counter+=1
            elif counter<len(target) and target[counter]!=i:
                ans.append("Push")
                ans.append("Pop")
        return ans