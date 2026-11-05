import heapq

class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        if self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop(-1)
        # if len(self.stack) == 0: 
        #     self.min_stack = []
        #     return 
        if self.min_stack[-1] == top:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
