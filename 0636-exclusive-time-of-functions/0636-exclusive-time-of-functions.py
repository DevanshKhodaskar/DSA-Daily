class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call = []
        ans = [0] * n

        for log in logs:
            fid, typ, t = log.split(":")
            call.append([int(fid), typ, int(t), 0])

        stack = []

        for ele in call:
            if ele[1] == "start":
                stack.append(ele)

            else:
                start = stack.pop()

                time = ele[2] - start[2] + 1
                exe_time = time - start[3]

                ans[ele[0]] += exe_time

                if stack:
                    stack[-1][3] += time

        return ans