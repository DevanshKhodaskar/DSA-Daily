class Solution:
    def minLights(self, lights: list[int]) -> int:
        

        def emptylights(lights):
            n = len(lights)
            diff = [0] * (n + 1)

            for i in range(n):
                if lights[i] > 0:
                    left = max(0, i - lights[i])
                    right = min(n - 1, i + lights[i])

                    diff[left] += 1
                    diff[right + 1] -= 1

            covered = 0
            ans = set()

            for i in range(n):
                covered += diff[i]
                if covered == 0:
                    ans.add(i)

            return ans 



        arr = set(emptylights(lights))
        ans = 0
        n = len(lights)
        while arr:
            ele = arr.pop()
            if ele + 1 in arr:
                if ele + 2 in arr:
                    arr.remove(ele + 1)
                    arr.remove(ele + 2)
                    ans += 1
                else:
                    arr.remove(ele + 1)
                    ans += 1
            else:
                ans += 1
        return ans