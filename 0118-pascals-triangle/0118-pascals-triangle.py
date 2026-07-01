class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            temp = [0]
            for j in range(len(ans[-1])):
                left = ans[-1][j]
                right = ans[-1][j]
                temp[j]+=left
                temp.append(right)
            ans.append(temp)
        return ans