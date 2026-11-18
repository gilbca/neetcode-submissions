class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        n = self.stack[-1]
        self.stack.pop(-1)
        if n == self.min_stack[-1]:
            self.min_stack.pop(-1)
            

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]