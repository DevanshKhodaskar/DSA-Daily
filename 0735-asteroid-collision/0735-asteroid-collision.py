class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)): 
            # print("initial:",stack)

            if stack and stack[-1][1] > 0 and asteroids[i]<0:

                if stack and stack[-1][1] == abs(asteroids[i]):
                    stack.pop()
                    continue

                if stack and stack[-1][1] > abs(asteroids[i]):
                    continue

                while stack and stack[-1][1] > 0 and stack[-1][1] < abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1][1] == abs(asteroids[i]):
                    stack.pop()
                    continue

                if not stack or stack[-1][1] < 0: 
                    stack.append([i,asteroids[i]])
            
            else:
                stack.append([i,asteroids[i]])

            # print("final:",stack)



        z = [x[1] for x in stack]
        return z
            



                
        