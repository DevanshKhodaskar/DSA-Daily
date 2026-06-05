class MyQueue:

    def __init__(self):
        self.arr = []        

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        arr2 = []
        while self.arr:arr2.append(self.arr.pop())
        temp = arr2.pop()
        while arr2:self.arr.append(arr2.pop())        
        return temp

    def peek(self) -> int:
        return self.arr[0] if self.arr else None
        

    def empty(self) -> bool:
        return not self.arr
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()