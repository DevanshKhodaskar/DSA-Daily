class MinStack:

    def __init__(self):
        self.s = []
        

    def push(self, val: int) -> None:
        minimum = self.getMin()
        if minimum == None or val < minimum:
            minimum = val

        self.s.append([val,minimum]) 
    
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1][0] if self.s else None

        

    def getMin(self) -> int:
        return self.s[-1][1] if self.s else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()