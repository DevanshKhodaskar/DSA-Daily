from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        m = set([0])

        q = deque([0])

        farthest = 1

        while q:

            i = q.popleft()

            j = max(i + minJump, farthest)

            while j <= min(i + maxJump, len(s) - 1):

                if s[j] == '0':

                    if j == len(s) - 1:
                        return True

                    if j not in m:
                        m.add(j)
                        q.append(j)

                j += 1

            farthest = i + maxJump + 1

        return len(s) == 1