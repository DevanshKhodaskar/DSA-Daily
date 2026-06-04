from collections import defaultdict
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1

        stack = []
        seen = set()
        for i in s:
            dic[i] -= 1

            if i in seen:
                continue

            while stack and stack[-1] > i and dic[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(i)
            seen.add(i)
        return "".join(stack)
        